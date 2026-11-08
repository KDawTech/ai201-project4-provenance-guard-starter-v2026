#!/usr/bin/env python3
"""Unit 8: three real trials of the five PRE-DEFINED Unit 7 criteria.

    python run_eval.py --label before
    python run_eval.py --label after

Never invents human samples, model scores, or outcomes. All HTTP values
come from the running local service. Direct label coverage uses actual
scoring.py::score_to_label, since no API accepts arbitrary combined scores.
"""
import argparse
import json
import statistics
import sys
import uuid
from datetime import datetime, timezone
from pathlib import Path

import config
import scoring
import scenarios

BASE = f'http://{config.HOST}:{config.PORT}'
TARGETS = {
  1:'At most 1/10 human samples classified ai per trial',
  2:'AI median minus human median >= 0.12 per trial',
  3:'Direct label checks at 0.15, 0.55, 0.95 yield human, unsure, ai (3/3)',
  4:'5/5 appeals become under_review, original verdict and scores unchanged',
  5:'5/5 malformed requests return 4xx with no attribution decision',
}
NAMES={1:'Human false positives',2:'Score spread',3:'Label coverage',4:'Appeal auditability',5:'Invalid requests'}


def get(client,url,timeout):
    r=client.get(url,timeout=timeout)
    return r.status_code,r.json()


def post(client,url,payload,timeout):
    try:
        r=client.post(url,json=payload,timeout=timeout)
        try: data=r.json()
        except ValueError:data={'raw':r.text[:200]}
        return {'status':r.status_code,'json':data}
    except Exception as exc:
        return {'status':None,'error':f'{type(exc).__name__}: {exc}','json':{}}


def new_creator(prefix,run_id,index):
    return f'eval8_{prefix}_{run_id}_{index}'


def score_inputs(client,base,texts,prefix,run_id,timeout):
    outputs=[]
    for i,text in enumerate(texts,1):
        out=post(client,base+'/submit',{'creator_id':new_creator(prefix,run_id,i),'text':text},timeout)
        out['sample']=f'{prefix}_{i}'
        outputs.append(out)
    return outputs


def all_scored(rows):
    return all(x.get('status')==200 and isinstance(x.get('json',{}).get('confidence'),(float,int)) for x in rows)


def criterion_1(client,base,run_id,timeout,human):
    responses=score_inputs(client,base,human,'human',run_id,timeout)
    n=sum(x['json'].get('guess')=='ai' for x in responses)
    ok=all_scored(responses) and n<=1
    return {'met':ok,'value':f'{n}/10 AI flags','detail':responses,'note':'A failed HTTP response also counts as a miss.'}


def criterion_2(client,base,run_id,timeout,human):
    hs=score_inputs(client,base,human[:5],'separation_h',run_id,timeout)
    ai=score_inputs(client,base,scenarios.AI_TEXTS,'separation_ai',run_id,timeout)
    if all_scored(hs+ai):
        hm=statistics.median(x['json']['confidence'] for x in hs)
        am=statistics.median(x['json']['confidence'] for x in ai)
        gap=round(am-hm,4); met=gap>=0.12
        value=f'AI median {am:.4f} - human median {hm:.4f} = {gap:+.4f}'
    else:
        met=False;gap=None;value='Unscorable HTTP response(s)'
    return {'met':met,'value':value,'gap':gap,'detail':{'human':hs,'ai':ai}}


def criterion_3():
    vals=[]
    for s in scenarios.LABEL_TEST_SCORES:
        guess,label=scoring.score_to_label(s)
        vals.append({'score':s,'guess':guess,'label':label})
    met=[x['guess'] for x in vals]==['human','unsure','ai']
    return {'met':met,'value':f"{sum(x['guess']==expected for x,expected in zip(vals,['human','unsure','ai']))}/3 labels",'detail':vals,
            'note':'Direct function checks measure label mapping, not model accuracy.'}


def criterion_4(client,base,run_id,timeout,human):
    items=[]
    for i,text in enumerate(human[:5],1):
        sub=post(client,base+'/submit',{'text':text,'creator_id':new_creator('appeal',run_id,i)},timeout)
        ident=sub['json'].get('content_id')
        if sub['status']!=200 or not ident:
            items.append({'i':i,'passed':False,'submit':sub,'reason':'No valid submission/content_id'})
            continue
        reason='I wrote this personally and I request a human review of the detection score.'
        ape=post(client,base+'/appeal',{'content_id':ident,'reasoning':reason},timeout)
        try:
            code,item=get(client,base+'/content/'+ident,timeout)
            _,log=get(client,base+'/log?limit=500',timeout)
            entries=[e for e in log.get('entries',[]) if e.get('content_id')==ident]
        except Exception as exc:
            code=None;item={};entries=[];ape['network_error']=repr(exc)
        original=next((e for e in entries if e.get('status')=='decided'),{})
        challenge=next((e for e in entries if e.get('event')=='appeal'),{})
        retained=bool(original) and all(original.get(k)==sub['json'].get(k) for k in ['guess','model_score','style_score','label'])
        passed=(ape['status']==200 and ape['json'].get('status')=='under_review' and code==200
                and item.get('status')=='under_review' and retained and challenge.get('status')=='under_review')
        items.append({'i':i,'content_id':ident,'passed':passed,'submit':sub,'appeal':ape,
                      'status_response':item,'original_decision':original,'appeal_event':challenge,
                      'original_fields_unchanged':retained})
    n=sum(x['passed'] for x in items)
    return {'met':n==5,'value':f'{n}/5 preserved appeal flows','detail':items}


def criterion_5(client,base,run_id,timeout):
    items=[]
    for i,b in enumerate(scenarios.INVALID_BODIES,1):
        payload=dict(b)
        if 'creator_id' in payload:
            payload['creator_id']=new_creator('invalid',run_id,i)
        out=post(client,base+'/submit',payload,timeout)
        items.append({'case':i,'status':out['status'],'response':out['json'],
                      'passed':bool(out['status'] and 400<=out['status']<500 and
                          'content_id' not in out['json'] and out['json'].get('guess') is None)})
    try:
        _,log=get(client,base+'/log?limit=20',timeout)
        recent=log.get('entries',[])[-5:]
        log_ok=len(recent)==5 and all(e.get('event')=='rejected' and e.get('status')=='rejected' for e in recent)
    except Exception: log_ok=False;recent=[]
    n=sum(x['passed'] for x in items)
    return {'met':n==5 and log_ok,'value':f'{n}/5 4xx; rejection audit: {"yes" if log_ok else "no"}',
            'detail':items,'audit_rejections':recent,
            'note':'Last five log entries should be rejections; run with no concurrent writers.'}


def save(data,root,label):
    results=root/'results';results.mkdir(parents=True,exist_ok=True)
    raw=results/f'unit8_criteria_{label}.json'
    raw.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    lines=[f'# Unit 8 acceptance criteria — {label}','',
           'Actual runs produced by `run_eval.py`; all non-direct scores came from POST /submit.',
           f"Timestamp (UTC): {data['started_at']}",'',
           '| Criterion | Target | Run 1 | Run 2 | Run 3 | Verdict |',
           '|---|---|---|---|---|---|']
    for c in range(1,6):
        trials=data['results'][str(c)]
        values=[(x['value'].replace('|','/')) for x in trials]
        verdict='MET' if len(trials)==3 and all(x['met'] for x in trials) else 'MISSED'
        lines.append(f"| {c}. {NAMES[c]} | {TARGETS[c]} | "+' | '.join(values+['NOT RUN']*(3-len(values)))+f' | {verdict} |')
    lines+=['','## Real responses / traces','',
            'The values below are observed, not predictions. All trials remain visible even if they are identical.','']
    for c in range(1,6):
        lines += [f'### {c}. {NAMES[c]}','']
        for i,row in enumerate(data['results'][str(c)],1):
            lines += [f'#### Trial {i}: {"MET" if row["met"] else "MISSED"}',
                      '',f'Observation: {row["value"]}','','```json',
                      json.dumps(row,ensure_ascii=False,indent=2),'```','']
    lines+=['## Diagnoses (fill after examining misses)','',
            'For each MISSED criterion: name the **stage** (route, model signal, style signal, combining rule, label mapping) and the **mechanism**. Do not invent a cause.','']
    report=results/f'unit8_criteria_{label}.md'
    report.write_text('\n'.join(lines),encoding='utf-8')
    return raw,report


def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--label',choices=['before','after'],required=True)
    ap.add_argument('--trials',type=int,default=3)
    ap.add_argument('--url',default=BASE)
    ap.add_argument('--timeout',type=float,default=90)
    a=ap.parse_args()
    if a.trials!=3:raise SystemExit('Unit 8 requires EXACTLY three trials for this runner.')
    problems=scenarios.validate()
    if problems:raise SystemExit('Cannot start a genuine evaluation:\n- '+'\n- '.join(problems))
    try:import requests
    except ImportError:raise SystemExit('Install requirements: python -m pip install -r requirements.txt')
    session=requests.Session()
    try:
        s,h=get(session,a.url+'/health',5)
        if s!=200: raise RuntimeError(f'/health returned {s}')
        if not h.get('rate_limiting'):raise RuntimeError('Rate limiting is OFF; enable Unit 8 and restart app.py')
    except Exception as exc:
        raise SystemExit(f'Cannot reach Unit 8 service: {exc}\nStart python app.py in another terminal.')
    human=scenarios.human_samples()
    data={'label':a.label,'started_at':datetime.now(timezone.utc).isoformat(),
          'base_url':a.url,'targets':TARGETS,'results':{str(i):[] for i in range(1,6)}}
    root=Path(__file__).resolve().parent
    for trial in range(1,4):
        run_id=uuid.uuid4().hex[:8]
        print(f'\n=== Trial {trial}/3: {a.label} ===',flush=True)
        funcs=[lambda:criterion_1(session,a.url,run_id,a.timeout,human),
               lambda:criterion_2(session,a.url,run_id,a.timeout,human),
               lambda:criterion_3(),
               lambda:criterion_4(session,a.url,run_id,a.timeout,human),
               lambda:criterion_5(session,a.url,run_id,a.timeout)]
        for c,f in enumerate(funcs,1):
            row=f()
            data['results'][str(c)].append(row)
            raw,report=save(data,root,a.label)
            print(f'  C{c} {"MET" if row["met"] else "MISSED"}: {row["value"]}',flush=True)
    print(f'\nWrote {raw.relative_to(root)} and {report.relative_to(root)}')
    print('Treat MISSED criteria honestly; they earn credit with specific diagnoses.')

if __name__=='__main__':main()

#!/usr/bin/env python3
"""Record 10 USER-written paragraphs for the false-positive acceptance criterion."""
import json
from pathlib import Path

PATH=Path(__file__).resolve().parent/'data'/'unit8_human_samples.json'


def main():
    PATH.parent.mkdir(exist_ok=True)
    try:
        data=json.loads(PATH.read_text(encoding='utf-8')) if PATH.exists() else []
    except (ValueError,OSError):
        data=[]
    if not isinstance(data,list): data=[]
    print(f'{len(data)}/10 samples saved. Paste writing that YOU wrote, not AI-generated text.')
    print('Paste one paragraph per prompt. Press Enter when finished; type q to save and quit.\n')
    while len(data)<10:
        s=input(f'Human sample {len(data)+1}/10 > ').strip()
        if s.lower()=='q': break
        if len(s.split())<8:
            print('Needs 8+ words. Please paste a longer excerpt you personally wrote.')
            continue
        data.append(s)
        PATH.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
        print(f'Saved {len(data)}/10')
    print(f'Wrote {PATH}. Count: {len(data)}/10')
    if len(data)==10:print('Ready: python run_eval.py --label before')

if __name__=='__main__':main()

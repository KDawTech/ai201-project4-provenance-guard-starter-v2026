"""Five measurable Unit 8 scenarios, aligned with criteria.md (Unit 7).

Run with `python run_eval.py --label before` after supplying YOUR original writing.
No fabricated human-authored examples are included.
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
HUMAN_FILE = ROOT / 'data' / 'unit8_human_samples.json'

# Explicitly AI-written reference pieces, generated as example test inputs.
# They are NOT presented as independently verified detector benchmarks.
AI_TEXTS = [
    "The integration of artificial intelligence into organizational workflows has introduced several opportunities for operational improvement. By automating routine processes, organizations can allocate additional resources to strategic initiatives. Effective implementation requires appropriate governance, regular evaluation, and ongoing stakeholder communication. These considerations can improve the reliability and consistency of the resulting system.",
    "In recent years, sustainable transportation has emerged as an important priority for urban planning. Electric buses, protected cycling infrastructure, and pedestrian-friendly neighborhoods can contribute to reduced emissions. However, successful adoption depends on funding, public engagement, and coordinated infrastructure investment. Cities should evaluate these factors systematically before introducing large-scale changes.",
    "Developing an effective study routine requires clearly defined goals, consistent scheduling, and regular self-assessment. Students may benefit from dividing large assignments into smaller manageable tasks and reviewing key concepts over time. A balanced approach also considers adequate rest and realistic expectations. When these strategies are applied consistently, the overall learning process may become more productive.",
    "Modern information systems rely on multiple layers of security to protect confidential data. Authentication, authorization, encryption, and monitoring each serve a distinct purpose within a broader security architecture. Organizations should evaluate risks regularly and establish clear procedures for responding to incidents. Continuous improvement can help maintain an appropriate level of protection as technologies evolve.",
    "Community gardens can offer meaningful benefits to residents of densely populated neighborhoods. Shared green spaces may encourage social interaction, provide opportunities for environmental education, and support access to fresh produce. Maintaining these spaces requires volunteers, funding, and clearly defined responsibilities. With appropriate planning, community gardens can become a valuable part of local neighborhood development."
]

LABEL_TEST_SCORES = [0.15, 0.55, 0.95]
INVALID_BODIES = [
    {'creator_id': 'invalid_missing'},
    {'text': '  ', 'creator_id': 'invalid_empty'},
    {'text': 123, 'creator_id': 'invalid_nonstring'},
    {'text': 'This is a complete sentence with enough words to be scored if the identity was present.'},
    {'text': 'a' * 20001, 'creator_id': 'invalid_huge'},
]


def human_samples():
    if not HUMAN_FILE.exists():
        return []
    data = json.loads(HUMAN_FILE.read_text(encoding='utf-8'))
    if not isinstance(data,list):
        raise ValueError('human sample JSON must be a list')
    return data


def validate():
    problems=[]
    try:
        samples=human_samples()
    except (ValueError, OSError) as e:
        return [f'Cannot read {HUMAN_FILE}: {e}']
    if len(samples)!=10:
        problems.append('Criterion 1 needs exactly 10 genuinely human-written samples. Run python unit8_add_human.py')
    for i,t in enumerate(samples,1):
        if not isinstance(t,str) or len(t.split())<8:
            problems.append(f'Human sample {i} needs at least 8 words of your OWN writing')
    if len(AI_TEXTS)!=5:
        problems.append('Criterion 2 needs exactly five AI-written reference samples')
    return problems


# Included for transparency and for the starter's scenario-inspection workflow.
# run_eval.py performs additional endpoint/direct-function checks for criteria 3/4.
def get_scenarios():
    human=human_samples()
    return [
      {'criterion':1,'name':'human false positives','texts':human},
      {'criterion':2,'name':'score separation','texts':human[:5]+AI_TEXTS},
      {'criterion':3,'name':'label coverage','scores':LABEL_TEST_SCORES},
      {'criterion':4,'name':'appeal auditability','texts':human[:5],'flow':'submit -> appeal -> /content -> /log'},
      {'criterion':5,'name':'invalid input rejection','bodies':INVALID_BODIES},
    ]

SCENARIOS = get_scenarios()

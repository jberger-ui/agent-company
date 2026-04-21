from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
required = [
    ROOT / 'COMPANY.md',
    ROOT / 'teams',
    ROOT / 'agents',
    ROOT / 'projects',
    ROOT / 'tasks',
    ROOT / 'skills',
]
missing = [str(p) for p in required if not p.exists()]
if missing:
    raise SystemExit('Missing required paths: ' + ', '.join(missing))
print('Structure looks valid.')

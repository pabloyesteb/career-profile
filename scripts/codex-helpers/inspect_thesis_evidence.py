#!/usr/bin/env python3
"""Read-only historical thesis inspection; never imports repository code."""
import csv
import hashlib
import json
from collections import defaultdict
from pathlib import Path
import subprocess

REPO = Path('/home/pablo/TUM/SoSe 26/TFM/contact-rich-control')
OUT = Path(__file__).resolve().parents[1] / '.cache/thesis_analysis'


def git(*args):
    return subprocess.check_output(['git', '-C', str(REPO), *args], text=True)


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    records = []
    roots = ['python_src/trajectory_execution', 'experiments/config',
             'experiments/offsets', 'docs/final_presentation/scripts', 'docker']
    for root in roots:
        for p in sorted((REPO / root).rglob('*')):
            if not p.is_file() or p.suffix not in {'.py', '.yaml', '.sh', '.tex'}:
                continue
            if any(x in p.parts for x in ['runs', '__pycache__', 'c_generated_code']):
                continue
            data = p.read_bytes()
            records.append({'path': str(p.relative_to(REPO)), 'bytes': len(data),
                            'sha256': hashlib.sha256(data).hexdigest()})
    for rel in ['docs/final_presentation/final_presentation.tex', 'README.md',
                'experiments/run_battery.py', 'experiments/audit_results.py',
                'experiments/audit_gyroscopic_term.py', 'experiments/bench_substep_feedback.py']:
        p = REPO / rel
        records.append({'path': rel, 'sha256': hashlib.sha256(p.read_bytes()).hexdigest()})
    for p in sorted((REPO / 'experiments/runs').rglob('config.yaml')):
        records.append({'path': str(p.relative_to(REPO)),
                        'sha256': hashlib.sha256(p.read_bytes()).hexdigest()})
    source_root = Path(__file__).resolve().parents[1] / '00_sources/master_thesis'
    local_sources = {p.name: hashlib.sha256(p.read_bytes()).hexdigest()
                     for p in sorted(source_root.iterdir()) if p.is_file()}
    (OUT / 'repository_snapshot.json').write_text(json.dumps({
        'head': git('rev-parse', 'HEAD').strip(), 'branch': git('branch', '--show-current').strip(),
        'status': git('status', '--porcelain'), 'submodules': git('submodule', 'status'),
        'local_sources': local_sources, 'files': records}, indent=2))
    (OUT / 'history.txt').write_text(git('log', '-60', '--format=%H %ad %s', '--date=iso-strict'))
    results = []
    for p in sorted((REPO / 'experiments/runs').rglob('metrics.csv')):
        # Prioritize explicit thesis target/sweep evidence, not every historical run.
        if not any(x in str(p) for x in ['target_config', 'tc_', 'alpha_ablation', 'preview_sweep']):
            continue
        with p.open(newline='') as f:
            rows = list(csv.DictReader(f))
        groups = defaultdict(list)
        for row in rows:
            groups[row.get('experiment', '?')].append(row)
        for name, rows in groups.items():
            successes = sum(str(r.get('success', '')).lower() in {'1', '1.0', 'true'} for r in rows)
            results.append({'file': str(p.relative_to(REPO)), 'experiment': name,
                            'rows': len(rows), 'successes': successes,
                            'columns': list(rows[0]) if rows else [],
                            'sha256': hashlib.sha256(p.read_bytes()).hexdigest()})
    (OUT / 'run_summary.json').write_text(json.dumps(results, indent=2))
    print(f'{len(records)} source hashes; {len(results)} selected saved experiment branches')
    for r in results:
        print(f"{r['file']} | {r['experiment']} | {r['successes']}/{r['rows']}")


if __name__ == '__main__':
    main()

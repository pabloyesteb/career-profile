#!/usr/bin/env python3
"""Read-only Git evidence export; never imports or executes pyLowOrder code."""
import csv
import json
import subprocess
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPO = Path('/home/pablo/pyLowOrder')
OUT = ROOT / '.cache/pyloworder_analysis'


def git(*args):
    return subprocess.check_output(['git', '-C', str(REPO), *args], text=True)


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    commits = git('log', '--all', '--format=%H', '--author=p.yesteb@upm.es').splitlines()
    rows = []
    files = Counter()
    for commit in commits:
        values = git('show', '-s', '--format=%H%n%P%n%aI%n%an%n%ae%n%s', commit).splitlines()
        changed = git('diff-tree', '--root', '--no-commit-id', '--name-only', '-r', commit).splitlines()
        files.update(changed)
        rows.append(dict(zip(['commit', 'parents', 'author_date', 'author', 'email', 'subject'], values))
                    | {'changed_files': ';'.join(changed)})
        patch = git('show', '--format=fuller', '--stat', '--patch', '--no-ext-diff', commit)
        (OUT / f'{commit}.patch').write_text(patch)
    with (ROOT / '01_inventory/pyloworder_commits.csv').open('w', newline='') as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    snapshot = {'head': git('rev-parse', 'HEAD').strip(),
                'branch': git('branch', '--show-current').strip(),
                'status': git('status', '--porcelain'),
                'shallow': git('rev-parse', '--is-shallow-repository').strip(),
                'remotes': git('remote', '-v'),
                'identities': git('shortlog', '-sne', '--all'),
                'commits': len(rows), 'changed_file_counts': files.most_common()}
    (OUT / 'snapshot.json').write_text(json.dumps(snapshot, indent=2))
    print(json.dumps(snapshot, indent=2))


if __name__ == '__main__':
    main()

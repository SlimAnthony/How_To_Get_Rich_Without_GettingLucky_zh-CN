#!/usr/bin/env python3
"""Content-integrity checks for the chapter Markdown files.

Validates things a translation project needs but a generic linter won't catch:
broken internal links, filename/UUID format, chapter numbering, and drift
between CLAUDE.md's chapter status table and each file's own
`Translation Process` field.

Exit code is non-zero if any check fails.
"""
import glob
import re
import sys
import urllib.parse

CHAPTER_RE = re.compile(r'^(\d{2}) (.+) ([0-9a-f]{32})\.md$')
LINK_RE = re.compile(r'\[[^\]]*\]\(([^)]*\.md[^)]*)\)')
STATUS_RE = re.compile(r'Translation Process:\s*(Done|To Do|In Progress)')
NUMBER_RE = re.compile(r'^Number:\s*(\d+)', re.MULTILINE)
CLAUDE_TABLE_ROW_RE = re.compile(
    r'^\|\s*(\d+)\s*\|[^|]+\|\s*(Done|To Do|In Progress)\s*\|', re.MULTILINE
)


def load_chapter_files():
    files = sorted(glob.glob('[0-9]*.md'))
    chapters = {}
    errors = []
    for f in files:
        m = CHAPTER_RE.match(f)
        if not m:
            errors.append(f'Filename does not match "NN Title <uuid>.md" pattern: {f}')
            continue
        num = int(m.group(1))
        chapters.setdefault(num, []).append(f)
    return chapters, files, errors


def check_numbering(chapters):
    errors = []
    for num in range(1, 52):
        if num not in chapters:
            errors.append(f'Missing chapter number {num:02d}')
        elif len(chapters[num]) > 1:
            errors.append(f'Duplicate chapter number {num:02d}: {chapters[num]}')
    return errors


def check_links(files):
    fileset = set(files)
    errors = []
    for f in files:
        text = open(f, encoding='utf-8').read()
        for m in LINK_RE.finditer(text):
            target = urllib.parse.unquote(m.group(1))
            if target.startswith('http'):
                continue
            if target not in fileset:
                errors.append(f'{f}: broken link -> {target}')
    return errors


def check_number_field(files):
    errors = []
    for f in files:
        text = open(f, encoding='utf-8').read()
        m = CHAPTER_RE.match(f)
        num_m = NUMBER_RE.search(text)
        if m and num_m and int(num_m.group(1)) != int(m.group(1)):
            errors.append(
                f'{f}: filename number {m.group(1)} != frontmatter "Number: {num_m.group(1)}"'
            )
    return errors


def check_status_drift(files):
    errors = []
    try:
        claude_md = open('CLAUDE.md', encoding='utf-8').read()
    except FileNotFoundError:
        return ['CLAUDE.md not found; skipping status-drift check']

    table_status = {int(n): s for n, s in CLAUDE_TABLE_ROW_RE.findall(claude_md)}

    for f in files:
        m = CHAPTER_RE.match(f)
        if not m:
            continue
        num = int(m.group(1))
        text = open(f, encoding='utf-8').read()
        status_m = STATUS_RE.search(text)
        file_status = status_m.group(1) if status_m else None
        claude_status = table_status.get(num)
        if file_status and claude_status and file_status != claude_status:
            errors.append(
                f'{f}: file says "Translation Process: {file_status}" '
                f'but CLAUDE.md table says "{claude_status}"'
            )
    return errors


def main():
    chapters, files, filename_errors = load_chapter_files()

    all_errors = []
    all_errors.extend(filename_errors)
    all_errors.extend(check_numbering(chapters))
    all_errors.extend(check_links(files))
    all_errors.extend(check_number_field(files))
    all_errors.extend(check_status_drift(files))

    if all_errors:
        print(f'FAILED: {len(all_errors)} issue(s) found\n')
        for e in all_errors:
            print(f'  - {e}')
        return 1

    print(f'OK: {len(files)} chapter files checked, no issues found')
    return 0


if __name__ == '__main__':
    sys.exit(main())

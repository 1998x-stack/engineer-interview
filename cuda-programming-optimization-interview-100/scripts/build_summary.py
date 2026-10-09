from pathlib import Path
import re
root=Path(__file__).resolve().parents[1]
lines=['# CUDA 编程优化面试 100 题 - SUMMARY','']
for chapter in sorted((root/'questions').iterdir()):
    if not chapter.is_dir(): continue
    lines += [f'## {chapter.name}','']
    for p in sorted(chapter.glob('q*.md')):
        first=next((ln for ln in p.read_text(encoding='utf-8').splitlines() if ln.startswith('# Q')), p.stem)
        title=first[2:] if first.startswith('# ') else first
        lines.append(f'- [{title}]({p.relative_to(root).as_posix()})')
    lines.append('')
(root/'SUMMARY.md').write_text('\
'.join(lines),encoding='utf-8')
print('SUMMARY.md rebuilt')

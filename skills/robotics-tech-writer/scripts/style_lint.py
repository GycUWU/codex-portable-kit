#!/usr/bin/env python3
"""Soft style linter for Chinese engineering Markdown."""
from __future__ import annotations
import argparse
import re
from pathlib import Path
from collections import Counter

WATCH = [
    "值得注意的是", "不难发现", "显而易见", "至关重要", "尤为关键",
    "从本质上讲", "综上所述", "总体而言", "奠定坚实基础",
    "具有重要意义", "这一设计有效地",
]
TRANSITIONS = ["首先", "其次", "最后"]
BOLD_RE = re.compile(r"\*\*[^*\n]{1,80}\*\*")
HEADING_RE = re.compile(r"^\s{0,3}#{1,6}\s+", re.M)
TABLE_LINE_RE = re.compile(r"^\s*\|.*\|\s*$", re.M)
SENTENCE_RE = re.compile(r"[^。！？!?；;\n]+[。！？!?；;]?")
PARA_SPLIT_RE = re.compile(r"\n\s*\n+")

def visible_text(md: str) -> str:
    md = re.sub(r"```.*?```", "", md, flags=re.S)
    md = re.sub(r"`[^`\n]+`", "CODE", md)
    md = re.sub(r"!\[[^\]]*\]\([^)]+\)", "", md)
    md = re.sub(r"\[[^\]]+\]\([^)]+\)", "LINK", md)
    return md

def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("file")
    args = ap.parse_args()
    p = Path(args.file)
    text = p.read_text(encoding="utf-8")
    plain = visible_text(text)
    warnings = []

    for phrase in WATCH:
        n = plain.count(phrase)
        if n >= 2:
            warnings.append(f"repeated stock phrase: {phrase!r} x{n}")
        elif n == 1 and phrase in {"至关重要", "具有重要意义", "奠定坚实基础"}:
            warnings.append(f"check whether importance claim is evidenced: {phrase!r}")

    tr_counts = {
        x: len(re.findall(rf"(^|[。！？\n])\s*{re.escape(x)}[，,:：]?", plain))
        for x in TRANSITIONS
    }
    if all(tr_counts[x] >= 1 for x in TRANSITIONS) and sum(tr_counts.values()) >= 4:
        warnings.append("possible mechanical 首先/其次/最后 sequencing")

    bold_count = len(BOLD_RE.findall(text))
    char_count = max(len(plain.strip()), 1)
    if bold_count >= 12 and bold_count / max(char_count / 1000, 1) > 5:
        warnings.append(f"heavy bold usage: {bold_count} bold spans")

    headings = len(HEADING_RE.findall(text))
    paragraphs = [x.strip() for x in PARA_SPLIT_RE.split(plain) if x.strip() and not x.lstrip().startswith("#")]
    if headings >= 10 and paragraphs and headings / len(paragraphs) > 0.7:
        warnings.append("heading density is high; document may be overly fragmented")

    table_lines = len(TABLE_LINE_RE.findall(text))
    total_lines = max(len(text.splitlines()), 1)
    if table_lines >= 15 and table_lines / total_lines > 0.35:
        warnings.append("large fraction of document is tables; check whether prose would explain better")

    sentences = [s.strip() for s in SENTENCE_RE.findall(plain) if len(s.strip()) >= 4]
    if len(sentences) >= 12:
        lengths = [len(s) for s in sentences]
        avg = sum(lengths) / len(lengths)
        variance = sum((x - avg) ** 2 for x in lengths) / len(lengths)
        if variance < 35:
            warnings.append("sentence lengths are unusually uniform; check for mechanical rhythm")

    endings = []
    for s in sentences:
        core = re.sub(r"[。！？!?；;\s]+$", "", s)
        if len(core) >= 6:
            endings.append(core[-4:])
    for ending, n in Counter(endings).most_common(3):
        if n >= 4:
            warnings.append(f"repeated sentence ending pattern: *{ending!r} x{n}")

    print(f"{p}: {len(warnings)} warning(s)")
    for w in warnings:
        print(f"- {w}")

if __name__ == "__main__":
    main()

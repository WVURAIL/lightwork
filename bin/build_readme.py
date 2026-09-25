#!/usr/bin/env python3
"""Generate README.md from _data/memos.yml.

    python3 bin/build_readme.py           # rewrite README.md
    python3 bin/build_readme.py --check   # exit 1 if it is out of date

Why this exists. The memo index used to live only in README.md, as a
hand-numbered Markdown list that jekyll-readme-index rendered as the site's
front page. The series has gaps -- there is no memo 5, 7, 11, 12, 13 or 17 --
and they were written as bare `5.` and `7.` lines. Markdown reads a lone
numeral on its own line as continuation text, so it folded them into the end of
the previous memo's description ("...first working horn antenna. 5.") and then
renumbered the surviving items 1..32. Every number the reader saw was wrong,
and the numbers are the point of a numbered series.

The list is _data/memos.yml now, and the site renders from it. README.md is
still worth having -- it is what github.com shows -- so it is generated from
the same file rather than kept in step by hand. CI runs --check.

Standard library only, so it runs anywhere with a python3. The YAML reader
below understands the subset this one generated file uses, deliberately: adding
PyYAML to make a build script work is a dependency for the sake of eleven lines
of parsing.
"""

import os
import re
import sys

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(HERE, "_data/memos.yml")
README = os.path.join(HERE, "README.md")


def load_memos(path=DATA):
    """Read the generated memo list. One record per `- number:` line."""
    memos, cur = [], None
    for raw in open(path, encoding="utf-8"):
        line = raw.rstrip("\n")
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        m = re.match(r"^- (\w+):\s*(.*)$", line)
        if m:
            if cur:
                memos.append(cur)
            cur = {}
            key, value = m.group(1), m.group(2)
        else:
            m = re.match(r"^\s+(\w+):\s*(.*)$", line)
            if not m:
                sys.exit("::error::%s: cannot read line: %r" % (path, line))
            key, value = m.group(1), m.group(2)
        if cur is None:
            sys.exit("::error::%s: a field appears before the first `- number:`" % path)
        cur[key] = _scalar(value)
    if cur:
        memos.append(cur)
    if not memos:
        sys.exit("::error::%s: no memos found" % path)
    return sorted(memos, key=lambda x: x["number"])


def _scalar(value):
    value = value.strip()
    if value in ("true", "false"):
        return value == "true"
    if re.fullmatch(r"-?\d+", value):
        return int(value)
    if len(value) >= 2 and value[0] == value[-1] == '"':
        return value[1:-1].replace('\\"', '"').replace("\\\\", "\\")
    return value


HEAD = """<!-- Generated from _data/memos.yml by bin/build_readme.py. Do not edit by hand:
     run the script instead, or CI will tell you the two disagree. -->

# LightWork Memo Series

The LightWork Memo series is an informal series of numbered memoranda on topics
related to citizen science with radio telescopes. The rendered index, with the
videos and the build templates, is at **<https://wvurail.org/lightwork/>**.

This series is intended to encourage the public in the United States, and
throughout the world, to collaborate on the design, construction and operation
of radio telescopes for the purpose of furthering science, engineering and
education. Series guidelines are described in Memo 000, below. The creation of a
memo series is motivated by the success that a focused memo series can have on
organizing the design and construction of large astronomical facilities.

The memo series title has two implications. The first is that this memo series
concerns Work with radio wavelength Light. The second is that we envision that
those developing the radio telescopes will grow a large collaboration, making a
significant contribution to the world's understanding of the universe. Many
hands make LightWork.

## The memos

Numbered in the order they were written. Numbers that were never used are
listed as gaps rather than closed up, so that the number beside a memo is
always its own. Some larger PDFs must be downloaded to be viewed; GitHub does
not preview all of them.

"""

TAIL = """
## Videos, templates and notes

The [site](https://wvurail.org/lightwork/) also carries the video series and
the elevation-axis and elevation-mount templates. The
[notes directory](notes/) holds those templates as PDF and SVG, along with
hints for Raspberry Pi computers.

## Adding a memo

1. Put the PDF in `memos/`.
2. Add an entry to `_data/memos.yml`.
3. Run `python3 bin/build_readme.py` and commit both files.

A memo that has been announced but not yet contributed goes in with
`status: announced` and no `file:`. It is then listed without a link, because a
link in the index is a promise that the file is there.
"""


def render(memos):
    out = [HEAD]
    expected = 0
    for m in memos:
        while expected < m["number"]:
            out.append("%d. *(never used)*" % expected)
            expected += 1
        expected = m["number"] + 1

        bits = []
        target = m.get("file") or m.get("url")
        label = "LightWork Memo %03d" % m["number"]
        bits.append("[%s](%s)" % (label, target) if target else "%s" % label)
        bits.append(m["title"])
        if m.get("note"):
            bits.append("&mdash; " + m["note"])

        flags = {"draft": "**under construction**",
                 "superseded": "**superseded**",
                 "announced": "**announced, PDF not yet contributed**"}
        if m.get("status") in flags:
            bits.append("(%s)" % flags[m["status"]])
        out.append("%d. %s" % (m["number"], " ".join(bits)))

        detail = []
        if m.get("author"):
            detail.append(m["author"])
        if m.get("date"):
            detail.append(m["date"])
        if m.get("superseded_by"):
            detail.append("replaced by memo %03d" % m["superseded_by"])
        if m.get("supersedes"):
            detail.append("replaces memo %03d" % m["supersedes"])
        if detail:
            out.append("   * %s" % ", ".join(detail))

    return "\n".join(out) + "\n" + TAIL


def main(argv):
    memos = load_memos()
    want = render(memos)

    if "--check" in argv:
        have = open(README, encoding="utf-8").read() if os.path.exists(README) else ""
        if have.replace("\r\n", "\n") == want:
            print("README.md is in step with _data/memos.yml (%d memos)." % len(memos))
            return 0
        sys.exit("::error::README.md is out of date. _data/memos.yml has changed "
                 "since it was last generated. Run `python3 bin/build_readme.py` "
                 "and commit the result.")

    open(README, "w", encoding="utf-8", newline="\n").write(want)
    print("wrote README.md from %d memos in _data/memos.yml" % len(memos))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

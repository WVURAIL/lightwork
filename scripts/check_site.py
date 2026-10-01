#!/usr/bin/env python3
"""Check the built memo index, downloads, templates, and compatibility copies."""
import argparse
from html.parser import HTMLParser
import json
from pathlib import Path
from urllib.parse import unquote, urlsplit

from build_memo_index import ROOT, load_memos, validate


class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []
        self.memo_rows = 0

    def handle_starttag(self, tag, attributes):
        attrs = dict(attributes)
        classes = attrs.get("class", "").split()
        if tag == "li" and "memo" in classes and "memo--gap" not in classes:
            self.memo_rows += 1
        for key in ("href", "src"):
            if key in attrs:
                self.links.append(attrs[key])


def check(site, baseurl):
    memos = load_memos()
    validate(memos)
    parsed = Links()
    parsed.feed((site / "index.html").read_text(encoding="utf-8"))
    if parsed.memo_rows != len(memos):
        raise ValueError("The rendered memo list is incomplete")
    for link in parsed.links:
        url = urlsplit(link)
        if url.scheme or url.netloc or not url.path:
            continue
        path = unquote(url.path)
        if path.startswith("/"):
            if baseurl and not path.startswith(baseurl + "/"):
                continue
            path = path[len(baseurl):].lstrip("/")
        target = site / path
        if target.is_dir():
            target = target / "index.html"
        if not target.is_file():
            raise FileNotFoundError(f"Rendered page links a missing file: {link}")
    downloads = {memo["file"] for memo in memos if memo.get("file")}
    for folder in ("memos", "templates", "worksheets", "presentations"):
        downloads.update(str(p.relative_to(ROOT)) for p in (ROOT / folder).rglob("*")
                         if p.is_file() and p.suffix != ".md")
    for name in downloads:
        if not (site / name).is_file() or (site / name).read_bytes() != (ROOT / name).read_bytes():
            raise ValueError(f"Published download missing or changed: {name}")
    manifest = json.loads((ROOT / "docs/file-map.json").read_text())
    for old in manifest["published_files"]:
        if (site / old).read_bytes() != (ROOT / manifest["files"][old]).read_bytes():
            raise ValueError(f"Earlier download changed: {old}")
    for old, new in manifest["generated_assets"].items():
        if (site / old).read_bytes() != (site / new).read_bytes():
            raise ValueError(f"Earlier generated asset changed: {old}")
    aliases = len(manifest["published_files"]) + len(manifest["generated_assets"])
    print(f"Verified {len(memos)} memo records, {len(downloads)} downloads, and {aliases} earlier addresses")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--site", type=Path, required=True)
    parser.add_argument("--baseurl", default="/lightwork")
    args = parser.parse_args()
    check(args.site, args.baseurl.rstrip("/"))

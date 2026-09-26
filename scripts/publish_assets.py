#!/usr/bin/env python3
"""Keep earlier download addresses working in the built site."""
import argparse
import json
from pathlib import Path
import shutil

ROOT = Path(__file__).resolve().parents[1]


def contained(root, name):
    path = (root / name).resolve()
    path.relative_to(root.resolve())
    return path


def publish(site, root=ROOT):
    site = Path(site).resolve()
    root = Path(root).resolve()
    manifest = json.loads((root / "docs/file-map.json").read_text())
    copies = []
    for old in manifest["published_files"]:
        new = manifest["files"][old]
        source = contained(root, new)
        copies += [(source, contained(site, new)), (source, contained(site, old))]
    for old, new in manifest["generated_assets"].items():
        copies.append((contained(site, new), contained(site, old)))
    for source, target in copies:
        if not source.is_file():
            raise FileNotFoundError(f"Download source missing: {source}")
        if target.exists() and target.read_bytes() != source.read_bytes():
            raise ValueError(f"Refusing to replace different content at {target}")
    for source, target in copies:
        if source == target:
            continue
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(source, target)
    total = len(manifest["published_files"]) + len(manifest["generated_assets"])
    print(f"Preserved {total} earlier download and stylesheet addresses")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--site", type=Path, required=True)
    args = parser.parse_args()
    publish(args.site)

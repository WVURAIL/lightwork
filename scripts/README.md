# Publishing tools

Run these from the repository root:

| Command | Purpose |
| --- | --- |
| `python3 scripts/build_memo_index.py` | Generate the memo index from `_data/memos.yml` |
| `python3 scripts/build_memo_index.py --check` | Validate the catalog and check the committed index |
| `python3 scripts/publish_assets.py --site _site` | Preserve earlier download addresses after Jekyll builds |
| `python3 scripts/check_site.py --site _site --baseurl /lightwork` | Check rendered links, published downloads, and compatibility copies |

These tools use Python's standard library.

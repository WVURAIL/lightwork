# Contributing

Keep numbered technical memos and their supporting materials in this repository.
Classroom lessons belong in [dspira](https://github.com/WVURAIL/dspira).

## Add a memo or revision

1. Save the PDF in `memos/` as `memo-NNN-rN.pdf`, using its actual memo and revision numbers.
2. Put editable originals in `sources/memos/` with matching names.
3. Update `_data/memos.yml`, retaining the author's title, credits, status, and memo number.
4. Move any replaced PDF into `memos/history/` and update its existing file-map entries.
5. Add its former path to `docs/file-map.json` so earlier download addresses retain that exact revision.
6. Run `python3 scripts/build_memo_index.py` and commit the generated index with the changes.

Do not invent a revision number when the original document has none.
An editable source can be newer than its published PDF; preserve both revision numbers.
Announced memos use `status: announced` without a download link until their PDF is contributed.

## Other files

- Keep printable templates in `templates/`, with related PDFs, SVGs, and images together.
- Put editable template and worksheet sources in `sources/`.
- Keep worksheets and teaching slides in their named folders.
- Store historical computer notes in `reference/`; do not present them as current setup instructions.
- Use lowercase names with hyphens, and underscores for Python files.

Update affected website and DSPIRA lesson links when moving published files.
Keep historical revisions available through the file map and verify their contents after a move.

## Check a change

```sh
python3 scripts/build_memo_index.py --check
python3 -m unittest discover -s tests
bundle exec jekyll build --baseurl /lightwork
python3 scripts/publish_assets.py --site _site
python3 scripts/check_site.py --site _site --baseurl /lightwork
```

The workflow uses the GitHub Pages Jekyll environment and repeats these checks before deployment.

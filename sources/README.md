# Editable originals

- [memos](memos/): Pages and Word originals, named by memo number and revision.
- [templates](templates/): the elevation-axis Python generator and elevation-mount Pages document.
- [worksheets](worksheets/): the Milky Way viewpoints Pages document.
- [papers](papers/): the unnumbered URSI radio-telescope Word manuscript, revision 4.

A newer source does not imply that a matching PDF was published.
The website's current memo PDFs are selected explicitly in `_data/memos.yml`.
Keep original titles, credits, and revision numbers when editing or exporting a document.

The elevation-axis generator needs NumPy and Matplotlib.
Run it from `templates/elevation-axis/` to write its PDF, PNG, and SVG into that folder:

```sh
python3 ../../sources/templates/elevation_axis.py
```

The checked-in template exports remain the original published files.

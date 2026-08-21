<!-- Generated from _data/memos.yml by bin/build_readme.py. Do not edit by hand:
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


0. [LightWork Memo 000](memos/LightWorkMemo000-r3.pdf) Memo inviting contributions to the LightWork Memo Series &mdash; Guidelines for the series, and an invitation to contribute to the topic of citizen science with radio telescopes.
   * Glen Langston, 2017 August 11
1. [LightWork Memo 001](memos/LightWorkMemo001-01.pdf) First system temperature measurements with a horn antenna
2. [LightWork Memo 002](memos/LightWorkMemo002-r2.pdf) Report on system temperature after a number of modifications
3. [LightWork Memo 003](memos/LightWorkMemo003-r2.pdf) Measurements of system gain as a function of feed probe placement
4. [LightWork Memo 004](memos/LightWorkMemo004-r3.pdf) Full system description of the first working horn antenna
5. *(never used)*
6. [LightWork Memo 006](memos/LightWorkMemo006-r6.pdf) Sketch of amplifier board design for citizen science radio telescopes
7. *(never used)*
8. [LightWork Memo 008](memos/LightWorkMemo008-r1.pdf) Performance of an amplifier system using low-cost LNA4ALL amplifiers
9. [LightWork Memo 009](memos/LightWorkMemo009-r3.pdf) Performance of an amplifier system using ZX60-P103LN+ amplifiers
10. [LightWork Memo 010](memos/LightWorkMemo010-4.pdf) Measurements with an aluminium foam board horn and improved infrastructure
11. *(never used)*
12. *(never used)*
13. *(never used)*
14. [LightWork Memo 014](memos/LightWorkMemo014r9.pdf) Galactic mapping with horn and amplifier box
15. [LightWork Memo 015](memos/LightWorkMemo015-2.pdf) Science Aficionados Amplifier Box B
16. [LightWork Memo 016](memos/LightWorkMemo016-1.pdf) Commercial parts list for Amplifier Box B
17. *(never used)*
18. [LightWork Memo 018](memos/LightWorkMemo018-r1.pdf) Galactic spectra data overview
19. [LightWork Memo 019](memos/LightWorkMemo019-r1.pdf) Mapping the Milky Way
20. [LightWork Memo 020](memos/LightWorkMemo020-r5.pdf) Radio astronomy with GNU Radio Companion
21. [LightWork Memo 021](memos/LightWorkMemo021-r6.pdf) Horn telescope base construction guide
22. [LightWork Memo 022](memos/LightWorkMemo022-r14.pdf) Horn telescope construction guide
23. [LightWork Memo 023](memos/LightWorkMemo023-r2-EventCapture.pdf) Event capture with the ADALM Pluto (**under construction**)
24. [LightWork Memo 024](memos/LightWorkMemo024-r2-Armed.pdf) Milky Way Galaxy armed and dangerous (**under construction**)
25. [LightWork Memo 025](memos/LightWorkMemo025-r5-DetectingPulsars.pdf) Sensitivity of horn radio telescopes for detecting pulsars
26. [LightWork Memo 026](memos/LightWorkMemo026-r2-CalibrateMaps.pdf) Calibration and imaging steps (**under construction**)
27. [LightWork Memo 027](memos/LightWorkMemo027-r2-4HornEvents.pdf) Event detection with four horns (**under construction**)
28. [LightWork Memo 028](memos/LightWorkMemo028-r7-NoiseTemp.pdf) Measure the noise temperature of the first LNA
29. [LightWork Memo 029](memos/LightWorkMemo029-r2-HydrogenLineProject.pdf) Overview of construction and use of a radio telescope
30. [LightWork Memo 030](memos/LightWork0030-r1-ATaleOfThreeLNAs.pdf) A tale of three DSPIRA LNAs &mdash; Construction and analysis of three very high sensitivity versions of the WVU RAIL low-noise amplifiers for radio astronomy.
31. [LightWork Memo 031](memos/LightWorkMemo031.pdf) Additive interferometry with two horn telescopes
32. [LightWork Memo 032](memos/LightWorkMemo032-PailOfMilkyWay-r5.pdf) Gather a pail of Milky Way &mdash; Construction guide for a very small, very sensitive horn radio telescope.
33. [LightWork Memo 033](https://arxiv.org/pdf/2411.00057) A high school student's radio telescope and observations &mdash; A remarkably clear description of building a radio telescope and observing with it. Published on arXiv rather than in this repository.
   * Jack Phelps
34. [LightWork Memo 034](memos/LightWorkMemo034-SimpleBase-r5.pdf) Guide to building a Pail-of-Milky-Way telescope base &mdash; Construction guide for easily pointing a horn radio telescope. (**superseded**)
   * replaced by memo 036
35. [LightWork Memo 035](memos/LightWorkMemo035-ConeHorn-r6.pdf) Guide to building a cone horn telescope &mdash; Construction guide for an even simpler and more sensitive radio telescope.
36. [LightWork Memo 036](memos/LightWorkMemo036-ConeHornBase-r7.pdf) Updated telescope base for the cone horn &mdash; Simpler to build than the base in memo 34, and works with the cone horn.
   * replaces memo 034
37. LightWork Memo 037 Finding pointing offsets from 24 hours of observations &mdash; Named and numbered by its author; the PDF has not been contributed yet. (**announced, PDF not yet contributed**)

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

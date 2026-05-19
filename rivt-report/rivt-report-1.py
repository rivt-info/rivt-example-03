#! python

"""generate
rivt report

Run this Python file to generate a rivt report. Copy and rename the file
(starting with rivt-report- ...) to save custom report settings. The
setting file is stored in the rivt folder (root folder) and published
to the _published folder.

For PDF and text reports the script re-reads and formats each rivt file but
does not rewrite the individual files unless specified in the
settings (note: rewriting docs adds execution time). HTML docs are always
rewritten.

Modify the report settings between the double lines where needed.
See https://www.rivt.info for more details.
"""

# ========= Modify the report settings between the double lines ==============
iniS = """
[report]
; ---------- report settings --------------------------------------------------
;
;           report name including extension (pdf, html, txt)
;
repname = rivt-treehouse-report.pdf
;
;           comma separated list of excluded doc numbers eg. rv102, rv204
;
exclude = -- 
;
;           regenerate pdf or text doc files - true or false
;
regen = false 
;
;           clear _restpdf, docs, pdfdocs and textdocs folders before new report   
;
;clean_published = false
;
;           include report cover page - true or false
;
cover = true 
;
;           logo path starts in rivt-folder, logo size in % page width
;
coverlogo = src/img/tree1.png
coverlogo_size = 50
title = Treehouse Design 
subtitle = example rivt report
client = user example
projectref = proj. 0001
authors = R Holland 
copyright = StL
version = 1.0.0a12
;
;           logo paths start in rivt folder
;
running_logo = src/img/rivt02.png 
running_label = rivt
;
;          letter, legal, A4
;
pdf_pagesize = letter 
;
;          margin values for top, right, bottom and left
;
pdf_margins = 1in, 1in, 1in, 1in 
;
;         underline links in PDF - true or false
;
pdf_link = true 
;
; ------------- end settings --------------------------------------------------
;
"""
# ============================================================================

# the following line is required after the settings
import rivtlib.rvreport  # noqa: E402, F401

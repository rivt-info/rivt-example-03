#! python

"""generate rivt report

Run this Pyton file to generate a rivt report. Copy and rename the file
(starting with rivt-report- ...) to save custom report settings. The
setting file is stored in the rivt folder (root folder) and published
to the _published folder.

For PDF and text reports the script re-reads and formats each rivt file but
does not rewrite the individual PDF and text doc files unless specified in the
settings (note: rewriting docs adds execution time). HTML docs are always
rewritten.

Modify the report settings between the double lines where needed.
See https://www.rivt.info for more details.
"""

# ========= Modify the report settings between the double lines ==============
iniS = """
[report]
; ---------- report settings -------------------------------------
; - comma separated list of excluded doc numbers eg. rv102, rv204
exclude = -- 
;
; - regenerate pdf and text doc files - true or false
regen = false 
;
; - report name with extension (pdf, html, txt)
repname = rivt-treehouse-report.pdf 
;
; --------------cover format ---------------------------------------------------
; include report cover page - true or false
cover = true 
; - logo path starts in rivt folder
;
coverlogo = src/img/tree1.png 
title = Treehouse Design Report
subtitle = example rivt report
client = user example
projectref = proj. 0001
; - separate multiple authors with commas
authors = R Holland 
copyright = StL
; ------------- running typography settings -----------------------------------
version = 1.0.0a11
; - logo path starts in rivt folder
running_logo = src/img/logo2.png 
running_label = rivt
; - letter, legal, A4
pdf_pagesize = letter 
; - top, right, bottom, left
pdf_margins = 1in, 1in, 1in, 1in 
; - underline links in PDF - true or false
pdf_link = true 
"""
# ============================================================================

# this import line is required following the settings
import rivtlib.rvreport  # noqa: E402, F401

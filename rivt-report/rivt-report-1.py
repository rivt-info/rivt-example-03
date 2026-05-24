#! python
"""generate rivt report

Run this Python script in the rivt-report folder to write reports to the
_published folder. Copy and rename this file to save custom report settings
(e.g. rivt-folder-new.py).

The script does not regenerate individual PDF docs unless specified in the
settings. Regenerating individual PDF docs adds execution time. HTML and text
docs are always regenerated. See https://www.rivt.info for more details.
"""

# ========= Modify report settings between the double lines ==============
iniS = """
[report]
;----- report file name including extension (pdf, html, txt)
rept_filename = rivt-treehouse-report.txt
;----- regenerate pdf or text doc files - true or false
regen = false 
;----- comma separated list of excluded doc numbers eg. rv102, rv204
exclude = -- 
;----- initialize/clear the _restpdf, docs, pdfdocs and txtdocs folders
keep_files = true
; update the configuration files from rivt before publishing
auto_cfg = true
;----- paths start in report-folder, logo size is % page width
title = Treehouse Design 
subtitle =rivt report
coverlogo = rvsrc/img/tree1.png
coverlogo_size = 50
client = Example
project_ref = Proj. 0001
authors = R Holland 
copyright = StL
version = 1.0.0a12
;----- logo and labels for header and footer
running_logo = rvsrc/img/rivt02.png 
running_label = rivt
;----- page size letter, legal, A4 - margins top, right, bottom and left
pdf_pagesize = letter
pdf_margins = 1in, 1in, 1in, 1in 
;----- underline links in PDF - true or false
pdf_link = true 
"""
# ============================================================================
# the following line is required after settings
import rivtlib.rvreport  # noqa: E402, F401

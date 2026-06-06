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
[settings]
;------- report file name including the extension - pdf, html, txt
;-----------------------------------------
rept_filename = rivt-treefort-report.pdf
;------------------------------------------
;------- comma separated list of excluded doc numbers eg. rv102, rv204
exclude = -- 
;-------  rivt writes config files, false allows for manual editing
auto_cfg = true
;------- regenerate pdf doc files 
regen_pdf = false 

[format]
title = Tree Fort Design 
subtitle =rivt report
client = Report Example
project_ref = Proj. 0001
authors = R Holland 
copyright = StL
version = 1.0.0a12
;----- logo, header, footer files are in *page* folder, size is % page width
coverlogo = tree1.png
coverlogo_size = 50
running_logo = rivt02.png 
running_label = rivt
;----- underline links in PDF - true or false
pdf_link = true 
;----- page size letter, legal, A4 - margins top, right, bottom and left
pdf_pagesize = letter
pdf_margins = 1in, 1in, 1in, 1in 
"""
# ============================================================================
# the following line is required after settings
import rivtlib.rvreport

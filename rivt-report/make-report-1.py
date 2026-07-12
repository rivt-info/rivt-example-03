#! python
"""generate a rivt report

Run this Python script in the rivt-report folder to write reports to the
_published folder. Copy and rename this file to save custom report settings
(e.g. make-report-new.py).

To save execution time the script does not regenerate individual PDF docs
unless specified in the settings. HTML and text docs are always regenerated.
See https://www.rivt.info for more details.

The report may be published in each format in a single compilation. 
"""

import os
import sys
import importlib

# ==== Modify report settings between the double lines ========================
# ==== Edit typeS list with desired output formats ["txt","pdf","html"] =======
# ==== Update rept_filename, must start with rivt- , do not modify .{typeS} ===
for typeS in ["txt"]:  
    reportsetS = f"""
    [report]
    ;-----------------------------------------
    rept_filename = rivt-treefort-report.{typeS}
    version = 1.0.0a13
    exclude = -- ; comma separated doc numbers to exclude eg. rv102, rv204
    [process]
    ;-----------------------------------------
    auto_cfg = true ; writes config files, false allows for manual editing
    regen_pdf = false ; regenerate pdf doc files 
    rep_verbose = true ; generate report - verbose output
    [layout]
    ;--------------- cover page and runner settings
    ;--- add logo files to rvsrc/img folder, size is % page width
    title = Tree Fort
    subtitle = Structural Design
    client = Report Example
    project_ref = Proj. 0003
    authors = R Holland 
    copyright = StL
    coverlogo = tree1.png
    coverlogo_size = 50
    running_logo = rivt02.png 
    running_label = rivt
    ;---------------- PDF settings
    ; colors: red, blue, green, black, gray, brown, maroon, gray, olive, cyan
    ; margins: top, right, bottom, left    page size: letter, legal, A4 
    pdf_link_underline = false
    pdf_link_color = blue
    pdf_pagesize = letter
    pdf_margins = 1in, 1in, 1in, 1in 
    ;------------- TOC levels
    ; 1: include subdivisions    2: include subdivisions and sections
    toc_level = 1
    """
    # ============================================================================
    # the following lines are required following the settings
    # set variables to pass on each loop
    os.environ["reportset"] = reportsetS
    module_name = 'rivtlib.rvreport'
    if module_name in sys.modules:
        # Reloads the module on subsequent iterations
        importlib.reload(sys.modules[module_name])
    else:
        # Loads the module for the very first time
        __import__(module_name)
    
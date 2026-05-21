#! python

import rivtlib.rvapi as rv

# the following inital settings are only needed if defaults are overridden
# The leading hash and semicolon are required
# rv setwidth = 80  ; set width of text output (default 80 characters)
# rv setpublic = false ; heading changed to public (default false - private)
# rv addtag = false ; API tag is added to each section number (default false)
# rv makefolders = true ; generate rivt folders if needed (default true)
# rv cleanfolders = false ; clean rivt folders (default false)
# rv updateconfig = true ; update config files from rivt file (default true)

rv.I("""Summary

    This report covers the structural design of a treehouse in Novato,
    California. The design follows the requirements of the California Building
    Code (CBC).
    
    The treehouse is supported by a single Douglas fir beam spanning 12 feet
    between two trees. The beam supports a uniformly distributed load (UDL)
    from the treehouse floor and live load from occupants. The design includes
    calculations for the required beam size and material properties to ensure
    safety and compliance with building codes.

    """)


rv.I("""Load Combinations and Geometry 

    Dead and live load contributions to beam UDL.

    ASCE 7-05 Load Effects _[T]
    =============   ==============================================
    Equation No.    Load Combination
    =============   ==============================================
    16-1            1.4(D+F)
    16-2            1.2(D+F+T) + 1.6(L+H) + 0.5(Lr or S or R)
    16-3            1.2(D+F+T) + 1.6(Lr or S or R) + (f1L or 0.8W)
    =============   ==============================================

    | IMAGE | src/img/tree3d.png | Treehouse, 40, num
    
    """)


# %% doc
rv.D("""Publish Doc

    _[[METADATA]] 
    [doc]
    authors = R Holland
    version = 1.0.0a11
    repo = https://github.com/rivt-info/rivt-single-doc
    license = https://opensource.org/license/mit/
    copyright = --
    fork1_authors = --
    fork1_version = --
    fork1_repo = --
    fork1_license = https://opensource.org/license/mit/

    [layout]
    coverlogo = src/img/tree3d.png
    coverlogo_size = 50
    runninglogo = src/img/logo2.png
    runninglabel = rivt
    title = Treehouse Design
    subtitle =  -
    copyright = -
    client = user example
    projectref = 0001
    pdf_pagesize = letter
    pdf_margins = 1in, 1in, 1in, 1in 
    pdf_link_underline = true
    text_width = 80
    clean_publish = false
    _[[END]]

    | PUBLISH | Doc A-1 | text
    """)

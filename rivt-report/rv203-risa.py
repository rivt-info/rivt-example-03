import rivtlib.rvapi as rv

# %% rv.I(r"""Applied deck forces - RISA model 
rv.I(r"""Applied Deck and Railing forces - RISA model 


    | IMAGE | risa4.png | Risa Model, 70, num, not

    | IMAGE | risa9.png | Rail Lateral Forces, 60, num, not

    """)

# %% rv.I(r"""Resultant axial forces - RISA model | pdfpage
rv.I(r"""Resultant axial forces - RISA model | pdfpage

    | IMAGE | risa6.png | Strut Axial Forces, 70, num, not

    """)

# %% rv.I(r"""Top rail shear reactions - RISA model | pdfpage
rv.T(r"""Top rail shear reactions - RISA model | n | text |

    Under the California Building Code (CBC), handrails and guard railings
    must resist a uniform load of 50 plf and a concentrated point load of 200
    lbs, both applied horizontally to the top rail. Intermediate rails,
    balusters, and infill panels must separately withstand a concentrated load
    of 50 lbs.

    Structural Schematic of Railing and Loads (drawn by AI)

      =======  <-- Top Rail
         |     <-- Lateral Load (P)
         | 
         |
         |
         |  Height (h)
         |
         |
         |
         |
    ===========  <-- Fixed Support / Deck Surface
    
    """)


# %% rv.D(r"""Publish Doc 
rv.D(r"""Publish Doc 

    | PUBLISH | RISA Analysis | pdf

    _[[METADATA]] 
    [process]
    ;-----------------------------------------
    doc_verbose = true; if false minmize output during doc processing
    auto_cfg = true ; if false, config files are not updated from rivt file
    [doc]
    ;-----------------------------------------
    authors = R Holland
    version = 1.0.0a13
    repo = https://github.com/rivt-info/rivt-example-03
    license = https://opensource.org/license/mit/
    copyright = --
    fork1_authors = --
    fork1_version = --
    fork1_repo = --
    fork1_license = https://opensource.org/license/mit/
    [layout]
    ;----------------------- cover page and runner settings
    ;--- add logo files to rvsrc/img folder, size is % page width
    subtitle =  Doc Example
    copyright = --
    client = user manual
    coverpage = false
    coverlogo_size = 70
    coverlogo = tree1.png
    runninglogo = logo2.png
    runninglabel = rivt
    project_ref = proj. 0003
    ;------------------------ PDF settings
    ;--- colors: red, blue, green, black, gray, brown, maroon, gray, olive, cyan
    ;--- margins: top, right, bottom, left    page size: letter, legal, A4    
    pdf_link_color = black
    pdf_link_underline = true
    pdf_pagesize = letter
    pdf_margins = 1in, 1in, 1in, 1in 
    ;----------------------- TOC levels
    ;--- 1: include subdivisions   2: include subdivisions and sections
    toc_level = 1
    _[[END]]

    """)

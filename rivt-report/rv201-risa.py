import rivtlib.rvapi as rv

# %% rv.I("""Applied deck forces - RISA model 
rv.I("""Applied deck forces - RISA model 


    | IMAGE | rvsrc/img/risa4.png | Risa Model, 70, num, not

    """)

# %% rv.I("""Resultant axial forces - RISA model | pdfpage
rv.I("""Resultant axial forces - RISA model | pdfpage

    | IMAGE | rvsrc/img/risa6.png | Strut Axial Forces, 70, num, not

    """)

# %% rv.I("""Top rail shear reactions - RISA model | pdfpage
rv.I("""Top rail shear reactions - RISA model | pdfpage

    Under the California Building Code (CBC), handrails and guards (railings)
    must resist a uniform load of 50 plf and a concentrated point load of 200
    lbs, both applied horizontally to the top rail. Intermediate rails,
    balusters, and infill panels must separately withstand a concentrated load
    of 50 lbs.

    _[[TEXT]] text
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
    
    Structural Schematic of Railing and Loads Drawn by AI
    _[[END]]


    | IMAGE | rvsrc/img/risa9.png | Rail Lateral Forces, 60, num, not

    """)


# %% rv.D("""Publish Doc 
rv.D("""Publish Doc 

    | PUBLISH | RISA Analysis | txt

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

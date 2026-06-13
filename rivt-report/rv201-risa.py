import rivtlib.rvapi as rv

rv.I("""Applied deck forces - RISA model 


    | IMAGE | rvsrc/img/risa4.png | Risa Model, 70, num, not

    """)

rv.I("""Resultant axial forces - RISA model | pdfpage

    | IMAGE | rvsrc/img/risa6.png | Strut Axial Forces, 70, num, not

    """)

rv.I("""Top rail shear reactions - RISA model | pdfpage

    Under the California Building Code (CBC), handrails and guards (railings)
    must resist a uniform load of 50 plf and a concentrated point load of 200
    lbs, both applied horizontally to the top rail. Intermediate rails,
    balusters, and infill panels must separately withstand a concentrated load
    of 50 lbs.

    _[[MARKUP]] literal
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


rv.D("""Publish Doc 

    | PUBLISH | RISA Analysis | pdf

    _[[METADATA]] 
    [doc]
    authors = R Holland
    version = 1.0.0a12
    repo = https://github.com/rivt-info/rivt-single-doc
    license = https://opensource.org/license/mit/
    copyright = --
    fork1_authors = --
    fork1_version = --
    fork1_repo = --
    fork1_license = https://opensource.org/license/mit/

    [layout]
    coverlogo = tree1.png
    coverlogo_size = 70
    runninglogo = logo2.png
    runninglabel = rivt
    coverpage = false
    subtitle =  Doc Example
    copyright = --
    client = user manual
    project_ref = proj. 0001
    pdf_pagesize = letter
    pdf_margins = 1in, 1in, 1in, 1in 
    pdf_link_underline = true
    ;----- table of contents levels: = 1 shows subdivisions, = 2 includes sections. 
    toc_level = 1
    
    [process]
    doc_verbose = true; if false, minimum output during doc processing
    auto_cfg = true ; if false, config files are not updated from rivt file
    _[[END]]

    """)

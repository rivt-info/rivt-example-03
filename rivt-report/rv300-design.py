import rivtlib.rvapi as rv

rv.I("""Summary  

    This division covers design of Tree Fort components.

    | IMAGE | rvsrc/img/outputc.jpg | Report Flow Chart, 80, num, not   
    
    """)


|rv.I("""Geometry and Components


    | IMAGE | rvsrc/img/members1.png | Component Labels, 80, num, not   


    | IMAGE | rvsrc/img/dim1.jpg | Dimensions, 80, num, not   

    
    """)

rv.D("""Publish Doc 

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
    
    [process]
    auto_cfg = true ; if false, config files are not updated from rivt file
    _[[END]]

    | PUBLISH | Component Design | pdf

    """)

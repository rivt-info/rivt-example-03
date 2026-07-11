import rivtlib.rvapi as rv


rv.I("""Strut to Tree Connection

    Use Simpson Strong Tie online selection tool.

    | IMAGE | rvsrc/img/ss12.jpg | Screenshot: Option 1, 100, num, time 
    
    | IMAGE | rvsrc/img/ss14.jpg | Screenshot: Option 2, 100, num, time 

    """)

rv.I("""Top rail Corner | pdfpage

    Use AWC online connection tool.

    | IMAGE | rvsrc/img/awc4.jpg | Screenshot: Top Rail - Corner Plate Input, 100, num, not 

    | IMAGE | rvsrc/img/awc5.jpg | Screenshot: Top Rail - Corner Plate Capacity, 100, num, not
 
    Use 4-#8 screws = 55 lbs * 4 = Capacity 220 lbs | Demand = 200 lbs.

    """)

# %% rv.D("""Publish Doc
rv.D("""Publish Doc

    | PUBLISH | Connection Design | pdf

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

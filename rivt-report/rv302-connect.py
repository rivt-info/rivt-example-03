import rivtlib.rvapi as rv


rv.I("""Strut to Tree Connection

    Use Simpson Strong Tie online selection tool.

    | IMAGE | rvsrc/img/ss12.jpg | Option 1, 100, num, time 
    
    | IMAGE | rvsrc/img/ss14.jpg | Option 2, 100, num, time 

    """)

rv.I("""Top rail Corner | pdfpage

    Use AWC online connection tool.

    | IMAGE | rvsrc/img/awc4.jpg | Top Rail - Corner Plate Input, 100, num, not 

    | IMAGE | rvsrc/img/awc5.jpg | Top Rail - Corner Plate Capacity, 100, num, not
 
    Use 4-#8 screws = 55 lbs * 4 = Capacity 220 lbs | Demand = 200 lbs.

    """)

# %% rv.D("""Publish Doc
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
    coverlogo = tree1.png
    coverlogo_size = 70
    coverpage = false
    subtitle =  Doc Example
    client = user manual
    project_ref = proj. 0001
    copyright = --
    runninglogo = logo2.png
    runninglabel = rivt
    pdf_pagesize = letter
    pdf_margins = 1in, 1in, 1in, 1in 
    pdf_link_underline = true
    
    [process]
    auto_cfg = true ; if false, config files are not updated from rivt file
    _[[END]]

    | PUBLISH | Connection Design | pdf

    """)

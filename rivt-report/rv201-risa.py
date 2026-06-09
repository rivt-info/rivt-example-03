# %% rv.V("""Loads and Geometry
import rivtlib.rvapi as rv

rv.I("""RISA Model

    | IMAGE | rvsrc/risa4.png | Risa Model, 70, num, not


    | IMAGE | rvsrc/risa6.png | Strut Axial Forces, 70, num, not


    | IMAGE | rvsrc/risa9.png | Rail Lateral Forces, 70, num, not

    
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
    private_heading = true ; if false, default heading changed to public
    auto_cfg = true ; if false, config files are not updated from rivt file
    _[[END]]

    | PUBLISH | Deck Design | pdf
    """)

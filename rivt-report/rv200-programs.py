# %% rv.V("""Loads and Geometry
import rivtlib.rvapi as rv

rv.I("""Analysis Programs
    
    This report division includes RISA and OpenSees analysis and illustrates
    methods for running and importing outputs from external programs.
    
    - _[U] RISA-3D, https://risa.com/products/risa-3d | for determining connections forces 


    - _[U] OpenSees, https://opensees.berkeley.edu | for determing the period of the tree fort system.
      
    
    | IMAGE | rvsrc/img/outputb.jpg | Report Flow Chart, 80, num, not 
    
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

    | PUBLISH | Analysis | pdf
    """)

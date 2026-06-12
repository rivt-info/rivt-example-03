import rivtlib.rvapi as rv

rv.I("""Load Combinations and Geometry 


    | IMAGE | rvsrc/img/tree4.png | Tree Fort Plan, 50, num, not


    ASCE 7-05 Load Effects _[T]
    =============   ==============================================
    Equation No.    Load Combination
    =============   ==============================================
    16-1            1.4(D+F)
    16-2            1.2(D+F+T) + 1.6(L+H) + 0.5(Lr or S or R)
    16-3            1.2(D+F+T) + 1.6(Lr or S or R) + (f1L or 0.8W)
    =============   ==============================================
    """)


rv.V("""Unit Loads 


    Unit weights imported from csv file created by AI. _[B]

    | TABLE | rvsrc/data/df-wts.csv | Unit Weights - Doug Fir, 25, head, num 


    Variables assigned by inline definitions. _[B]

    Member Nominal Loads and Properties _[T]
    D_1 ==: 2.0 * plf | plf, klf, 2 | 2x6 planks DL         
    D_2 ==: 2.6 * plf | plf, klf, 2 | 2x8 joists DL         
    D_3 ==: 2.9 * plf | plf, klf, 2 | 4x4 posts and struts
    E_1 ==: 29000 * ksi | ksi, MPA, 2 | modulus of elasticity
    LL_1 ==: 40 * psf | psf, kPA, 2 | ASCE7-05 floor LL
    HL_1 ==: 20 * psf | psf, kPA, 2 | ASCE7-05 HL
    
    
    """)

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
    auto_cfg = true ; if false, config files are not updated from rivt file
    _[[END]]

    | PUBLISH | Loads | pdf
    """)

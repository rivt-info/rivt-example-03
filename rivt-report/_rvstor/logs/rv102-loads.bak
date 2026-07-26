import rivtlib.rvapi as rv

# %% rv.I("""Load Combinations and Geometry 
rv.I("""Load Combinations and Geometry 


    | IMAGE | tree4.png | Tree Fort Plan, 50, num, not


    ASCE 7-05 Load Effects _[T]
    =============   ==============================================
    Equation No.    Load Combination
    =============   ==============================================
    16-1            1.4(D+F)
    16-2            1.2(D+F+T) + 1.6(L+H) + 0.5(Lr or S or R)
    16-3            1.2(D+F+T) + 1.6(Lr or S or R) + (f1L or 0.8W)
    =============   ==============================================
    """)


# %% rv.V("""Unit Loads 
rv.V("""Unit Loads 


    Unit weights imported from csv file - table created by AI. _[B]

    | TABLE | df-wts.csv | Unit Weights - Doug Fir, 25, head, num 


    Variables assigned by inline definitions. _[B]

    Member Nominal Loads and Properties _[T]
    D_1 ==: 2.0 * p_ft | p_ft, kN_m, 2 | 2x6 planks DL         
    D_2 ==: 2.6 * p_ft | p_ft, kN_m, 2 | 2x8 joists DL         
    D_3 ==: 2.9 * p_ft | p_ft, kN_m, 2 | 4x4 posts and struts
    E_1 ==: 29000 * k_si | k_si, MPA, 2 | modulus of elasticity
    LL_1 ==: 40 * p_sf | p_sf, kPA, 2 | ASCE7-05 floor LL
    HL_1 ==: 20 * p_sf | p_sf, kPA, 2 | ASCE7-05 HL
    
    
    """)

# %% rv.D("""Publish Doc
rv.D("""Publish Doc

    | PUBLISH | Loads | txt

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

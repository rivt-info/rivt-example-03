# %% rv.V("""Loads and Geometry
import rivtlib.rvapi as rv

rv.V("""Loads 
    
    Successive value definitions are formatted as a table. Variable
    values are defined with the define operator. The line tag [T] labels and
    numbers the table.
    
    Define Unit Loads _[T]
    D_1 ==: 3.8 * psf | psf, kPA, 2 | joists DL         
    D_2 ==: 2.1 * psf | psf, kPA, 2 | plywood DL          
    D_3 ==: 10.0 * psf | psf, kPA, 2 | partitions DL       
    D_4 ==: 2 * 1.5 * klf | klf, kN_m, 2 | fixed machinery DL
    L_1 ==: 40 * psf | psf, kPA, 2 | ASCE7-O5 LL
    b_1 ==: 10 * inch | inch, mm, 2 | beam width
    h_1 ==: 18 * inch | inch, mm, 2 | beam depth
    E_1 ==: 29000 * ksi | ksi, MPA, 2 | modulus of elasticity
    Fb_1 ==: 20000 * psqin | psqin, MPA, 2 | allowable stress   
    
    
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
    coverlogo = src/img/tree3d.png
    coverlogo_size = 50
    runninglogo = logo2.png
    runninglabel = rivt
    title = Treehouse Design
    subtitle =  -
    copyright = -
    client = user example
    projectref = 0001
    pdf_pagesize = letter
    pdf_margins = 1in, 1in, 1in, 1in 
    pdf_link_underline = true
    text_width = 80
    clean_publish = false
    _[[END]]

    | PUBLISH | Doc A-2 | text
    """)

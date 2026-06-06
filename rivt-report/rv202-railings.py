# %% rv.V("""Loads and Geometry
import rivtlib.rvapi as rv


rv.I("""Introduction

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
    
    Structural Schematic of Railing and Loads
    
    _[[END]]


    """)


rv.V("""Railing Design 

    | PYTHON | rvsrc/scripts/sectprop2.py | Import Functions


    Design properties.
    
    _[[ARGS]] post1 | units: inch, pounds
    h_1 = 42.  # post height
    P_1 = 200  # concentrated load 
    b_1 = 3.5  # post width
    d_1 = 3.5  # post depth
    E_1 = 1.5*(10**6)  # modulus of elasticity
    F_b = 1000  # allowable bending stress
    C_D = 1.0   # load duration factor
    C_M = 0.85  # wet service factor
    C_F = 1.0   # size factor
    C_t = 1.0   # temperature factor
    C_i = 0.8   # incising factor
    C_r = 1.0   # repetitive member factor
    C_c = 1.0   # curvature factor
    C_L = 1.0   # beam stability factor
    C_b = 1.0   # bearing area factor
    deflect_limit = 360.0 # max allowable deflection ln_1/deflect_limit
    _[[END]]

    Design Results
    | FUNCTION | nds_post_check, post1, beamchk1, str | Check Deck Beam

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

    | PUBLISH | Railing Design | text
    """)

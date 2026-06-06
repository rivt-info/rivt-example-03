# %% rv.V("""Loads and Geometry
import rivtlib.rvapi as rv

rv.V("""Design Properties
    


    | IMAGE | rvsrc/img/members1.png | Member Designations, 80, num 


    Import deck loads and functions.
    | VALTABLE | rv_stor/v102-2.csv | Load values from rv102-loads.py, 40
     
    | PYTHON | rvsrc/scripts/sectprop2.py | Import Functions

    """)


rv.V("""Deck Design Summary

    Design properties.

    _[[ARGS]] beam1 | units: inch, pounds
    ln_1 = 4*12.  # beam span
    w_1 = 45*.5/12  # uniform linear load 
    b_1 = 5.5  # beam width
    d_1 = 1.5  # beam depth
    E_1 = 1.5*(10**6)  # modulus of elasticity
    F_b = 1000 # allowable bending stress
    C_D = 1.0  # load duration factor
    C_M = 0.85 # wet service factor
    C_F = 1.0  # size factor
    C_t = 1.0  # temperature factor
    C_i = 0.8  # incising factor
    C_r = 1.0  # repetitive member factor
    C_c = 1.0  # curvature factor
    C_L = 1.0  # beam stability factor
    C_b = 1.0  # bearing area factor
    deflect_limit = 240.0 # max allowable deflection ln_1/deflect_limit
    _[[END]]


    Design Results
    | FUNCTION | nds_beam_check, beam1, beamchk1, str | Check Deck Beam

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

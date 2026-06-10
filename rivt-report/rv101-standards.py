#! python

import rivtlib.rvapi as rv

rv.I("""Summary

    The design loads are based on the standards of the California Building
    Code (CBC) outlined below.  Standard math symbols are profided for reference.

    | TABLE | rvsrc/data/bldgstd.csv | California Building Standards, 40, head, num 
    


    Math Abbreviations _[T]
    ================== ============================================================
    Abbreviation        Definition
    ================== ============================================================
    :math:`D`            dead load
    :math:`L`            live load
    :math:`D_m`          module dead load
    :math:`E`            earthquake load
    :math:`F_a`          acceleration site coefficient
    :math:`F_v`          velocity site coefficient
    :math:`F_N`          normal wind force
    :math:`GC_{Ms}`      net moment static coefficient
    :math:`GC_{Md}`     net moment dynamic coefficient
    :math:`GC_M`         net moment coefficient
    :math:`GC_P`         net pressure coefficient
    :math:`GC_{Ps}`      net static pressure coefficient
    :math:`GC_{Pd}`      net dynamic pressure coefficient
    :math:`k_1`         hazard coefficient
    :math:`k_2`         terrain and structure coefficient
    :math:`k_3`         topography coefficient
    :math:`K_{zt}`      topographic Factor
    :math:`K_z`         velocity pressure exposure coefficient
    :math:`MRI`         mean return interval
    :math:`p_d`         net design wind pressure on module - Pa
    :math:`SDOF`        single degree of freedom
    :math:`S_s`         short period mapped acceleration
    :math:`S_D{S}`     site design response acceleration
    :math:`S_1`         1 second period mapped acceleration
    :math:`S_M{S}`     short period parameter
    :math:`S_{M1}`      1 second period parameter
    :math:`T`           fundamental period of structure
    :math:`M_{tor}`     wind moment about panel center
    :math:`T_0`         short period spectral cap
    :math:`T_S`         long period spectral cap
    :math:`V_b`         basic wind speed
    :math:`V_B`         seismic design base shear
    :math:`W`           wind load / seismic weight of structure
    :math:`F_b`         NDS - Reference bending design value
    :math:`F_t`         NDS - Reference tension design value
    :math:`F_v`         NDS - Reference shear design value
    :math:`F_{Cperp}`   NDS - Reference compression perpendicular to grain 
    :math:`F_c`         NDS - Reference compression parallel to grain 
    :math:`E`           NDS - Modulus of elasticity
    :math:`E_{min}`     NDS - Reference modulus for stability and stiffness
    :math:`G`           NDS - Specific gravity
    :math:`C_D`         NDS - Load duration factor
    :math:`C_M`         NDS - Wet service factor
    :math:`C_F`         NDS - Size factor
    :math:`C_{fu}`      NDS - Flat use factor
    :math:`C_i`         NDS - Incising factor
    :math:`C_r`         NDS - Repetitive member factor
    :math:`C_t`         NDS - Temperature factor
    :math:`C_c`         NDS - Curvature factor
    :math:`C_l`         NDS - Column stability factor
    :math:`C_L`         NDS - Beam stability factor
    :math:`C_p`         NDS - Column stability factor
    :math:`C_b`         NDS - Bearing area factor
    :math:`C_T`         NDS - Buckling stiffness factor
    :math:`C_{s}`       NDS - Slenderness factor
    :math:`C_{T}`       NDS - Buckling stiffness factor
    :math:`F'_{b}`      NDS - Adjusted bending design value
    :math:`F'_{t}`      NDS - Adjusted tension design value
    :math:`F'_{v}`      NDS - Adjusted shear design value
    :math:`F'_{Cperp}`  NDS - Adjusted compression perpendicular 
    :math:`F'_{c}`      NDS - Adjusted compression parallel to grain 
    :math:`E'`          NDS - Adjusted modulus of elasticity
    :math:`E'_{min}`    NDS - Adjusted modulus ofor stability and stiffness
    ================== ============================================================
    
    """)


# %% doc
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
    
    [process]
    auto_cfg = true ; if false, config files are not updated from rivt file
    _[[END]]

    | PUBLISH | Building Standards | pdf
    """)

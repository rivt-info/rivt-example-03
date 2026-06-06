
--------------------------------------------------------------------------------
Railing Design | R Holland | v-1.0.0a12 | 2026-06-03 - 06:18PM
--------------------------------------------------------------------------------


2.2.1  Introduction
--------------------------------------------------------------------------------
 
Under the California Building Code (CBC), handrails and guards (railings)
must resist a uniform load of 50 plf and a concentrated point load of 200
lbs, both applied horizontally to the top rail. Intermediate rails,
balusters, and infill panels must separately withstand a concentrated load
of 50 lbs.
 
 
 
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
 
 

 
 
 

2.2.2  Railing Design
--------------------------------------------------------------------------------
 

Table 1: Import Functions (rvsrc/scripts/sectprop2.py)

===============================  ============================================
Function                         Docstring
===============================  ============================================
rectsect(b, d)                   section modulus of rectangle
rectinertia(b, d)                moment of inertia of rectangle
midspan_delta(ln, w, e, i)       mid-span deflection of simply supported beam
                                 with UDL
bending_stress_udl(ln, w, b, d)  Maximum bending stress in a simply supported
                                 beam with UDL.
nds_beam_check(** kwargs)        Check stress and deflection for a simply
                                 supported wood beam using NDS.
nds_post_check(** kwargs)        Check stress at cantilever post
===============================  ============================================

 
 
Design properties.
 
    Function Arguments Dictionary : post1 (units: inch, pounds)
    ===========================================================================
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
    ===========================================================================


 
Design Results
┌  Eq-1 | Check Deck Beam
│
│       nds_post_check | units: inch, pounds
└


Post Check Results:
===============================    
P: 200.00
fb: 1175.51
Fb_prime: 680.00
E_prime: 1275000.00
stress_ratio: Not OK
deflection: 1.55
deflection_ratio:  Not OK



 
 

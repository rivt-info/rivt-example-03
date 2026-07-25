
--------------------------------------------------------------------------------
| rivt | Member Design | R Holland | v-1.0.0a13 | 2026-07-25 - 06:26AM
--------------------------------------------------------------------------------


3.3-1 | Deck Design Properties
================================================================================
 
Import deck loads and functions.


 

Table 1: Values from rv102-loads.py (v102-2.csv)
==========  =============  =============  =====================
variable    value          [value]        description
==========  =============  =============  =====================
D_1         2.00 lb_ft     0.03 kN_m      2x6 planks DL
D_2         2.60 lb_ft     0.04 kN_m      2x8 joists DL
D_3         2.90 lb_ft     0.04 kN_m      4x4 posts and struts
E_1         29000.00 k_si  199947.96 MPA  modulus of elasticity
LL_1        40.00 p_sf     1.92 kPA       ASCE7-05 floor LL
HL_1        20.00 p_sf     0.96 kPA       ASCE7-05 HL
==========  =============  =============  =====================


 
 

Table 2: Import Functions (checks.py)

=========================  ========================================
Function                   Docstring
=========================  ========================================
nds_beam_check(** kwargs)  Check stress and deflection for a simply
                           supported wood beam using NDS.
nds_post_check(** kwargs)  Check stress at cantilever post
=========================  ========================================

 
 

3.3-2 | Deck Design Summary
--------------------------------------------------------------------------------
 
Design properties as dictionary for checking function nds_beam_chk
 
    Function Arguments Dictionary : beam1 (units: inch, pounds)
    ===========================================================================
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
    ===========================================================================


 
 
Design Results


 
 
 

3.3-3 | Strut
--------------------------------------------------------------------------------
 
Check strut D/C ratio with BeamChek 2023
 
          ----------------------------------------
Fig. 1 - Screenshot: Strut Check [file: bmck1.jpg  ]
          ----------------------------------------

 
 

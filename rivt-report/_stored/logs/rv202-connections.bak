# %% rv.V("""Loads and Geometry
import rivtlib.rvapi as rv

rv.V("""Table
    

    Define Unit Loads _[T]
    D_1 ==: 3.8 * psf | psf, kPA, 2 | joists DL         
    D_2 ==: 2.1 * psf | psf, kPA, 2 | plywood DL          
    D_3 ==: 10.0 * psf | psf, kPA, 2 | partitions DL       
    D_4 ==: 2 * 1.5 * klf | klf, kN_m, 2 | fixed machinery DL
    
    """)

rv.I("""Summary

    This report covers the structural design of a treehouse in Novato,
    California. The design follows the requirements of the California Building
    Code (CBC).
    
    The treehouse is supported by a single Douglas fir beam spanning 12 feet
    between two trees. The beam supports a uniformly distributed load (UDL)
    from the treehouse floor and live load from occupants. The design includes
    calculations for the required beam size and material properties to ensure
    safety and compliance with building codes.


    """)


rv.I("""Load Combinations and Geometry 

    Dead and live load contributions to beam UDL.

    ASCE 7-05 Load Effects _[T]
    =============   ==============================================
    Equation No.    Load Combination
    =============   ==============================================
    16-1            1.4(D+F)
    16-2            1.2(D+F+T) + 1.6(L+H) + 0.5(Lr or S or R)
    16-3            1.2(D+F+T) + 1.6(Lr or S or R) + (f1L or 0.8W)
    =============   ==============================================

    | IMAGE | src/img/tree3d.png | Treehouse, 40, num
    
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
    runninglogo = logo2.png
    runninglabel = rivt
    subtitle =  -
    copyright = -
    client = user example
    projectref = 0001
    pdf_pagesize = letter
    pdf_margins = 1in, 1in, 1in, 1in 
    pdf_link_underline = true
    text_width = 80
    _[[END]]

    | PUBLISH | Doc 4 | text
    """)

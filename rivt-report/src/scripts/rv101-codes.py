#! python
# %% Start
import rivtlib.rvapi as rv


# rv setpublic = false
# a true setting flips all section headers from private to public - default private
# rv setwidth = 80
# sets width of text output - default 80 characters
# rv addtag = false
# a true setting adds the API tag to each section number - default false

rv.I("""Summary

    The structural design of several components of a treehouse platform is
    provided.




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

    | IMG | /src/ins/panels01.PNG | 0.35, Beam Geometry _[F]
    
    "Title of Article." Wikipedia, Wikimedia Foundation, Day Mo. Year last updated,
    URL. Accessed Day Mo. Year.

    """)

# %%
rv.V("""Loads and Geometry 

    Beam Loads and Properties _[T]
    D_1 := 3.8*PSF | KPA, 2 | joists DL         
    D_2 := 2.1*PSF | KPA, 2 | plywood DL          
    D_3 := 10.0*PSF | KPA, 2 | partitions DL       
    D_4 := 2*0.5*KLF | KNLM, 2 | fixed machinery  DL
    L_1 := 40*PSF | KPA, 2 | ASCE7-O5 LL 
    
    | VALUE | rvlocal | v-beam1.csv | Beam Geometry _[T]

    Total UDL factored dead load  _[E]
    dl_1 <= 1.2 * (W_1 *(D_1 + D_2 + D_3) + D_4) | KLF, KNLM, 2 | ASCE7-05 Eq. 16-2

    Total UDL factored live load  _[E]
    ll_1 <= 1.6 * W_1 * L_1 | KLF, KNLM, 2 | ASCE7-05 Eq. 16-2
    
    Total Load  _[E]
    omega_1 <= dl_1 + ll_1 | KLF, KNLM, 2 | ASCE7-05 Eq. 16-2

    Bending moment at mid-span  _[E]
    m_1 <= omega_1 * S_1**2 / 8 | KIP_FT, KN_M, 2 | mid-span UDL moment 

    """)

# %%
rv.S("""Publish Doc

    _[[METADATA]] 
    [doc]
    authors = R Holland
    version = 1.0.0a11
    repo = https://github.com/rivt-info/rivt-single-doc
    license = https://opensource.org/license/mit/
    copyright = -
    fork1_authors = -
    fork1_version = -
    fork1_repo = -
    fork1_license = 
    
    [layout]
    coverlogo = tree3d.png
    runninglogo = logo2.png
    runninglabel = rivt
    subtitle =  -
    copyright = -
    client = user example
    projectnum = 0003
    pdf_pagesize = letter
    pdf_margins = 1in, 1in, 1in, 1in 
    pdf_link_underline = true
    text_width = 80
    _[[END]]

    | PUBLISH | Treehouse Loads | html

    """)

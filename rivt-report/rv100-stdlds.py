#! python

import rivtlib.rvapi as rv

# The following settings are needed if defaults need to be changed (defaults
# in parenthesis). A leading hash (#) and trailing semicolon (;) are required.

# rv set_width = 80  ; character width of text output (80)
# rv no_tag = true ; if false, the API type is added to section number (true)


# %% rv.I("""Summary
rv.I("""Summary

    This report covers the structural design of a treehouse in Novato,
    California. The treehouse is supported by a mature maple tree with an
    24-inch diameter trunk. The design is based on the requirements of the
    California Building Code (CBC).
    
    The design report is organized into the following sections:

    | IMAGE | rvsrc/img/reportflow.png | Treehouse Report - Flow Chart, 65, num, time

    """)


# %% rv.I("""Drawing Symbols | pdfpage
rv.I("""Drawing Symbols | pdfpage

    **Drawing Abbreviations** _[T]
    ============ ==============================================
    Abbreviation   Definition
    ============ ==============================================
    ASD           Allowable Stress Design
    ACI           American Concrete Institute
    AISC          American Institute of Steel Construction
    AISI          American Iron and Steel Institute
    ASTM          American Society for Testing and Materials
    AWS           American Welding Society
    AB            Anchor Bolt
    BDRY          Boundry
    CBC           Califiornia Building Code
    CRC           Califiornia Residential Code
    CIP           Cast-In-Place
    CLR           Clear
    CONC          Concrete
    CMU           Concrete Masonry Unit
    CRSI          Concrete Reinforcing Steel Institute
    CONST JT      Construction Joint
    CONT          Continuous
    CJ            Control Joint
    D-C           Demand-Capacity (ratio)
    DIA           Diameter
    DIM           Dimension
    EA            Each
    EF            Each Face
    EJ            Expansion Joint
    ES            Each Side
    EW            Each Way
    EXP Bolt      Expansion Bolt
    EXP JT        Expansion Joint
    FTG           Footing
    FND           Foundation
    GALV          Galvanized
    GA            Gauge
    GR            Grade
    HT            Height
    IN            Inch
    ID            Inside Diameter
    ICBO          International Conference of Building Officials
    K             Kip (1000 Pounds)
    LWC           Light Weight Concrete
    LRFD          Load and Resistance Factor Design
    NWC           Normal Weight Concrete
    NIC           Not in Contract
    OC            On Center
    OD            Outside Diameter
    OPNG          Opening
    PVC           Polyvinyl Chloride
    PSF           Pounds per Square Foot
    PSI           Pounds per Square Inch
    R             Radius
    REINF         Reinforced
    SIM           Similar
    SOG           Slab on Grade
    SL            Splice Length
    SQ            Square
    STD           Standard
    SDI           Steel Deck Institute
    SF            Step Footing or Square Foot
    SYM           Symmetrical
    THK           Thick or Thickness
    T&B           Top and Bottom
    T&G           Tongue and Groove
    TOC           Top of Concrete
    TOF           Top of Foundation
    TOS           Top of Steel
    TOW           Top of Wall
    TYP           Typical
    UNO           Unless Noted Otherwise
    WWF           Welded Wire Fabric
    W/            With
    WP            Working Point
    ============ ==============================================

""")

# %% rv.D("""Publish Doc
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
    private_heading = true ; if false, default heading changed to public
    auto_cfg = true ; if false, config files are not updated from rivt file
    _[[END]]

    | PUBLISH | Standards and Loads | pdf
    """)

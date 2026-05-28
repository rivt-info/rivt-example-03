
--------------------------------------------------------------------------------
Doc A-1 | R Holland | v-1.0.0a11 | 2026-05-28 - 03:35PM
--------------------------------------------------------------------------------


1.1  Summary
--------------------------------------------------------------------------------
 
This report covers the structural design of a treehouse in Novato,
California. The design follows the requirements of the California Building
Code (CBC).
 
The treehouse is supported by a single Douglas fir beam spanning 12 feet
between two trees. The beam supports a uniformly distributed load (UDL)
from the treehouse floor and live load from occupants. The design includes
calculations for the required beam size and material properties to ensure
safety and compliance with building codes.
 
 

1.2  Load Combinations and Geometry
--------------------------------------------------------------------------------
 
Dead and live load contributions to beam UDL.
 

Table 1: ASCE 7-05 Load Effects
=============   ==============================================
Equation No.    Load Combination
=============   ==============================================
16-1            1.4(D+F)
16-2            1.2(D+F+T) + 1.6(L+H) + 0.5(Lr or S or R)
16-3            1.2(D+F+T) + 1.6(Lr or S or R) + (f1L or 0.8W)
=============   ==============================================
 
          ----------------------------------------
Fig. 1 - Treehouse [file: rvsrc/img/tree3d.png ] 
          ----------------------------------------

 
 

1.3  Symbols
--------------------------------------------------------------------------------
 
 
 

Table 2: **Math Symbols**
================== ============================================================
Abbreviation        Definition
================== ============================================================
D                   dead load
L                   live load
D_m                 module dead load
E                   earthquake load
F_a                 acceleration site coefficient
F_v                 velocity site coefficient
:math:`F_N`         normal wind force
GC_M_s              net moment static coefficient
:math:`GC_{M{_d}}`  net moment dynamic coefficient
:math:`GC_M`        net moment coefficient
GC_P                net pressure coefficient
GC_P_s              net static pressure coefficient
GC_P_d              net dynamic pressure coefficient
k_1                 hazard coefficient
k_2                 terrain and structure coefficient
k_3                 topography coefficient
Kzt                 topographic Factor
K_z                 velocity pressure exposure coefficient
MRI                 mean return interval
p_d                 net design wind pressure on module - Pa
SDOF                single degree of freedom
S_s                 short period mapped acceleration
S_D_S               site design response acceleration
S_1                 1 second period mapped acceleration
S_M_S               short period parameter
S_M_1               1 second period parameter
T                   fundamental period of structure
M_t_o_r             wind moment about panel center
T_0                 short period spectral cap
T_S                 long period spectral cap
V_b                 basic wind speed
V_B                 seismic design base shear
W                   wind load / seismic weight of structure
================== ============================================================
 
 
 

Table 3: **Drawing Abbreviations**
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
 
 


--------------------------------------------------------------------------------
| rivt | Open Sees Analysis | R Holland | v-1.0.0a12 | 2026-06-26 - 11:48PM
--------------------------------------------------------------------------------


2.2 | OpenSees Analysis
================================================================================
 
This section analyzes the period of the tree + tree fort system. The
OpenSees model is schematically shown below:
 
        y
        ^
        |
    m2  o  Node 3 (Branches)
        |
    k2  |   Spring 2 (upper trunk)
        |
    m1  o  Node 2 (Tree Fort)
        |
    k1  |   Spring 1 (lower trunk)
        |
        o  Node 1 (Fixed Base)
    -----------
    (Ground)

AI schematic model of tree + tree-fort system

 
 

2.2 - 2 | osp-mod1 Model values
--------------------------------------------------------------------------------
 
 
==========  =======  =========  =================================
variable    value    [value]    description
==========  =======  =========  =================================
mass1       1.5      1.5        mass of tree fort, kN/g
mass2       3.5      3.5        mass of branches, kN/g
trk1        1100     1100       lower tree trunk stiffness, kN/cm
trk2        2100     2100       upper tree trunk stiffness, kN/cm
==========  =======  =========  =================================
 
 

2.2 - 3 | Insert ops-mod1 Output
--------------------------------------------------------------------------------
 
Model Input
 
 
 

2.2 - 4 | Model plots and output
--------------------------------------------------------------------------------
 
 
Model Plots


 
          ----------------------------------------
Fig. 1 - OPS Model  | Fig. 2 - OPS First Mode 
files: rvsrc/img/figure1.png, rvsrc/img/figure2.png 
          ----------------------------------------


 
 
Model Output


 
 
 

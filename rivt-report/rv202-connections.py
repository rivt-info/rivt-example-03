.. |s| unicode:: 0xA0 



.. |blklogo| image:: ../src/--
:height: 100px
:alt: logo





.. contents:: Table of Contents 
:depth: 4

|


.. header::
.. list-table::
    :class: header-box
    :align: left
    :widths: 90 10
    
    * - **rivt-report-example.pdf** - v1.0.0a11 |s| |s| |s| |s| Sect: **###Section###**
        - p. **###Page###**   

        

.. footer:: 
.. list-table::
    :class: footer-box
    :align: left
    :widths: 84 22 16
    
    * - 2026-05-15 |s| |s| |s| **|** |s| |s| |s| R Holland        
        - **rivt**        
        - |blklogo|

                



Doc 1
======================================================================



**1-1**.1 Summary
--------------------------------------------------------------------------------
 
This report covers the structural design of a treehouse in Novato,
California. The design follows the requirements of the California Building
Code (CBC).
 
The treehouse is supported by a single Douglas fir beam spanning 12 feet
between two trees. The beam supports a uniformly distributed load (UDL)
from the treehouse floor and live load from occupants. The design includes
calculations for the required beam size and material properties to ensure
safety and compliance with building codes.
 
 
 



------------

**1-1**.2 Load Combinations and Geometry
--------------------------------------------------------------------------------
 
Dead and live load contributions to beam UDL.
 

**Table 1**: ASCE 7-05 Load Effects


=============   ==============================================
Equation No.    Load Combination
=============   ==============================================
16-1            1.4(D+F)
16-2            1.2(D+F+T) + 1.6(L+H) + 0.5(Lr or S or R)
16-3            1.2(D+F+T) + 1.6(Lr or S or R) + (f1L or 0.8W)
=============   ==============================================
 

.. figure:: c:/git/rivt-example-03-git/rivt-report/src/img/tree1.png
    :width: 0.3%
    :align: center

    **Fig. 1** - Treehouse 
    

 
 
Doc 2
======================================================================



**1-2**.1 Loads and Geometry
--------------------------------------------------------------------------------
 
Successive value definitions are formatted as a table. Variable
values are defined with the define operator. The line tag [T] labels and
numbers the table.
 

**Table 1**: Define Unit Loads


==========  ===============  =============  =====================
variable    value            [value]        description
==========  ===============  =============  =====================
D_1         3.80 psf         0.18 kPA       joists DL
D_2         2.10 psf         0.10 kPA       plywood DL
D_3         10.00 psf        0.48 kPA       partitions DL
D_4         3.00 klf         43.78 kN_m     fixed machinery DL
L_1         40.00 psf        1.92 kPA       ASCE7-O5 LL
b_1         10.00 inch       254.00 mm      beam width
h_1         18.00 inch       457.20 mm      beam depth
E_1         29000.00 ksi     199947.96 MPA  modulus of elasticity
Fb_1        20000.00 lb_in2  137.90 MPA     allowable stress
==========  ===============  =============  =====================
 
 
 
Doc 3
======================================================================



**2-1**.1 Introduction
--------------------------------------------------------------------------------
 
Successive value definitions are formatted as a table. Variable
values are defined with the define operator. The line tag [T] labels and
numbers the table.
 

**Table 1**: Define Unit Loads


==========  ===============  =============  =====================
variable    value            [value]        description
==========  ===============  =============  =====================
D_1         3.80 psf         0.18 kPA       joists DL
D_2         2.10 psf         0.10 kPA       plywood DL
D_3         10.00 psf        0.48 kPA       partitions DL
D_4         3.00 klf         43.78 kN_m     fixed machinery DL
L_1         40.00 psf        1.92 kPA       ASCE7-O5 LL
b_1         10.00 inch       254.00 mm      beam width
h_1         18.00 inch       457.20 mm      beam depth
E_1         29000.00 ksi     199947.96 MPA  modulus of elasticity
Fb_1        20000.00 lb_in2  137.90 MPA     allowable stress
==========  ===============  =============  =====================
 
 
 
Doc 4
======================================================================



**2-2**.1 Introduction
--------------------------------------------------------------------------------
 
Successive value definitions are formatted as a table. Variable
values are defined with the define operator. The line tag [T] labels and
numbers the table.
 

**Table 1**: Define Unit Loads


==========  ========  =========  =============
variable    value     [value]    description
==========  ========  =========  =============
D_1         3.80 psf  0.18 kPA   joists DL
D_2         2.10 psf  0.10 kPA   plywood DL
==========  ========  =========  =============
 
 

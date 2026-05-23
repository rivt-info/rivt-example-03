.. |s| unicode:: 0xA0 



.. |blklogo| image:: ../rvsrc/img/logo2.png
   :height: 100px
   :alt: logo


    
.. header::
    .. list-table::
        :class: header-box
        :align: left
        :widths: 90 10
        
        * - **|D.2|** Doc B-2 - v1.0.0a11 |s| |s| |s| |s|  **###Section###**
          - p. **###Page###**   

          

.. footer:: 
    .. list-table::
        :class: footer-box
        :align: left
        :widths: 84 22 16
        
        * - 2026-05-23 |s| |s| |s| **|** |s| |s| |s| R Holland        
          - **rivt**        
          - |blklogo|

                  


**02.1** Table test
--------------------------------------------------------------------------------
 
 

**Table 1**: Define Unit Loads


==========  =========  ==========  ==================
variable    value      [value]     description
==========  =========  ==========  ==================
D_1         3.80 psf   0.18 kPA    joists DL
D_2         2.10 psf   0.10 kPA    plywood DL
D_3         10.00 psf  0.48 kPA    partitions DL
D_4         3.00 klf   43.78 kN_m  fixed machinery DL
==========  =========  ==========  ==================
 
 



------------

**02.2** overview
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

**02.3** Load Combinations
--------------------------------------------------------------------------------
 
Dead and live load contributions to beam UDL.
 

**Table 2**: ASCE 7-05 Load Effects


=============   ==============================================
Equation No.    Load Combination
=============   ==============================================
16-1            1.4(D+F)
16-2            1.2(D+F+T) + 1.6(L+H) + 0.5(Lr or S or R)
16-3            1.2(D+F+T) + 1.6(Lr or S or R) + (f1L or 0.8W)
=============   ==============================================
 

.. figure:: c:/git/rivt-example-03-git/rivt-report/rvsrc/img/tree3d.png
    :width: 40%
    :align: center

    **Fig. 1** - Treehouse 
    

 
 

# HZBC

The High-Z Black Hole Catalog is a database containing information on over 400 supermassive blackholes with redshift greater than 4 (z > 4) taken from various research papers.


Notes:

1. Some entries lack a documented black hole mass and is approximated by, given M1450:

mass = 10 ^ [(- M1450 - 3.459) / 2.5] — [1]

2. There were errors in the papers Mazzucchelli et al. (2017) and Mazzucchelli et al. (2023), where the Eddington ratios (f_Edd) were abnormal. Thus, the f_Edd were recalculated by, given BHM/mass and L_bol:

f_Edd = L_bol / (1.3e38 × MBH) — [2]

Errors are approximated using the error propagation formula:

f_Edd Upper Error = f_Edd × √[(L_bol Upper Error / L_bol) ^ 2 + (MBH Upper Error / MBH) ^ 2]

f_Edd Lower Error = f_Edd × √[(Lbol Lower Error / L_bol) ^ 2 + (MBH Lower Error / MBH) ^ 2]

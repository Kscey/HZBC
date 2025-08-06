# High-z Black Hole Catalog (HZBC)

The High-z Black Hole Catalog is a database containing information on over 500 supermassive blackholes (SMBHs) with redshift greater than 4 (z > 4) taken from various research papers. It also includes information on several tentative SMBHs and galaxies containing SMBHs. Most of the data is extracted directly from research papers without modifications with a few exceptions, which are detailed in the Notes section.

The HZBC is organised into 3 catagories:

1. [catalogMain.csv](catalogueMain.csv) contains information on **SMBHs**
2. catalogTentative.csv contained information on **tentative SMBHs or tentative galaxies containing SMBHs**
3. catalogGalaxy.csv contains information on **galaxies containing SMBHs**

Additionally, the remaining components in this repository are as follows:

1. dataMain.py, dataTentative.py, dataGalaxy.py contains the raw data entered into this catalog
2. databaseCreation.py contains code used to process the raw data into CSV format
3. functions.py contains functions used in databaseCreation.py
4. fEddCalculator.py in Tool Files contains code used to recalculate any abnormal Eddington ratio values
5. reviewPapers.csv in Tool Files is a database of research papers referenced in the catalog
6. review.py in Tool Files contains raw data entered into reviewPapers.csv

## Notes

1. Some entries lack a documented black hole mass and are approximated by, given M1450:

mass = 10 ^ [(- M1450 - 3.459) / 2.5] — [1]

2. There were errors in the papers [Mazzucchelli et al. (2017)](https://iopscience.iop.org/article/10.3847/1538-4357/aa9185/pdf) and [Mazzucchelli et al. (2023)](https://arxiv.org/pdf/2306.16474), where the Eddington ratios (f_Edd) were abnormal. Thus, the f_Edd were recalculated by, given BHM/mass and L_bol:

f_Edd = L_bol / (1.3e38 × MBH) — [2]

Errors are approximated using the error propagation formula:

f_Edd Upper Error = f_Edd × √[(L_bol Upper Error / L_bol) ^ 2 + (MBH Upper Error / MBH) ^ 2]

f_Edd Lower Error = f_Edd × √[(Lbol Lower Error / L_bol) ^ 2 + (MBH Lower Error / MBH) ^ 2]

## Acknowledgment

If this catalogue has been used as a source in your research paper, please include a link to this GitHub repository (https://github.com/Kscey/HZBC). 

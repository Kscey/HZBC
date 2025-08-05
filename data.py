import numpy as np

# Tool to help convert RA DEC coordinates: https://www.astrouw.edu.pl/~jskowron/ra-dec/?q=d++53.12654+-27.81809

# Arrays are manually populated to include or amend information
# 1a. Some bolometric luminosities need to be converted from units of solar luminosities to ergs per second (1 solar luminosity = 3.846e33 ergs per second)
# 1b. This can be done by adding "S" to the end of the bolometric luminosity
# 2a. Some entries lack a documented black hole mass and is approximated by formula [1] — mass = 10 ** ((-M1450 -3.459) / 2.5)
# 2b. This is done automatically without any input
# 3a. There were errors in the papers Mazzucchelli et al. (2017) and Mazzucchelli et al. (2023), where the Eddington ratios (f_Edd) were abnormal. Thus, the f_Edd were recalculated by formula [2] — f_Edd = (Lbol)/(1.3e38 * (MBH)), while the errors were approximated using the error propagation formula
# 3b. This is done manually

entry0 = np.array([["J1342+0928", "Banados et al. (2018), Venemans et al. (2017), Onoue et al. (2020), Novak et al. (2019), Yang et al. (2021)",
                    "https://arxiv.org/abs/1712.01860, https://iopscience.iop.org/article/10.3847/2041-8213/aa943a, https://arxiv.org/pdf/2006.16268, https://iopscience.iop.org/article/10.3847/1538-4357/ab2beb, https://iopscience.iop.org/article/10.3847/1538-4357/ac2b32",
                    "ULAS", "13:42:08.097", "+09:28:38.28", "",
                    "7.5413", "0.0007", "0.0007", "9.1e8", "1.4e8", "1.3e8", "13.3e46", "1.1e46", "1.1e46",
                    "1.1", "0.2", "0.2", "-26.57", "0.04", "0.04", "", "", "",
                    "", "", "", "150", "30", "30", "", "", "",
                    "coordinates from Venemens et al. (2017), mass, Edd, M1450 from Onoue et al. (2020), SFR from Novak et al. (2019)"]])

# Coordinates found from: https://iopscience.iop.org/article/10.3847/2041-8213/aa943a Venemans et al. (2017)
# Updated (newer) mass, Edd and M1450 from: https://arxiv.org/pdf/2006.16268 Onoue et al. (2020) abstract
# SFR from: https://iopscience.iop.org/article/10.3847/1538-4357/ab2beb Novak et al. (2019)
# L_bol from: https://iopscience.iop.org/article/10.3847/1538-4357/ac2b32 Yang et al. (2021)
# How to present? Which data to keep?

entry1 = np.array([["J1243+0100", "Matsuoka et al. (2019), Izumi et al. (2021)",
                    "https://arxiv.org/abs/1901.10487, https://arxiv.org/pdf/2104.05738###",
                    "HSC", "12:43:53.93", "+01:00:38.50", "",
                    "7.0749", "0.001", "0.001", "3.3e8", "2e8", "2e8", "1.4e46", "0.1e46", "0.1e46",
                    "0.34", "0.2", "0.2", "-24.13", "0.08", "0.08", "", "", "",
                    "220", "8", "8", "742", "16", "16", "", "", "",
                    "z, SFR from Izumi et al. (2021)"]])

# What does the b in 2019b mean? Have to keep it?
# Updated (newer) redshift and SFR from: https://arxiv.org/pdf/2104.05738### Izumi et al. (2021) pg.6

entry2 = np.array([["J1120+0641", "Mortlock et al.(2011), De Rosa et al. (2014), Yang et al. (2021)",
                    "https://arxiv.org/abs/1106.6088, https://arxiv.org/pdf/1311.3260, https://iopscience.iop.org/article/10.3847/1538-4357/ac2b32",
                    "ULAS", "11:20:01.48", "+06:41:24.30", "",
                    "7.0851", "0.0005", "0.0005", "1.35e9", "0.04e9", "0.04e9", "13.4e46", "1.0e46", "1.0e46",
                    "0.8", "0.1", "0.1", "-26.44", "", "", "", "", "",
                    "", "", "", "", "", "", "", "", "",
                    "coordinates from De Rosa et al. (2014), z, M1450, M, L_bol from Yang et al. (2021)"]])

# Coordinates found from: https://arxiv.org/pdf/1311.3260 De Rosa et al. (2014)
# Redshift, M1450, M, L_bol, f_Edd from: https://iopscience.iop.org/article/10.3847/1538-4357/ac2b32 Yang et al. (2021)

entry3 = np.array([["J0038-1527", "Wang et al. (2018)",
                    "https://arxiv.org/abs/1810.11925",
                    "DELS", "00:38:36.10", "-15:27:23.06", "",
                    "7.021", "0.005", "0.005", "1.33e9", "0.25e9", "0.25e9", "2.16e47", "", "",
                    "1.25", "0.19", "0.19", "-27.10", "0.08", "0.08", "", "", "",
                    "", "", "", "", "", "", "", "", "",
                    ""]])

entry4 = np.array([["J0252-0503", "Yang et al. (2019), Wang et al (2020)",
                    "https://iopscience.iop.org/article/10.3847/1538-3881/ab1be1/meta, https://arxiv.org/abs/2004.10877",
                    "DES", "02:52:16.64", "-05:03:31.80", "",
                    "7.02", "0.001", "0.001", "1.39e9", "1.6e8", "1.6e8", "1.3e47", "0.1e47", "0.1e47",
                    "0.7", "0.1", "0.1", "-26.50", "0.09", "0.09", "", "", "",
                    "", "", "", "", "", "", "", "", "",
                    "M1450 from Yang et al. (2019), z from Wang et al (2020)"]])

# M1450 from: https://iopscience.iop.org/article/10.3847/1538-3881/ab1be1/meta Yang et al. (2019)
# z from: https://arxiv.org/abs/2004.10877 Wang et al (2020)

entry5 = np.array([["J2356+0017", "Matsuoka et al. (2019)",
                    "https://arxiv.org/abs/1908.07910",
                    "HSC", "23:56:46.33", "+00:17:47.30", "",
                    "7.01", "", "", "5.5e8", "2.06e7", "1.99e7", "", "", "",
                    "", "", "", "-25.31", "0.04", "0.04", "", "", "",
                    "", "", "", "", "", "", "", "", "",
                    ""]])

# Currently unsure where the mass comes from

entry6 = np.array([["J0313−1806", "Wang et al. (2021)",
                    "https://arxiv.org/abs/2101.03179",
                    "PS1+DELS+VHS+WISE", "03:13:43.84", "-18:06:36.40", "",
                    "7.6423", "0.0013", "0.0013", "1.6e9", "0.4e9", "0.4e9", "1.4e47", "0.1e47", "0.1e47",
                    "0.67", "0.14", "0.14", "-26.13", "0.05", "0.05", "", "", "",
                    "40-240", "", "", "225", "25", "25", "", "", "",
                    ""]])

entry7 = np.array([["J1007+2115", "Yang et al. (2020)",
                    "https://arxiv.org/abs/2006.13452",
                    "PS1+DELS+UHS+WISE", "10:07:58.26", "+21:15:29.20", "",
                    "7.5149", "0.0004", "0.0004", "1.5e9", "0.2e9", "0.2e9", "1.9e47", "0.1e47", "0.1e47",
                    "1.06", "0.2", "0.2", "-26.66", "0.07", "0.07", "", "", "",
                    "80-520", "", "", "700", "", "", "", "", "",
                    ""]])

entry8 = np.array([["(Galaxy) J0014-3022/UHZ1", "Bogdan et al. (2023), Castellano et al. (2023), Goulding et al. (2023)",
                    "https://arxiv.org/abs/2305.15458, https://iopscience.iop.org/article/10.3847/2041-8213/accea5/meta, https://arxiv.org/pdf/2308.02750",
                    "JWST", "00:14:16.096", "-30:22:40.285", "",
                    "10.073", "0.002", "0.002", "4e7", "6e7", "3e7", "5e45", "", "",
                    "", "", "", "", "", "", "87.7", "7.2", "7.2",
                    "4.5", "2.9", "2.2", "4.5", "2.9", "2.2", "0.4e8", "1.8e8", "0.2e8",
                    "F444W, SFR, Mstar from Castellano et al. (2023), z from Goulding et al. (2023)"]])

# F444W, SFR, Mstar from: https://iopscience.iop.org/article/10.3847/2041-8213/accea5/meta Castellano et al. (2023)
# z from: https://arxiv.org/pdf/2308.02750 Goulding et al. (2023)

entry9 = np.array([["(Galaxy) J0013-3020/GHZ9", "Kovacs et al. (2024), Castellano et al. (2023), Atek et al. (2023)",
                    "https://arxiv.org/abs/2403.14745, https://iopscience.iop.org/article/10.3847/2041-8213/accea5/meta, https://arxiv.org/pdf/2305.01793",
                    "JWST", "00:13:54.90", "-30:20:43.93", "",
                    "10.37", "0.32", "1.09", "8e7", "3.7e7", "3.2e7", "1e46", "0.5e46", "0.4e46",
                    "", "", "", "", "", "", "40.9", "3.9", "3.9",
                    "", "", "", "", "", "", "3.3e8", "2.9e8", "2.4e8",
                    "F444W, Mstar, SFR [14.4 (+15.0/-7.3)] from Castellano et al. (2023), SFR [0.56 (+0.23/-0.29)] from Atek et al. (2023)"]])

# F444W, Mstar, SFR from: https://iopscience.iop.org/article/10.3847/2041-8213/accea5/meta Castellano et al. (2023)
# SFR from: https://arxiv.org/pdf/2305.01793 Atek et al. (2023)

entry10 = np.array([["(Galaxy) GNz11", "Maiolino et al. (2023), Bunker et al. (2023), Oesch et al. (2016)",
                     "https://arxiv.org/abs/2305.12492, https://arxiv.org/pdf/2302.07256, https://arxiv.org/pdf/1603.00461",
                     "JWST", "12:36:25.46", "+62:14:31.40", "",
                     "10.6", "", "", "1.6e6", "1e0.3", "1e0.3", "1.08e45", "", "",
                     "", "", "", "", "", "", "", "", "",
                     "31", "59", "19", "31", "59", "19", "", "", "",
                     "SFR from Bunker et al. (2023), coordinates from Oesch et al. (2016)"]])

# SFR from: https://arxiv.org/pdf/2302.07256 Bunker et al. (2023)
# Coordinates from: https://arxiv.org/pdf/1603.00461 Oesch et al. (2016)

entry11 = np.array([["(Galaxy) J1420+5253/CEERS_01019/CEERS_1019", "Larson et al. (2023)",
                     "https://arxiv.org/abs/2303.08918",
                     "JWST", "14:20:08.49", "+52:53:26.38", "",
                     "8.679", "0.09", "0.15", "log6.95", "log0.37", "log0.37", "log45.1", "log0.2", "log0.2",
                     "1.2", "0.5", "0.5", "", "", "", "", "", "",
                     "30", "", "", "30", "", "", "", "", "",
                     ""]])

entry12 = np.array([["J1205−0000", "Onoue et al. (2019), Sawamura et al. (2025), Izumi et al. (2021)",
                     "https://arxiv.org/abs/1904.07278, https://arxiv.org/pdf/2502.16858, https://iopscience.iop.org/article/10.3847/1538-4357/abd7ef",
                     "HSC", "12:05:05.09", "-00:00:27.90", "",
                     "6.7230", "0.0003", "0.0003", "2.2e9", "0.2e9", "0.6e9", "", "", "",
                     "0.16", "0.04", "0.02", "-24.56", "0.04", "0.04", "", "", "",
                     "122", "5", "5", "528", "8", "8", "", "", "",
                     ""]])

# SFR_TIR from: https://arxiv.org/pdf/2502.16858 Sawamura et al. (2025)
# z, SFR_CII from: https://iopscience.iop.org/article/10.3847/1538-4357/abd7ef Izumi et al. (2021)

entry13 = np.array([["J2239+0207", "Onoue et al. (2019), Ishimoto et al. (2020)",
                     "https://arxiv.org/abs/1904.07278, https://iopscience.iop.org/article/10.3847/1538-4357/abb80b/pdf",
                     "HSC", "22:39:47.47", "+02:07:47.50", "",
                     "6.245", "0.008", "0.007", "1.1e9", "0.3e9", "0.2e9", "", "", "",
                     "0.17", "0.04", "0.05", "-24.69", "0.04", "0.04", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     "coordinates from Ishimoto et al. (2020)"]])

# coordinates from: https://iopscience.iop.org/article/10.3847/1538-4357/abb80b/pdf Ishimoto et al. (2020)

entry14 = np.array([["J2216−0016", "Onoue et al. (2019), Ishimoto et al. (2020)",
                     "https://arxiv.org/abs/1904.07278, https://iopscience.iop.org/article/10.3847/1538-4357/abb80b/pdf",
                     "HSC", "22:16:44.47", "-00:16:50.10", "",
                     "6.109", "0.007", "0.008", "0.7e9", "0.14e9", "0.23e9", "", "", "",
                     "0.15", "0.05", "0.03", "-23.82", "0.04", "0.04", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     "coordinates from Ishimoto et al. (2020)"]])

# coordinates from: https://iopscience.iop.org/article/10.3847/1538-4357/abb80b/pdf Ishimoto et al. (2020)

entry15 = np.array([["J1208−0200", "Onoue et al. (2019), Ishimoto et al. (2020)",
                     "https://arxiv.org/abs/1904.07278, https://iopscience.iop.org/article/10.3847/1538-4357/abb80b/pdf",
                     "HSC", "12:08:59.23", "-02:00:34.80", "",
                     "6.144", "0.008", "0.01", "0.71e9", "0.24e9", "0.52e9", "", "", "",
                     "0.24", "0.18", "0.08", "-24.73", "0.02", "0.02", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     "coordinates from Ishimoto et al. (2020)"]])

# coordinates from: https://iopscience.iop.org/article/10.3847/1538-4357/abb80b/pdf Ishimoto et al. (2020)

entry16 = np.array([["J0100+2802/J0100+28", "Wu et al. (2015), D'Odorico et al. (2023), Venemans et al. (2020), Mazzucchelli et al. (2023)",
                     "https://arxiv.org/abs/1502.07418, https://academic.oup.com/mnras/article/523/1/1399/7172883, https://iopscience.iop.org/article/10.3847/1538-4357/abc563, https://arxiv.org/pdf/2306.16474",
                     "SDSS", "01:00:13.02", "+28:02:25.80", "",
                     "6.3269", "0.0002", "0.0002", "log10.1", "log0.2", "log0.1", "log48.15", "log0.04", "log0.04",
                     "0.863091", "0.511638", "0.193076", "-29.26", "0.20", "0.20", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     "coordinates from D'Odorico et al. (2023), distance, z from Venemans et al. (2020), mass, L_bol, (recalculated using formula [2]) f_Edd from Mazzucchelli et al. (2023)"]])

# coordinates from: https://academic.oup.com/mnras/article/523/1/1399/7172883 D'Odorico et al. (2023)
# distance, z from: https://iopscience.iop.org/article/10.3847/1538-4357/abc563 Venemans et al. (2020)
# mass, L_bol, f_Edd from: https://arxiv.org/pdf/2306.16474 Mazzucchelli et al. (2023)

entry17 = np.array([["J1034-1425/P158–14/J158.6-14.42", "Eilers et al. (2020)",
                     "https://arxiv.org/abs/2002.01811",
                     "PSO", "10:34:46.509", "-14:25:15.855", "",
                     "6.052", "0.001", "0.001", "1.57e9", "0.12e9", "0.12e9", "2.04e47", "", "",
                     "1.01", "0.08", "0.08", "-27.41", "", "", "", "", "",
                     "230", "", "", "", "", "", "", "", "",
                     ""]])

entry18 = np.array([["J0330–4025", "Eilers et al. (2020), Reed et al. (2017)",
                     "https://arxiv.org/abs/2002.01811, https://academic.oup.com/mnras/article/468/4/4702/3089747",
                     "VDES", "03:30:27.920", "-40:25:16.200", "",
                     "6.239", "0.004", "0.004", "4.96e9", "0.51e9", "0.51e9", "8.91e46", "", "",
                     "0.14", "0.01", "0.01", "-26.42", "0.06", "0.06", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     "M1450 from Reed et al. (2017)"]])

# M1450 from: https://academic.oup.com/mnras/article/468/4/4702/3089747 Reed et al. (2017)

entry19 = np.array([["J2100–1715", "Eilers et al. (2020)",
                     "https://arxiv.org/abs/2002.01811",
                     "CFHQS", "21:00:54.616", "-17:15:22.500", "",
                     "6.082", "0.002", "0.002", "2.18e9", "0.21e9", "0.21e9", "4.37e46", "", "",
                     "0.15", "0.02", "0.02", "-25.55", "", "", "", "", "",
                     "170", "", "", "", "", "", "", "", "",
                     ""]])

entry20 = np.array([["J2229+1457", "Eilers et al. (2020), Willott et al. (2015)",
                     "https://arxiv.org/abs/2002.01811, https://iopscience.iop.org/article/10.1088/0004-637X/801/2/123#apj509348t2",
                     "CFHQS", "22:29:01.649", "+14:57:08.980", "",
                     "6.144", "0.006", "0.006", "1.44e9", "0.25e9", "0.25e9", "2.29e46", "", "",
                     "0.12", "0.02", "0.02", "-24.78", "", "", "", "", "",
                     "60", "8", "8", "19", "10", "10", "", "", "",
                     "SFR from Willott et al. (2015)"]])

# SFR from: https://iopscience.iop.org/article/10.1088/0004-637X/801/2/123#apj509348t2 Willott et al. (2015)

entry21 = np.array([["J0017+1705/J004+17/J004.3+17.08", "Eilers et al. (2020), ",
                     "https://arxiv.org/abs/2002.01811",
                     "PSO", "00:17:34.467", "+17:05:10.696", "",
                     "5.8165", "0.0023", "0.0023", "1.05e9", "", "", "", "", "",
                     "", "", "", "-26.01", "", "", "", "", "",
                     "20", "", "", "", "", "", "", "", "",
                     ""]])

entry22 = np.array([["J1335+3533", "Eilers et al. (2018), Ishimoto et al. (2020)",
                     "https://arxiv.org/abs/1806.05691, https://iopscience.iop.org/article/10.3847/1538-4357/abb80b/pdf",
                     "SDSS", "13:35:50.81", "+35:33:15.82", "",
                     "5.9012", "0.0019", "0.0019", "4.09e9", "0.58e9", "0.58e9", "1.62e47", "0.03e47", "0.03e47",
                     "0.30", "0.04", "0.04", "-26.67", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     "coordinates from Ishimoto et al. (2020)"]])

# coordinates from: https://iopscience.iop.org/article/10.3847/1538-4357/abb80b/pdf Ishimoto et al. (2020)

entry23 = np.array([["J1236+6215/JADES-GN+189.15197+62.25964/GN-954/954", "Maiolino et al. (2024), Juodžbalis et al. (2025)",
                     "https://arxiv.org/abs/2308.01230, https://arxiv.org/html/2504.03551v1",
                     "JWST", "12:36:36.47", "+62:15:34.70", "",
                     "6.759", "", "", "log7.74", "log0.31", "log0.32", "log45.24", "log0.15", "log0.17",
                     "0.25", "0.05", "0.05", "", "", "", "", "", "",
                     "", "", "", "", "", "", "log10.66", "log0.09", "log0.1",
                     "coordinates, z, mass, L_bol, f_Edd from Juodžbalis et al. (2025), little red dot"]])

# coordinates, z, mass, L_bol, f_Edd from: https://arxiv.org/html/2504.03551v1 Juodžbalis et al. (2025)

entry24 = np.array([["J1236+6213/JADES-GN+189.17974+62.22463/GN-1093/1093", "Maiolino et al. (2024), Juodžbalis et al. (2025)",
                     "https://arxiv.org/abs/2308.01230, https://arxiv.org/html/2504.03551v1",
                     "JWST", "12:36:43.14", "+62:13:28.67", "",
                     "5.594", "", "", "log7.07", "log0.34", "log0.33", "log44.52", "log0.18", "log0.16",
                     "0.15", "0.06", "0.04", "", "", "", "", "", "",
                     "", "", "", "", "", "", "log8.34", "log0.2", "log0.2",
                     "coordinates, z, mass, L_bol, f_Edd from Juodžbalis et al. (2025), little red dot"]])

# coordinates, z, mass, L_bol, f_Edd from: https://arxiv.org/html/2504.03551v1 Juodžbalis et al. (2025)

entry25 = np.array([["(Tentative) J1236+6214/JADES-GN+189.11794+62.23552/3608", "Maiolino et al. (2024)",
                     "https://arxiv.org/abs/2308.01230",
                     "JWST", "", "", "",
                     "5.26894", "", "", "6.60693e6", "9.242e6", "3.51664e6", "1.e44", "", "",
                     "0.11", "", "", "", "", "", "", "", "",
                     "", "", "", "", "", "", "log8.38", "log0.11", "log0.15",
                     "tentative source according to https://arxiv.org/html/2504.03551v1 Juodžbalis et al. (2025), little red dot"]])

entry26 = np.array([["J0332-2748/JADES-GS+53.13284-27.80186/GS-8083/8083", "Maiolino et al. (2024), Juodžbalis et al. (2025)",
                     "https://arxiv.org/abs/2308.01230, https://arxiv.org/html/2504.03551v1",
                     "JWST", "03:32:31.88", "-27:48:06.70", "",
                     "4.753", "", "", "log7.11", "log0.31", "log0.31", "log44.06", "log0.05", "log0.05",
                     "0.07", "0.01", "0.01", "", "", "", "", "", "",
                     "", "", "", "", "", "", "log8.45", "log0.03", "log0.03",
                     "coordinates, z, mass, L_bol, f_Edd from Juodžbalis et al. (2025), little red dot"]])

# coordinates, z, mass, L_bol, f_Edd from: https://arxiv.org/html/2504.03551v1 Juodžbalis et al. (2025)

entry27 = np.array([["J1236+6215/JADES-GN+189.22059+62.26368/GN-11836/11836", "Maiolino et al. (2024), Juodžbalis et al. (2025)",
                     "https://arxiv.org/abs/2308.01230, https://arxiv.org/html/2504.03551v1",
                     "JWST", "12:36:52.94", "+62:15:49.25", "",
                     "4.409", "", "", "log7.00", "log0.32", "log0.32", "log44.20", "log0.05", "log0.05",
                     "0.13", "0.03", "0.02", "", "", "", "", "", "",
                     "", "", "", "", "", "", "log7.79", "log0.3", "log0.3",
                     "coordinates, z, mass, L_bol, f_Edd from Juodžbalis et al. (2025), little red dot"]])

# coordinates, z, mass, L_bol, f_Edd from: https://arxiv.org/html/2504.03551v1 Juodžbalis et al. (2025)

entry28 = np.array([["J1236+6217/JADES-GN+189.12252+62.29285/GN-20621/20621", "Maiolino et al. (2024), Juodžbalis et al. (2025)",
                     "https://arxiv.org/abs/2308.01230, https://arxiv.org/html/2504.03551v1",
                     "JWST", "12:36:29.40", "+62:17:34.26", "",
                     "4.682", "", "", "log7.09", "log0.35", "log0.34", "log44.24", "log0.23", "log0.19",
                     "0.11", "0.06", "0.03", "", "", "", "", "", "",
                     "", "", "", "", "", "", "log8.06", "log0.7", "log0.7",
                     "coordinates, z, mass, L_bol, f_Edd from Juodžbalis et al. (2025), little red dot"]])

# coordinates, z, mass, L_bol, f_Edd from: https://arxiv.org/html/2504.03551v1 Juodžbalis et al. (2025)

entry29 = np.array([["J1237+6211/JADES-GN+189.26978+62.19421/GN-53757/53757", "Maiolino et al. (2024), Juodžbalis et al. (2025)",
                     "https://arxiv.org/abs/2308.01230, https://arxiv.org/html/2504.03551v1",
                     "JWST", "12:37:04.75", "+62:11:39.16", "",
                     "4.447", "", "", "log7.33", "log0.31", "log0.31", "log44.29", "log0.02", "log0.02",
                     "0.07", "0.01", "0.009", "", "", "", "", "", "",
                     "", "", "", "", "", "", "log10.18", "log0.13", "log0.12",
                     "coordinates, z, mass, L_bol, f_Edd from Juodžbalis et al. (2025), little red dot"]])

# coordinates, z, mass, L_bol, f_Edd from: https://arxiv.org/html/2504.03551v1 Juodžbalis et al. (2025)

entry30 = np.array([["J1236+6213/JADES-GN+189.16802+62.21701 /GN-61888/61888", "Maiolino et al. (2024), Juodžbalis et al. (2025)",
                     "https://arxiv.org/abs/2308.01230, https://arxiv.org/html/2504.03551v1",
                     "JWST", "12:36:40.32", "+62:13:01.24", "",
                     "5.874", "", "", "log7.08", "log0.33", "log0.32", "log44.46", "log0.13", "log0.10",
                     "0.20", "0.06", "0.03", "", "", "", "", "", "",
                     "", "", "", "", "", "", "log8.11", "log0.92", "log0.92",
                     "coordinates, z, mass, L_bol, f_Edd from Juodžbalis et al. (2025), little red dot"]])

# coordinates, z, mass, L_bol, f_Edd from: https://arxiv.org/html/2504.03551v1 Juodžbalis et al. (2025)

entry31 = np.array([["J1236+6213/JADES-GN+189.24898+62.21835/GN-62309/62309", "Maiolino et al. (2024), Juodžbalis et al. (2025)",
                     "https://arxiv.org/abs/2308.01230, https://arxiv.org/html/2504.03551v1",
                     "JWST", "12:36:59.76", "+62:13:06.06", "",
                     "5.172", "", "", "log6.30", "log0.36", "log0.33", "log43.57", "log0.13", "log0.12",
                     "0.15", "0.05", "0.05", "", "", "", "", "", "",
                     "", "", "", "", "", "", "log8.12", "log0.12", "log0.13",
                     "coordinates, z, mass, L_bol, f_Edd from Juodžbalis et al. (2025), little red dot"]])

# coordinates, z, mass, L_bol, f_Edd from: https://arxiv.org/html/2504.03551v1 Juodžbalis et al. (2025)

entry32 = np.array([["J1236+6210/JADES-GN+189.1974+62.17723/GN-73488/73488", "Maiolino et al. (2024), Juodžbalis et al. (2025)",
                     "https://arxiv.org/abs/2308.01230, https://arxiv.org/html/2504.03551v1",
                     "JWST", "12:36:47.38", "+62:10:38.03", "",
                     "4.133", "", "", "log7.95", "log0.30", "log0.30", "log45.45", "log0.07", "log0.05",
                     "0.25", "0.02", "0.02", "", "", "", "", "", "",
                     "", "", "", "", "", "", "log9.78", "log0.2", "log0.2",
                     "coordinates, z, mass, L_bol, f_Edd from Juodžbalis et al. (2025), little red dot"]])

# coordinates, z, mass, L_bol, f_Edd from: https://arxiv.org/html/2504.03551v1 Juodžbalis et al. (2025)

entry33 = np.array([["J1237+6211/JADES-GN+189.29323+62.199/GN-77652/77652", "Maiolino et al. (2024), Juodžbalis et al. (2025)",
                     "https://arxiv.org/abs/2308.01230, https://arxiv.org/html/2504.03551v1",
                     "JWST", "12:37:10.38", "+62:11:56.40", "",
                     "5.229", "", "", "log6.62", "log0.34", "log0.32", "log44.11", "log0.04", "log0.05",
                     "0.24", "0.09", "0.08", "", "", "", "", "", "",
                     "", "", "", "", "", "", "log7.87", "log0.16", "log0.28",
                     "coordinates, z, mass, L_bol, f_Edd from Juodžbalis et al. (2025), little red dot"]])

# coordinates, z, mass, L_bol, f_Edd from: https://arxiv.org/html/2504.03551v1 Juodžbalis et al. (2025)

entry34 = np.array([["J0332-2749/JADES-GS+53.12654-27.81809/GS-10013704/10013704", "Maiolino et al. (2024), Juodžbalis et al. (2025)",
                     "https://arxiv.org/abs/2308.01230, https://arxiv.org/html/2504.03551v1",
                     "JWST", "03:32:30.37", "-27:49:05.12", "",
                     "5.919", "", "", "log7.44", "log0.31", "log0.31", "log44.29", "log0.02", "log0.02",
                     "0.055", "0.007", "0.006", "", "", "", "", "", "",
                     "", "", "", "", "", "", "log8.88", "log0.66", "log0.66",
                     "coordinates, z, mass, L_bol, f_Edd from Juodžbalis et al. (2025), little red dot"]])

# coordinates, z, mass, L_bol, f_Edd from: https://arxiv.org/html/2504.03551v1 Juodžbalis et al. (2025)

entry35 = np.array([["J0332-2753/GS_3073", "Ubler et al. (2023), Barchiesi et al. (2022)",
                     "https://arxiv.org/abs/2302.06647, https://arxiv.org/pdf/2212.00038",
                     "JWST", "03:32:18.93", "-27:53:02.96", "",
                     "5.55", "", "", "1.58489e8", "2.39618e8", "9.53936e7", "5.0e45", "1.08e46", "3.43e45",
                     "0.25", "1.35", "0.15", "", "", "", "", "", "",
                     "16", "14", "7", "", "", "", "", "", "",
                     "use H-alpha for mass, use geometric mean of two method for L_bol, SFR [90 (+30/-30)] from Barchiesi et al. (2022)"]])

# SFR from: https://arxiv.org/pdf/2212.00038 Barchiesi et al. (2022)

entry36 = np.array([["(Galaxy) J1420+5302/CEERS_01244", "Harikane et al. (2023)",
                     "https://arxiv.org/pdf/2303.11946",
                     "JWST", "14:20:57.76", "+53:02:09.80", "",
                     "4.478", "", "", "3.2e7", "0.3e7", "0.2e7", "1.9e45", "3.8e45", "0.6e45",
                     "0.46", "1.04", "0.16", "", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     "+df_Edd may be unusually large because Harikane et al. (2023) estimates L_bol and -dL_bol using equation 17 but estimates +dL_bol using equation 18"]])

entry37 = np.array([["(Galaxy) J0014-3025/GLASS_160133", "Harikane et al. (2023)",
                     "https://arxiv.org/pdf/2303.11946",
                     "JWST", "00:14:19.27", "-30:25:27.80", "",
                     "4.015", "", "", "2.3e6", "0.1e6", "0.1e6", "1.1e45", "6.1e45", "0.9e45",
                     "3.68", "21.21", "2.84", "", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     "+df_Edd may be unusually large because Harikane et al. (2023) estimates L_bol and -dL_bol using equation 17 but estimates +dL_bol using equation 18"]])

entry38 = np.array([["(Galaxy) J0014-3025/GLASS_150029", "Harikane et al. (2023)",
                     "https://arxiv.org/pdf/2303.11946",
                     "JWST", "00:14:18.52", "-30:25:21.30", "",
                     "4.583", "", "", "3.7e6", "0.2e6", "0.3e6", "9.1e44", "13.8e44", "7.1e44",
                     "1.89", "3.31", "1.49", "", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     "+df_Edd may be unusually large because Harikane et al. (2023) estimates L_bol and -dL_bol using equation 17 but estimates +dL_bol using equation 18"]])

entry39 = np.array([["(Galaxy) J1419+5252/CEERS_00746/CEERS 3210", "Harikane et al. (2023)",
                     "https://arxiv.org/pdf/2303.11946",
                     "JWST", "14:19:14.19", "+52:52:06.05", "",
                     "5.624", "", "", "5.8e7", "1.5e7", "1.3e7", "1.1e46", "0.1e46", "0.2e46",
                     "1.47", "0.60", "0.52", "", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     "+df_Edd may be unusually large because Harikane et al. (2023) estimates L_bol and -dL_bol using equation 17 but estimates +dL_bol using equation 18"]])

entry40 = np.array([["(Galaxy) J1420+5303/CEERS_01665", "Harikane et al. (2023)",
                     "https://arxiv.org/pdf/2303.11946",
                     "JWST", "14:20:42.77", "+53:03:33.07", "",
                     "4.483", "", "", "1.9e7", "0.8e7", "0.5e7", "4.8e45", "7.2e45", "3.6e45",
                     "1.93", "4.61", "1.59", "", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     "+df_Edd may be unusually large because Harikane et al. (2023) estimates L_bol and -dL_bol using equation 17 but estimates +dL_bol using equation 18"]])

entry41 = np.array([["(Galaxy) J1419+5249/CEERS_00672", "Harikane et al. (2023)",
                     "https://arxiv.org/pdf/2303.11946",
                     "JWST", "14:19:33.52", "+52:49:58.07", "",
                     "5.666", "", "", "5.0e7", "1.7e7", "1.3e7", "4.3e45", "0.4e45", "1.4e45",
                     "0.65", "0.31", "0.33", "", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     "+df_Edd may be unusually large because Harikane et al. (2023) estimates L_bol and -dL_bol using equation 17 but estimates +dL_bol using equation 18"]])

entry42 = np.array([["(Galaxy) J1419+5249/CEERS_02782/CEERS 1670", "Harikane et al. (2023)",
                    "https://arxiv.org/pdf/2303.11946",
                     "JWST", "14:19:17.63", "+52:49:49.00", "",
                     "5.241", "", "", "4.2e7", "1.2e7", "1.0e7", "2.8e45", "2.3e45", "1.4e45",
                     "0.51", "0.71", "0.32", "", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     "+df_Edd may be unusually large because Harikane et al. (2023) estimates L_bol and -dL_bol using equation 17 but estimates +dL_bol using equation 18"]])

entry43 = np.array([["(Galaxy) J1419+5252/CEERS_00397", "Harikane et al. (2023)",
                     "https://arxiv.org/pdf/2303.11946",
                     "JWST", "14:19:20.69", "+52:52:57.07", "",
                     "6.000", "", "", "1.0e7", "0.8e7", "0.5e7", "2.8e45", "14.2e45", "2.2e45",
                     "2.02", "20.68", "1.80", "", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     "+df_Edd may be unusually large because Harikane et al. (2023) estimates L_bol and -dL_bol using equation 17 but estimates +dL_bol using equation 18"]])

entry44 = np.array([["(Galaxy) J1420+5258/CEERS_00717", "Harikane et al. (2023)",
                     "https://arxiv.org/pdf/2303.11946",
                     "JWST", "14:20:19.54", "+52:58:19.09", "",
                     "6.936", "", "", "9.8e7", "4.4e7", "3.2e7", "7.1e44", "51.8e44", "4.3e44",
                     "0.06", "0.63", "0.04", "", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     "+df_Edd may be unusually large because Harikane et al. (2023) estimates L_bol and -dL_bol using equation 17 but estimates +dL_bol using equation 18"]])

entry45 = np.array([["(Galaxy) J1420+5258/CEERS_01236", "Harikane et al. (2023)",
                     "https://arxiv.org/pdf/2303.11946",
                     "JWST", "14:20:34.87", "+52:58:02.02", "",
                     "4.484", "", "", "1.8e7", "1.0e7", "0.6e7", "1.8e44", "2.6e44", "0.5e44",
                     "0.08", "0.20", "0.04", "", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     "+df_Edd may be unusually large because Harikane et al. (2023) estimates L_bol and -dL_bol using equation 17 but estimates +dL_bol using equation 18"]])

entry46 = np.array([["J1129+1846//P172+18/J172+18/J172.3+18.77", "Banados et al. (2021), Wang et al. (2024)",
                     "https://www.mpg.de/16498963/mpia-pr_banados_quasar_2021_preprint.pdf, https://arxiv.org/html/2404.15413v1#S1",
                     "PSO", "11:29:25.37", "+18:46:24.29", "",
                     "6.823", "0.003", "0.001", "2.9e8", "0.7e8", "0.6e8", "6.5e46", "", "",
                     "2.2", "0.6", "0.4", "-25.81", "0.10", "0.10", "", "", "",
                     "<5-35", "", "", "", "", "", "", "", "",
                     "SFR_CII from Wang et al. (2024)"]])

# SFR_CII from: https://arxiv.org/html/2404.15413v1#S1 Wang et al. (2024)

entry47 = np.array([["J2157-3602", "Wolf et al. (2018), Onken et al. (2020), Lai et al. (2023)",
                     "https://arxiv.org/abs/1805.04317, https://arxiv.org/pdf/2005.06868, https://arxiv.org/pdf/2302.10397",
                     "SMSS", "21:57:28.23", "-36:02:15.21", "",
                     "4.692", "", "", "log10.31", "log0.17", "log0.14", "log47.87", "log0.10", "log0.10",
                     "0.29", "0.11", "0.10", "", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     "z from Onken et al. (2020), mass, L_bol, f_Edd from Lai et al. (2023)"]])

# z from: https://arxiv.org/pdf/2005.06868 Onken et al. (2020)
# mass, L_bol, f_Edd from: https://arxiv.org/pdf/2302.10397 Lai et al. (2023)

entry48 = np.array([["J1609+5328", "Matsuoka et al. (2019)",
                     "https://arxiv.org/pdf/1908.07910",
                     "HSC", "16:09:53.03", "+53:28:21.00", "",
                     "6.92", "", "", "", "", "", "", "", "",
                     "", "", "", "-22.75", "1.67", "1.67", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry49 = np.array([["J0839+3900", "Wang et al. (2019), Yang et al. (2021)",
                     "https://iopscience.iop.org/article/10.3847/1538-4357/ab2be5/pdf, https://iopscience.iop.org/article/10.3847/1538-4357/ac2b32",
                     "DELS", "08:39:46.88", "+39:00:11.50", "",
                     "6.905", "0.01", "0.01", "0.671e9", "0.003e9", "0.003e9", "1.78e46", "0.7e46", "0.7e46",
                     "2.1", "0.1", "0.1", "-26.29", "0.20", "0.20", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     "mass, L_bol, f_Edd from Yang et al. (2019)"]])

# mass, L_bol, f_Edd from: https://iopscience.iop.org/article/10.3847/1538-4357/ac2b32 Yang et al. (2019)

entry50 = np.array([["J2348-3054", "Banados et al. (2016), Venemans et al. (2020), Venemens et al. (2015), Venemans et al. (2013), Mazzucchelli et al. (2017)",
                     "https://arxiv.org/pdf/1608.03279, https://iopscience.iop.org/article/10.3847/1538-4357/abc563, https://iopscience.iop.org/article/10.3847/0004-637X/816/1/37/meta, https://iopscience.iop.org/article/10.1088/0004-637X/779/1/24, https://iopscience.iop.org/article/10.3847/1538-4357/aa9185/pdf",
                     "VIK", "23:48:33.34", "-30:54:10.24", "",
                     "6.9007", "0.0005", "0.0005", "2.1e9", "0.5e9", "0.5e9", "0.43e47", "0.20e47", "0.13e47",
                     "0.167055", "0.0913789", "0.0870263", "-25.72", "0.14", "0.14", "", "", "",
                     "100-680", "", "", "", "", "", "", "", "",
                     "z from Venemans et al. (2020), SFR from Venemens et al. (2015), mass, M1450 from Venemans et al. (2013), L_bol, (recalculated using formula [2]) f_Edd from Mazzucchelli et al. (2017)"]])        

# z from: https://iopscience.iop.org/article/10.3847/1538-4357/abc563 Venemans et al. (2020)
# SFR from: https://iopscience.iop.org/article/10.3847/0004-637X/816/1/37/meta Venemans et al. (2015)
# mass, M1450 from: https://iopscience.iop.org/article/10.1088/0004-637X/779/1/24 Venemans et al. (2013)
# L_bol, f_Edd from: https://iopscience.iop.org/article/10.3847/1538-4357/aa9185/pdf Mazzucchelli et al. (2017)

entry51 = np.array([["J2210+0304", "Matsuoka et al. (2018)",
                     "https://arxiv.org/pdf/1803.01861",
                     "HSC", "22:10:27.24", "+03:04:28.50", "",
                     "6.9", "", "", "", "", "", "", "", "",
                     "", "", "", "-24.44", "0.06", "0.06", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry52 = np.array([["J2211-6320", "Yang et al. (2021), Wang et al. (2024)",
                     "https://iopscience.iop.org/article/10.3847/1538-4357/ac2b32, https://arxiv.org/html/2404.15413v1#S1",
                     "DES", "22:11:00.60", "-63:20:55.90", "",
                     "6.8449", "0.0003", "0.0003", "0.55e9", "0.24e9", "0.24e9", "5.9e46", "0.2e46", "0.2e46",
                     "0.8", "0.4", "0.4", "-25.38", "", "", "", "", "",
                     "132-828", "", "", "", "", "", "", "", "",
                     "coordinates, SFR_CII from Wang et al. (2024)"]])

# coordinates, SFR_CII from: https://arxiv.org/html/2404.15413v1#S1 Wang et al. (2024)

entry53 = np.array([["J0246-5219", "Yang et al. (2021), Wang et al. (2024)",
                     "https://iopscience.iop.org/article/10.3847/1538-4357/ac2b32, https://arxiv.org/html/2404.15413v1#S1",
                     "DES", "02:46:55.90", "-52:19:49.90", "",
                     "6.8876", "0.0003", "0.0003", "1.05e9", "0.37e9", "0.37e9", "10.2e46", "1.0e46", "1.0e46",
                     "0.8", "0.3", "0.3", "-25.36", "", "", "", "", "",
                     "193-1210", "", "", "", "", "", "", "", "",
                     "coordinates, SFR_CII from Wang et al. (2024)"]])

# coordinates, SFR_CII from: https://arxiv.org/html/2404.15413v1#S1 Wang et al. (2024)

entry54 = np.array([["J0020-3653", "Reed et al. (2019)",
                     "https://academic.oup.com/mnras/article/487/2/1874/5505847",
                     "VDES", "00:20:31.47", "-36:53:41.80", "",
                     "6.834", "0.0004", "0.0004", "1.67e9", "0.32e9", "0.32e9", "1.35e47", "0.03e47", "0.03e47",
                     "0.62", "0.12", "0.12", "-26.92", "0.03", "0.03", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry55 = np.array([["J0319-1008", "Yang et al. (2021), Wang et al. (2024)",
                     "https://iopscience.iop.org/article/10.3847/1538-4357/ac2b32, https://arxiv.org/html/2404.15413v1#S1",
                     "DES", "03:19:41.66", "-10:08:46.00", "",
                     "6.8275", "0.0021", "0.0021", "0.40e9", "0.03e9", "0.03e9", "9.6e46", "1.4e46", "1.4e46",
                     "1.9", "0.3", "0.3", "-25.36", "", "", "", "", "",
                     "146-916", "", "", "", "", "", "", "", "",
                     "coordinates, SFR_CII from Wang et al. (2024)"]])

# coordinates, SFR_CII from: https://arxiv.org/html/2404.15413v1#S1 Wang et al. (2024)

entry56 = np.array([["J0112+0110", "Matsuoka et al. (2019)",
                     "https://arxiv.org/pdf/1908.07910",
                     "HSC", "01:12:57.84", "+01:10:42.40", "",
                     "6.82", "", "", "", "", "", "", "", "",
                     "", "", "", "-24.07", "0.35", "0.35", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry57 = np.array([["J0411-0907", "Yang et al. (2021), Wang et al. (2024), Wang et al. (2019)",
                     "https://iopscience.iop.org/article/10.3847/1538-4357/ac2b32, https://arxiv.org/html/2404.15413v1#S1, https://iopscience.iop.org/article/10.3847/1538-4357/ab2be5/pdf",
                     "DELS", "04:11:28.63", "-09:07:49.70", "",
                     "6.8260", "0.0007", "0.0007", "0.95e9", "0.09e9", "0.09e9", "15.9e46", "1.0e46", "1.0e46",
                     "1.3", "0.2", "0.2", "-26.61", "0.12", "0.12", "", "", "",
                     "119-745", "", "", "", "", "", "", "", "",
                     "coordinates, SFR_CII from Wang et al. (2024), M1450 from Wang et al. (2019)"]])

# coordinates, SFR_CII from: https://arxiv.org/html/2404.15413v1#S1 Wang et al. (2024)
# M1450 from: https://iopscience.iop.org/article/10.3847/1538-4357/ab2be5/pdf Wang et al. (2019)

entry58 = np.array([["J1429-0104", "Matsuoka et al. (2018)",
                     "https://arxiv.org/pdf/1704.05854",
                     "HSC", "14:29:03.08", "-01:04:43.40", "",
                     "6.8", "", "", "", "", "", "", "", "",
                     "", "", "", "-23.00", "0.26", "0.26", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry59 = np.array([["J0109-3047", "Banados et al. (2016), Venemans et al. (2020), Mazzuchelli et al. (2017)",
                     "https://arxiv.org/pdf/1608.03279, https://iopscience.iop.org/article/10.3847/1538-4357/abc563, https://iopscience.iop.org/article/10.3847/1538-4357/aa9185/pdf",
                     "VIK", "01:09:53.13", "-30:47:26.31", "",
                     "6.7904", "0.0003", "0.0003", "1.33e9", "0.38e9", "0.62e9", "0.51e47", "0.05e47", "0.06e47",
                     "0.294968", "0.0891001", "0.141815", "-25.64", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     "z from Venemans et al. (2020), L_bol, mass, (recalculated using formula [2]) f_Edd from Mazzucchelli et al. (2017)"]])

# z from: https://iopscience.iop.org/article/10.3847/1538-4357/abc563 Venemans et al. (2020)
# L_bol, mass, f_Edd from: https://iopscience.iop.org/article/10.3847/1538-4357/aa9185/pdf Mazzucchelli et al. (2017)

entry60 = np.array([["J1612+5559", "Matsuoka et al. (2019)",
                     "https://arxiv.org/pdf/1908.07910",
                     "HSC", "16:12:07.12", "+55:59:19.20", "",
                     "6.78", "", "", "", "", "", "", "", "",
                     "", "", "", "-23.02", "0.32", "0.32", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry61 = np.array([["J0829+4117", "Wang et al. (2019), Yang et al. (2021)",
                     "https://iopscience.iop.org/article/10.3847/1538-4357/ab2be5/pdf, https://iopscience.iop.org/article/10.3847/1538-4357/ac2b32",
                     "DELS", "08:29:31.98", "+41:17:40.90", "",
                     "6.768", "0.006", "0.006", "0.71e9", "0.02e9", "0.02e9", "12.8e46", "1.2e46", "1.2e46",
                     "1.4", "0.1", "0.1", "-26.36", "0.15", "0.15", "", "", "",
                     "<19-122", "", "", "", "", "", "", "", "",
                     "mass, L_bol, f_Edd from Yang et al. (2021), coordinates, SFR_CII from Wang et al. (2024)"]])

# mass, L_bol, f_Edd from: https://iopscience.iop.org/article/10.3847/1538-4357/ac2b32 Yang et al. (2021)
# coordinates, SFR_CII from: https://arxiv.org/html/2404.15413v1#S1 Wang et al. (2024)

entry62 = np.array([["J1104+2134", "Yang et al. (2021), Wang et al. (2024), Wang et al. (2019)",
                     "https://iopscience.iop.org/article/10.3847/1538-4357/ac2b32, https://arxiv.org/html/2404.15413v1#S1, https://iopscience.iop.org/article/10.3847/1538-4357/ab2be5/pdf",
                     "DELS", "11:04:21.58", "+21:34:28.90", "",
                     "6.7662", "0.0009", "0.0009", "1.69e9", "0.15e9", "0.15e9", "15.1e46", "0.9e46", "0.9e46",
                     "0.7", "0.1", "0.1", "-26.67", "0.13", "0.13", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     "coordinates, SFR_CII from Wang et al. (2024), M1450 from Wang et al. (2019)"]])

# coordinates, SFR_CII from: https://arxiv.org/html/2404.15413v1#S1 Wang et al. (2024)
# M1450 from: https://iopscience.iop.org/article/10.3847/1538-4357/ab2be5/pdf Wang et al. (2019)

entry63 = np.array([["J0244-5008", "Reed et al. (2019)",
                     "https://academic.oup.com/mnras/article/487/2/1874/5505847",
                     "VDES", "02:44:01.02", "-50:08:53.70", "",
                     "6.724", "0.0008", "0.0008", "1.15e9", "0.39e9", "0.39e9", "1.44e47", "0.02e47", "0.02e47",
                     "0.96", "0.33", "0.33", "-26.72", "0.05", "0.05", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry64 = np.array([["J0910+1656", "Yang et al. (2021), Wang et al. (2024), Wang et al. (2019)",
                     "https://iopscience.iop.org/article/10.3847/1538-4357/ac2b32, https://arxiv.org/html/2404.15413v1#S1, https://iopscience.iop.org/article/10.3847/1538-4357/ab2be5/pdf",
                     "DELS", "09:10:13.65", "+16:56:30.20", "",
                     "6.7289", "0.0005", "0.0005", "0.41e9", "0.03e9", "0.03e9", "5.3e46", "0.6e46", "0.6e46",
                     "1.0", "0.1", "0.1", "-25.57", "0.14", "0.14", "", "", "",
                     "105-658", "", "", "", "", "", "", "", "",
                     "coordinates, SFR_CII from Wang et al. (2024), M1450 from Wang et al. (2019)"]])

# coordinates, SFR_CII from: https://arxiv.org/html/2404.15413v1#S1 Wang et al. (2024)
# M1450 from: https://iopscience.iop.org/article/10.3847/1538-4357/ab2be5/pdf Wang et al. (2019)

entry65 = np.array([["J1344+0128", "Matusuka et al. (2019)",
                     "https://arxiv.org/pdf/1908.07910",
                     "HSC", "13:44:00.87", "+01:28:27.80", "",
                     "6.72", "", "", "", "", "", "", "", "",
                     "", "", "", "-23.46", "0.15", "0.15", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry66 = np.array([["J0213-0626", "Matsuoka et al. (2018), Wang et al. (2024)",
                     "https://arxiv.org/pdf/1803.01861, https://arxiv.org/html/2404.15413v1#S1",
                     "HSC", "02:13:16.94", "-06:26:15.20", "",
                     "6.72", "", "", "", "", "", "log44.18", "log0.02", "log0.02",
                     "", "", "", "-25.24", "0.02", "0.02", "", "", "",
                     "13-86", "", "", "", "", "", "", "", "",
                     ""]])

# SFR_CII from: https://arxiv.org/html/2404.15413v1#S1 Wang et al. (2024)

entry67 = np.array([["J0837+4929", "Yang et al. (2021), Wang et al. (2024), Wang et al. (2019)",
                     "https://iopscience.iop.org/article/10.3847/1538-4357/ac2b32, https://arxiv.org/html/2404.15413v1#S1, https://iopscience.iop.org/article/10.3847/1538-4357/ab2be5/pdf",
                     "DELS", "08:37:37.83", "+49:29:00.60", "",
                     "6.710", "0.008", "0.008", "0.81e9", "0.01e9", "0.01e9", "14.5e46", "0.4e46", "0.4e46",
                     "1.4", "0.1", "0.1", "-26.42", "0.18", "0.18", "", "", "",
                     "36-229", "", "", "", "", "", "", "", "",
                     "coordinates, SFR_CII from Wang et al. (2024), M1450 from Wang et al. (2019)"]])

# M1450 from: https://iopscience.iop.org/article/10.3847/1538-4357/ab2be5/pdf Wang et al. (2019)
# coordinates, SFR_CII from: https://arxiv.org/html/2404.15413v1#S1 Wang et al. (2024)

entry68 = np.array([["J0001+0000", "Matsuoka et al. (2019)",
                     "https://arxiv.org/pdf/1908.07910",
                     "HSC", "00:01:42.54", "+00:00:57.50", "",
                     "6.69", "", "", "", "", "", "", "", "",
                     "", "", "", "-24.49", "0.59", "0.59", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry69 = np.array([["J1231+0052", "Matsuoka et al. (2019)",
                     "https://arxiv.org/pdf/1908.07910",
                     "HSC", "12:31:37.77", "+00:52:30.30", "",
                     "6.69", "", "", "", "", "", "", "", "",
                     "", "", "", "-24.39", "0.09", "0.09", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry70 = np.array([["J2232+2930/J338.2+29.50", "Banados et al. (2016), Wang et al. (2019), Mazzucchelli et al. (2017)",
                     "https://arxiv.org/pdf/1608.03279, https://iopscience.iop.org/article/10.3847/1538-4357/ab2be5/pdf, https://iopscience.iop.org/article/10.3847/1538-4357/aa9185/pdf",
                     "PSO", "22:32:55.14", "+29:30:32.31", "",
                     "6.666", "0.0004", "0.0004", "2.70e9", "0.85e9", "0.97e9", "4.04e47", "2.14e47", "0.90e47",
                     "1.151", "0.709236", "0.486553", "-26.31", "0.15", "0.15", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     "z, M1450 from Wang et al. (2019), L_bol, mass, (recalculated using formula [2]) f_Edd from Mazzucchelli et al. (2017)"]])

# z, M1450 from: https://iopscience.iop.org/article/10.3847/1538-4357/ab2be5/pdf Wang et al. (2019)
# L_bol, mass, f_Edd from: https://iopscience.iop.org/article/10.3847/1538-4357/aa9185/pdf Mazzucchelli et al. (2017)

entry71 = np.array([["J1216+4519", "Wang et al. (2019), Yang et al. (2021), Wang et al. (2024)",
                     "https://iopscience.iop.org/article/10.3847/1538-4357/ab2be5/pdf, https://iopscience.iop.org/article/10.3847/1538-4357/ac2b32, https://arxiv.org/html/2404.15413v1#S1",
                     "DELS", "12:16:27.58", "+45:19:10.70", "",
                     "6.654", "0.01", "0.01", "0.61e9", "0.20e9", "0.20e9", "5.8e46", "1.2e46", "1.2e46",
                     "0.8", "0.3", "0.3", "-25.58", "0.14", "0.14", "", "", "",
                     "<16-104", "", "", "", "", "", "", "", "",
                     "mass, L_bol, f_Edd from Yang et al. (2021), coordinates, SFR_CII from Wang et al. (2024)"]])

# mass, L_bol, f_Edd from: https://iopscience.iop.org/article/10.3847/1538-4357/ac2b32 Yang et al. (2021)
# coordinates, SFR_CII from: https://arxiv.org/html/2404.15413v1#S1 Wang et al. (2024)

entry72 = np.array([["J2102-1458", "Wang et al. (2019), Yang et al. (2021), Wang et al. (2024)",
                     "https://iopscience.iop.org/article/10.3847/1538-4357/ab2be5/pdf, https://iopscience.iop.org/article/10.3847/1538-4357/ac2b32, https://arxiv.org/html/2404.15413v1#S1",
                     "VHS", "21:02:19.23", "-14:58:53.90", "",
                     "6.6645", "0.0002", "0.0002", "0.74e9", "0.11e9", "0.11e9", "6.0e46", "0.5e46", "0.5e46",
                     "0.6", "0.1", "0.1", "-25.50", "0.2", "0.2", "", "", "",
                     "81-511", "", "", "", "", "", "", "", "",
                     "z, mass, L_bol, f_Edd from Yang et al. (2021), coordinates, SFR_CII from Wang et al. (2024)"]])

# z, mass, L_bol, f_Edd from: https://iopscience.iop.org/article/10.3847/1538-4357/ac2b32 Yang et al. (2021)
# coordinates, SFR_CII from: https://arxiv.org/html/2404.15413v1#S1 Wang et al. (2024)

entry73 = np.array([["J0910-0414", "Wang et al. (2019), Yang et al. (2021), Wang et al. (2024)",
                     "https://iopscience.iop.org/article/10.3847/1538-4357/ab2be5/pdf, https://iopscience.iop.org/article/10.3847/1538-4357/ac2b32, https://arxiv.org/html/2404.15413v1#S1",
                     "DELS", "09:10:54.54", "-04:14:06.90", "",
                     "6.6363", "0.0003", "0.0003", "3.59e9", "0.61e9", "0.61e9", "15.0e46", "1.1e46", "1.1e46",
                     "0.3", "0.1", "0.1", "-26.36", "0.15", "0.15", "", "", "",
                     "271-1697", "", "", "", "", "", "", "", "",
                     "z, mass, L_bol, f_Edd from Yang et al. (2021), coordinates, SFR_CII from Wang et al. (2024)"]])

# z, mass, L_bol, f_Edd from: https://iopscience.iop.org/article/10.3847/1538-4357/ac2b32 Yang et al. (2021)
# coordinates, SFR_CII from: https://arxiv.org/html/2404.15413v1#S1 Wang et al. (2024)

entry74 = np.array([["J1048-0109", "Venemans et al. (2020), Wang et al. (2019), ",
                     "https://iopscience.iop.org/article/10.3847/1538-4357/abc563, https://iopscience.iop.org/article/10.3847/1538-4357/ab2be5/pdf",
                     "DELS", "10:48:19.077", "-01:09:40.42", "",
                     "6.6759", "0.0002", "0.0002", "", "", "", "", "", "",
                     "", "", "", "-25.97", "0.18", "0.18", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     "M1450 from Wang et al. (2019)"]])

# M1450 from: https://iopscience.iop.org/article/10.3847/1538-4357/ab2be5/pdf Wang et al. (2019)

entry75 = np.array([["J0024+3913/J006.1+39.22", "Tang et al. (2017), Koptelova et al. (2019)",
                     "https://academic.oup.com/mnras/article/466/4/4568/2712523, https://arxiv.org/pdf/1907.07458",
                     "PSO", "00:24:29.77", "+39:13:18.95", "",
                     "6.61", "0.02", "0.02", "2.19e8", "0.30e8", "0.30e8", "", "", "",
                     "", "", "", "-25.96", "0.08", "0.08", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     "mass from Koptelova et al. (2019)"]])

# mass from: https://arxiv.org/pdf/1907.07458 Koptelova et al. (2019)

entry76 = np.array([["J0305-3150", "Mazzucchelli et al. (2017)",
                     "https://iopscience.iop.org/article/10.3847/1538-4357/aa9185/pdf",
                     "VIK", "03:05:16.916", "-31:50:55.90", "",
                     "6.6145", "0.0001", "0.0001", "0.90e9", "0.29e9", "0.27e9", "0.75e47", "0.10e47", "0.34e47",
                     "0.641026", "0.223538", "0.348468", "-26.13", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     "f_Edd recalculated using formula [2]"]])

entry77 = np.array([["J0923+0402", "Yang et al. (2021), Wang et al. (2024), Wang et al. (2019)",
                     "https://iopscience.iop.org/article/10.3847/1538-4357/ac2b32, https://arxiv.org/html/2404.15413v1#S1, https://iopscience.iop.org/article/10.3847/1538-4357/ab2be5/pdf",
                     "DELS/HSC", "09:23:47.12", "+04:02:54.40", "",
                     "6.6330", "0.0003", "0.0003", "1.77e9", "0.02e9", "0.02e9", "21.7e46", "3.0e46", "3.0e46",
                     "1.0", "0.1", "0.1", "-26.61", "0.11", "0.11", "", "", "",
                     "116-729", "", "", "", "", "", "", "", "",
                     "coordinates, SFR_CII from Wang et al. (2024), M1450 from Wang et al. (2019), additional information here: https://arxiv.org/pdf/2306.16474  Mazzucchelli et al. (2023)"]])

# coordinates, SFR_CII from: https://arxiv.org/html/2404.15413v1#S1 Wang et al. (2024)
# M1450 from: https://iopscience.iop.org/article/10.3847/1538-4357/ab2be5/pdf Wang et al. (2019)

entry78 = np.array([["J2132+1217/P323+12/J323.1+12.29", "Mazzucchelli et al. (2017), Wang et al. (2019), Mazzucchelli et al. (2023)",
                     "https://arxiv.org/pdf/1710.01251, https://iopscience.iop.org/article/10.3847/1538-4357/ab2be5/pdf, https://arxiv.org/pdf/2306.16474",
                     "PSO", "21:32:33.191", "+12:17:55.26", "",
                     "6.5881", "0.0003", "0.0003", "log8.92", "log0.09", "log0.12", "log47.27", "log0.06", "log0.07",
                     "1.722093", "0.47153", "0.488433", "-27.04", "0.12", "0.12", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     "M1450 from Wang et al. (2019), mass, L_bol, (recalculated using formula [2]) f_Edd from Mazzucchelli et al. (2023)"]])

# M1450 from: https://iopscience.iop.org/article/10.3847/1538-4357/ab2be5/pdf Wang et al. (2019)
# mass, L_bol, f_Edd from: https://arxiv.org/pdf/2306.16474 Mazzucchelli et al. (2023)

entry79 = np.array([["J1526-2050/P231–20/J231.6-20.83", "Mazzucchelli et al. (2017), Mazzucchelli et al. (2023)",
                     "https://arxiv.org/pdf/1710.01251, https://arxiv.org/pdf/2306.16474",
                     "PSO", "15:26:37.841", "-20:50:00.66", "",
                     "6.5864", "0.0005", "0.0005", "log9.52", "log0.04", "log0.04", "log47.36", "log0.04", "log0.04",
                     "0.532178", "0.072611", "0.066222", "-27.14", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     "mass, L_bol, (recalculated using formula [2]) f_Edd from Mazzucchelli et al. (2023)"]])

# mass, L_bol, f_Edd from: https://arxiv.org/pdf/2306.16474 Mazzucchelli et al. (2023)

entry80 = np.array([["J0706+2921", "Yang et al. (2021), Wang et al. (2024), Wang et al. (2019)",
                     "https://iopscience.iop.org/article/10.3847/1538-4357/ac2b32, https://arxiv.org/html/2404.15413v1#S1, https://iopscience.iop.org/article/10.3847/1538-4357/ab2be5/pdf",
                     "DELS", "07:06:26.38", "+29:21:05.50", "",
                     "6.6037", "0.0003", "0.0003", "2.11e9", "0.16e9", "0.16e9", "33.9e46", "1.5e46", "1.5e46",
                     "1.3", "0.1", "0.1", "-27.51", "0.08", "0.08", "", "", "",
                     "129-808", "", "", "", "", "", "", "", "",
                     "coordinates, SFR_CII from Wang et al. (2024), M1450 from Wang et al. (2019), additional information here: https://arxiv.org/pdf/2306.16474  Mazzucchelli et al. (2023)"]])

# coordinates, SFR_CII from: https://arxiv.org/html/2404.15413v1#S1 Wang et al. (2024)
# M1450 from: https://iopscience.iop.org/article/10.3847/1538-4357/ab2be5/pdf Wang et al. (2019)

entry81 = np.array([["J1135+5011", "Yang et al. (2021), Wang et al. (2024), Wang et al. (2019)",
                     "https://iopscience.iop.org/article/10.3847/1538-4357/ac2b32, https://arxiv.org/html/2404.15413v1#S1, https://iopscience.iop.org/article/10.3847/1538-4357/ab2be5/pdf",
                     "DELS", "11:35:08.92", "+50:11:32.60", "",
                     "6.5851", "0.0008", "0.0008", "1.49e9", "0.05e9", "0.05e9", "10.8e46", "0.8e46", "0.8e46",
                     "0.6", "0.1", "0.1", "-26.19", "0.17", "0.17", "", "", "",
                     "107-669", "", "", "", "", "", "", "", "",
                     "coordinates, SFR_CII from Wang et al. (2024), M1450 from Wang et al. (2019)"]])

# coordinates, SFR_CII from: https://arxiv.org/html/2404.15413v1#S1 Wang et al. (2024)
# M1450 from: https://iopscience.iop.org/article/10.3847/1538-4357/ab2be5/pdf Wang et al. (2019)

entry82 = np.array([["J0921+0007", "Yang et al. (2021), Matsuoka et al. (2018), Wang et al. (2024)",
                     "https://iopscience.iop.org/article/10.3847/1538-4357/ac2b32, https://arxiv.org/pdf/1803.01861, https://arxiv.org/html/2404.15413v1#S1",
                     "HSC", "09:21:20.56", "+00:07:22.90", "",
                     "6.5646", "0.0003", "0.0003", "0.26e9", "0.01e9", "0.01e9", "6.1e46", "0.6e46", "0.6e46",
                     "1.9", "0.2", "0.2", "-24.79", "0.10", "0.10", "", "", "",
                     "62-389", "", "", "", "", "", "", "", "",
                     "coordinates, SFR_CII from Wang et al. (2024), M1450 from Matsuoka et al. (2018)"]])

# coordinates, SFR_CII from: https://arxiv.org/html/2404.15413v1#S1 Wang et al. (2024)
# M1450 from: https://arxiv.org/pdf/1803.01861 Matsuoka et al. (2018)

entry83 = np.array([["J0226+0302/J036.5+03.04", "Banados et al. (2016), Mazzucchelli et al. (2017), Wang et al. (2019), D'Odorico et al. (2023)",
                     "https://arxiv.org/pdf/1608.03279, https://iopscience.iop.org/article/10.3847/1538-4357/aa9185/pdf, https://iopscience.iop.org/article/10.3847/1538-4357/ab2be5/pdf, https://academic.oup.com/mnras/article/523/1/1399/7172883",
                     "PSO", "02:26:01.87", "+03:02:59.42", "",
                     "6.5405", "0.0001", "0.0001", "log9.43", "log0.08", "log0.10", "log47.5", "log0.04", "log0.05",
                     "0.903767", "0.202531", "0.166613", "-27.18", "0.12", "0.12", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     "L_bol, (recalculated using formula [2]) f_Edd from Mazzucchelli et al. (2017), M1450 from Wang et al. (2019), z, mass from D'Odorico et al. (2023)"]])

# L_bol, f_Edd from: https://iopscience.iop.org/article/10.3847/1538-4357/aa9185/pdf Mazzucchelli et al. (2017)
# M1450 from: https://iopscience.iop.org/article/10.3847/1538-4357/ab2be5/pdf Wang et al. (2019)
# z, mass from: https://academic.oup.com/mnras/article/523/1/1399/7172883 D'Odorico et al. (2023)

entry84 = np.array([["J0224-4711", "Reed et al. (2019), Wang et al. (2024)",
                     "https://academic.oup.com/mnras/article/487/2/1874/5505847, https://arxiv.org/html/2404.15413v1#S1",
                     "VDES", "02:24:26.54", "-47:11:29.40", "",
                     "6.526", "0.0003", "0.0003", "2.12e9", "0.42e9", "0.42e9", "3.13e47", "0.04e47", "0.04e47",
                     "1.13", "0.22", "0.22", "-26.72", "0.05", "0.05", "", "", "",
                     "370-2316", "", "", "", "", "", "", "", "",
                     "SFR_CII from Wang et al. (2024), additional information here: https://arxiv.org/pdf/2306.16474  Mazzucchelli et al. (2023)"]])

# SFR_CII from: https://arxiv.org/html/2404.15413v1#S1 Wang et al. (2024)

entry85 = np.array([["J0439+1634", "Yang et al. (2021), Wang et al. (2024)",
                     "https://iopscience.iop.org/article/10.3847/1538-4357/ac2b32, https://arxiv.org/html/2404.15413v1#S1",
                     "UHS", "04:39:47.10", "+16:34:15.80", "",
                     "6.5188", "0.0004", "0.0004", "0.63e9", "0.02e9", "0.02e9", "4.6e46", "0.1e46", "0.1e46",
                     "0.6", "0.1", "0.1", "-25.31", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     "coordinates from Wang et al. (2024), additional information here: https://arxiv.org/pdf/2306.16474  Mazzucchelli et al. (2023)"]])

# coordinates from: https://arxiv.org/html/2404.15413v1#S1 Wang et al. (2024)

entry86 = np.array([["J1110-1329/J167.6-13.49", "Banados et al. (2016), Decarli et al. (2018), Mazzucchelli et al. (2017)",
                     "https://arxiv.org/pdf/1608.03279, https://iopscience.iop.org/article/10.3847/1538-4357/aaa5aa, https://arxiv.org/pdf/1710.01251",
                     "PSO", "11:10:33.976", "-13:29:45.60", "",
                     "6.508", "0.001", "0.001", "0.30e9", "0.08e9", "0.12e9", "0.47e47", "0.16e47", "0.22e47",
                     "1.20513", "0.52114", "0.742014", "-25.62", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     "coordinates, z errors from Decarli et al. (2018), mass, L_bol, (recalaculated using formula [2]) f_Edd from Mazzucchelli et al. (2017)"]])

# coordinates, z errors from: https://iopscience.iop.org/article/10.3847/1538-4357/aaa5aa Decarli et al. (2018)
# mass, L_bol, f_Edd from: https://arxiv.org/pdf/1710.01251 Mazzucchelli et al. (2017)

entry87 = np.array([["J1545+4232", "Matsuoka et al. (2018), Ishimoto et al. (2020)",
                     "https://arxiv.org/pdf/1803.01861, https://iopscience.iop.org/article/10.3847/1538-4357/abb80b/pdf",
                     "HSC", "15:45:05.62", "+42:32:11.60", "",
                     "6.511", "0.003", "0.004", "", "", "", "log44.68", "log0.03", "log0.03",
                     "", "", "", "-24.76", "0.17", "0.17", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     "z, M1450 from Ishimoto et al. (2020)"]])

# z, M1450 from: https://iopscience.iop.org/article/10.3847/1538-4357/abb80b/pdf Ishimoto et al. (2020)

entry88 = np.array([["J1350-0027", "Matsuoka et al. (2019)",
                     "https://arxiv.org/pdf/1908.07910",
                     "HSC", "13:50:12.04", "-00:27:05.20", "",
                     "6.49", "", "", "", "", "", "", "", "",
                     "", "", "", "-24.38", "0.19", "0.19", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry89 = np.array([["J1629+2407/J247.2+24.12", "Mazzucchelli et al. (2017)",
                     "https://arxiv.org/pdf/1710.01251",
                     "PSO", "16:29:11.296", "+24:07:39.74", "",
                     "6.476", "0.004", "0.004", "0.52e9", "0.22e9", "0.25e9", "1.77e47", "0.06e47", "0.76e47",
                     "2.61834", "1.11131", "1.68778", "-26.53", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     "f_Edd recalculated using formula [2]"]])

entry90 = np.array([["J2131-4359", "Yang et al. (2019)",
                     "https://iopscience.iop.org/article/10.3847/1538-3881/ab1be1/meta",
                     "DES", "21:31:10.29", "-43:59:02.50", "",
                     "6.45", "", "", "", "", "", "", "", "",
                     "", "", "", "-24.93", "0.25", "0.25", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry91 = np.array([["J1724+1901/J261+19/J261.0+19.02", "Mazzucchelli et al. (2017), Wang et al. (2019), Eilers et al. (2020)",
                     "https://arxiv.org/pdf/1710.01251, https://iopscience.iop.org/article/10.3847/1538-4357/ab2be5/pdf, https://arxiv.org/pdf/2002.01811",
                     "PSO", "17:24:08.743", "+19:01:43.12", "",
                     "6.494", "0.011", "0.007", "", "", "", "log46.69", "", "",
                     "0.80", "0.12", "0.12", "-25.51", "0.19", "0.19", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     "M1450 from Wang et al. (2019), z, L_bol, f_Edd from Eilers et al. (2020)"]])

# M1450 from: https://iopscience.iop.org/article/10.3847/1538-4357/ab2be5/pdf Wang et al. (2019)
# z, L_bol, f_Edd from: https://arxiv.org/pdf/2002.01811 Eilers et al. (2020)

entry92 = np.array([["J1212+0505/P183+05/J183.1+05.09", "Mazzucchelli et al. (2017), Wang et al. (2019), Mazzucchelli et al. (2023)",
                     "https://arxiv.org/pdf/1710.01251, https://iopscience.iop.org/article/10.3847/1538-4357/ab2be5/pdf, https://arxiv.org/pdf/2306.16474",
                     "PSO", "12:12:26.981", "+05:05:33.49", "",
                     "6.4386", "0.0004", "0.0004", "log9.41", "log0.21", "log0.41", "log47.2", "log0.16", "log0.25",
                     "0.474304", "0.362793", "0.356458", "-26.80", "0.10", "0.10", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     "M1450 from Wang et al. (2019), mass, L_bol, (recalculated using formula [2]) f_Edd from Mazzucchelli et al. (2023)"]])

# M1450 from: https://iopscience.iop.org/article/10.3847/1538-4357/ab2be5/pdf Wang et al. (2019)
# mass, L_bol, f_Edd from: https://arxiv.org/pdf/2306.16474 Mazzucchelli et al. (2023)

entry93 = np.array([["J2318-3113", "Decarli et al. (2018)",
                     "https://iopscience.iop.org/article/10.3847/1538-4357/aaa5aa",
                     "VIK", "23:18:18.351", "-31:13:46.35", "",
                     "6.444", "0.005", "0.005", "", "", "", "", "", "",
                     "", "", "", "-26.11", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry94 = np.array([["J0210-0456", "Banados et al. (2016), Willott et al. (2015)",
                     "https://arxiv.org/pdf/1608.03279, https://iopscience.iop.org/article/10.1088/0004-637X/801/2/123#apj509348t2",
                     "CFHQS", "02:10:13.19", "-04:56:20.90", "",
                     "6.4323", "0.0005", "0.0005", "0.8e8", "1.0e8", "0.6e8", "", "", "",
                     "", "", "", "-24.53", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     "z, mass from Willott et al. (2015)"]])

# z, mass from: https://iopscience.iop.org/article/10.1088/0004-637X/801/2/123#apj509348t2 Willott et al. (2015)

entry95 = np.array([["J0045+0901/J011.3+09.03", "Mazzucchelli et al. (2017)",
                     "https://arxiv.org/pdf/1710.01251",
                     "PSO", "00:45:33.568", " +09:01:56.96", "",
                     "6.42", "0.05", "0.05", "", "", "", "", "", "",
                     "", "", "", "-25.95", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry96 = np.array([["J1148+5251", "Banados et al. (2016), Willott et al. (2015)",
                     "https://arxiv.org/pdf/1608.03279, https://iopscience.iop.org/article/10.1088/0004-637X/801/2/123#apj509348t2",
                     "SDSS", "11:48:16.65", "+52:51:50.39", "",
                     "6.4189", "0.0006", "0.0006", "4.9e9", "4.9e9", "2.5e9", "", "", "",
                     "", "", "", "-27.62", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     "z, mass from Willott et al. (2015)"]])

# z, mass from: https://iopscience.iop.org/article/10.1088/0004-637X/801/2/123#apj509348t2 Willott et al. (2015)

entry97 = np.array([["J2329-0301", "Banados et al. (2016), Ishimoto et al. (2020)",
                     "https://arxiv.org/pdf/1608.03279, https://iopscience.iop.org/article/10.3847/1538-4357/abb80b/pdf",
                     "CFHQS", "23:29:08.28", "-03:01:58.80", "",
                     "6.4164", "0.0008", "0.0008", "", "", "", "", "", "",
                     "", "", "", "-25.25", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     "z from Ishimoto et al. (2020)"]])

# z from: https://iopscience.iop.org/article/10.3847/1538-4357/abb80b/pdf Ishimoto et al. (2020)

entry98 = np.array([["J0216-5226", "Yang et al. (2019)",
                     "https://iopscience.iop.org/article/10.3847/1538-3881/ab1be1/meta",
                     "DES", "02:16:38.85", "-52:26:20.60", "",
                     "6.41", "", "", "", "", "", "", "", "",
                     "", "", "", "-25.19", "0.19", "0.19", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry99 = np.array([["J1004+0239", "Matsuoka et al. (2018)",
                     "https://arxiv.org/pdf/1803.01861",
                     "HSC", "10:04:01.36", "+02:39:30.70", "",
                     "6.41", "", "", "", "", "", "log44.27", "log0.01", "log0.01",
                     "", "", "", "-24.52", "0.03", "0.03", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry100 = np.array([["J1535+1943", "Wang et al. (2019), Yang et al. (2021), D'Odorico et al. (2023)",
                     "https://iopscience.iop.org/article/10.3847/1538-4357/ab2be5/pdf, https://iopscience.iop.org/article/10.3847/1538-4357/ac2b32, https://academic.oup.com/mnras/article/523/1/1399/7172883",
                     "DELS", "15:35:32.87", "+19:43:20.10", "",
                     "6.370", "0.001", "0.001", "3.53e9", "0.33e9", "0.33e9", "33.5e46", "1.7e46", "1.7e46",
                     "0.8", "0.1", "0.1", "-27.01", "0.13", "0.13", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     "z, mass, L_bol, f_Edd from Yang et al. (2021), coordinates from D'Odorico et al. (2023), additional information here: https://arxiv.org/pdf/2306.16474  Mazzucchelli et al. (2023)"]])

# z, mass, L_bol, f_Edd from: https://iopscience.iop.org/article/10.3847/1538-4357/ac2b32 Yang et al. (2021)
# coordinates from: https://academic.oup.com/mnras/article/523/1/1399/7172883 D'Odorico et al. (2023)

entry101 = np.array([["J1137+0045", "Matsuoka et al. (2019)",
                     "https://arxiv.org/pdf/1908.07910",
                     "HSC", "11:37:53.64", "+00:45:09.70", "",
                     "6.4", "", "", "", "", "", "", "", "",
                     "", "", "", "-24.20", "0.13", "0.13", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry102 = np.array([["J0844+0226", "Matsuoka et al. (2019)",
                     "https://arxiv.org/pdf/1908.07910",
                     "HSC", "08:44:56.62", "+02:26:40.50", "",
                     "6.40", "", "", "", "", "", "", "", "",
                     "", "", "", "-21.57", "0.47", "0.47", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry103 = np.array([["J2236+0032", "Banados et al. (2016), Matsuoka et al. (2016)",
                     "https://arxiv.org/pdf/1608.03279, https://iopscience.iop.org/article/10.3847/0004-637X/828/1/26",
                     "HSC", "22:36:44.58", "+00:32:56.90", "",
                     "6.40", "", "", "", "", "", "", "", "",
                     "", "", "", "-23.66", "0.10", "0.10", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     "M1450 from Matsuoka et al. (2016), very uncertain redshift"]])

# M1450 from: https://iopscience.iop.org/article/10.3847/0004-637X/828/1/26 Matsuoka et al. (2016)

entry104 = np.array([["J0859+0022", "Banados et al. (2016), Ishimoto et al. (2020), Onoue et al. (2019)",
                     "https://arxiv.org/pdf/1608.03279, https://iopscience.iop.org/article/10.3847/1538-4357/abb80b/pdf, https://arxiv.org/pdf/1904.07278",
                     "HSC", "08:59:07.19", "+00:22:55.90", "",
                     "6.3903", "0.0005", "0.0005", "0.38e8", "0.10e8", "0.18e8", "", "", "",
                     "1.1", "0.5", "0.3", "-23.10", "0.27", "0.27", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     "z from Ishimoto et al. (2020), M1450, mass, f_Edd from Onoue et al. (2019), L_bol (LyA) from Matsuoka et al. (2018)"]])

# z from: https://iopscience.iop.org/article/10.3847/1538-4357/abb80b/pdf Ishimoto et al. (2020)
# M1450, mass, f_Edd from: https://arxiv.org/pdf/1904.07278 Onoue et al. (2019)


entry105 = np.array([["J1036-0232/J159.2-02.54/P159-02", "Banados et al. (2016), Decarli et al. (2018), Yue et al. (2024)",
                     "https://arxiv.org/pdf/1608.03279, https://iopscience.iop.org/article/10.3847/1538-4357/aaa5aa, https://arxiv.org/pdf/2309.04614",
                     "PSO", "10:36:54.191", "-02:32:37.94", "",
                     "6.38", "0.05", "0.05", "log9.096", "log0.007", "log0.005", "", "", "",
                     "0.93", "", "", "-26.80", "", "", "", "", "",
                     "", "", "", "", "", "", "log10.14", "log0.34", "log0.36",
                     "z, coordinates from Decarli et al. (2018), mass, f_Edd, M_star from Yue et al. (2024)"]])

# z, coordinates from: https://iopscience.iop.org/article/10.3847/1538-4357/aaa5aa Decarli et al. (2018)
# mass, f_Edd, M_star from: https://arxiv.org/pdf/2309.04614 Yue et al. (2024)

entry106 = np.array([["J0803+3138", "Wang et al. (2019), Yang et al. (2021)",
                     "https://iopscience.iop.org/article/10.3847/1538-4357/ab2be5/pdf, https://iopscience.iop.org/article/10.3847/1538-4357/ac2b32",
                     "DELS", "08:03:05.42", "+31:38:34.20", "",
                     "6.377", "0.006", "0.006", "1.40e9", "0.18e9", "0.18e9", "13.4e46", "1.1e46", "1.1e46",
                     "0.8", "0.1", "0.1", "-26.51", "0.14", "0.14", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     "mass, L_bol, f_Edd from Yang et al. (2021)"]])

# mass, L_bol, f_Edd from: https://iopscience.iop.org/article/10.3847/1538-4357/ac2b32 Yang et al. (2021)

entry107 = np.array([["J1152+0055", "Banados et al. (2016), Ishimoto et al. (2020), Onoue et al. (2019)",
                     "https://arxiv.org/pdf/1608.03279, https://iopscience.iop.org/article/10.3847/1538-4357/abb80b/pdf, https://arxiv.org/pdf/1904.07278",
                     "VIK/HSC", "11:52:21.27", "+00:55:36.69", "",
                     "6.3637", "0.0005", "0.0005", "6.3e8", "0.8e8", "1.2e8", "", "", "",
                     "0.43", "0.08", "0.05", "-25.08", "0.07", "0.07", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     "z, mass from Ishimoto et al. (2020), mass, f_Edd from Onoue et al. (2019), L_bol from Matsuoka et al. (2018)"]])

# z, M1450 from: https://iopscience.iop.org/article/10.3847/1538-4357/abb80b/pdf Ishimoto et al. (2020)
# mass, f_Edd from: https://arxiv.org/pdf/1904.07278 Onoue et al. (2019)


entry108 = np.array([["J0211-0203", "Matsuoka et al. (2018)",
                     "https://arxiv.org/pdf/1803.01861",
                     "HSC", "02:11:44.53", "-02:03:03.90", "",
                     "6.37", "", "", "", "", "", "", "", "",
                     "", "", "", "-23.36", "0.06", "0.06", "43.64", "0.04", "0.04",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry109 = np.array([["J2304+0045", "Matsuoka et al. (2018), Ishimoto et al. (2020)",
                     "https://arxiv.org/pdf/1803.01861, https://iopscience.iop.org/article/10.3847/1538-4357/abb80b/pdf	",
                     "HSC", "23:04:22.97", "+00:45:05.40", "",
                     "6.3504", "0.0002", "0.0002", "", "", "", "log43.79", "log0.03", "log0.03",
                     "", "", "", "-24.28", "0.03", "0.03", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     "z from Ishimoto et al. (2020)"]])

# z from: https://iopscience.iop.org/article/10.3847/1538-4357/abb80b/pdf Ishimoto et al. (2020)

entry110 = np.array([["J1316+1028", "Wang et al. (2019), Yang et al. (2021)",
                     "https://iopscience.iop.org/article/10.3847/1538-4357/ab2be5/pdf, https://iopscience.iop.org/article/10.3847/1538-4357/ac2b32",
                     "DELS", "13:16:08.14", "+10:28:32.80", "",
                     "6.35", "0.04", "0.04", "1.01e9", "0.37e9", "0.37e9", "14.8e46", "3.3e46", "3.3e46",
                     "1.2", "0.5", "0.5", "-25.73", "0.17", "0.17", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     "mass, L_bol, f_Edd from Yang et al. (2021)"]])

# mass, L_bol, f_Edd from: https://iopscience.iop.org/article/10.3847/1538-4357/ac2b32 Yang et al. (2021)

entry111 = np.array([["J0857+0056", "Matsuoka et al. (2018)",
                     "https://arxiv.org/pdf/1704.05854",
                     "HSC", "08:57:38.53", "+00:56:12.70", "",
                     "6.35", "", "", "", "", "", "", "", "",
                     "", "", "", "-23.01", "0.07", "0.07", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry112 = np.array([["J2255+0251", "Matsuoka et al. (2018)",
                     "https://arxiv.org/pdf/1803.01861",
                     "HSC", "22:55:38.04", "+02:51:26.60", "",
                     "6.34", "", "", "", "", "", "", "", "",
                     "", "", "", "-23.87", "0.04", "0.04", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry113 = np.array([["J2211-3206/J332.8-32.10", "Decarli et al. (2018), Mazzucchelli et al. (2023)",
                     "https://iopscience.iop.org/article/10.3847/1538-4357/aaa5aa, https://arxiv.org/pdf/2306.16474",
                     "VIK/VST-ATLAS", "22:11:12.391", "-32:06:12.94", "",
                     "6.3394", "0.0010", "0.0010", "log9.3", "log0.15", "log0.24", "log47.44", "0.04", "0.05",
                     "1.061834", "0.449866", "0.465366", "-26.71", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     "mass, L_bol, (recalculated using formula [2]) f_Edd from Mazzucchelli et al. (2023), additional information here: https://iopscience.iop.org/article/10.3847/1538-4357/ab2f75#apjab2f75fn1 Mazzucchelli et al. (2019), https://academic.oup.com/mnras/article/478/2/1649/4944228 Chehade et al. (2018)"]])

# mass, L_bol, f_Edd from: https://arxiv.org/pdf/2306.16474 Mazzucchelli et al. (2023)

entry114 = np.array([["J1406-0116", "Matsuoka et al. (2018), Ishimoto et al. (2020)",
                     "https://arxiv.org/pdf/1803.01861, https://iopscience.iop.org/article/10.3847/1538-4357/abb80b/pdf",
                     "HSC", "14:06:29.12", "-01:16:11.20", "",
                     "6.292", "0.002", "0.002", "", "", "", "", "", "",
                     "", "", "", "-24.76", "0.18", "0.18", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

# z, M1450 from: https://iopscience.iop.org/article/10.3847/1538-4357/abb80b/pdf Ishimoto et al. (2020)

entry115 = np.array([["J1148+0702", "Decarli et al. (2018), Shen et al. (2019)",
                     "https://iopscience.iop.org/article/10.3847/1538-4357/aaa5aa, https://iopscience.iop.org/article/10.3847/1538-4357/ab03d9/pdf",
                     "ULAS", "11:48:03.286", "+07:02:08.33", "",
                     "6.344", "0.006", "0.006", "", "", "", "", "", "",
                     "", "", "", "-26.49", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     "z from Shen et al. (2019)"]])

# z from: https://iopscience.iop.org/article/10.3847/1538-4357/ab03d9/pdf Shen et al. (2019)

entry116 = np.array([["J0142-3327/J025.6-33.46", "Carnall et al. (2015), Mazzucchelli et al. (2023)",
                     "https://academic.oup.com/mnrasl/article/451/1/L16/954689, https://arxiv.org/pdf/2306.16474",
                     "ATLAS", "01:42:43.70", "-33:27:45.72", "",
                     "6.31", "0.03", "0.03", "log9.37", "log0.17", "log0.1", "log47.66", "log0.02", "log0.02",
                     "1.49988", "0.722074", "0.315783", "-27.8", "0.2", "0.2", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     "mass, L_bol, (recalculated using formula [2]) f_Edd from Mazzucchelli et al. (2023)"]])

# mass, L_bol, f_Edd from: https://arxiv.org/pdf/2306.16474 Mazzucchelli et al. (2023)

entry117 = np.array([["J1030+0524/J1030+05", "Banados et al. (2016), D'Odorico et al. (2023), Yue et al. (2024), Mazzucchelli et al. (2023)",
                     "https://arxiv.org/pdf/1608.03279, https://academic.oup.com/mnras/article/523/1/1399/7172883, https://arxiv.org/pdf/2309.04614, https://arxiv.org/pdf/2306.16474",
                     "SDSS", "10:30:27.11", "+05:24:55.06", "",
                     "6.304", "0.002", "0.002", "log9.187", "log0.004", "log0.003", "log47.32", "log0.11", "log0.14",
                     "0.94", "", "", "-26.99", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     "z from D'Odorico et al. (2023), mass, f_Edd from Yue et al. (2024), L_bol from Mazzucchelli et al. (2023)"]])

# z from: https://academic.oup.com/mnras/article/523/1/1399/7172883 D'Odorico et al. (2023)
# mass, f_Edd from: https://arxiv.org/pdf/2309.04614 Yue et al. (2024)
# L_bol from: https://arxiv.org/pdf/2306.16474 Mazzucchelli et al. (2023)

entry118 = np.array([["J1146-0005", "Matsuoka et al. (2018)",
                     "https://arxiv.org/pdf/1803.01861",
                     "HSC", "11:46:58.89", "-00:05:37.70", "",
                     "6.30", "", "", "", "", "", "", "", "",
                     "", "", "", "-21.46", "0.63", "0.63", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry119 = np.array([["J1525+4303", "Matsuoka et al. (2019)",
                     "https://arxiv.org/pdf/1908.07910",
                     "HSC", "15:25:55.79", "+43:03:24.00", "",
                     "6.27", "", "", "", "", "", "", "", "",
                     "", "", "", "-23.61", "0.06", "0.06", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry120 = np.array([["(Tentative) J0905+0300", "Matsuoka et al. (2018)",
                     "https://arxiv.org/pdf/1704.05854",
                     "HSC", "09:05:44.65", "+03:00:58.80", "",
                     "6.27", "", "", "", "", "", "", "", "",
                     "", "", "", "-22.55", "0.11", "0.11", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry121 = np.array([["J1146+0124", "Matsuoka et al. (2018)",
                     "https://arxiv.org/pdf/1803.01861",
                     "HSC", "11:46:48.42", "+01:24:20.10", "",
                     "6.27", "", "", "", "", "", "", "", "",
                     "", "", "", "-23.71", "0.07", "0.07", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry122 = np.array([["J1623+3112", "Ishimoto et al. (2020), Eilers et al. (2017)",
                     "https://iopscience.iop.org/article/10.3847/1538-4357/abb80b/pdf, https://iopscience.iop.org/article/10.3847/1538-4357/aa6c60",
                     "SDSS", "16:23:31.81", "+31:12:00.53", "",
                     "6.2572", "0.0024", "0.0024", "", "", "", "", "", "",
                     "", "", "", "-26.55", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     "Instrument from Eilers et al. (2017)"]])

# Instrument from: https://iopscience.iop.org/article/10.3847/1538-4357/aa6c60 Eilers et al. (2017)

entry123 = np.array([["J0050+3445", "Ishimoto et al. (2020), Eilers et al. (2017)",
                     "https://iopscience.iop.org/article/10.3847/1538-4357/abb80b/pdf, https://iopscience.iop.org/article/10.3847/1538-4357/aa6c60",
                     "CFHQS", "00:55:02.91", "+34:45:21.65", "",
                     "6.253", "0.003", "0.003", "", "", "", "", "", "",
                     "", "", "", "-26.70", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     "Instrument from Eilers et al. (2017)"]])

# Instrument from: https://iopscience.iop.org/article/10.3847/1538-4357/aa6c60 Eilers et al. (2017)

entry124 = np.array([["J0323-4701", "Eilers et al. (2020), Reed et al. (2017)",
                     "https://arxiv.org/pdf/2002.01811, https://academic.oup.com/mnras/article/468/4/4702/3089747",
                     "VDES", "03:23:40.340", "-47:11:29.400", "",
                     "6.241", "0.002", "0.002", "0.28e9", "0.20e9", "0.20e9", "log46.81", "", "",
                     "1.76", "1.24", "1.24", "-26.02", "0.07", "0.07", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     "M1450 from Reed et al. (2017)"]])

# M1450 from: https://academic.oup.com/mnras/article/468/4/4702/3089747 Reed et al. (2017)

entry125 = np.array([["J0143-5545", "Reed et al. (2017)",
                     "https://academic.oup.com/mnras/article/468/4/4702/3089747",
                     "VDES", "01:43:10.24", "-55:45:10.68", "",
                     "6.25", "0.01", "0.01", "", "", "", "", "", "",
                     "", "", "", "-25.65", "0.12", "0.12", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry126 = np.array([["J0844-0052", "Matsuoka et al. (2018)",
                     "https://arxiv.org/pdf/1704.05854",
                     "HSC", "08:44:31.60", "-00:52:54.60", "",
                     "6.25", "", "", "", "", "", "", "", "",
                     "", "", "", "-23.74", "0.23", "0.23", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry127 = np.array([["J2032-2114/P308-21/J308.0-21.23", "Banados et al. (2016), Decarli et al. (2018)",
                     "https://arxiv.org/pdf/1608.03279, https://iopscience.iop.org/article/10.3847/1538-4357/aaa5aa",
                     "PSO", "20:32:09.996", "-21:14:02.31", "",
                     "6.24", "0.05", "0.05", "", "", "", "", "", "",
                     "", "", "", "-26.35", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     "coordinates, z from Decarli et al. (2018)"]])

# coordinates, z from: https://iopscience.iop.org/article/10.3847/1538-4357/aaa5aa Decarli et al. (2018)

entry128 = np.array([["J1048+4637", "Banados et al. (2016)",
                     "https://arxiv.org/pdf/1608.03279",
                     "SDSS", "10:48:45.07", "+46:37:18.55", "",
                     "6.2284", "", "", "", "", "", "", "", "",
                     "", "", "", "-27.24", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry129 = np.array([["J0410-4414", "Reed et al. (2017)",
                     "https://academic.oup.com/mnras/article/468/4/4702/3089747",
                     "VDES", "04:10:03.23", "-44:14:40.70", "",
                     "6.21", "0.01", "0.01", "", "", "", "", "", "",
                     "", "", "", "-26.14", "0.09", "0.09", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry130 = np.array([["J0136+0226", "Banados et al. (2016), Shen et al. (2019)",
                     "https://arxiv.org/pdf/1608.03279, https://iopscience.iop.org/article/10.3847/1538-4357/ab03d9/pdf",
                     "CFHQS", "01:36:03.17", "+02:26:05.70", "",
                     "6.206", "0.009", "0.009", "", "", "", "", "", "",
                     "", "", "", "-24.66", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     "z from Shen et al. (2019)"]])

# z from: https://iopscience.iop.org/article/10.3847/1538-4357/ab03d9/pdf Shen et al. (2019)

entry131 = np.array([["(Tentative) J0217-0208", "Matsuoka et al. (2018)",
                     "https://arxiv.org/pdf/1704.05854",
                     "HSC", "02:17:21.59", "-02:08:52.60", "",
                     "6.20", "", "", "", "", "", "", "", "",
                     "", "", "", "-23.19", "0.04", "0.04", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry132 = np.array([["J1217+0131/J184.3+01.52", "Banados et al. (2016), Wang et al. (2018)",
                     "https://arxiv.org/pdf/1608.03279, https://arxiv.org/pdf/1703.07490",
                     "PSO", "12:17:21.34", "+01:31:42.47", "",
                     "6.17", "0.05", "0.05", "", "", "", "", "", "",
                     "", "", "", "-25.37", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     "z from Wang et al. (2018)"]])

# z from: https://arxiv.org/pdf/1703.07490 Wang et al. (2018)

entry133 = np.array([["J0227-0605", "Banados et al. (2016), Shen et al. (2019)",
                     "https://arxiv.org/pdf/1608.03279, https://iopscience.iop.org/article/10.3847/1538-4357/ab03d9/pdf",
                     "CFHQS/HSC/VIK", "02:27:43.29", "-06:05:30.20", "",
                     "6.212", "0.007", "0.007", "", "", "", "", "", "",
                     "", "", "", "-25.28", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

# Instrument from: https://iopscience.iop.org/article/10.3847/1538-4357/ab03d9/pdf Shen et al. (2019)

entry134 = np.array([["J1512+4422", "Matsuoka et al. (2019)",
                     "https://arxiv.org/pdf/1908.07910",
                     "HSC", "15:12:48.71", "+44:22:17.50", "",
                     "6.19", "", "", "", "", "", "", "", "",
                     "", "", "", "-22.07", "0.04", "0.04", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry135 = np.array([["J0918+0139", "Matsuoka et al. (2018)",
                     "https://arxiv.org/pdf/1803.01861",
                     "HSC", "09:18:33.17", "+01:39:23.30", "",
                     "6.19", "", "", "", "", "", "", "", "",
                     "", "", "", "-23.71", "0.04", "0.04", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry136 = np.array([["J1429+5447", "Banados et al. (2016), Shen et al. (2019)",
                     "https://arxiv.org/pdf/1608.03279, https://iopscience.iop.org/article/10.3847/1538-4357/ab03d9/pdf",
                     "CFHQS", "14:29:52.17", "+54:47:17.70", "",
                     "6.119", "0.008", "0.008", "", "", "", "", "", "",
                     "", "", "", "-26.10", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     "z from Shen et al. (2019)"]])

# z from: https://iopscience.iop.org/article/10.3847/1538-4357/ab03d9/pdf Shen et al. (2019)

entry137 = np.array([["J2255+0503", "Matsuoka et al. (2019)",
                     "https://arxiv.org/pdf/1908.07910",
                     "HSC", "22:55:20.78", "+05:03:43.30", "",
                     "6.18", "", "", "", "", "", "", "", "",
                     "", "", "", "-24.43", "0.02", "0.02", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry138 = np.array([["J1425-0015", "Matsuoka et al. (2018)",
                     "https://arxiv.org/pdf/1704.05854	",
                     "HSC", "14:25:17.72", "-00:15:40.90", "",
                     "6.18", "", "", "", "", "", "", "", "",
                     "", "", "", "-23.44", "0.02", "0.02", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry139 = np.array([["J0402+2451/J0402+2452/P060+24/J060+24/J060.5+24.85", "Banados et al. (2016), Shen et al. (2019), Mazzucchelli et al. (2023)",
                     "https://arxiv.org/pdf/1608.03279, https://iopscience.iop.org/article/10.3847/1538-4357/ab03d9/pdf, https://arxiv.org/pdf/2306.16474",
                     "PSO", "04:02:12.69", "+24:51:24.43", "",
                     "6.170", "0.006", "0.006", "log9.18", "log0.07", "log0.09", "log47.3", "log0.08", "log0.1",
                     "1.014044", "0.27115", "0.281994", "-26.95", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     "z from Shen et al. (2019), mass, L_bol, (recalculated using formula [2]) f_Edd from Mazzucchelli et al. (2023)"]])

# z from: https://iopscience.iop.org/article/10.3847/1538-4357/ab03d9/pdf Shen et al. (2019)
# mass, L_bol, f_Edd from: https://arxiv.org/pdf/2306.16474 Mazzucchelli et al. (2023)

entry140 = np.array([["J0844-0132", "Matsuoka et al. (2018)",
                     "https://arxiv.org/pdf/1803.01861",
                     "HSC", "08:44:08.61", "-01:32:16.50", "",
                     "6.18", "", "", "", "", "", "", "", "",
                     "", "", "", "-23.97", "0.11", "0.11", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry141 = np.array([["(Tentative) J2232+0012", "Matsuoka et al. (2018)",
                     "https://arxiv.org/pdf/1704.05854",
                     "HSC", "22:32:12.03", "+00:12:38.40", "",
                     "6.18", "", "", "", "", "", "", "", "",
                     "", "", "", "-22.81", "0.10", "0.10", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry142 = np.array([["J0221-0802", "Banados et al. (2016), Shen et al. (2019)",
                     "https://arxiv.org/pdf/1608.03279, https://iopscience.iop.org/article/10.3847/1538-4357/ab03d9/pdf",
                     "CFHQS", "02:21:22.71", "-08:02:51.50", "",
                     "6.161", "0.054", "0.054", "", "", "", "", "", "",
                     "", "", "", "-24.70", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     "z from Shen et al. (2019)"]])

# z from: https://iopscience.iop.org/article/10.3847/1538-4357/ab03d9/pdf Shen et al. (2019)

entry143 = np.array([["(Tentative) J2201+0155", "Matsuoka et al. (2018)",
                     "https://arxiv.org/pdf/1704.05854",
                     "HSC", "22:01:32.07", "+01:55:29.00", "",
                     "6.16", "", "", "", "", "", "", "", "",
                     "", "", "", "-22.97", "0.04", "0.04", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry144 = np.array([["J1146-0154", "Matsuoka et al. (2016)",
                     "https://arxiv.org/pdf/1803.01861",
                     "HSC", "11:46:32.66", "-01:54:38.30", "",
                     "6.16", "", "", "", "", "", "", "", "",
                     "", "", "", "-23.43", "0.07", "0.07", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry145 = np.array([["J2219+0102/VIMOS2911001793", "Kashikawa et al. (2015)",
                     "https://arxiv.org/pdf/1410.7401",
                     "HSC", "22:19:17.22", "+01:02:48.90", "",
                     "6.156", "", "", "", "", "", "", "", "",
                     "", "", "", "-23.10", "0.11", "0.11", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry146 = np.array([["J1347-0157", "Matsuoka et al. (2019)",
                     "https://arxiv.org/pdf/1908.07910",
                     "HSC", "13:47:33.69", "-01:57:50.60", "",
                     "6.15", "", "", "", "", "", "", "", "",
                     "", "", "", "-24.73", "0.02", "0.02", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry147 = np.array([["J2356-0622/P359–06/J359.1-06.38", "Decarli et al. (2018), Wang et al. (2016), Mazzucchelli et al. (2023)",
                     "https://iopscience.iop.org/article/10.3847/1538-4357/aaa5aa, https://arxiv.org/pdf/1602.04659, https://arxiv.org/pdf/2306.16474",
                     "PSO", "23:56:32.455s", "-06:22:59.26", "",
                     "6.15", "0.02", "0.02", "log9.0", "log0.09", "log0.12", "log47.3", "log0.13", "log0.19",
                     "1.534817", "0.641691", "0.658087", "-26.79", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     "z from Wang et al. (2016), mass, L_bol, (recalculated using formula [2]) f_Edd from Mazzucchelli et al. (2023)"]])

# z from: https://arxiv.org/pdf/1602.04659 Wang et al. (2016)
# mass, L_bol, f_Edd from: https://arxiv.org/pdf/2306.16474 Mazzucchelli et al. (2023)

entry148 = np.array([["J1250+3130", "Banados et al. (2016), Ishimoto et al. (2020)",
                     "https://arxiv.org/pdf/1608.03279, https://iopscience.iop.org/article/10.3847/1538-4357/abb80b/pdf",
                     "SDSS", "12:50:51.93", "+31:30:21.90", "",
                     "6.138", "0.005", "0.005", "", "", "", "", "", "",
                     "", "", "", "-26.53", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     "z from Ishimoto et al. (2020)"]])

# z from: https://iopscience.iop.org/article/10.3847/1538-4357/abb80b/pdf Ishimoto et al. (2020)

entry149 = np.array([["J0909+0440", "Matsuoka et al. (2018)",
                     "https://arxiv.org/pdf/1803.01861",
                     "HSC", "09:09:21.50", "+04:40:42.90", "",
                     "6.15", "", "", "", "", "", "", "", "",
                     "", "", "", "-24.88", "0.02", "0.02", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry150 = np.array([["J0834+0211", "Matsuoka et al. (2018)",
                     "https://arxiv.org/pdf/1803.01861",
                     "HSC", "08:34:00.88", "+02:11:46.90", "",
                     "6.15", "", "", "", "", "", "", "", "",
                     "", "", "", "-24.05", "0.09", "0.09", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry151 = np.array([["J2318-3029", "Venemans et al. (2020), Decarli et al. (2018)",
                     "https://iopscience.iop.org/article/10.3847/1538-4357/abc563, https://iopscience.iop.org/article/10.3847/1538-4357/aaa5aa",
                     "VIK", "23:18:33.099", "-30:29:33.58", "",
                     "6.1456", "0.0002", "0.0002", "", "", "", "", "", "",
                     "", "", "", "-26.21", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     "M1450 from Decarli et al. (2018)"]])

# M1450 from: https://iopscience.iop.org/article/10.3847/1538-4357/aaa5aa Decarli et al. (2018)

entry152 = np.array([["J1448+4333", "Matsuoka et al. (2019)",
                     "https://arxiv.org/pdf/1908.07910",
                     "HSC", "14:48:23.33", "+43:33:05.90", "",
                     "6.14", "", "", "", "", "", "", "", "",
                     "", "", "", "-24.36", "0.04", "0.04", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry153 = np.array([["J0421-2657/P065–26/J065.4-26.95", "Decarli et al. (2018), Banados et al. (2016), Mazzucchelli et al. (2023)",
                     "https://iopscience.iop.org/article/10.3847/1538-4357/aaa5aa, https://arxiv.org/pdf/1608.03279, https://arxiv.org/pdf/2306.16474",
                     "PSO", "04:21:38.052", "-26:57:15.60", "",
                     "6.14", "0.05", "0.05", "log9.56", "log0.13", "log0.18", "log47.35", "log0.04", "log0.04",
                     "0.474304", "0.171724", "0.166258", "-27.25", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     "M1450 from Banados et al. (2016), mas, L_bol, (recalculated using formula [2]) f_Edd from Mazzucchelli et al. (2023)"]])

# M1450 from: https://arxiv.org/pdf/1608.03279 Banados et al. (2016)
# mass, L_bol, f_Edd from: https://arxiv.org/pdf/2306.16474 Mazzucchelli et al. (2023)

entry154 = np.array([["J1401+2749/P210+27/J210.4+27.82", "Banados et al. (2016), Shen et al. (2019)",
                     "https://arxiv.org/pdf/1608.03279, https://iopscience.iop.org/article/10.3847/1538-4357/ab03d9/pdf",
                     "PSO/UHS", "14:01:47.34", "+27:49:35.03", "",
                     "6.166", "0.007", "0.007", "", "", "", "", "", "",
                     "", "", "", "-26.54", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     "instrument, z from Shen et al. (2019)"]])

# instrument, z from: https://iopscience.iop.org/article/10.3847/1538-4357/ab03d9/pdf Shen et al. (2019)

entry155 = np.array([["J1609+3041", "Banados et al. (2016), Shen et al. (2019)",
                     "https://arxiv.org/pdf/1608.03279, https://iopscience.iop.org/article/10.3847/1538-4357/ab03d9/pdf",
                     "ULAS", "16:09:37.27", "+30:41:47.78", "",
                     "6.146", "0.006", "0.006", "", "", "", "", "", "",
                     "", "", "", "-26.38", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     "z from Shen et al. (2019)"]])

# z from: https://iopscience.iop.org/article/10.3847/1538-4357/ab03d9/pdf Shen et al. (2019)

entry156 = np.array([["J1431-0724/J217-07/J217.9-07.41", "Banados et al. (2016), D'Odorico et al. (2023), Mazzucchelli et al. (2023)",
                     "https://arxiv.org/pdf/1608.03279, https://academic.oup.com/mnras/article/523/1/1399/7172883, https://arxiv.org/pdf/2306.16474",
                     "PSO", "14:31:40.45", "-07:24:43.47", "",
                     "6.166", "0.004", "0.004", "log8.90", "log0.16", "log0.27", "log47.13", "log0.15", "log0.23",
                     "1.306341", "0.793116", "0.808866", "-26.35", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     "z, mass from D'Odorico et al. (2023), L_bol, (recalculated using formula [2]) f_Edd from Mazzucchelli et al. (2023)"]])

# z, mass from: https://academic.oup.com/mnras/article/523/1/1399/7172883 D'Odorico et al. (2023)
# L_bol, f_Edd from: https://arxiv.org/pdf/2306.16474 Mazzucchelli et al. (2023)


entry157 = np.array([["J1319+0950/J1319+09", "D'Odorico et al. (2023), Venemans et al. (2020), Banados et al. (2016)",
                     "https://academic.oup.com/mnras/article/523/1/1399/7172883, https://iopscience.iop.org/article/10.3847/1538-4357/abc563, https://arxiv.org/pdf/1608.03279",
                     "ULAS", "13:19:11.291", "+09:50:51.49", "",
                     "6.1347", "0.0005", "0.0005", "log9.53", "log0.05", "log0.05", "log47.3", "log0.07", "log0.08",
                     "0.452957", "0.096595", "0.126803", "-27.05", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     "coordinates from Venemans et al. (2020), M1450 from Banados et al. (2016), L_bol, (recalculated using formula [2]) f_Edd from Mazzucchelli et al. (2023)"]])

# coordinates from: https://iopscience.iop.org/article/10.3847/1538-4357/abc563 Venemans et al. (2020)
# M1450 from: https://arxiv.org/pdf/1608.03279 Banados et al. (2016)
# L_bol, f_Edd from: https://arxiv.org/pdf/2306.16474 Mazzucchelli et al. (2023)

entry158 = np.array([["J1516+4228", "Matsuoka et al. (2019)",
                     "https://arxiv.org/pdf/1908.07910",
                     "HSC", "15:16:57.87", "+42:28:52.90", "",
                     "6.13", "", "", "", "", "", "", "", "",
                     "", "", "", "-24.35", "0.01", "0.01", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry159 = np.array([["J0001+0006", "Matsuoka et al. (2019)",
                     "https://arxiv.org/pdf/1908.07910",
                     "HSC", "00:01:33.30", "+00:06:05.40", "",
                     "6.13", "", "", "", "", "", "", "", "",
                     "", "", "", "-23.72", "0.06", "0.06", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry160 = np.array([["J1254-0014", "Matsuoka et al. (2019)",
                     "https://arxiv.org/pdf/1908.07910",
                     "HSC", "12:54:37.08", "-00:14:10.70", "",
                     "6.13", "", "", "", "", "", "", "", "",
                     "", "", "", "-20.91", "0.32", "0.32", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry161 = np.array([["(Tentative) J1440-0107", "Matsuoka et al. (2018)",
                     "https://arxiv.org/pdf/1704.05854",
                     "HSC", "14:40:01.30", "-01:07:02.20", "",
                     "6.13", "", "", "", "", "", "", "", "",
                     "", "", "", "-22.59", "0.10", "0.10", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry162 = np.array([["(Tentative) J1423-0018", "Matsuoka et al. (2018)",
                     "https://arxiv.org/pdf/1704.05854",
                     "HSC", "14:23:31.71", "-00:18:09.10", "",
                     "6.13", "", "", "", "", "", "", "", "",
                     "", "", "", "-21.88", "0.20", "0.20", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry163 = np.array([["J0033-0125", "Banados et al. (2016), Shen et al. (2019)",
                     "https://arxiv.org/pdf/1608.03279, https://iopscience.iop.org/article/10.3847/1538-4357/ab03d9/pdf",
                     "CFHQS", "00:33:11.40", "-01:25:24.90", "",
                     "5.978", "0.010", "0.010", "", "", "", "", "", "",
                     "", "", "", "-25.14", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     "z from Shen et al. (2019)"]])

# z from: https://iopscience.iop.org/article/10.3847/1538-4357/ab03d9/pdf Shen et al. (2019)

entry164 = np.array([["J1509-1749/J1509-1", "Decarli et al. (2018), D'Odorico et al. (2023), Mazzucchelli et al. (2023)",
                     "https://iopscience.iop.org/article/10.3847/1538-4357/aaa5aa, https://academic.oup.com/mnras/article/523/1/1399/7172883, https://arxiv.org/pdf/2306.16474",
                     "CFHQS", "15:09:41.778", "-17:49:26.80", "",
                     "6.1225", "0.0007", "0.0006", "log9.30", "log0.15", "log0.22", "log47.37", "log0.06", "log0.08",
                     "0.903767", "0.396152", "0.329876", "-27.14", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     "mass from D'Odorico et al. (2023), L_bol, (recalculated using formula [2]) f_Edd from Mazzucchelli et al. (2023)"]])

# mass from: https://academic.oup.com/mnras/article/523/1/1399/7172883 D'Odorico et al. (2023)
# L_bol, f_Edd from: https://arxiv.org/pdf/2306.16474 Mazzucchelli et al. (2023)

entry165 = np.array([["J0422-1927/P065–19/J065.5-19.45", "Decarli et al. (2018)",
                     "https://iopscience.iop.org/article/10.3847/1538-4357/aaa5aa",
                     "PSO", "04:22:00.994", "-19:27:28.68", "",
                     "6.12", "0.05", "0.05", "", "", "", "", "", "",
                     "", "", "", "-26.62", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry166 = np.array([["J1427+3312", "Banados et al. (2016), Shen et al. (2019), Khusanova et al. (2022)",
                     "https://arxiv.org/pdf/1608.03279, https://iopscience.iop.org/article/10.3847/1538-4357/ab03d9/pdf, https://www.aanda.org/articles/aa/full_html/2022/08/aa43660-22/aa43660-22.html",
                     "FIRST", "14:27:38.59", "+33:12:42.00", "",
                     "6.118", "0.005", "0.005", "", "", "", "", "", "",
                     "", "", "", "-26.10", "", "", "", "", "",
                     "30-90", "", "", "", "", "", "", "", "",
                     "z from Shen et al. (2019), SFR_CII from Khusanova et al. (2022)"]])

# z from: https://iopscience.iop.org/article/10.3847/1538-4357/ab03d9/pdf Shen et al. (2019)
# SFR_CII from: https://www.aanda.org/articles/aa/full_html/2022/08/aa43660-22/aa43660-22.html Khusanova et al. (2022)

entry167 = np.array([["J2315-0023", "Banados et al. (2016), Jiang et al. (2008)",
                     "https://arxiv.org/pdf/1608.03279, https://iopscience.iop.org/article/10.1088/0004-6256/135/3/1057",
                     "SDSS", "23:15:46.57", "-00:23:58.10", "",
                     "6.117", "0.006", "0.006", "", "", "", "", "", "",
                     "", "", "", "-25.14", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     "z from Jiang et al. (2008)"]])

# z from: https://iopscience.iop.org/article/10.1088/0004-6256/135/3/1057 Jiang et al. (2008)

entry168 = np.array([["J2252+0225", "Matsuoka et al. (2018)",
                     "https://arxiv.org/pdf/1803.01861",
                     "HSC", "22:52:05.44", "+02:25:31.90", "",
                     "6.12", "", "", "", "", "", "", "", "",
                     "", "", "", "-22.74", "0.06", "0.06", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry169 = np.array([["J1558-0724/J239-07/J239.7-07.40", "Banados et al. (2016), Eilers et al. (2020)",
                     "https://arxiv.org/pdf/1608.03279, https://arxiv.org/pdf/2002.01811",
                     "PSO", "15:58:50.99", "-07:24:09.59", "",
                     "6.1097", "0.0024", "0.0024", "2.99e9", "0.09e9", "0.09e9", "log47.33", "", "",
                     "0.55", "0.02", "0.02", "-27.46", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     "z, mass, L_bol, f_Edd from Eilers et al. (2020)"]])

# z, mass, L_bol, f_Edd from: https://arxiv.org/pdf/2002.01811 Eilers et al. (2020)

entry170 = np.array([["J1428-1602/P217–16/J217.0-16.04", "Decarli et al. (2018), Mazzucchelli et al. (2023)",
                     "https://iopscience.iop.org/article/10.3847/1538-4357/aaa5aa, https://arxiv.org/pdf/2306.16474",
                     "PSO", "14:28:21.394", "-16:02:43.29", "",
                     "6.11", "0.05", "0.05", "log9.02", "log0.19", "log0.34", "log47.26", "log0.08", "log0.1",
                     "1.33677", "0.78188", "0.77608", "-26.93", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     "mass, L_bol, (recalculated using formula [2]) f_Edd from Mazzucchelli et al. (2023)"]])

# mass, L_bol, f_Edd from: https://arxiv.org/pdf/2306.16474 Mazzucchelli et al. (2023)                     

entry171 = np.array([["J0004-0049", "Matsuoka et al. (2019)",
                     "https://arxiv.org/pdf/1908.07910",
                     "HSC", "00:04:45.81", "-00:49:44.30", "",
                     "6.10", "", "", "", "", "", "", "", "",
                     "", "", "", "-23.90", "0.06", "0.06", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry172 = np.array([["J0454-4448", "Reed et al. (2017), Decarli et al. (2018)",
                     "https://academic.oup.com/mnras/article/468/4/4702/3089747, https://iopscience.iop.org/article/10.3847/1538-4357/aaa5aa",
                     "VDES", "04:54:01.79", "-44:48:31.10", "",
                     "6.0581", "0.0006", "0.0006", "", "", "", "", "", "",
                     "", "", "", "-26.36", "0.05", "0.05", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     "z from Decarli et al. (2018)"]])

# z from: https://iopscience.iop.org/article/10.3847/1538-4357/aaa5aa Decarli et al. (2018)

entry173 = np.array([["J0009+3252/J002.3+32.87", "Banados et al. (2016)",
                     "https://arxiv.org/pdf/1608.03279",
                     "PSO", "00:09:30.89", "+32:52:12.94", "",
                     "6.10", "", "", "", "", "", "", "", "",
                     "", "", "", "-25.65", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry174 = np.array([["J1406-0144", "Matsuoka et al. (2018)",
                     "https://arxiv.org/pdf/1803.01861",
                     "HSC", "14:06:46.88", "-01:44:02.60", "",
                     "6.10", "", "", "", "", "", "", "", "",
                     "", "", "", "-23.37", "0.16", "0.16", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry175 = np.array([["(Tentative) J0235-0532", "Matsuoka et al. (2018)",
                     "https://arxiv.org/pdf/1704.05854",
                     "HSC", "02:35:42.42", "-05:32:41.60", "",
                     "6.09", "", "", "", "", "", "", "", "",
                     "", "", "", "-23.01", "0.05", "0.05", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry176 = np.array([["J1602+4228", "Banados et al. (2016), Ishimoto et al. (2020), Shen et al. (2019)",
                     "https://arxiv.org/pdf/1608.03279, https://iopscience.iop.org/article/10.3847/1538-4357/abb80b/pdf, https://iopscience.iop.org/article/10.3847/1538-4357/ab03d9/pdf",
                     "SDSS/UHS", "16:02:53.98", "+42:28:24.94", "",
                     "6.083", "0.005", "0.005", "", "", "", "", "", "",
                     "", "", "", "-26.94", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     "z from Ishimoto et al. (2020), instrument from Shen et al. (2019)"]])

# z from: https://iopscience.iop.org/article/10.3847/1538-4357/abb80b/pdf Ishimoto et al. (2020)
# instrument from: https://iopscience.iop.org/article/10.3847/1538-4357/ab03d9/pdf Shen et al. (2019)

entry177 = np.array([["J0935-0110", "Matsuoka et al. (2019)",
                     "https://arxiv.org/pdf/1908.07910",
                     "HSC", "09:35:43.32", "-01:10:33.30", "",
                     "6.08", "", "", "", "", "", "", "", "",
                     "", "", "", "-21.97", "0.18", "0.28", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry178 = np.array([["J2228+0152", "Matsuoka et al. (2018), Ishimoto et al. (2020)",
                     "https://arxiv.org/pdf/1704.05854, https://iopscience.iop.org/article/10.3847/1538-4357/abb80b/pdf",
                     "HSC", "22:28:47.71", "+01:52:40.50", "",
                     "6.0805", "0.0004", "0.0004", "", "", "", "", "", "",
                     "", "", "", "-24.00", "0.04", "0.04", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     "z from Ishimoto et al. (2020)"]])

# z from: https://iopscience.iop.org/article/10.3847/1538-4357/abb80b/pdf Ishimoto et al. (2020)

entry179 = np.array([["J1932+7139/J293.0+71.65", "Banados et al. (2016)",
                     "https://arxiv.org/pdf/1608.03279",
                     "PSO", "19:32:07.62", "+71:39:08.41", "",
                     "6.08", "", "", "", "", "", "", "", "",
                     "", "", "", "-26.92", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry180 = np.array([["J0303-0019", "Banados et al. (2016), Kurk et al. (2009), Ishimoto et al. (2020)",
                     "https://arxiv.org/pdf/1608.03279, https://iopscience.iop.org/article/10.1088/0004-637X/702/2/833, https://iopscience.iop.org/article/10.3847/1538-4357/abb80b/pdf",
                     "SDSS", "03:03:31.40", "-00:19:12.90", "",
                     "6.078", "0.007", "0.007", "2e8", "1e8", "0.5e8", "", "", "",
                     "1.6", "0.4", "0.6", "-25.56", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     "mass, f_Edd from Kurk et al. (2009), z from Ishimoto et al. (2020)"]])

# mass, f_Edd from: https://iopscience.iop.org/article/10.1088/0004-637X/702/2/833 Kurk et al. (2009)
# z from: https://iopscience.iop.org/article/10.3847/1538-4357/abb80b/pdf Ishimoto et al. (2020)

entry181 = np.array([["J0353+0104", "Banados et al. (2016), Shen et al. 92019",
                     "https://arxiv.org/pdf/1608.03279, https://iopscience.iop.org/article/10.3847/1538-4357/ab03d9/pdf",
                     "SDSS", "03:53:49.73:", "01:04:04.66", "",
                     "6.057", "0.005", "0.005", "", "", "", "", "", "",
                     "", "", "", "-26.43", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     "z from Shen et al. (2019), additional information (mass, f_Edd) here: https://iopscience.iop.org/article/10.1088/0004-637X/739/2/56#apj398369fd4 De Rosa et al. (2011)"]])

# z from: https://iopscience.iop.org/article/10.3847/1538-4357/ab03d9/pdf Shen et al. (2019)

entry182 = np.array([["J1034-1425/J158.6-14.42", "Chehade et al. (2018)",
                     "https://academic.oup.com/mnras/article/478/2/1649/4944228",
                     "VST-ATLAS", "10:34:46.51", "-14:25:15.96", "",
                     "6.07", "0.03", "0.03", "", "", "", "", "", "",
                     "", "", "", "-27.23", "0.08", "0.08", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry183 = np.array([["J1559+2212", "Wang et al. (2018)",
                     "https://arxiv.org/pdf/1703.07490",
                     "DELS", "15:59:09.09", "+22:12:14.43", "",
                     "6.07", "0.02", "0.02", "", "", "", "", "", "",
                     "", "", "", "-25.83", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry184 = np.array([["J0420-4453", "Reed et al. (2017)",
                     "https://academic.oup.com/mnras/article/468/4/4702/3089747",
                     "VDES", "04:20:11.34", "-44:53:23.80", "",
                     "6.07", "0.01", "0.01", "", "", "", "", "", "",
                     "", "", "", "-26.25", "0.06", "0.06", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry185 = np.array([["J0911+0152", "Matsuoka et al. (2018)",
                     "https://arxiv.org/pdf/1704.05854",
                     "HSC", "09:11:14.27", "+01:52:19.40", "",
                     "6.07", "", "", "", "", "", "", "", "",
                     "", "", "", "-22.09", "0.07", "0.07", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry186 = np.array([["J1416+0147", "Matsuoka et al. (2018)",
                     "https://arxiv.org/pdf/1803.01861",
                     "HSC", "14:16:53.01", "+01:47:02.20", "",
                     "6.07", "", "", "", "", "", "", "", "",
                     "", "", "", "-23.27", "0.10", "0.10", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry187 = np.array([["J0842+1218", "Banados et al. (2016), Venemans et al. (2020), D'Odorico et al. (2023), Mazzucchelli et al. (2023)",
                     "https://arxiv.org/pdf/1608.03279, https://iopscience.iop.org/article/10.3847/1538-4357/abc563, https://academic.oup.com/mnras/article/523/1/1399/7172883, https://arxiv.org/pdf/2306.16474",
                     "SDSS/UHS", "08:42:29.438", "+12:18:50.47", "",
                     "6.0754", "0.0005", "0.0005", "log9.30", "log0.07", "log0.09", "log47.25", "log0.05", "log0.05",
                     "0.685578", "0.146203", "0.148406", "-26.91", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     "coordinates, z from Venemans et al. (2020), mass from D'Odorico et al. (2023), L_bol, (recalculated using formula [2]) f_Edd from Mazzucchelli et al. (2023), instrument from Shen et al. (2019)"]])

# coordinates, z from: https://iopscience.iop.org/article/10.3847/1538-4357/abc563 Venemans et al. (2020)
# mass from: https://academic.oup.com/mnras/article/523/1/1399/7172883 D'Odorico et al. (2023)
# L_bol, f_Edd (MgII) from: https://arxiv.org/pdf/2306.16474 Mazzucchelli et al. (2023)
# instrument from: https://iopscience.iop.org/article/10.3847/1538-4357/ab03d9/pdf Shen et al. (2019)

entry188 = np.array([["J1630+4012", "Banados et al. (2016), Shen et al. (2019)",
                     "https://arxiv.org/pdf/1608.03279, https://iopscience.iop.org/article/10.3847/1538-4357/ab03d9/pdf",
                     "SDSS", "16:30:33.90", "+40:12:09.69", "",
                     "6.066", "0.007", "0.007", "", "", "", "", "", "",
                     "", "", "", "-26.19", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     "z from Shen et al. (2019)"]])

# z from: https://iopscience.iop.org/article/10.3847/1538-4357/ab03d9/pdf Shen et al. (2019)

entry189 = np.array([["J0106-0030", "Matsuoka et al. (2019)",
                     "https://arxiv.org/pdf/1908.07910",
                     "HSC", "01:06:03.68", "-00:30:15.20", "",
                     "6.06", "", "", "", "", "", "", "", "",
                     "", "", "", "-23.53", "0.05", "0.05", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry190 = np.array([["J1201+0133", "Matsuoka et al. (2018)",
                     "https://arxiv.org/pdf/1704.05854",
                     "HSC", "12:01:03.02", "+01:33:56.40", "",
                     "6.06", "", "", "", "", "", "", "", "",
                     "", "", "", "-23.85", "0.02", "0.02", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry191 = np.array([["J0559-1534/J089.9-15.58", "Banados et al. (2016), Mazzucchelli et al. (2023)",
                     "https://arxiv.org/pdf/1608.03279, https://arxiv.org/pdf/2306.16474",
                     "PSO", "05:59:45.47", "-15:35:00.20", "",
                     "6.05", "", "", "log9.57", "log0.08", "log0.1", "log47.57", "log0.05", "log0.06",
                     "0.769231", "0.181707", "0.186768", "-26.93", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     "mass, L_bol, (recalculated using formula [2]) f_Edd from Mazzucchelli et al. (2023)"]])

# mass, L_bol, f_Edd from: https://arxiv.org/pdf/2306.16474 Mazzucchelli et al. (2023)

entry192 = np.array([["J0828+2633", "Banados et al. (2016)",
                     "https://arxiv.org/pdf/1608.03279",
                     "ULAS", "08:28:13.41", "+26:33:55.49", "",
                     "6.05", "", "", "", "", "", "", "", "",
                     "", "", "", "-26.37", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry193 = np.array([["J2223+0326", "Matsuoka et al. (2018)",
                     "https://arxiv.org/pdf/1803.01861",
                     "HSC", "22:23:09.51", "+03:26:20.30", "",
                     "6.05", "", "", "", "", "", "", "", "",
                     "", "", "", "-25.20", "0.02", "0.02", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry194 = np.array([["J2318-0246", "Banados et al. (2016)",
                     "https://arxiv.org/pdf/1608.03279",
                     "CFHQS", "23:18:02.80", "-02:46:34.00", "",
                     "6.05", "", "", "", "", "", "", "", "",
                     "", "", "", "-25.10", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry195 = np.array([["J0957+0053", "Matsuoka et al. (2018)",
                     "https://arxiv.org/pdf/1803.01861",
                     "HSC", "09:57:40.39", "+00:53:33.60", "",
                     "6.05", "", "", "", "", "", "", "", "",
                     "", "", "", "-22.98", "0.04", "0.04", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry196 = np.array([["J1641+3755", "Banados et al. (2016), Willott et al. (2010)",
                     "https://arxiv.org/pdf/1608.03279, https://iopscience.iop.org/article/10.1088/0004-6256/140/2/546",
                     "CFHQS", "16:41:21.73", "+37:55:20.15", "",
                     "6.047", "0.003", "0.003", "2.4e8", "1.0e8", "0.8e8", "", "", "",
                     "2.3", "", "", "-25.67", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     "z, mass, f_Edd from Willott et al. (2010)"]])

# z, mass, f_Edd from: https://iopscience.iop.org/article/10.1088/0004-6256/140/2/546 Willott et al. (2010)

entry197 = np.array([["J1603+5510/ELAIS1091000446", "Kashikawa et al. (2015)",
                     "https://iopscience.iop.org/article/10.1088/0004-637X/798/1/28",
                     "HSC", "16:03:49.07", "+55:10:32.30", "",
                     "6.041", "", "", "", "", "", "", "", "",
                     "", "", "", "-22.58", "0.13", "0.13", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry198 = np.array([["J1429-0002", "Matsuoka et al. (2018)",
                     "https://arxiv.org/pdf/1704.05854",
                     "HSC", "14:29:20.22", "-00:02:07.40", "",
                     "6.04", "", "", "", "", "", "", "", "",
                     "", "", "", "-23.42", "0.04", "0.04", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry199 = np.array([["J1207+0630", "Decarli et al. (2018), Banados et al. (2016), Shen et al. (2019)",
                     "https://iopscience.iop.org/article/10.3847/1538-4357/aaa5aa, https://arxiv.org/pdf/1608.03279, https://iopscience.iop.org/article/10.3847/1538-4357/ab03d9/pdf",
                     "ULAS", "12:07:37.440", "+06:30:10.37", "",
                     "6.028", "0.013", "0.013", "", "", "", "", "", "",
                     "", "", "", "-26.63", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     "M1450 from Banados et al. (2016), z from Shen et al. (2019)"]])

# M1450 from: https://arxiv.org/pdf/1608.03279 Banados et al. (2016)
# z from: https://iopscience.iop.org/article/10.3847/1538-4357/ab03d9/pdf Shen et al. (2019)

entry200 = np.array([["J1402+4024/J210.7+40.40", "Banados et al. (2016)",
                     "https://arxiv.org/pdf/1608.03279",
                     "PSO", "14:02:54.67", "+40:24:03.19", "",
                     "6.04", "", "", "", "", "", "", "", "",
                     "", "", "", "-25.86", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry201 = np.array([["J1400-0125", "Matsuoka et al. (2018)",
                     "https://arxiv.org/pdf/1803.01861",
                     "HSC", "14:00:29.99", "-01:25:21.00", "",
                     "6.04", "", "", "", "", "", "", "", "",
                     "", "", "", "-23.70", "0.05", "0.05", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry202 = np.array([["J1400-0011", "Matsuoka et al. (2018)",
                     "https://arxiv.org/pdf/1803.01861",
                     "HSC", "14:00:28.79", "-00:11:51.50", "",
                     "6.04", "", "", "", "", "", "", "", "",
                     "", "", "", "-22.95", "0.11", "0.11", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry203 = np.array([["J2054-0005", "Banados et al. (2020), Wang et al. (2013), Willott et al. (2015)",
                     "https://arxiv.org/pdf/1608.03279, https://iopscience.iop.org/article/10.1088/0004-637X/773/1/44, https://iopscience.iop.org/article/10.1088/0004-637X/801/2/123#apj509348t2",
                     "SDSS", "20:54:06.49", "-00:05:14.80", "",
                     "6.0391", "0.0001", "0.0001", "0.9e9", "1.6e9", "0.6e9", "", "", "",
                     "", "", "", "-26.21", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     "z from Wang et al. (2013), mass from Willott et al. (2015)"]])

# z from: https://iopscience.iop.org/article/10.1088/0004-637X/773/1/44 Wang et al. (2013)
# mass from: https://iopscience.iop.org/article/10.1088/0004-637X/801/2/123#apj509348t2 Willott et al. (2015)

entry204 = np.array([["J0408-5632", "D'Odorico et al. (2023), Mazzucchelli et al. (2023), Reed et al. (2017)",
                     "https://academic.oup.com/mnras/article/523/1/1399/7172883, https://arxiv.org/pdf/2306.16474, https://academic.oup.com/mnras/article/468/4/4702/3089747",
                     "VDES", "04:08:19.23", "-56:32:28.80", "",
                     "6.033", "0.004", "0.004", "log9.31", "log0.08", "log0.09", "log47.19", "log0.08", "log0.1",
                     "0.583521", "0.166913", "0.162271", "-26.51", "0.05", "0.05", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     "L_bol, (recalculated using formula [2]) f_Edd from Mazzucchelli et al. (2023), M1450 from Reed et al. (2017)"]])

# L_bol, f_Edd (Mg II) from: https://arxiv.org/pdf/2306.16474 Mazzucchelli et al. (2023)
# M1450 from: https://academic.oup.com/mnras/article/468/4/4702/3089747 Reed et al. (2017)

entry205 = np.array([["J0206-0255", "Mastuoka et al. (2018)",
                     "https://arxiv.org/pdf/1704.05854",
                     "HSC/DELS", "02:06:11.20", "-02:55:37.80", "",
                     "6.03", "", "", "", "", "", "", "", "",
                     "", "", "", "-24.91", "0.03", "0.03", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     "additional information here: https://iopscience.iop.org/article/10.3847/1538-4357/ab2be5/pdf Wang et al. (2019)"]])

entry206 = np.array([["J0202-0251", "Matsuoka et al. (2018)",
                     "https://arxiv.org/pdf/1704.05854	",
                     "HSC", "02:02:58.21", "-02:51:53.60", "",
                     "6.03", "", "", "", "", "", "", "", "",
                     "", "", "", "-23.39", "0.07", "0.07", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry207 = np.array([["(Tentative) J1416+0015", "Matsuoka et al. (2018)",
                     "https://arxiv.org/pdf/1704.05854",
                     "HSC", "14:16:12.71", "+00:15:46.20", "",
                     "6.03", "", "", "", "", "", "", "", "",
                     "", "", "", "-22.39", "0.10", "0.10", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry208 = np.array([["J1137+3549", "Banados et al. (2016), Ishimoto et al. (2020), Shen et al. (2019)",
                     "https://arxiv.org/pdf/1608.03279, https://iopscience.iop.org/article/10.3847/1538-4357/abb80b/pdf, https://iopscience.iop.org/article/10.3847/1538-4357/ab03d9/pdf",
                     "SDSS/UHS", "11:37:17.73", "+35:49:56.85", "",
                     "6.009", "0.010", "0.010", "", "", "", "", "", "",
                     "", "", "", "-27.36", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     "z from Ishimoto et al. (2020), instrument from Shen et al. (2019)"]])

# z from: https://iopscience.iop.org/article/10.3847/1538-4357/abb80b/pdf Ishimoto et al. (2020)
# instrument from: https://iopscience.iop.org/article/10.3847/1538-4357/ab03d9/pdf Shen et al. (2019)

entry209 = np.array([["J2215+2606/P333+26/J333.9+26.10", "Banados et al. (2016), Shen et al. (2019)",
                     "https://arxiv.org/pdf/1608.03279, https://iopscience.iop.org/article/10.3847/1538-4357/ab03d9/pdf",
                     "PSO", "22:15:56.63", "+26:06:29.41", "",
                     "6.027", "0.007", "0.007", "", "", "", "", "", "",
                     "", "", "", "-26.44", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     "z from Shen et al. (2019)"]])

# z from: https://iopscience.iop.org/article/10.3847/1538-4357/ab03d9/pdf Shen et al. (2019)

entry210= np.array([["(Tentative) J1417+0117", "Matsuoka et al. (2018)",
                     "https://arxiv.org/pdf/1704.05854",
                     "HSC", "14:17:28.67", "+01:17:12.40", "",
                     "6.02", "", "", "", "", "", "", "", "",
                     "", "", "", "-22.83", "0.05", "0.05", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry211 = np.array([["J0818+1722/J0818+17", "Banados et al. (2016), D'Odorico et al. (2023), Mazzucchelli et al. (2023)",
                     "https://arxiv.org/pdf/1608.03279, https://academic.oup.com/mnras/article/523/1/1399/7172883, https://arxiv.org/pdf/2306.16474",
                     "SDSS", "08:18:27.40", "+17:22:52.01", "",
                     "5.960", "0.010", "0.010", "log9.76", "log0.06", "log0.08", "log47.56", "log0.08", "log0.1",
                     "0.485352", "0.121687", "0.123227", "-27.52", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     "z, mass from D'Odorico et al. (2023), L_bol, (recalculated using formula [2]) f_Edd from Mazzucchelli et al. (2023), there is one case where this black hole is referred to as 'J0818+1733' in https://iopscience.iop.org/article/10.3847/1538-4357/aa6c60 Eilers et al. (2017)"]])

# z, mass from: https://academic.oup.com/mnras/article/523/1/1399/7172883 D'Odorico et al. (2023)
# L_bol, f_Edd from: https://arxiv.org/pdf/2306.16474 Mazzucchelli et al. (2023)

entry212 = np.array([["J0159-3633/J029-36/J029.9-36.56", "Carnall et al. (2015), Chehade et al. (2018)",
                     "https://academic.oup.com/mnrasl/article/451/1/L16/954689, https://academic.oup.com/mnras/article/478/2/1649/4944228",
                     "ATLAS", "01:59:57.96", "-36:33:56.88", "",
                     "6.02", "0.03", "0.03", "", "", "", "", "", "",
                     "", "", "", "-26.97", "0.08", "0.08", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     "M1450 from Chehade et al. (2018)"]])

# M1450 from: https://academic.oup.com/mnras/article/478/2/1649/4944228 Chehade et al. (2018)

entry213 = np.array([["J1257+6349", "Banados et al. (2016), Jiang et al. (2015), Shen et al. (2019)",
                     "https://arxiv.org/pdf/1608.03279, https://iopscience.iop.org/article/10.1088/0004-6256/149/6/188, https://iopscience.iop.org/article/10.3847/1538-4357/ab03d9/pdf",
                     "SDSS", "12:57:57.48", "+63:49:37.16", "",
                     "5.992", "0.010", "0.010", "", "", "", "", "", "",
                     "", "", "", "-26.14", "0.12", "0.12", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     "M1450 from Jiang et al. (2015), z from Shen et al. (2019)"]])

# M1450 from: https://iopscience.iop.org/article/10.1088/0004-6256/149/6/188 Jiang et al. (2015)
# z from: https://iopscience.iop.org/article/10.3847/1538-4357/ab03d9/pdf Shen et al. (2019)

entry214 = np.array([["J1306+0356/J1306+03", "Venemans et al. (2020), Banados et al. (2016), D'Odorico et al. (2023), Mazzucchelli et al. (2023)",
                     "https://iopscience.iop.org/article/10.3847/1538-4357/abc563, https://arxiv.org/pdf/1608.03279, https://academic.oup.com/mnras/article/523/1/1399/7172883, https://arxiv.org/pdf/2306.16474",
                     "SDSS", "13:06:08.259", "+03:56:26.19", "",
                     "6.0330", "0.0002", "0.0002", "log9.29", "log0.09", "log0.12", "log47.24", "log0.05", "log0.06",
                     "0.685578", "0.178661", "0.248874", "-26.81", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     "M1450 from Banados et al. (2016), mass from D'Odorico et al. (2023), L_bol, (recalculated using formula [2]) f_Edd from Mazzucchelli et al. (2023)"]])

# M1450 from: https://arxiv.org/pdf/1608.03279 Banados et al. (2016)
# mass from: https://academic.oup.com/mnras/article/523/1/1399/7172883 D'Odorico et al. (2023)
# L_bol, f_Edd from: https://arxiv.org/pdf/2306.16474 Mazzucchelli et al. (2023)

entry215 = np.array([["J0902+0155", "Matsuoka et al. (2018)",
                     "https://arxiv.org/pdf/1704.05854",
                     "HSC", "09:02:54.87", "+01:55:10.90", "",
                     "6.01", "", "", "", "", "", "", "", "",
                     "", "", "", "-22.51", "0.04", "0.04", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry216 = np.array([["(Tentative) J0853+0139", "Matsuoka et al. (2018)",
                     "https://arxiv.org/pdf/1704.05854",
                     "HSC", "08:53:48.84", "+01:39:11.00", "",
                     "6.01", "", "", "", "", "", "", "", "",
                     "", "", "", "-22.51", "0.14", "0.14", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry217 = np.array([["J2240-1839/P340–18/J340.2-18.66", "Decarli et al. (2018), Chehade etal. (2018)",
                     "https://iopscience.iop.org/article/10.3847/1538-4357/aaa5aa, https://academic.oup.com/mnras/article/478/2/1649/4944228",
                     "PSO", "22:40:48.997", "−18:39:43.81", "",
                     "6.01", "0.05", "0.05", "", "", "", "", "", "",
                     "", "", "", "-26.42", "0.10", "0.10", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     "M1450 from Chehade et al. (2018)"]])

# M1450 from: https://academic.oup.com/mnras/article/478/2/1649/4944228 Chehade et al. (2018)

entry218 = np.array([["J1219+0050", "Matsuoka et al. (2018)",
                     "https://arxiv.org/pdf/1803.01861",
                     "HSC", "12:19:05.34", "+00:50:37.50", "",
                     "6.01", "", "", "", "", "", "", "", "",
                     "", "", "", "-23.85", "0.05", "0.05", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry219 = np.array([["(Tentative) J1207-0005", "Matsuoka et al. (2016)",
                     "https://iopscience.iop.org/article/10.3847/0004-637X/828/1/26",
                     "HSC", "12:07:54.14", "-00:05:53.30", "",
                     "6.01", "", "", "", "", "", "", "", "",
                     "", "", "", "-22.59", "0.08", "0.08", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry220 = np.array([["J0216-0455", "Willott et al. (2009), Banados et al. (2016)",
                     "https://iopscience.iop.org/article/10.1088/0004-6256/137/3/3541, https://arxiv.org/pdf/1608.03279",
                     "CFHQS", "02:16:27.81", "-04:55:34.10", "",
                     "6.01", "", "", "", "", "", "", "", "",
                     "", "", "", "-22.49", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

# M1450 from: https://arxiv.org/pdf/1608.03279 Banados et al. (2016)

entry221 = np.array([["(Tentative) J2228+0128", "Matsuoka et al. (2016)",
                     "https://iopscience.iop.org/article/10.3847/0004-637X/828/1/26",
                     "HSC", "22:28:27.83", "+01:28:09.50", "",
                     "6.01", "", "", "", "", "", "", "", "",
                     "", "", "", "-22.40", "0.12", "0.12", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry222 = np.array([["J1426-0128", "Matsuoka et al. (2019)",
                     "https://arxiv.org/pdf/1908.07910",
                     "HSC", "14:26:11.33", "-01:28:22.80", "",
                     "6.01", "", "", "", "", "", "", "", "",
                     "", "", "", "-23.75", "0.10", "0.10", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry223 = np.array([["J0055+0146", "Willott et al. (2015), Willott et al. (2009), Banados et al. (2016)",
                     "https://iopscience.iop.org/article/10.1088/0004-637X/801/2/123#apj50934, https://iopscience.iop.org/article/10.1088/0004-6256/137/3/3541, https://arxiv.org/pdf/1608.03279",
                     "CFHQS", "00:55:02.91", "+01:46:18.30", "",
                     "6.0060", "0.0008", "0.0008", "2.4e8", "2.6e8", "1.4e8", "", "", "",
                     "1.2", "", "", "-24.81", "", "", "", "", "",
                     "83", "13", "13", "", "", "", "", "", "",
                     "coordinates from Willott et al. (2009), f_Edd from Willott et al. (2010), M1450 from Banados et al. (2016)"]])

# coordinates from: https://iopscience.iop.org/article/10.1088/0004-6256/137/3/3541 Willott et al. (2009)
# f_Edd from: https://iopscience.iop.org/article/10.1088/0004-6256/140/2/546 Willott et al. (2010)
# M1450 from: https://arxiv.org/pdf/1608.03279 Banados et al. (2016)

entry224 = np.array([["J2310+1855/J2310+18", "Wang et al. (2013), D'Odorico et al. (2023), Banados et al. (2016), Shen et al. (2019), Mazzucchelli et al. (2023)",
                     "https://iopscience.iop.org/article/10.1088/0004-637X/773/1/44, https://academic.oup.com/mnras/article/523/1/1399/7172883, https://arxiv.org/pdf/1608.03279, https://iopscience.iop.org/article/10.3847/1538-4357/ab03d9/pdf, https://arxiv.org/pdf/2306.16474",
                     "SDSS", "23:10:38.89", "+18:55:19.70", "",
                     "5.956", "0.011", "0.011", "log9.67", "log0.06", "log0.08", "9.3e13S", "", "",
                     "0.508226", "0.151611", "0.15683", "-27.80", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     "coordinates, mass from D'Odorico et al. (2023), M1450 from Banados et al. (2016), z from Shen et al. (2019), (recalculated using formula [2]) f_Edd from Mazzucchelli et al. (2023)"]])

# coordinates, mass from: https://academic.oup.com/mnras/article/523/1/1399/7172883 D'Odorico et al. (2023)
# M1450 from: https://arxiv.org/pdf/1608.03279 Banados et al. (2016)
# z from: https://iopscience.iop.org/article/10.3847/1538-4357/ab03d9/pdf Shen et al. (2019)
# f_Edd from: https://arxiv.org/pdf/2306.16474 Mazzucchelli et al. (2023)

entry225 = np.array([["J2250-5015", "D'Odorico et al. (2023), Mazzucchelli et al. (2023), Reed et al. (2017)",
                     "https://academic.oup.com/mnras/article/523/1/1399/7172883, https://arxiv.org/pdf/2306.16474, https://academic.oup.com/mnras/article/468/4/4702/3089747",
                     "VDES", "22:50:02.01", "-50:15:42.20", "",
                     "5.985", "0.003", "0.003", "log9.66", "log0.41", "log0.41", "log47.44", "log0.07", "log0.08",
                     "0.463507", "0.73239", "0.293722", "-26.80", "0.04", "0.04", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     "L_bol, (recalculated using formula [2]) f_Edd from Mazzucchelli et al. (2023), M1450 from Reed et al. (2017)"]])

# L_bol, f_Edd from: https://arxiv.org/pdf/2306.16474 Mazzucchelli et al. (2023)
# M1450 from: https://academic.oup.com/mnras/article/468/4/4702/3089747 Reed et al. (2017)


entry226 = np.array([["J0028+0457/J007.0+04.95", "Banados et al. (2016), Jiang et al. (2015), Shen et al. (2019), Mazzucchelli et al. (2023)",
                     "https://arxiv.org/pdf/1608.03279, https://iopscience.iop.org/article/10.1088/0004-6256/149/6/188, https://iopscience.iop.org/article/10.3847/1538-4357/ab03d9/pdf, https://arxiv.org/pdf/2306.16474",
                     "PSO/SDSS", "00:28:06.56", "+04:57:25.64", "",
                     "5.982", "0.012", "0.012", "log9.89", "log0.09", "log0.11", "log47.12", "log0.15", "log0.22",
                     "0.130634", "0.061718", "0.059582", "-26.38", "0.10", "0.10", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     "M1450 from Jiang et al. (2015), z from Shen et al. (2019), mass, L_bol, (recalculated using formula [2]) f_Edd from Mazzucchelli et al. (2023)"]])

# M1450 from: https://iopscience.iop.org/article/10.1088/0004-6256/149/6/188 Jiang et al. (2015)
# z from: https://iopscience.iop.org/article/10.3847/1538-4357/ab03d9/pdf Shen et al. (2019)
# mass, L_bol, f_Edd from: https://arxiv.org/pdf/2306.16474 Mazzucchelli et al. (2023)

entry227 = np.array([["J0231-2850/J037.9-28.83", "Banados et al. (2016)",
                     "https://arxiv.org/pdf/1608.03279",
                     "PSO", "02:31:52.96", "-28:50:20.08", "",
                     "6.00", "", "", "", "", "", "", "", "",
                     "", "", "", "-26.23", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry228 = np.array([["J2356+0023", "Banados et al. (2016), Shen et al. (2019)",
                     "https://arxiv.org/pdf/1608.03279, https://iopscience.iop.org/article/10.3847/1538-4357/ab03d9/pdf",
                     "SDSS", "23:56:51.58", "+00:23:33.30", "",
                     "5.987", "0.014", "0.014", "", "", "", "", "", "",
                     "", "", "", "-25.50", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     "z from Shen et al. (2019)"]])

# z from: https://iopscience.iop.org/article/10.3847/1538-4357/ab03d9/pdf Shen et al. (2019)

entry229 = np.array([["J0001+2650/P000+26", "Shen et al. (2019)",
                     "https://iopscience.iop.org/article/10.3847/1538-4357/ab03d9/pdf",
                     "PSO/UHS", "00:01:21.63", "+26:50:09.20", "",
                     "5.733", "0.007", "0.007", "", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry230 = np.array([["J0002+2550", "Ishimoto et al. (2020)",
                     "https://iopscience.iop.org/article/10.3847/1538-4357/abb80b/pdf",
                     "SDSS/UHS", "00:02:39.39", "+25:50:34.96", "",
                     "5.818", "0.007", "0.007", "", "", "", "", "", "",
                     "", "", "", "-27.31", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry231 = np.array([["J0008−0626", "Shen at al. (2019), Jiang et al. (2015)",
                     "https://iopscience.iop.org/article/10.3847/1538-4357/ab03d9/pdf, https://iopscience.iop.org/article/10.1088/0004-6256/149/6/188",
                     "SDSS", "00:08:25.77", "-06:26:04.60", "",
                     "5.929", "0.003", "0.003", "", "", "", "", "", "",
                     "", "", "", "-26.04", "0.09", "0.09", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     "z, M1450 from Jiang et al. (2015)"]])

# z, M1450 from: https://iopscience.iop.org/article/10.1088/0004-6256/149/6/188 Jiang et al. (2015)

entry232 = np.array([["J0203+0012", "Shen et al. (2019), Eilers et al. (2017), Jiang et al. (2008)",
                     "https://iopscience.iop.org/article/10.3847/1538-4357/ab03d9/pdf, https://iopscience.iop.org/article/10.3847/1538-4357/aa6c60, https://iopscience.iop.org/article/10.1088/0004-6256/135/3/1057",
                     "SDSS/ULAS", "02:03:32.38", "+00:12:29.27", "",
                     "5.709", "0.010", "0.010", "", "", "", "", "", "",
                     "", "", "", "-25.72", "0.10", "0.10", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     "coordinates from Eilers et al. (2017), M1450 from Jiang et al. (2008)"]])

# coordinates from: https://iopscience.iop.org/article/10.3847/1538-4357/aa6c60 Eilers et al. (2017)
# M1450 from: https://iopscience.iop.org/article/10.1088/0004-6256/135/3/1057 Jiang et al. (2008)

entry233 = np.array([["J0300−2232/J045.1–22.54", "Banados et al. (2016), Shen et al. (2019)",
                     "https://arxiv.org/pdf/1608.03279, https://iopscience.iop.org/article/10.3847/1538-4357/ab03d9/pdf",
                     "PSO", "03:00:44.18", "-22:32:27.19", "",
                     "5.684", "0.008", "0.008", "", "", "", "", "", "",
                     "", "", "", "-26.26", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

# z from: https://iopscience.iop.org/article/10.3847/1538-4357/ab03d9/pdf Shen et al. (2019)

entry234 = np.array([["J0810+5105", "Banados et al. (2016), Shen et al. (2019)",
                     "https://arxiv.org/pdf/1608.03279, https://iopscience.iop.org/article/10.3847/1538-4357/ab03d9/pdf",
                     "SDSS", "08:10:54.31", "+51:05:40.10", "",
                     "5.805", "0.010", "0.010", "", "", "", "", "", "",
                     "", "", "", "-26.82", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     "z from Shen et al. (2019)"]])

# z from: https://iopscience.iop.org/article/10.3847/1538-4357/ab03d9/pdf Shen et al. (2019)

entry235 = np.array([["J0835+3217", "Shen et al. (2019), Jiang et al. (2016)",
                     "https://iopscience.iop.org/article/10.3847/1538-4357/ab03d9/pdf, https://iopscience.iop.org/article/10.3847/1538-4357/833/2/222",
                     "SDSS", "08:35:25.76", "+32:17:52.60", "",
                     "5.902", "0.009", "0.009", "", "", "", "", "", "",
                     "", "", "", "-25.76", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     "M1450 from Jiang et al. (2016)"]])

# M1450 from: https://iopscience.iop.org/article/10.3847/1538-4357/833/2/222 Jiang et al. (2016)

entry236 = np.array([["J0836+0054/J0836+00", "Banados et al. (2016), Shen et al. (2019), D'Odorico et al. (2023), Mazzucchelli et al. (2023)",
                     "https://arxiv.org/pdf/1608.03279, https://iopscience.iop.org/article/10.3847/1538-4357/ab03d9/pdf, https://academic.oup.com/mnras/article/523/1/1399/7172883, https://arxiv.org/pdf/2306.16474",
                     "SDSS", "08:36:43.86", "+00:54:53.26", "",
                     "5.834", "0.007", "0.007", "log9.59", "log0.13", "log0.20", "log47.85", "", "",
                     "1.72", "0.51", "0.51", "-27.75", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     "z from Shen et al. (2019), mass from D'Odorico et al. (2023), L_bol, f_Edd from Mazzucchelli et al. (2023)"]])

# z from: https://iopscience.iop.org/article/10.3847/1538-4357/ab03d9/pdf Shen et al. (2019)
# mass from: https://academic.oup.com/mnras/article/523/1/1399/7172883 D'Odorico et al. (2023)
# L_bol, f_Edd from: https://arxiv.org/pdf/2306.16474 Mazzucchelli et al. (2023)

entry237 = np.array([["J0840+5624", "Shen et al. (2019), Banados et al. (2016)",
                     "https://iopscience.iop.org/article/10.3847/1538-4357/ab03d9/pdf, https://arxiv.org/pdf/1608.03279",
                     "SDSS", "08:40:35.09", "+56:24:19.90", "",
                     "5.816", "0.010", "0.010", "", "", "", "", "", "",
                     "", "", "", "-27.24", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     "M1450 from Banados et al. (2016)"]])

# M1450 from: https://arxiv.org/pdf/1608.03279 Banados et al. (2016)

entry238 = np.array([["J0841+2905", "Banados et al. (2016), Shen et al. (2019)",
                     "https://arxiv.org/pdf/1608.03279, https://iopscience.iop.org/article/10.3847/1538-4357/ab03d9/pdf",
                     "SDSS", "08:41:19.52", "+29:05:04.55", "",
                     "5.954", "0.005", "0.005", "", "", "", "", "", "",
                     "", "", "", "-26.50", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     "z from Shen et al. (2019)"]])

# z from: https://iopscience.iop.org/article/10.3847/1538-4357/ab03d9/pdf Shen et al. (2019)

entry239 = np.array([["J0850+3246", "Banados et al. (2016), Shen et al. (2019), Jiang et al. (2015)",
                     "https://arxiv.org/pdf/1608.03279, https://iopscience.iop.org/article/10.3847/1538-4357/ab03d9/pdf, https://iopscience.iop.org/article/10.1088/0004-6256/149/6/188",
                     "SDSS/UHS", "08:50:48.25", "+32:46:47.94", "",
                     "5.730", "0.013", "0.013", "", "", "", "", "", "",
                     "", "", "", "-26.74", "0.08", "0.08", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     "z from Shen et al. (2019), M1450 from Jiang et al. (2015)"]])

# z from: https://iopscience.iop.org/article/10.3847/1538-4357/ab03d9/pdf Shen et al. (2019)
# M1450 from: https://iopscience.iop.org/article/10.1088/0004-6256/149/6/188 Jiang et al. (2015)

entry240 = np.array([["J0927+2001/J0927+20", "Ishimoto et al. (2020), D'Odorico et al. (2023), Mazzucchelli et al. (2023)",
                     "https://iopscience.iop.org/article/10.3847/1538-4357/abb80b/pdf, https://academic.oup.com/mnras/article/523/1/1399/7172883, https://arxiv.org/pdf/2306.16474",
                     "SDSS/UHS", "09:27:2182", "+20:01:23.64", "",
                     "5.7722", "0.0006", "0.0006", "log9.11", "log0.10", "log0.13", "log47.08", "log0.15", "log0.24",
                     "0.717888", "0.349656", "0.33309", "-26.76", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     "mass from D'Odorico et al. (2023), L_bol, (recalculated using formula [2]) from Mazzucchelli et al. (2023)"]])

# mass from: https://academic.oup.com/mnras/article/523/1/1399/7172883 D'Odorico et al. (2023)
# L_bol, f_Edd from: https://arxiv.org/pdf/2306.16474 Mazzucchelli et al. (2023)

entry241 = np.array([["J1044−0125", "Venemans et al. (2020), Willott et al. (2015), Wang et al. (2013), Banados et al. (2016)",
                     "https://iopscience.iop.org/article/10.3847/1538-4357/abc563, https://iopscience.iop.org/article/10.1088/0004-637X/801/2/123#apj509348t2, https://iopscience.iop.org/article/10.1088/0004-637X/773/1/44, https://arxiv.org/pdf/1608.03279",
                     "SDSS", "10:44:33.040", "-01:25:02.08", "",
                     "5.7846", "0.0005", "0.0005", "1.1e10", "1.9e10", "0.7e10", "11.6e13S", "", "",
                     "", "", "", "-27.38", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     "mass from Willott et al. (2015), L_bol from Wang et al. (2013), M1450 from Banados et al. (2016)"]])

# mass from: https://iopscience.iop.org/article/10.1088/0004-637X/801/2/123#apj509348t2 Willott et al. (2015)
# L_bol from: https://iopscience.iop.org/article/10.1088/0004-637X/773/1/44 Wang et al. (2013)
# M1450 from: https://arxiv.org/pdf/1608.03279 Banados et al. (2016)

entry242 = np.array([["J1143+3808", "Eilers et al. (2020), Shen et al. (2019)",
                     "https://arxiv.org/pdf/2002.01811, https://iopscience.iop.org/article/10.3847/1538-4357/ab03d9/pdf",
                     "SDSS/UHS", "11:43:38.347", "+38:08:28.823", "",
                     "5.8366", "0.0023", "0.0023", "", "", "", "", "", "",
                     "", "", "", "-26.69", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     "instrument from Shen et al. (2019)"]])

# instrument from: https://iopscience.iop.org/article/10.3847/1538-4357/ab03d9/pdf Shen et al. (2019)

entry243 = np.array([["J1243+2529", "Shen et al. (2019), Jiang et al. (2016)",
                     "https://iopscience.iop.org/article/10.3847/1538-4357/ab03d9/pdf, https://iopscience.iop.org/article/10.3847/1538-4357/833/2/222",
                     "SDSS", "12:43:40.81", "+25:29:23.90", "",
                     "5.842", "0.006", "0.006", "", "", "", "", "", "",
                     "", "", "", "-26.22", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     "M1450 from Jiang et al. (2016)"]])

# M1450 from: https://iopscience.iop.org/article/10.3847/1538-4357/833/2/222 Jiang et al. (2016)

entry244 = np.array([["J1403+0902", "Shen et al. (2019), Jiang et al. (2015)",
                     "https://iopscience.iop.org/article/10.3847/1538-4357/ab03d9/pdf, https://iopscience.iop.org/article/10.1088/0004-6256/149/6/188",
                     "SDSS", "14:03:19.13", "+09:02:50.90", "",
                     "5.787", "0.013", "0.013", "", "", "", "", "", "",
                     "", "", "", "-26.27", "0.11", "0.11", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     "instrument, M1450 from Jiang et al. (2015)"]])

# instrument, M1450 from: https://iopscience.iop.org/article/10.1088/0004-6256/149/6/188 Jiang et al. (2015)

entry245 = np.array([["J1425+3254", "Shen et al. (2019), Cool et al. (2006), Carilli et al. (2010)",
                     "https://iopscience.iop.org/article/10.3847/1538-4357/ab03d9/pdf, https://iopscience.iop.org/article/10.1086/505535/pdf, https://iopscience.iop.org/article/10.1088/0004-637X/714/1/834",
                     "NDWFS", "14:25:16.34", "+32:54:09.60", "",
                     "5.862", "0.006", "0.006", "", "", "", "", "", "",
                     "", "", "", "-26.09", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     "instrument from Cool et al. (2006), M1450 from Carilli et al. (2010)"]])

# instrument from: https://iopscience.iop.org/article/10.1086/505535/pdf Cool et al. (2006)
# M1450 from: https://iopscience.iop.org/article/10.1088/0004-637X/714/1/834 Carilli et al. (2010)

entry246 = np.array([["J1436+5007", "Shen et al. (2019), Banados et al. (2016)",
                     "https://iopscience.iop.org/article/10.3847/1538-4357/ab03d9/pdf, https://arxiv.org/pdf/1608.03279",
                     "SDSS", "14:36:11.74", "+50:07:06.90", "",
                     "5.809", "0.010", "0.010", "", "", "", "", "", "",
                     "", "", "", "-26.56", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     "instrument, M1450 from Banados et al. (2016)"]])

# instrument, M1450 from: https://arxiv.org/pdf/1608.03279 Banados et al. (2016)

entry247 = np.array([["J1514+2114/P228+21/J228.6+21.23", "Banados et al. (2016), Shen et al. (2019)",
                     "https://arxiv.org/pdf/1608.03279, https://iopscience.iop.org/article/10.3847/1538-4357/ab03d9/pdf",
                     "PSO", "15:14:44.91", "+21:14:19.78", "",
                     "5.893", "0.015", "0.015", "", "", "", "", "", "",
                     "", "", "", "-26.11", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     "z from Shen et al. (2019)"]])

# z from: https://iopscience.iop.org/article/10.3847/1538-4357/ab03d9/pdf Shen et al. (2019)

entry248 = np.array([["J1545+6028", "Banados et al. (2016), Shen et al. (2019)",
                     "https://arxiv.org/pdf/1608.03279, https://iopscience.iop.org/article/10.3847/1538-4357/ab03d9/pdf",
                     "SDSS", "15:45:52.09", "+60:28:23.95", "",
                     "5.794", "0.007", "0.007", "", "", "", "", "", "",
                     "", "", "", "-27.65", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     "z from Shen et al. (2019)"]])

# z from: https://iopscience.iop.org/article/10.3847/1538-4357/ab03d9/pdf Shen et al. (2019)

entry249 = np.array([["J1621+5155", "Jiang et al. (2016), Shen et al. (2019)",
                     "https://iopscience.iop.org/article/10.3847/1538-4357/833/2/222, https://iopscience.iop.org/article/10.3847/1538-4357/ab03d9/pdf",
                     "SDSS", "16:21:00.92", "+51:55:48.90", "",
                     "5.637", "0.008", "0.008", "", "", "", "", "", "",
                     "", "", "", "-26.94", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     "coordinates, z from Shen et al. (2019)"]])

# coordinates, z from: https://iopscience.iop.org/article/10.3847/1538-4357/ab03d9/pdf Shen et al. (2019)

entry250 = np.array([["J2307+0031", "Shen et al. (2019), Jiang et al. (2016)",
                     "https://iopscience.iop.org/article/10.3847/1538-4357/ab03d9/pdf, https://iopscience.iop.org/article/10.3847/1538-4357/833/2/222",
                     "SDSS", "23:07:35.35", "+00:31:49.4", "",
                     "5.900", "0.010", "0.010", "", "", "", "", "", "",
                     "", "", "", "-24.71", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     "instrument, M1450 from Jiang et al. (2016)"]])

# instrument, M1450 from: https://iopscience.iop.org/article/10.3847/1538-4357/833/2/222 Jiang et al. (2016)

entry251 = np.array([["J2329−0403", "Shen et al. (2019), Willott et al. (2009)",
                     "https://iopscience.iop.org/article/10.3847/1538-4357/ab03d9/pdf, https://iopscience.iop.org/article/10.1088/0004-6256/137/3/3541",
                     "CFHQS", "23:29:14.46", "-04:03:24.1", "",
                     "5.883", "0.007", "0.007", "", "", "", "", "", "",
                     "", "", "", "-24.36", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     "instrument, M1450 from Willott et al. (2009)"]])

# instrument, M1450 from: https://iopscience.iop.org/article/10.1088/0004-6256/137/3/3541 Willott et al. (2009)

entry252 = np.array([["J0005−0006", "Ishimoto et al. (2020), Jiang et al. (2008)",
                     "https://iopscience.iop.org/article/10.3847/1538-4357/abb80b/pdf, https://iopscience.iop.org/article/10.1088/0004-6256/135/3/1057",
                     "HSC/SDSS", "00:05:52.34", "-00:06:55.80", "",
                     "5.844", "0.001", "0.001", "", "", "", "", "", "",
                     "", "", "", "-25.82", "0.10", "0.10", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     "instrument, M1450 from Jiang et al. (2008)"]])

# instrument, M1450 from: https://iopscience.iop.org/article/10.1088/0004-6256/135/3/1057 Jiang et al. (2008)

entry253 = np.array([["J0011+1446", "Shemmer et al. (2006)",
                     "https://iopscience.iop.org/article/10.1086/503543/pdf",
                     "SDSS", "00:11:15.23", "+14:46:01.80", "",
                     "4.97", "", "", "", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry254 = np.array([["J1026+4719", "Shemmer et al. (2006)",
                     "https://iopscience.iop.org/article/10.1086/503543/pdf",
                     "SDSS", "10:26:22.89", "+47:19:07.00", "",
                     "4.94", "", "", "", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry255 = np.array([["J1053+5804", "Shemmer et al. (2006)",
                     "https://iopscience.iop.org/article/10.1086/503543/pdf",
                     "SDSS", "10:53:22.98", "+58:04:12.10", "",
                     "5.21", "", "", "", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry256 = np.array([["J1302+0030", "Shemmer et al. (2006)",
                     "https://iopscience.iop.org/article/10.1086/503543/pdf",
                     "SDSS", "13:02:16.13", "+00:30:32.10", "",
                     "4.47", "", "", "", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry257 = np.array([["J1408+0205", "Shemmer et al. (2006)",
                     "https://iopscience.iop.org/article/10.1086/503543/pdf",
                     "SDSS", "14:08:50.91", "+02:05:22.70", "",
                     "4.01", "", "", "", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry258 = np.array([["J1411+1217", "Ishimoto et al. (2020), Shemmer et al. (2006)",
                     "https://iopscience.iop.org/article/10.3847/1538-4357/abb80b/pdf, https://iopscience.iop.org/article/10.1086/503543/pdf",
                     "SDSS/HSC", "14:11:11.29", "+12:17:37.28", "",
                     "5.904", "0.002", "0.002", "", "", "", "", "", "",
                     "", "", "", "-26.69", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     "instrument from Shemmer et al. (2006)"]])

# instrument from: https://iopscience.iop.org/article/10.1086/503543/pdf Shemmer et al. (2006)

entry259 = np.array([["J1433+0227", "Trakhtenbrot et al. (2011)",
                     "https://iopscience.iop.org/article/10.1088/0004-637X/730/1/7",
                     "SDSS", "14:33:52.21", "+02:27:14.10", "",
                     "4.722", "", "", "log9.11", "", "", "log47.37", "", "",
                     "log0.09", "", "", "", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry260 = np.array([["J1442+0110", "Shemmer et al. (2006)",
                     "https://iopscience.iop.org/article/10.1086/503543/pdf",
                     "SDSS", "14:42:31.72", "+01:10:55.20", "",
                     "4.51", "", "", "", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry261 = np.array([["J1532-0039", "Shemmer et al. (2006)",
                     "https://iopscience.iop.org/article/10.1086/503543/pdf",
                     "SDSS", "15:32:59.96", "-00:39:44.10", "",
                     "4.62", "", "", "", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry262 = np.array([["J1536+5008", "Shemmer et al. (2006)",
                     "https://iopscience.iop.org/article/10.1086/503543/pdf",
                     "SDSS", "15:36:50.26", "+50:08:10.30", "",
                     "4.93", "", "", "", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry263 = np.array([["J1626+2751", "Shemmer et al. (2006)",
                     "https://iopscience.iop.org/article/10.1086/503543/pdf",
                     "SDSS", "16:26:26.50", "+27:51:32.40", "",
                     "5.28", "", "", "", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry264 = np.array([["J1653+4054", "Shemmer et al. (2006)",
                     "https://iopscience.iop.org/article/10.1086/503543/pdf",
                     "SDSS", "16:53:54.61", "+40:54:02.10 ", "",
                     "4.98", "", "", "", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry265 = np.array([["J2225-0014", "Trakhtenbrot et al. (2011)",
                     "https://iopscience.iop.org/article/10.1088/0004-637X/730/1/7",
                     "SDSS", "22:25:09.16", "-00:14:06.80", "",
                     "4.890", "", "", "log9.27", "", "", "log47.23", "", "",
                     "log-0.21", "", "", "", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry266 = np.array([["J2228-0757", "Shemmer et al. (2006)",
                     "https://iopscience.iop.org/article/10.1086/503543/pdf",
                     "SDSS", "22:28:45.14", "-07:57:55.30", "",
                     "5.14", "", "", "", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry267 = np.array([["J0007+0041", "Trakhtenbrot et al. (2011)",
                     "https://iopscience.iop.org/article/10.1088/0004-637X/730/1/7",
                     "SDSS", "00:07:49.17", "+00:41:19.40", "",
                     "4.786", "", "", "log8.90", "", "", "log46.57", "", "",
                     "log-0.51", "", "", "", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry268 = np.array([["J0035+0040", "Trakhtenbrot et al. (2011)",
                     "https://iopscience.iop.org/article/10.1088/0004-637X/730/1/7",
                     "SDSS", "00:35:25.28", "+00:40:02.80", "",
                     "4.759", "", "", "log8.49", "", "", "log46.91", "", "",
                     "log0.24", "", "", "", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry269 = np.array([["J0210-0018", "Trakhtenbrot et al. (2011)",
                     "https://iopscience.iop.org/article/10.1088/0004-637X/730/1/7",
                     "SDSS", "02:10:43.15", "-00:18:18.20 ", "",
                     "4.713", "", "", "log9.09", "", "", "log46.56", "", "",
                     "log-0.70", "", "", "", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry270 = np.array([["J0331-0741", "Trakhtenbrot et al. (2011), Trakhtenbrot et al. (2017)",
                     "https://iopscience.iop.org/article/10.1088/0004-637X/730/1/7, https://iopscience.iop.org/article/10.3847/1538-4357/836/1/8",
                     "SDSS", "03:31:19.67", "-07:41:43.10", "",
                     "4.72890", "", "", "log8.83", "", "", "log47.09", "", "",
                     "log0.08", "", "", "", "", "", "", "", "",
                     "625", "", "", "625", "", "", "2.16e10", "", "",
                     "z, SFR, M_star from Trakhtenbrot et al. (2017)"]])

# z, SFR, M_star from: https://iopscience.iop.org/article/10.3847/1538-4357/836/1/8 Trakhtenbrot et al. (2017)

entry271 = np.array([["J0759+1800", "Trakhtenbrot et al. (2011)",
                     "https://iopscience.iop.org/article/10.1088/0004-637X/730/1/7",
                     "SDSS", "07:59:07.58", "+18:00:54.70", "",
                     "4.804", "", "", "log8.95", "", "", "log47.07", "", "",
                     "log-0.05", "", "", "", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry272 = np.array([["J0800+3051", "Trakhtenbrot et al. (2011)",
                     "https://iopscience.iop.org/article/10.1088/0004-637X/730/1/7",
                     "SDSS", "08:00:23.03", "+30:51:00.00", "",
                     "4.677", "", "", "log8.49", "", "", "log47.26", "", "",
                     "log0.59", "", "", "", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry273 = np.array([["J0807+1328", "Trakhtenbrot et al. (2011)",
                     "https://iopscience.iop.org/article/10.1088/0004-637X/730/1/7",
                     "SDSS", "08:07:15.12", "+13:28:04.80", "",
                     "4.885", "", "", "log9.24", "", "", "log47.07", "", "",
                     "log-0.35", "", "", "", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry274 = np.array([["J0839+3524", "Trakhtenbrot et al. (2011)",
                     "https://iopscience.iop.org/article/10.1088/0004-637X/730/1/7",
                     "SDSS", "08:39:20.53", "+35:24:57.60", "",
                     "4.795", "", "", "log8.49", "", "", "log46.77", "", "",
                     "log0.11", "", "", "", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry275 = np.array([["J0857+3210", "Trakhtenbrot et al. (2011)",
                     "https://iopscience.iop.org/article/10.1088/0004-637X/730/1/7",
                     "SDSS", "08:57:07.94", "+32:10:32.00", "",
                     "4.801", "", "", "log9.10", "", "", "log47.25", "", "",
                     "log-0.03", "", "", "", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry276 = np.array([["J0923+0247", "Trakhtenbrot et al. (2011), Trakhtenbrot et al. (2017)",
                     "https://iopscience.iop.org/article/10.1088/0004-637X/730/1/7, https://iopscience.iop.org/article/10.3847/1538-4357/836/1/8",
                     "SDSS", "09:23:03.53", "+02:47:39.50", "",
                     "4.65887", "", "", "log8.68", "", "", "log46.67", "", "",
                     "log-0.18", "", "", "", "", "", "", "", "",
                     "361", "", "", "361", "", "", "2.30e10", "", "",
                     "z, SFR, M_star from Trakhtenbrot et al. (2017)"]])

# z, SFR, M_star from: https://iopscience.iop.org/article/10.3847/1538-4357/836/1/8 Trakhtenbrot et al. (2017)

entry277 = np.array([["J0935+0801", "Trakhtenbrot et al. (2011), Trakhtenbrot et al. (2017)",
                     "https://iopscience.iop.org/article/10.1088/0004-637X/730/1/7, https://iopscience.iop.org/article/10.3847/1538-4357/836/1/8",
                     "SDSS", "09:35:08.50", "+08:01:14.50", "",
                     "4.67078", "", "", "log8.82", "", "", "log46.87", "", "",
                     "log-0.13", "", "", "", "", "", "", "", "",
                     "191", "", "", "191", "", "", "1.06e10", "", "",
                     "z, SFR, M_star from Trakhtenbrot et al. (2017)"]])

# z, SFR, M_star from: https://iopscience.iop.org/article/10.3847/1538-4357/836/1/8 Trakhtenbrot et al. (2017)

entry278 = np.array([["J0935+4115", "Trakhtenbrot et al. (2011)",
                     "https://iopscience.iop.org/article/10.1088/0004-637X/730/1/7",
                     "SDSS", "09:35:23.32", "+41:15:18.70", "",
                     "4.802", "", "", "log9.18", "", "", "log47.12", "", "",
                     "log-0.24", "", "", "", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry279 = np.array([["J0944+1006", "Trakhtenbrot et al. (2011)",
                     "https://iopscience.iop.org/article/10.1088/0004-637X/730/1/7",
                     "SDSS", "09:44:09.52", "+10:06:56.70 ", "",
                     "4.771", "", "", "log8.65", "", "", "log46.93", "", "",
                     "log0.11", "", "", "", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry280 = np.array([["J1017+0327", "Trakhtenbrot et al. (2011)",
                     "https://iopscience.iop.org/article/10.1088/0004-637X/730/1/7",
                     "SDSS", "10:17:59.64", "+03:27:40.00", "",
                     "4.943", "", "", "log8.71", "", "", "log46.63", "", "",
                     "log-0.26", "", "", "", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry281 = np.array([["J1059+0234", "Trakhtenbrot et al. (2011)",
                     "https://iopscience.iop.org/article/10.1088/0004-637X/730/1/7",
                     "SDSS", "10:59:19.22", "+02:34:28.80", "",
                     "4.789", "", "", "log8.89", "", "", "log46.89", "", "",
                     "log-0.18", "", "", "", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry282 = np.array([["J1113+0253", "Trakhtenbrot et al. (2011)",
                     "https://iopscience.iop.org/article/10.1088/0004-637X/730/1/7",
                     "SDSS", "11:13:58.32", "+02:53:33.60", "",
                     "4.870", "", "", "log9.12", "", "", "log46.89", "", "",
                     "log-0.41", "", "", "", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry283 = np.array([["J1144+0557", "Trakhtenbrot et al. (2011)",
                     "https://iopscience.iop.org/article/10.1088/0004-637X/730/1/7",
                     "SDSS", "11:44:48.54", "+05:57:09.80", "",
                     "4.790", "", "", "log8.83", "", "", "log46.63", "", "",
                     "log-0.37", "", "", "", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry284 = np.array([["J1151+0303", "Trakhtenbrot et al. (2011)",
                     "https://iopscience.iop.org/article/10.1088/0004-637X/730/1/7",
                     "SDSS", "11:51:58.25", "+03:03:41.70", "",
                     "4.687", "", "", "log8.84", "", "", "log46.44", "", "",
                     "log-0.57", "", "", "", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry285 = np.array([["J1202+0720", "Trakhtenbrot et al. (2011)",
                     "https://iopscience.iop.org/article/10.1088/0004-637X/730/1/7",
                     "SDSS", "12:02:56.44", "+07:20:38.90", "",
                     "4.810", "", "", "log8.59", "", "", "log46.80", "", "",
                     "log0.04", "", "", "", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry286 = np.array([["J1235-0003", "Trakhtenbrot et al. (2011)",
                     "https://iopscience.iop.org/article/10.1088/0004-637X/730/1/7",
                     "SDSS", "12:35:03.04", "-00:03:31.60", "",
                     "4.700", "", "", "log9.11", "", "", "log46.65", "", "",
                     "log-0.64", "", "", "", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry287 = np.array([["J1306+0236", "Trakhtenbrot et al. (2011)",
                     "https://iopscience.iop.org/article/10.1088/0004-637X/730/1/7",
                     "SDSS", "13:06:19.38", "+02:36:58.90", "",
                     "4.860", "", "", "log9.71", "", "", "log47.35", "", "",
                     "log-0.54", "", "", "", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry288 = np.array([["J1317+1105", "Trakhtenbrot et al. (2011)",
                     "https://iopscience.iop.org/article/10.1088/0004-637X/730/1/7",
                     "SDSS", "13:17:37.28", "+11:05:33.10", "",
                     "4.744", "", "", "log8.95", "", "", "log46.87", "", "",
                     "log-0.25", "", "", "", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry289 = np.array([["J1321+0038", "Trakhtenbrot et al. (2011)",
                     "https://iopscience.iop.org/article/10.1088/0004-637X/730/1/7",
                     "SDSS", "13:17:37.28", "+11:05:33.10", "",
                     "4.726", "", "", "log8.98", "", "", "log46.70", "", "",
                     "log-0.45", "", "", "", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry290 = np.array([["J1328-0224", "Trakhtenbrot et al. (2011), Trakhtenbrot et al. (2017)",
                     "https://iopscience.iop.org/article/10.1088/0004-637X/730/1/7, https://iopscience.iop.org/article/10.3847/1538-4357/836/1/8",
                     "SDSS", "13:28:53.67", "-02:24:41.70", "",
                     "4.65815", "", "", "log9.08", "", "", "log46.81", "", "",
                     "log-0.45", "", "", "", "", "", "", "", "",
                     "206", "", "", "206", "", "", "2.40e10", "", "",
                     "z, SFR, M_star from Trakhtenbrot et al. (2017)"]])

# z, SFR, M_star from: https://iopscience.iop.org/article/10.3847/1538-4357/836/1/8 Trakhtenbrot et al. (2017)

entry291 = np.array([["J1331+0255", "Trakhtenbrot et al. (2011)",
                     "https://iopscience.iop.org/article/10.1088/0004-637X/730/1/7",
                     "SDSS", "13:31:25.57", "+02:55:35.60", "",
                     "4.762", "", "", "log8.83", "", "", "log46.55", "", "",
                     "log-0.46", "", "", "", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry292 = np.array([["J1341+0141", "Trakhtenbrot et al. (2011), Trakhtenbrot et al. (2017)",
                     "https://iopscience.iop.org/article/10.1088/0004-637X/730/1/7, https://iopscience.iop.org/article/10.3847/1538-4357/836/1/8",
                     "SDSS", "13:41:34.20", "+01:41:57.80", "",
                     "4.68944", "", "", "log9.82", "", "", "log47.26", "", "",
                     "log-0.74", "", "", "", "", "", "", "", "",
                     "3529", "", "", "3529", "", "", "8.06e11", "", "",
                     "z, SFR, M_star from Trakhtenbrot et al. (2017)"]])

# z, SFR, M_star from: https://iopscience.iop.org/article/10.3847/1538-4357/836/1/8 Trakhtenbrot et al. (2017)

entry293 = np.array([["J1345-0159", "Trakhtenbrot et al. (2011)",
                     "https://iopscience.iop.org/article/10.1088/0004-637X/730/1/7",
                     "SDSS", "13:45:46.97", "-01:59:40.30", "",
                     "4.728", "", "", "log8.86", "", "", "log46.60", "", "",
                     "log-0.43", "", "", "", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry294 = np.array([["J1404+0314", "Trakhtenbrot et al. (2011)",
                     "https://iopscience.iop.org/article/10.1088/0004-637X/730/1/7",
                     "SDSS", "14:04:04.64", "+03:14:04.00", "",
                     "4.903", "", "", "log9.51", "", "", "log47.02", "", "",
                     "log-0.66", "", "", "", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry295 = np.array([["J1436+0635", "Trakhtenbrot et al. (2011)",
                     "https://iopscience.iop.org/article/10.1088/0004-637X/730/1/7",
                     "SDSS", "14:36:29.94", "+06:35:08.00", "",
                     "4.817", "", "", "log8.99", "", "", "log46.98", "", "",
                     "log-0.19", "", "", "", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry296 = np.array([["J1443+0605", "Trakhtenbrot et al. (2011)",
                     "https://iopscience.iop.org/article/10.1088/0004-637X/730/1/7",
                     "SDSS", "14:43:52.95", "+06:05:33.10", "",
                     "4.884", "", "", "log8.96", "", "", "log46.69", "", "",
                     "log-0.45", "", "", "", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry297 = np.array([["J1447+1025", "Trakhtenbrot et al. (2011)",
                     "https://iopscience.iop.org/article/10.1088/0004-637X/730/1/7",
                     "SDSS", "14:47:34.10", "+10:25:13.20", "",
                     "4.679", "", "", "log8.03", "", "", "log46.51", "", "",
                     "log0.30", "", "", "", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry298 = np.array([["J1511+0408", "Trakhtenbrot et al. (2011), Trakhtenbrot et al. (2017)",
                     "https://iopscience.iop.org/article/10.1088/0004-637X/730/1/7, https://iopscience.iop.org/article/10.3847/1538-4357/836/1/8",
                     "SDSS", "15:11:55.98", "+04:08:03.00", "",
                     "4.66988", "", "", "log8.42", "", "", "log46.86", "", "",
                     "log0.26", "", "", "", "", "", "", "", "",
                     "2180", "", "", "2180", "", "", "5.02e10", "", "",
                     "z, SFR, M_star from Trakhtenbrot et al. (2017)"]])

# z, SFR, M_star from: https://iopscience.iop.org/article/10.3847/1538-4357/836/1/8 Trakhtenbrot et al. (2017)

entry299 = np.array([["J1616+0501", "Trakhtenbrot et al. (2011)",
                     "https://iopscience.iop.org/article/10.1088/0004-637X/730/1/7",
                     "SDSS", "16:16:22.11", "+05:01:27.70", "",
                     "4.869", "", "", "log9.43", "", "", "log47.33", "", "",
                     "log-0.27", "", "", "", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry300 = np.array([["J1654+2227", "Trakhtenbrot et al. (2011)",
                     "https://iopscience.iop.org/article/10.1088/0004-637X/730/1/7",
                     "SDSS", "16:54:36.86", "+22:27:33.70", "",
                     "4.717", "", "", "log9.55", "", "", "log47.02", "", "",
                     "log-0.70", "", "", "", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry301 = np.array([["J2057-0030", "Trakhtenbrot et al. (2011)",
                     "https://iopscience.iop.org/article/10.1088/0004-637X/730/1/7",
                     "SDSS", "20:57:24.15", "-00:30:18.00", "",
                     "4.680", "", "", "log9.23", "", "", "log47.36", "", "",
                     "log-0.05", "", "", "", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry302 = np.array([["J2200+0017", "Trakhtenbrot et al. (2011)",
                     "https://iopscience.iop.org/article/10.1088/0004-637X/730/1/7",
                     "SDSS", "22:00:08.66", "+00:17:44.80", "",
                     "4.804", "", "", "log8.82", "", "", "log47.04", "", "",
                     "log0.04", "", "", "", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry303 = np.array([["J2217-0013", "Trakhtenbrot et al. (2011)",
                     "https://iopscience.iop.org/article/10.1088/0004-637X/730/1/7",
                     "SDSS", "22:17:05.72", "-00:13:07.70", "",
                     "4.676", "", "", "log8.63", "", "", "log46.81", "", "",
                     "log0.00", "", "", "", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry304 = np.array([["J2244+1346", "Trakhtenbrot et al. (2011)",
                     "https://iopscience.iop.org/article/10.1088/0004-637X/730/1/7",
                     "SDSS", "22:44:53.06", "13:46:31.80", "",
                     "4.656", "", "", "log8.58", "", "", "log46.58", "", "",
                     "log-0.17", "", "", "", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry305 = np.array([["J0218+0007", "Yang et al. (2021), Wang et al. (2024)",
                     "https://iopscience.iop.org/article/10.3847/1538-4357/ac2b32, https://arxiv.org/html/2404.15413v1#S1",
                     "DR1+WISE", "02:18:47.04", "+00:07:15.20", "",
                     "6.766", "0.004", "0.004", "0.61e9", "0.07e9", "0.07e9", "6.4e46", "1.4e46", "1.4e46",
                     "0.8", "0.2", "0.2", "-25.55", "", "", "", "", "",
                     "95-594", "", "", "", "", "", "", "", "",
                     "coordinates, SFR_CII from Wang et al. (2024)"]])

# coordinates, SFR_CII from: https://arxiv.org/html/2404.15413v1#S1 Wang et al. (2024)

entry306 = np.array([["J0525−2406", "Yang et al. (2021), Wang et al. (2024)",
                     "https://iopscience.iop.org/article/10.3847/1538-4357/ac2b32, https://arxiv.org/html/2404.15413v1#S1",
                     "DR1+WISE", "05:25:59.68", "-24:06:23.00", "",
                     "6.543", "0.002", "0.002", "0.29e9", "0.04e9", "0.04e9", "6.8e46", "3.5e46", "3.5e46",
                     "1.8", "1.0", "1.0", "-25.47", "", "", "", "", "",
                     "374-2343", "", "", "", "", "", "", "", "",
                     "coordinates, SFR_CII from Wang et al. (2024)"]])

# coordinates, SFR_CII from: https://arxiv.org/html/2404.15413v1#S1 Wang et al. (2024)

entry307 = np.array([["J0923+0753", "Yang et al. (2021), Wang et al. (2024)",
                     "https://iopscience.iop.org/article/10.3847/1538-4357/ac2b32, https://arxiv.org/html/2404.15413v1#S1",
                     "DR1+WISE", "09:23:58.99", "+07:53:48.70", "",
                     "6.682", "0.002", "0.002", "0.49e9", "0.15e9", "0.15e9", "4.9e46", "2.0e46", "2.0e46",
                     "0.8", "0.4", "0.4", "-25.5", "", "", "", "", "",
                     "92-577", "", "", "", "", "", "", "", "",
                     "coordinates, SFR_CII from Wang et al. (2024)"]])

# coordinates, SFR_CII from: https://arxiv.org/html/2404.15413v1#S1 Wang et al. (2024)

entry308 = np.array([["J1058+2930", "Yang et al. (2021), Wang et al. (2024)",
                     "https://iopscience.iop.org/article/10.3847/1538-4357/ac2b32, https://arxiv.org/html/2404.15413v1#S1",
                     "DR1+WISE", "10:58:07.72", "+29:30:41.70", "",
                     "6.585", "0.005", "0.005", "0.54e9", "0.03e9", "0.03e9", "5.8e46", "1.5e46", "1.5e46",
                     "0.8", "0.2", "0.2", "-25.68", "", "", "", "", "",
                     "165-1031", "", "", "", "", "", "", "", "",
                     "coordinates, SFR_CII from Wang et al. (2024)"]])

# coordinates, SFR_CII from: https://arxiv.org/html/2404.15413v1#S1 Wang et al. (2024)

entry309 = np.array([["J2002−3013", "Yang et al. (2021), Wang et al. (2024)",
                     "https://iopscience.iop.org/article/10.3847/1538-4357/ac2b32, https://arxiv.org/html/2404.15413v1#S1",
                     "DR1+WISE", "20:02:41.59", "-30:13:21.70", "",
                     "6.673", "0.001", "0.001", "1.62e9", "0.27e9", "0.27e9", "15.4e46", "1.9e46", "1.9e46",
                     "0.8", "0.2", "0.2", "-26.9", "", "", "", "", "",
                     "127-796", "", "", "", "", "", "", "", "",
                     "coordinates, SFR_CII from Wang et al. (2024)"]])

# coordinates, SFR_CII from: https://arxiv.org/html/2404.15413v1#S1 Wang et al. (2024)

entry310 = np.array([["J2338+2143", "Yang et al. (2021)",
                     "https://iopscience.iop.org/article/10.3847/1538-4357/ac2b32",
                     "DR1+WISE", "23:38:07.03", "+21:43:58.20", "",
                     "6.565", "0.009", "0.009", "0.56e9", "0.03e9", "0.03e9", "7.6e46", "1.3e46", "1.3e46",
                     "1.1", "0.2", "0.2", "-26.0", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry311 = np.array([["J0148+0600/J0148+06", "D'Odorico et al. (2023), Mazzucchelli et al. (2023), Jiang et al. (2015)",
                     "https://academic.oup.com/mnras/article/523/1/1399/7172883, https://arxiv.org/pdf/2306.16474, https://iopscience.iop.org/article/10.1088/0004-6256/149/6/188",
                     "SDSS/ULAS", "01:48:37.64", "+06:00:20.06", "",
                     "5.977", "0.002", "0.002", "log9.58", "log0.08", "log0.10", "log47.46", "log0.04", "log0.04",
                     "0.583521", "0.130765", "0.091135", "-27.08", "0.06", "0.06", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     "(recalculated using formula [2]) f_Edd from Mazzucchelli et al. (2023), M1450 from Jiang et al. (2015), additional information (SFR_IR) here: https://iopscience.iop.org/article/10.3847/1538-4357/aba52d Li et al. (2020)"]])

# f_Edd from: https://arxiv.org/pdf/2306.16474 Mazzuchelli et al. (2023)
# M1450 from: https://iopscience.iop.org/article/10.1088/0004-6256/149/6/188 Jiang et al. (2015)
# SFR_IR from: https://iopscience.iop.org/article/10.3847/1538-4357/aba52d Li et al. (2020)

entry312 = np.array([["J0430−1445", "Wang et al. (2024)",
                     "https://arxiv.org/html/2404.15413v1#S1",
                     "", "04:30:43.66", "-14:45:41.20", "",
                     "6.718", "", "", "", "", "", "", "", "",
                     "", "", "", "-25.82", "", "", "", "", "",
                     "159-994", "", "", "", "", "", "", "", "",
                     ""]])

entry313 = np.array([["(Galaxy) J0014-3022/GHZ1", "Castellano et al. (2023)",
                     "https://iopscience.iop.org/article/10.3847/2041-8213/accea5/meta",
                     "JWST", "00:14:02.86", "-30:22:18.69", "",
                     "10.47", "0.38", "0.89", "", "", "", "", "", "",
                     "", "", "", "", "", "", "111.8", "4.4", "4.4",
                     "10.7", "42.7", "4.7", "10.7", "42.7", "4.7", "11.5e8", "7.1e8", "10.3e8",
                     ""]])

entry314 = np.array([["(Galaxy) J0014-3021/GHZ4", "Castellano et al. (2023)",
                     "https://iopscience.iop.org/article/10.3847/2041-8213/accea5/meta",
                     "JWST", "00:14:03.30", "-30:21:05.62", "",
                     "10.27", "1.2", "1.4", "", "", "", "", "", "",
                     "", "", "", "", "", "", "41.7", "3.1", "3.1",
                     "2.0", "14.2", "0.4", "2.0", "14.2", "0.4", "4.3e8", "1.5e8", "3.9e8",
                     ""]])

entry315 = np.array([["(Galaxy) J0013-3019/GHZ7", "Castellano et al. (2023)",
                     "https://iopscience.iop.org/article/10.3847/2041-8213/accea5/meta",
                     "JWST", "00:13:48.33", "-30:19:14.58", "",
                     "10.62", "0.55", "1.02", "", "", "", "", "", "",
                     "", "", "", "", "", "", "28.8", "3.6", "3.6",
                     "3.2", "10.0", "0.5", "3.2", "10.0", "0.5", "2.1e8", "1.8e8", "1.7e8",
                     ""]])

entry316 = np.array([["(Galaxy) J0013-3019/GHZ8", "Castellano et al. (2023)",
                     "https://iopscience.iop.org/article/10.3847/2041-8213/accea5/meta",
                     "JWST", "00:13:48.34", "-30:19:18.47", "",
                     "10.85", "0.45", "0.57", "", "", "", "", "", "",
                     "", "", "", "", "", "", "53.7", "5.2", "5.2",
                     "17.5", "13.6", "12.3", "17.5", "13.6", "12.3", "0.8e8", "6.4e8", "0.16e8",
                     ""]])

entry317 = np.array([["(Galaxy) J0014-3025/DHZ1", "Castellano et al. (2023)",
                     "https://iopscience.iop.org/article/10.3847/2041-8213/accea5/meta",
                     "JWST", "00:14:28.14", "-30:25:32.03", "",
                     "9.3127", "0.0002", "0.0002", "", "", "", "", "", "",
                     "", "", "", "", "", "", "353.3", "17.9", "17.9",
                     "25.4", "3.2", "4.3", "25.4", "3.2", "4.3", "25e8", "6.6e8", "5.0e8",
                     ""]])

entry318 = np.array([["J1202−0057", "Ishimoto et al. (2020)",
                     "https://iopscience.iop.org/article/10.3847/1538-4357/abb80b/pdf",
                     "HSC", "12:02:46.37", "-00:57:01.70", "",
                     "5.9289", "0.0002", "0.0002", "", "", "", "", "", "",
                     "", "", "", "-22.83", "0.08", "0.08", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry319 = np.array([["J0129–0035", "Wang et al. (2013), Venemans et al. (2020), Willott et al. (2015), Jiang et al. (2016)",
                     "https://iopscience.iop.org/article/10.1088/0004-637X/773/1/44, https://iopscience.iop.org/article/10.3847/1538-4357/abc563, https://iopscience.iop.org/article/10.1088/0004-637X/801/2/123#apj509348t2, https://iopscience.iop.org/article/10.3847/1538-4357/833/2/222",
                     "SDSS", "01:29:58.515", "-00:35:39.81", "",
                     "5.7787", "0.0001", "0.0001", "1.7e8", "3.1e8", "1.1e8", "0.57e13S", "", "",
                     "", "", "", "-24.39", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     "coordinates from Venemans et al. (2020), mass from Willott et al. (2015), M1450 from Jiang et al. (2016)"]])      

# coordinates from: https://iopscience.iop.org/article/10.3847/1538-4357/abc563 Venemans et al. (2020)
# mass from: https://iopscience.iop.org/article/10.1088/0004-637X/801/2/123#apj509348t2 Willott et al. (2015) 
# M1450 from: https://iopscience.iop.org/article/10.3847/1538-4357/833/2/222 Jiang et al. (2016)       

entry320 = np.array([["J0038-1025/P009–10/J009.7–10.43", "Decarli et al. (2018), D'Odorico et al. (2023), Mazzucchelli et al. (2023)",
                     "https://iopscience.iop.org/article/10.3847/1538-4357/aaa5aa, https://academic.oup.com/mnras/article/523/1/1399/7172883, https://arxiv.org/pdf/2306.16474",
                     "PSO", "00:38:56.522", "-10:25:53.90", "",
                     "5.938", "0.008", "0.008", "log9.90", "log0.09", "log0.11", "log47.34", "log0.08", "log0.09",
                     "0.211864", "0.060603", "0.058917", "", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     "z, mass from D'Odorico et al. (2023), L_bol, (recalculated using formula [2]) f_Edd from Mazzucchelli et al. (2023)"]])

# z, mass from: https://academic.oup.com/mnras/article/523/1/1399/7172883 D'Odorico et al. (2023)
# L_bol, f_Edd from: https://arxiv.org/pdf/2306.16474 Mazzucchelli et al. (2023)

entry321 = np.array([["J0046–2837", "Decarli et al. (2018)",
                     "https://iopscience.iop.org/article/10.3847/1538-4357/aaa5aa",
                     "VIK", "00:46:23.65", "-28:37:47.34", "",
                     "5.99", "0.05", "0.05", "", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry322 = np.array([["J0045+0901/J011+09/J011.3+09.03", "Eilers et al. (2020), Yang et al. (2021)",
                     "https://arxiv.org/pdf/2002.01811, https://iopscience.iop.org/article/10.3847/1538-4357/ac2b32",
                     "PSO", "00:45:33.566", "+09:01:56.928", "",
                     "6.4694", "0.0002", "0.0002", "0.63e9", "0.02e9", "0.02e9", "6.2e46", "0.6e46", "0.6e46",
                     "0.8", "0.1", "0.1", "-25.86", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     "mass, L_bol, f_Edd, M1450 from Yang et al. (2021)"]])

# mass, L_bol, f_Edd, M1450 from: https://iopscience.iop.org/article/10.3847/1538-4357/ac2b32 Yang et al. (2021)

entry323 = np.array([["J0346-1628/P056−16/J056–16/J056.7-16.47", "Eilers et al. (2020)",
                     "https://arxiv.org/pdf/2002.01811",
                     "PSO", "03:46:52.044", "-16:28:36.876", "",
                     "5.9670", "0.0023", "0.0023", "0.71e9", "0.04e9", "0.04e9", "log47.06", "", "",
                     "1.26", "0.08", "0.08", "-26.72", "", "", "", "", "",
                     "1", "", "", "", "", "", "", "", "",
                     ""]])

entry324 = np.array([["J1743+4124/J265+41/J265.9+41.41", "Eilers et al. (2020)",
                     "https://arxiv.org/pdf/2002.01811",
                     "PSO", "17:43:43.136", "+41:24:50.191", "",
                     "6.0263", "0.0023", "0.0023", "", "", "", "", "", "",
                     "", "", "", "-25.56", "", "", "", "", "",
                     "1710", "", "", "", "", "", "", "", "",
                     ""]])

entry325 = np.array([["J0332-2746/GS-30148179/30148179", "Juodžbalis et al. (2025)",
                     "https://arxiv.org/html/2504.03551v1",
                     "JWST", "03:32:34.10", "-27:46:47.46", "",
                     "5.922", "", "", "log7.12", "log0.34", "log0.35", "log44.25", "log0.06", "log0.08",
                     "0.11", "0.05", "0.03", "", "", "", "", "", "",
                     "", "", "", "", "", "", "log8.78", "log0.04", "log0.04",
                     ""]])

entry326 = np.array([["J0332-2746/GS-210600/210600", "Juodžbalis et al. (2025)",
                     "https://arxiv.org/html/2504.03551v1",
                     "JWST", "03:32:39.87", "-27:46:47.46", "",
                     "6.306", "", "", "log7.42", "log0.33", "log0.34", "log44.31", "log0.09", "log0.11",
                     "0.059", "0.017", "0.016", "", "", "", "", "", "",
                     "", "", "", "", "", "", "log8.26", "log0.02", "log0.02",
                     ""]])

entry327 = np.array([["J0332-2747/GS-204851/204851/GOODS-S-13971", "Juodžbalis et al. (2025)",
                     "https://arxiv.org/html/2504.03551v1",
                     "JWST", "03:32:33.26", "-27:47:24.90", "",
                     "5.480", "", "", "log7.68", "log0.32", "log0.31", "log44.98", "log0.17", "log0.12",
                     "0.16", "0.04", "0.02", "", "", "", "", "", "",
                     "", "", "", "", "", "", "log8.94", "log0.04", "log0.04",
                     ""]])

entry328 = np.array([["J0332-2752/GS-172975/172975", "Juodžbalis et al. (2025)",
                     "https://arxiv.org/html/2504.03551v1",
                     "JWST", "03:32:21.06", "-27:52:16.46", "",
                     "4.741", "", "", "log7.25", "log0.32", "log0.32", "log44.07", "log0.04", "log0.04",
                     "0.05", "0.01", "0.01", "", "", "", "", "", "",
                     "", "", "", "", "", "", "log8.98", "log0.14", "log0.14",
                     ""]])

entry329 = np.array([["J0332-2754/GS-159717/159717", "Juodžbalis et al. (2025)",
                     "https://arxiv.org/html/2504.03551v1",
                     "JWST", "03:32:23.41", "-27:54:04.54", "",
                     "5.077", "", "", "log7.44", "log0.30", "log0.30", "log45.13", "log0.008", "log0.008",
                     "0.38", "0.04", "0.04", "", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry330 = np.array([["J0332-2752/GS-38562/38562", "Juodžbalis et al. (2025)",
                     "https://arxiv.org/html/2504.03551v1",
                     "JWST", "03:32:32.61", "-27:52:17.94", "",
                     "4.822", "", "", "log7.53", "log0.30", "log0.31", "log44.74", "log0.08", "log0.08",
                     "0.13", "0.01", "0.01", "", "", "", "", "", "",
                     "", "", "", "", "", "", "log9.57", "log0.08", "log0.08",
                     ""]])

entry331 = np.array([["J1236+6213/JADES GN+189.09144+62.22811 1001830/GN-38509/38509", "Juodžbalis et al. (2025), Juodžbalis et al. (2024)",
                     "https://arxiv.org/html/2504.03551v1, https://www.nature.com/articles/s41586-024-08210-5#Sec2",
                     "JWST", "12:36:21.95", "-62:13:41.20", "",
                     "6.677", "0.004", "0.004", "log8.57", "log0.37", "log0.38", "log45.09", "log0.57", "log0.33",
                     "0.027", "0.014", "0.0096", "", "", "", "", "", "",
                     "1.38", "0.92", "0.45", "1.38", "0.92", "0.45", "log8.92", "log0.30", "log0.30",
                     "z, SFR from Juodžbalis et al. (2024)"]])

# z, SFR from: https://www.nature.com/articles/s41586-024-08210-5#Sec2 Juodžbalis et al. (2024)

entry332 = np.array([["(Tentative) J0332-2748/GS-200679/200679", "Juodžbalis et al. (2025)",
                     "https://arxiv.org/html/2504.03551v1",
                     "JWST", "10:12:27.34", "-27:48:22.32", "",
                     "4.547", "", "", "log6.19", "log0.60", "log0.30", "log43.63", "log0.09", "log0.39",
                     "0.23", "0.02", "0.19", "", "", "", "", "", "",
                     "", "", "", "", "", "", "log8.53", "log0.13", "log0.13",
                     ""]])

entry333 = np.array([["(Tentative) J0332-2751/GS-20057765/20057765", "Juodžbalis et al. (2025)",
                     "https://arxiv.org/html/2504.03551v1",
                     "JWST", "03:32:09.79", "-27:51:32.44", "",
                     "8.913", "", "", "log7.33", "log0.62", "log0.70", "log44.16", "log0.19", "log0.30",
                     "0.051", "0.090", "0.036", "", "", "", "", "", "",
                     "", "", "", "", "", "", "log8.08", "log0.30", "log0.30",
                     ""]])

entry334 = np.array([["(Tentative) J0332-2752/GS-20030333/20030333", "Juodžbalis et al. (2025)",
                     "https://arxiv.org/html/2504.03551v1",
                     "JWST", "03:32:12.90", "-27:52:40.40", "",
                     "7.891", "", "", "log7.42", "log0.65", "log0.48", "log44.44", "log0.11", "log0.14",
                     "0.08", "0.078", "0.056", "", "", "", "", "", "",
                     "", "", "", "", "", "", "log8.24", "log0.08", "log0.08",
                     ""]])

entry335 = np.array([["(Tentative) J0332-2753/GS-164055/164055", "Juodžbalis et al. (2025)",
                     "https://arxiv.org/html/2504.03551v1",
                     "JWST", "03:32:19.60", "-27:53:18.85", "",
                     "7.397", "", "", "log7.63", "log0.59", "log0.66", "log44.21", "log0.16", "log0.21",
                     "0.03", "0.048", "0.020", "", "", "", "", "", "",
                     "", "", "", "", "", "", "log7.99", "log0.23", "log0.23",
                     ""]])

entry336 = np.array([["(Tentative) J1236+6214/GN-4685/4685", "Juodžbalis et al. (2025)",
                     "https://arxiv.org/html/2504.03551v1",
                     "JWST", "12:36:23.11", "+62:14:20.90", "",
                     "7.415", "", "", "log7.36", "log0.45", "log0.42", "log44.13", "log0.10", "log0.12",
                     "0.045", "0.020", "0.020", "", "", "", "", "", "",
                     "", "", "", "", "", "", "log9.91", "log0.22", "log0.21",
                     ""]])

entry337 = np.array([["J0132-0216/J023-02/J023.0-02.26", "D'Odorico et al. (2023), Banados et al. (2016), Mazzucchelli et al. (2023)",
                     "https://academic.oup.com/mnras/article/523/1/1399/7172883, https://arxiv.org/pdf/1608.03279, https://arxiv.org/pdf/2306.16474",
                     "PSO", "01:32:01.70", "-02:16:03.11", "",
                     "5.817", "0.002", "0.002", "log9.39", "log0.05", "log0.06", "log47.33", "log0.06", "log0.07",
                     "0.669972", "0.128589", "0.131987", "-26.46", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     "M1450 from Banados et al. (2016), L_bol, (recalculated using formula [2]) f_Edd from Mazzucchelli et al. (2023)"]])

# M1450 from: https://arxiv.org/pdf/1608.03279 Banados et al. (2016)
# L_bol, f_Edd from: https://arxiv.org/pdf/2306.16474 Mazzucchelli et al. (2023)

entry338 = np.array([["J0140-1140/J025-11/J025.2-11.68", "D'Odorico et al. (2023), Banados et al. (2016), Mazzucchelli et al. (2023)",
                     "https://academic.oup.com/mnras/article/523/1/1399/7172883, https://arxiv.org/pdf/1608.03279, https://arxiv.org/pdf/2306.16474",
                     "PSO", "01:40:57.03", "-11:40:59.48", "",
                     "5.816", "0.002", "0.002", "log9.33", "log0.06", "log0.07", "log47.27", "log0.09", "log0.11",
                     "0.654722", "0.179271", "0.175955", "-26.87", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     "M1450 from Banados et al. (2016), L_bol, (recalculated using formula [2]) f_Edd from Mazzucchelli et al. (2023)"]])

# M1450 from: https://arxiv.org/pdf/1608.03279 Banados et al. (2016)
# L_bol, f_Edd from: https://arxiv.org/pdf/2306.16474 Mazzucchelli et al. (2023)

entry339 = np.array([["J0158-2905/J029-29/J029.5-29.08", "D'Odorico et al. (2023), Banados et al. (2016), Mazzucchelli et al. (2023)",
                     "https://academic.oup.com/mnras/article/523/1/1399/7172883, https://arxiv.org/pdf/1608.03279, https://arxiv.org/pdf/2306.16474",
                     "PSO", "01:58:04.14", "-29:05:19.25", "",
                     "5.976", "0.003", "0.003", "log9.34", "log0.06", "log0.07", "log47.49", "log0.07", "log0.08",
                     "1.086567", "0.268754", "0.273452", "-27.32", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     "M1450 from Banados et al. (2016), L_bol, (recalculated using formula [2]) f_Edd from Mazzucchelli et al. (2023)"]])

# M1450 from: https://arxiv.org/pdf/1608.03279 Banados et al. (2016)
# L_bol, f_Edd from: https://arxiv.org/pdf/2306.16474 Mazzucchelli et al. (2023)

entry340 = np.array([["J0423+0143/P065+01/J065+01/J065.9+01.72", "D'Odorico et al. (2023), Mazzucchelli et al. (2023)",
                     "https://academic.oup.com/mnras/article/523/1/1399/7172883, https://arxiv.org/pdf/2306.16474",
                     "PSO", "04:23:50.15", "+01:43:24.79", "",
                     "5.804", "0.004", "0.004", "log9.60", "log0.12", "log0.17", "log47.2", "log0.08", "log0.1",
                     "0.306236", "0.115479", "0.117502", "", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     "L_bol, (recalculated using formula [2]) f_Edd from Mazzucchelli et al. (2023)"]])

# L_bol, f_Edd from: https://arxiv.org/pdf/2306.16474 Mazzucchelli et al. (2023)

entry341 = np.array([["J0713+0855/J108+08/J108.4+08.92", "D'Odorico et al. (2023), Banados et al. (2016), Mazzucchelli et al. (2023)",
                     "https://academic.oup.com/mnras/article/523/1/1399/7172883, https://arxiv.org/pdf/1608.03279, https://arxiv.org/pdf/2306.16474",
                     "PSO", "07:13:46.31", "+08:55:32.65", "",
                     "5.955", "0.002", "0.002", "log9.49", "log0.08", "log0.10", "log47.46", "log0.1", "log0.13",
                     "0.717888", "0.235871", "0.237252", "-27.59", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     "M1450 from Banados et al. (2016), L_bol, (recalculated using formula [2]) f_Edd from Mazzucchelli et al. (2023)"]])

# M1450 from: https://arxiv.org/pdf/1608.03279 Banados et al. (2016)
# L_bol, f_Edd from: https://arxiv.org/pdf/2306.16474 Mazzucchelli et al. (2023)

entry342 = np.array([["J1213-1246/J183-12/J183.2-12.76", "D'Odorico et al. (2023), Banados et al. (2016), Mazzucchelli et al. (2023)",
                     "https://academic.oup.com/mnras/article/523/1/1399/7172883, https://arxiv.org/pdf/1608.03279, https://arxiv.org/pdf/2306.16474",
                     "PSO", "12:13:11.81", "-12:46:03.45", "",
                     "5.893", "0.006", "0.006", "log9.22", "log0.07", "log0.09", "log47.41", "log0.06", "log0.07",
                     "1.191397", "0.418241", "0.424716", "-27.49", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     "M1450 from Banados et al. (2016), L_bol, (recalculated using formula [2]) f_Edd from Mazzucchelli et al. (2023), additional information (SFR_IR) here: https://iopscience.iop.org/article/10.3847/1538-4357/aba52d Li et al. (2020)"]])

# M1450 from: https://arxiv.org/pdf/1608.03279 Banados et al. (2016)
# L_bol, f_Edd from: https://arxiv.org/pdf/2306.16474 Mazzucchelli et al. (2023)

entry343 = np.array([["J1609-1258/J242-12/J242.4-12.98", "D'Odorico et al. (2023), Banados et al. (2016), Mazzucchelli et al. (2023)",
                     "https://academic.oup.com/mnras/article/523/1/1399/7172883, https://arxiv.org/pdf/1608.03279, https://arxiv.org/pdf/2306.16474",
                     "PSO", "16:09:45.53", "-12:58:54.11", "",
                     "5.840", "0.006", "0.006", "log9.51", "log0.10", "log0.13", "log47.26", "log0.12", "log0.17",
                     "0.43257", "0.177475", "0.179317", "-26.92", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     "M1450 from Banados et al. (2016), L_bol, (recalculated using formula [2]) f_Edd from Mazzucchelli et al. (2023)"]])

# M1450 from: https://arxiv.org/pdf/1608.03279 Banados et al. (2016)
# L_bol, f_Edd from: https://arxiv.org/pdf/2306.16474 Mazzucchelli et al. (2023)

entry344 = np.array([["J2033-2738/J308-27/J308.4-27.64", "D'Odorico et al. (2023), Banados et al. (2016), Mazzucchelli et al. (2023)",
                     "https://academic.oup.com/mnras/article/523/1/1399/7172883, https://arxiv.org/pdf/1608.03279, https://arxiv.org/pdf/2306.16474",
                     "PSO", "20:33:55.91", "-27:38:54.60", "",
                     "5.799", "0.002", "0.002", "log9.09", "log0.05", "log0.05", "log47.35", "log0.06", "log0.07",
                     "1.39977", "0.268661", "0.258053", "-26.78", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     "M1450 from Banados et al. (2016), L_bol, (recalculated using formula [2]) f_Edd from Mazzucchelli et al. (2023)"]])

# M1450 from: https://arxiv.org/pdf/1608.03279 Banados et al. (2016)
# L_bol, f_Edd from: https://arxiv.org/pdf/2306.16474 Mazzucchelli et al. (2023)

entry345 = np.array([["(Tentative/Galaxy) J1419+5253/CEERS_01465", "Harikane et al. (2023)",
                     "https://arxiv.org/pdf/2303.11946",
                     "JWST", "14:19:33.12", "+52:53:17.70", "",
                     "5.274", "", "", "", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry346 = np.array([["J1210+0134", "Matsuoka et al. (2019)",
                     "https://arxiv.org/pdf/1908.07910",
                     "HSC", "12:10:49.13", "+01:34:26.70", "",
                     "5.97", "", "", "", "", "", "", "", "",
                     "", "", "", "-22.60", "0.07", "0.07", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry347 = np.array([["J0930+0057", "Matsuoka et al. (2019)",
                     "https://arxiv.org/pdf/1908.07910",
                     "HSC", "09:30:00.85", "+00:57:38.40", "",
                     "5.92", "", "", "", "", "", "", "", "",
                     "", "", "", "-24.91", "0.05", "0.05", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry348 = np.array([["J1618+5526", "Matsuoka et al. (2019)",
                     "https://arxiv.org/pdf/1908.07910",
                     "HSC", "16:18:19.77", "+55:26:54.00", "",
                     "5.91", "", "", "", "", "", "", "", "",
                     "", "", "", "-24.26", "0.09", "0.09", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry349 = np.array([["J1423−0225", "Matsuoka et al. (2019)",
                     "https://arxiv.org/pdf/1908.07910",
                     "HSC", "14:23:07.21", "-02:25:19.00", "",
                     "5.9", "", "", "", "", "", "", "", "",
                     "", "", "", "-24.26", "0.13", "0.13", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry350 = np.array([["J0238−0318", "Matsuoka et al. (2019)",
                     "https://arxiv.org/pdf/1908.07910",
                     "HSC", "02:38:58.09", "-03:18:45.40", "",
                     "5.83", "", "", "", "", "", "", "", "",
                     "", "", "", "-23.94", "0.03", "0.03", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry351 = np.array([["J1132+0038", "Matsuoka et al. (2019)",
                     "https://arxiv.org/pdf/1908.07910",
                     "HSC", "11:32:18.15", "+00:38:00.10", "",
                     "5.66", "", "", "", "", "", "", "", "",
                     "", "", "", "-23.18", "0.05", "0.05", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry352 = np.array([["J1548+0050", "Wang et al. (2019)",
                     "https://iopscience.iop.org/article/10.3847/1538-4357/ab2be5/pdf",
                     "DELS", "15:48:25.40", "+00:50:15.50", "",
                     "6.15", "0.05", "0.05", "", "", "", "", "", "",
                     "", "", "", "-25.62", "0.18", "0.18", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry353 = np.array([["J0843+2911", "Wang et al. (2019)",
                     "https://iopscience.iop.org/article/10.3847/1538-4357/ab2be5/pdf",
                     "DELS", "08:43:03.76", "+29:11:13.40", "",
                     "6.15", "0.03", "0.03", "", "", "", "", "", "",
                     "", "", "", "-25.79", "0.15", "0.15", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry354 = np.array([["J1041+2008", "Wang et al. (2019)",
                     "https://iopscience.iop.org/article/10.3847/1538-4357/ab2be5/pdf",
                     "DELS", "10:41:19.15", "20:08:24.00", "",
                     "6.12", "0.05", "0.05", "", "", "", "", "", "",
                     "", "", "", "-26.08", "0.11", "0.11", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry355 = np.array([["J0918+1940", "Wang et al. (2019)",
                     "https://iopscience.iop.org/article/10.3847/1538-4357/ab2be5/pdf",
                     "DELS", "09:18:28.65", "+19:40:45.00", "",
                     "5.92", "0.05", "0.05", "", "", "", "", "", "",
                     "", "", "", "-25.91", "0.13", "0.13", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry356 = np.array([["J1119+0113", "Wang et al. (2019)",
                     "https://iopscience.iop.org/article/10.3847/1538-4357/ab2be5/pdf",
                     "DELS", "11:19:21.65", "01:13:08.60", "",
                     "5.78", "0.05", "0.05", "", "", "", "", "", "",
                     "", "", "", "-25.57", "0.14", "0.14", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry357 = np.array([["J0858+0000", "Matsuoka et al. (2018)",
                     "https://arxiv.org/pdf/1803.01861",
                     "HSC", "08:58:13.51", "+00:00:57.10", "",
                     "5.99", "", "", "", "", "", "", "", "",
                     "", "", "", "-25.28", "0.01", "0.01", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry358 = np.array([["(Tentative) J0220−0432", "Matsuoka et al. (2018)",
                     "https://arxiv.org/pdf/1803.01861",
                     "HSC", "02:20:29.72", "-04:32:04.00", "",
                     "5.90", "", "", "", "", "", "", "", "",
                     "", "", "", "-22.17", "0.10", "0.10", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry359 = np.array([["J1422+0011", "Matsuoka et al. (2018)",
                     "https://arxiv.org/pdf/1803.01861",
                     "HSC", "14:22:00.23", "+00:11:03.00", "",
                     "5.89", "", "", "", "", "", "", "", "",
                     "", "", "", "-22.79", "0.07", "0.07", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry360 = np.array([["J2231−0035", "Matsuoka et al. (2018)",
                     "https://arxiv.org/pdf/1803.01861",
                     "HSC", "22:31:48.89", "-00:35:47.50", "",
                     "5.87", "", "", "", "", "", "", "", "",
                     "", "", "", "-22.67", "0.10", "0.10", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry361 = np.array([["(Tentative) J1209−0006", "Matsuoka et al. (2018)",
                     "https://arxiv.org/pdf/1803.01861",
                     "HSC", "12:09:23.99", "-00:06:46.50", "",
                     "5.86", "", "", "", "", "", "", "", "",
                     "", "", "", "-22.51", "0.05", "0.05", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry362 = np.array([["J1550+4318", "Matsuoka et al. (2018)",
                     "https://arxiv.org/pdf/1803.01861",
                     "HSC", "15:50:00.93", "+43:18:02.80", "",
                     "5.84", "", "", "", "", "", "", "", "",
                     "", "", "", "-22.86", "0.04", "0.04", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry363 = np.array([["J1414+0130", "Matsuoka et al. (2018)",
                     "https://arxiv.org/pdf/1704.05854",
                     "HSC", "14:14:39.54", "+01:30:36.5", "",
                     "5.94", "", "", "", "", "", "", "", "",
                     "", "", "", "-23.53", "0.04", "0.04", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry364 = np.array([["J0903+0211", "Matsuoka et al. (2018)",
                     "https://arxiv.org/pdf/1704.05854",
                     "HSC", "09:03:14.68", "+02:11:28.3", "",
                     "5.92", "", "", "", "", "", "", "", "",
                     "", "", "", "-23.20", "0.07", "0.07", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry365 = np.array([["J0839+0015", "Li et al. (2020)",
                     "https://iopscience.iop.org/article/10.3847/1538-4357/aba52d",
                     "SDSS", "08:39:55.36", "+00:15:54.2	", "",
                     "5.84", "0.04", "0.04", "", "", "", "", "", "",
                     "", "", "", "-25.4", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry366 = np.array([["J0341-0048/P055−00/J055.4−00.80", "Banados et al. (2016)",
                     "https://arxiv.org/pdf/1608.03279",
                     "PSO", "03:41:41.86", "-00:48:12.74", "",
                     "5.68", "", "", "", "", "", "", "", "",
                     "", "", "", "-26.37", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry367 = np.array([["J0901+1615/P135+16/J135.3+16.25", "Banados et al. (2016), Li et al. (2020)",
                     "https://arxiv.org/pdf/1608.03279, https://iopscience.iop.org/article/10.3847/1538-4357/aba52d",
                     "PSO", "09:01:32.65", "+16:15:06.83", "",
                     "5.63", "0.05", "0.05", "", "", "", "2.5e13S", "", "",
                     "", "", "", "-25.91", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     "L_bol from Li et al. (2020), additional information (SFR_IR) here: https://iopscience.iop.org/article/10.3847/1538-4357/aba52d Li et al. (2020)"]])

# z, L_bol from: https://iopscience.iop.org/article/10.3847/1538-4357/aba52d Li et al. (2020)

entry368 = np.array([["J1229+0419/P187+04/J187.3+04.32", "Banados et al. (2016), Li et al. (2020)",
                     "https://arxiv.org/pdf/1608.03279, https://iopscience.iop.org/article/10.3847/1538-4357/aba52d",
                     "PSO", "12:29:13.21", "+04:19:27.75", "",
                     "5.89", "0.02", "0.02", "", "", "", "1.4e13S", "", "",
                     "", "", "", "-25.62", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     "L_bol from Li et al. (2020), additional information (SFR_IR) here: https://iopscience.iop.org/article/10.3847/1538-4357/aba52d Li et al. (2020)"]])

# z, L_bol from: https://iopscience.iop.org/article/10.3847/1538-4357/aba52d Li et al. (2020)

entry369 = np.array([["J1403-1200/P210−12/J210.8−12.00", "Banados et al. (2016), Li et al. (2020)",
                     "https://arxiv.org/pdf/1608.03279, https://iopscience.iop.org/article/10.3847/1538-4357/aba52d",
                     "PSO", "14:03:29.33", "-12:00:34.14", "",
                     "5.84", "0.05", "0.05", "", "", "", "1.9e13S", "", "",
                     "", "", "", "-25.82", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     "L_bol from Li et al. (2020), additional information (SFR_IR) here: https://iopscience.iop.org/article/10.3847/1538-4357/aba52d Li et al. (2020)"]])

# z, L_bol from: https://iopscience.iop.org/article/10.3847/1538-4357/aba52d Li et al. (2020)

entry370 = np.array([["J1420-1602/P215−16/J215.15−16.04", "Banados et al. (2016), Li et al. (2020)",
                     "https://arxiv.org/pdf/1608.03279, https://iopscience.iop.org/article/10.3847/1538-4357/aba52d",
                     "PSO", "14:20:36.34", "-16:02:30.25", "",
                     "5.73", "0.02", "0.02", "", "", "", "10.8e13S", "", "",
                     "", "", "", "-27.54", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     "L_bol from Li et al. (2020), additional information (SFR_IR) here: https://iopscience.iop.org/article/10.3847/1538-4357/aba52d Li et al. (2020)"]])

# z, L_bol from: https://iopscience.iop.org/article/10.3847/1538-4357/aba52d Li et al. (2020)

entry371 = np.array([["J1421+2631/P215+26/J215.4+26.53", "Banados et al. (2023)",
                     "https://iopscience.iop.org/article/10.3847/1538-4365/acb3c7",
                     "PSO", "14:21:43.29", "+26:31:57.14	", "",
                     "6.28", "", "", "", "", "", "", "", "",
                     "", "", "", "-26.37", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry372 = np.array([["J0328−3253", "Venemans et al. (2015)",
                     "https://academic.oup.com/mnras/article/453/3/2259/1079051",
                     "VIK+KiDS", "03:28:35.511", "-32:53:22.92", "",
                     "5.86", "0.03", "0.03", "", "", "", "", "", "",
                     "", "", "", "-26.60", "0.04", "0.04", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry373 = np.array([["J1306+0359", "Eilers et al. (2017)",
                     "https://iopscience.iop.org/article/10.3847/1538-4357/aa6c60",
                     "SDSS", "13:06:08.27", "+03:59:26.36", "",
                     "6.016", "", "", "", "", "", "", "", "",
                     "", "", "", "-26.81", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry374 = np.array([["J0316−1340", "Willott et al. (2010)",
                     "https://iopscience.iop.org/article/10.1088/0004-6256/139/3/906",
                     "CFHQS", "03:16:49.87", "-13:40:32.30", "",
                     "5.99", "", "", "", "", "", "", "", "",
                     "", "", "", "-24.63", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry375 = np.array([["J1059−0906", "Willott et al. (2010)",
                     "https://iopscience.iop.org/article/10.1088/0004-6256/139/3/906",
                     "CFHQS", "10:59:28.61", "-09:06:20.40", "",
                     "5.92", "", "", "", "", "", "", "", "",
                     "", "", "", "-25.58", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry376 = np.array([["J2242+0334", "Willott et al. (2010)",
                     "https://iopscience.iop.org/article/10.1088/0004-6256/139/3/906",
                     "CFHQS", "22:42:37.55", "+03:34:21.60", "",
                     "5.88", "", "", "", "", "", "", "", "",
                     "", "", "", "-24.22", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry377 = np.array([["J2325+2628", "Wang et al. (2016)",
                     "https://arxiv.org/pdf/1602.04659",
                     "SDSS+WISE", "23:25:14.24", "+26:28:47.60", "",
                     "5.77", "0.05", "0.05", "", "", "", "", "", "",
                     "", "", "", "-26.98", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry378 = np.array([["J0309+2717", "Belladitta et al. (2020), Khusanova et al. (2022)",
                     "https://www.aanda.org/articles/aa/pdf/2020/03/aa37395-19.pdf, https://www.aanda.org/articles/aa/full_html/2022/08/aa43660-22/aa43660-22.html#R10",
                     "PSO", "03:09:47.49", "+27:17:57.31", "",
                     "6.10", "0.03", "0.03", "", "", "", "", "", "",
                     "", "", "", "-25.1", "", "", "", "", "",
                     "340–1200", "", "", "340–1200", "", "", "", "", "",
                     "SFR from Khusanova et al. (2022)"]])

# SFR from: https://www.aanda.org/articles/aa/full_html/2022/08/aa43660-22/aa43660-22.html#R10 Khusanova et al. (2022)

entry379 = np.array([["J2329-1520/P352–15/J352.4–15.33", "Banados et al. (2018)",
                     "https://iopscience.iop.org/article/10.3847/2041-8213/aac511",
                     "PSO", "23:29:36.8363", "-15:20:14.460", "",
                     "5.84", "0.02", "0.02", "", "", "", "", "", "",
                     "", "", "", "-25.59", "0.13", "0.13", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry380 = np.array([["J0102−0218", "Willott et al. (2009)",
                     "https://iopscience.iop.org/article/10.1088/0004-6256/137/3/3541",
                     "CFHQS", "01:02:50.64", "-02:18:09.90", "",
                     "5.95", "", "", "", "", "", "", "", "",
                     "", "", "", "-24.31", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry381 = np.array([["J0239−0045", "Jiang et al. (2016)",
                     "https://iopscience.iop.org/article/10.3847/1538-4357/833/2/222",
                     "SDSS", "02:39:30.24", "-00:45:05.30", "",
                     "5.82", "", "", "", "", "", "", "", "",
                     "", "", "", "-24.50", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry382 = np.array([["J2053+0047", "Jiang et al. (2016)",
                     "https://iopscience.iop.org/article/10.3847/1538-4357/833/2/222",
                     "SDSS", "20:53:21.77", "+00:47:06.80", "",
                     "5.92", "", "", "", "", "", "", "", "",
                     "", "", "", "-25.54", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry383 = np.array([["J2119−0040", "Jiang et al. (2016)",
                     "https://iopscience.iop.org/article/10.3847/1538-4357/833/2/222",
                     "SDSS", "21:19:51.89", "-00:40:20.10", "",
                     "5.87", "0.03", "0.03", "", "", "", "", "", "",
                     "", "", "", "-24.73", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry384 = np.array([["J2147+0107", "Jiang et al. (2016)",
                     "https://iopscience.iop.org/article/10.3847/1538-4357/833/2/222",
                     "SDSS", "21:47:55.42", "+01:07:55.50", "",
                     "5.81", "", "", "", "", "", "", "", "",
                     "", "", "", "-25.00", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry385 = np.array([["J1429+3304", "Cool et al. (2006)",
                     "https://iopscience.iop.org/article/10.1086/505535/pdf",
                     "NDWFS", "14:29:37.90", "+33:04:16.00", "",
                     "5.39", "", "", "", "", "", "", "", "",
                     "", "", "", "-25.52", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry386 = np.array([["J1427+3522", "Cool et al. (2006)",
                     "https://iopscience.iop.org/article/10.1086/505535/pdf",
                     "NDWFS", "14:27:29.70", "+35:22:09.00", "",
                     "5.53", "", "", "", "", "", "", "", "",
                     "", "", "", "-24.67", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry387 = np.array([["J0019-2417/J004.8–24.29", "Banados et al. (2016)",
                     "https://arxiv.org/pdf/1608.03279",
                     "PSO", "00:19:15.38", "-24:17:56.98", "",
                     "5.68", "", "", "", "", "", "", "", "",
                     "", "", "", "-27.24", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry388 = np.array([["J0037-0807/J009.3–08.11", "Banados et al. (2016)",
                     "https://arxiv.org/pdf/1608.03279",
                     "PSO", "00:37:25.76", "-08:07:08.46", "",
                     "5.72", "", "", "", "", "", "", "", "",
                     "", "", "", "-26.51", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry389 = np.array([["J0125-2552/J021.4–25.88", "Banados et al. (2016)",
                     "https://arxiv.org/pdf/1608.03279",
                     "PSO", "01:25:41.12", "-25:52:56.24", "",
                     "5.79", "", "", "", "", "", "", "", "",
                     "", "", "", "-27.08", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry390 = np.array([["J0240+1732/J040.0+17.54", "Banados et al. (2016)",
                     "https://arxiv.org/pdf/1608.03279",
                     "PSO", "02:40:03.82", "+17:32:44.91", "",
                     "5.68", "", "", "", "", "", "", "", "",
                     "", "", "", "-25.81", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry391 = np.array([["J0250-0255/J042.6–02.91", "Banados et al. (2016)",
                     "https://arxiv.org/pdf/1608.03279",
                     "PSO", "02:50:40.58", "-02:55:02.82", "",
                     "5.89", "", "", "", "", "", "", "", "",
                     "", "", "", "-26.59", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry392 = np.array([["J0317-2633/J049.2–26.55", "Banados et al. (2016)",
                     "https://arxiv.org/pdf/1608.03279",
                     "PSO", "03:17:10.42", "-26:33:15.71", "",
                     "5.94", "", "", "", "", "", "", "", "",
                     "", "", "", "-25.82", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry393 = np.array([["J0335-1547/J053.9–15.79", "Banados et al. (2016)",
                     "https://arxiv.org/pdf/1608.03279",
                     "PSO", "03:35:50.53", "-15:47:44.50", "",
                     "5.87", "", "", "", "", "", "", "", "",
                     "", "", "", "-26.25", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry394 = np.array([["J0444-0433/J071.0–04.55", "Banados et al. (2016)",
                     "https://arxiv.org/pdf/1608.03279",
                     "PSO", " 04:44:07.73", "-04:33:33.07", "",
                     "5.89", "", "", "", "", "", "", "", "",
                     "", "", "", "-26.60", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry395 = np.array([["J0445-0219/J071.4–02.33", "Banados et al. (2016)",
                     "https://arxiv.org/pdf/1608.03279",
                     "PSO", "04:45:48.18", "-02:19:59.84", "",
                     "5.69", "", "", "", "", "", "", "", "",
                     "", "", "", "-27.53", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry396 = np.array([["J0503-0730/J075.9–07.50", "Banados et al. (2016)",
                     "https://arxiv.org/pdf/1608.03279",
                     "PSO", "05:03:44.56", "-07:30:22.07", "",
                     "5.88", "", "", "", "", "", "", "", "",
                     "", "", "", "-26.62", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])                  

entry397 = np.array([["J0829+0303/J127.2+03.06", "Banados et al. (2016)",
                     "https://arxiv.org/pdf/1608.03279",
                     "PSO", "08:29:07.62", "+03:03:56.52", "",
                     "5.85", "", "", "", "", "", "", "", "",
                     "", "", "", "-26.03", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])                     

entry398 = np.array([["J0903-1350/J135.8–13.83", "Banados et al. (2016)",
                     "https://arxiv.org/pdf/1608.03279",
                     "PSO", "09:03:28.91", "-13:50:01.27", "",
                     "5.91", "", "", "", "", "", "", "", "",
                     "", "", "", "-25.86", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry399 = np.array([["J1031-0239/J157.9–02.65", "Banados et al. (2016)",
                     "https://arxiv.org/pdf/1608.03279",
                     "PSO", "10:31:37.69", "-02:39:35.67", "",
                     "5.88", "", "", "", "", "", "", "", "",
                     "", "", "", "-26.44", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry400 = np.array([["J1109+5657/J167.4+56.95", "Banados et al. (2016)",
                     "https://arxiv.org/pdf/1608.03279",
                     "PSO", "11:09:53.43", "+56:57:07.61", "",
                     "5.95", "", "", "", "", "", "", "", "",
                     "", "", "", "-26.00", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry401 = np.array([["J1128+2653/J172.1+26.88", "Banados et al. (2016)",
                     "https://arxiv.org/pdf/1608.03279",
                     "PSO", "11:28:42.48", "+26:53:12.00", "",
                     "5.77", "", "", "", "", "", "", "", "",
                     "", "", "", "-25.91", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry402 = np.array([["J1139-1217/J174.7–12.28", "Banados et al. (2016)",
                     "https://arxiv.org/pdf/1608.03279",
                     "PSO", "11:39:10.09", "-12:17:04.38", "",
                     "5.81", "", "", "", "", "", "", "", "",
                     "", "", "", "-26.49", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry403 = np.array([["J1141-2015/J175.4–20.26", "Banados et al. (2016)",
                     "https://arxiv.org/pdf/1608.03279",
                     "PSO", "11:41:38.20", "-20:15:55.65", "",
                     "5.69", "", "", "", "", "", "", "", "",
                     "", "", "", "-26.32", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry404 = np.array([["J1148+5253", "Banados et al. (2016)",
                     "https://arxiv.org/pdf/1608.03279",
                     "RD", "11:48:16.21", "+52:53:39.30", "",
                     "5.70", "", "", "", "", "", "", "", "",
                     "", "", "", "-24.20", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry405 = np.array([["J1148+0056", "Banados et al. (2016), Venemans et al. (2015)",
                     "https://arxiv.org/pdf/1608.03279, https://academic.oup.com/mnras/article/453/3/2259/1079051",
                     "VIK", "11:48:33.180", "+00:56:42.26", "",
                     "5.84", "0.03", "0.03", "", "", "", "", "", "",
                     "", "", "", "-24.84", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     "coordinates, z from Venemans et al. (2015)"]])

# coordinates, z from: https://academic.oup.com/mnras/article/453/3/2259/1079051 Venemans et al. (2015)

entry406 = np.array([["J1154-1211/J178.5–12.18", "Banados et al. (2016)",
                     "https://arxiv.org/pdf/1608.03279",
                     "PSO", "11:54:14.26", "-12:11:17.48", "",
                     "5.83", "", "", "", "", "", "", "", "",
                     "", "", "", "-26.10", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry407 = np.array([["J1215+0023", "Banados et al. (2016), Venemans et al. (2015)",
                     "https://arxiv.org/pdf/1608.03279, https://academic.oup.com/mnras/article/453/3/2259/1079051",
                     "VIK", "12:15:16.879", "+00:23:24.74", "",
                     "5.93", "0.03", "0.03", "", "", "", "", "", "",
                     "", "", "", "-25.45", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     "coordinates, z from Venemans et al. (2015)"]])

# coordinates, z from: https://academic.oup.com/mnras/article/453/3/2259/1079051 Venemans et al. (2015)

entry408 = np.array([["J1228-0233/J187.1–02.56", "Banados et al. (2016)",
                     "https://arxiv.org/pdf/1608.03279",
                     "PSO", "12:28:25.15", "-02:33:39.25", "",
                     "5.77", "", "", "", "", "", "", "", "",
                     "", "", "", "-25.81", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry409 = np.array([["J1256+2532/J194.1+25.54", "Banados et al. (2016)",
                     "https://arxiv.org/pdf/1608.03279",
                     "PSO", "12:56:30.97", "+25:32:51.45 ", "",
                     "5.91", "", "", "", "", "", "", "", "",
                     "", "", "", "-25.83", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry410 = np.array([["J1310+2532/J197.7+25.53", "Banados et al. (2016)",
                     "https://arxiv.org/pdf/1608.03279",
                     "PSO", "13:10:52.75", "+25:32:06.68", "",
                     "5.84", "", "", "", "", "", "", "", "",
                     "", "", "", "-26.00", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])                     

entry411 = np.array([["J1327+5732/J201.9+57.54", "Banados et al. (2016)",
                     "https://arxiv.org/pdf/1608.03279",
                     "PSO", "13:27:41.32", "+57:32:38.37", "",
                     "5.74", "", "", "", "", "", "", "", "",
                     "", "", "", "-26.05", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry412 = np.array([["J1356-2642/J209.2–26.70", "Banados et al. (2016)",
                     "https://arxiv.org/pdf/1608.03279",
                     "PSO", "13:56:49.41", "-26:42:30.23", "",
                     "5.72", "", "", "", "", "", "", "", "",
                     "", "", "", "-27.19", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry413 = np.array([["J1403+0902/J210.8+09.04", "Banados et al. (2016)",
                     "https://arxiv.org/pdf/1608.03279",
                     "PSO", "14:03:19.13", "+09:02:50.99", "",
                     "5.88", "", "", "", "", "", "", "", "",
                     "", "", "", "-26.42", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry414 = np.array([["J1409-1559/J212.2–15.98", "Banados et al. (2016)",
                     "https://arxiv.org/pdf/1608.03279",
                     "PSO", "14:09:11.38", "-15:59:11.66", "",
                     "5.83", "", "", "", "", "", "", "", "",
                     "", "", "", "-25.44", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry415 = np.array([["J1413-2233/J213.3–22.56", "Banados et al. (2016)",
                     "https://arxiv.org/pdf/1608.03279",
                     "PSO", "14:13:27.12", "-22:33:42.25", "",
                     "5.92", "", "", "", "", "", "", "", "",
                     "", "", "", "-26.85", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry416 = np.array([["J1414-1328/J213.7–13.48", "Banados et al. (2016)",
                     "https://arxiv.org/pdf/1608.03279",
                     "PSO", "14:14:55.90", "-13:28:49.28", "",
                     "5.78", "", "", "", "", "", "", "", "",
                     "", "", "", "-25.69", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry417 = np.array([["J1543+1700/J235.9+17.00", "Banados et al. (2016)",
                     "https://arxiv.org/pdf/1608.03279",
                     "PSO", "15:43:46.82", "+17:00:28.46", "",
                     "5.82", "", "", "", "", "", "", "", "",
                     "", "", "", "-26.53", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])                     

entry418 = np.array([["J1545+1636/J236.2+16.60", "Banados et al. (2016)",
                     "https://arxiv.org/pdf/1608.03279",
                     "PSO", "15:45:09.90", "+16:36:31.91", "",
                     "5.82", "", "", "", "", "", "", "", "",
                     "", "", "", "-25.89", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry419 = np.array([["J1555-0653/J238.8–06.89", "Banados et al. (2016)",
                     "https://arxiv.org/pdf/1608.03279",
                     "PSO", "15:55:24.25", "-06:53:51.59", "",
                     "5.81", "", "", "", "", "", "", "", "",
                     "", "", "", "-26.04", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry420 = np.array([["J1620-0011/J245.0–00.19", "Banados et al. (2016)",
                     "https://arxiv.org/pdf/1608.03279",
                     "PSO", "16:20:15.28", "-00:11:52.30", "",
                     "5.68", "", "", "", "", "", "", "", "",
                     "", "", "", "-25.27", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry421 = np.array([["J1748+2246/J267.0+22.78", "Banados et al. (2016)",
                     "https://arxiv.org/pdf/1608.03279",
                     "PSO", "17:48:00.51", "+22:46:52.36", "",
                     "5.95", "", "", "", "", "", "", "", "",
                     "", "", "", "-25.70", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry422 = np.array([["J2118-1055/J319.6–10.93", "Banados et al. (2016)",
                     "https://arxiv.org/pdf/1608.03279",
                     "PSO", "21:18:24.97", "-10:55:57.43", "",
                     "5.90", "", "", "", "", "", "", "", "",
                     "", "", "", "-26.72", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry423 = np.array([["J2123-2421/J320.8–24.36", "Banados et al. (2016)",
                     "https://arxiv.org/pdf/1608.03279",
                     "PSO", "21:23:28.88", "-24:21:37.44", "",
                     "5.73", "", "", "", "", "", "", "", "",
                     "", "", "", "-26.22", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry424 = np.array([["J2154-0930/J328.7–09.50", "Banados et al. (2016)",
                     "https://arxiv.org/pdf/1608.03279",
                     "PSO", "21:54:56.16", "-09:30:27.46", "",
                     "5.92", "", "", "", "", "", "", "", "",
                     "", "", "", "-26.34", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry425 = np.array([["J2204+0012", "Banados et al. (2016), Kim et al. (2015)",
                     "https://arxiv.org/pdf/1608.03279, https://iopscience.iop.org/article/10.1088/2041-8205/813/2/L35/pdf",
                     "IMS", "22:04:17.92", "+01:11:44.80", "",
                     "5.944", "0.002", "0.002", "", "", "", "", "", "",
                     "", "", "", "-24.32", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     "z from Kim et al. (2015)"]])

# z from: https://iopscience.iop.org/article/10.1088/2041-8205/813/2/L35/pdf Kim et al. (2015)

entry426 = np.array([["J2220–0101", "Banados et al. (2016), McGreer et al. (2013)",
                     "https://arxiv.org/pdf/1608.03279, https://iopscience.iop.org/article/10.1088/0004-637X/768/2/105",
                     "SDSS+UKIDSS", "22:20:18.49", "-01:01:46.89", "",
                     "5.62", "", "", "", "", "", "", "", "",
                     "", "", "", "-25.98", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     "instrument from McGreer et al. (2013)"]])

# instrument from: https://iopscience.iop.org/article/10.1088/0004-637X/768/2/105 McGreer et al. (2013)

entry427 = np.array([["J2228+0110", "Banados et al. (2016)",
                     "https://arxiv.org/pdf/1608.03279",
                     "SDSS", "22:28:43.54", "+01:10:32.20", "",
                     "5.95", "", "", "", "", "", "", "", "",
                     "", "", "", "-24.54", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry428 = np.array([["J2351+0624/J357.8+06.40", "Banados et al. (2016)",
                     "https://arxiv.org/pdf/1608.03279",
                     "PSO", "23:51:18.96", "+06:24:06.92", "",
                     "5.81", "", "", "", "", "", "", "", "",
                     "", "", "", "-25.28", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry429 = np.array([["J0000-0416/P000–04/J000.0–04.27", "Banados et al. (2023)",
                     "https://iopscience.iop.org/article/10.3847/1538-4365/acb3c7",
                     "PSO", "00:00:09.99", "-04:16:26.05", "",
                     "5.77", "", "", "", "", "", "", "", "",
                     "", "", "", "-25.84", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry430 = np.array([["J0000-1814/P000–18/J000.0-18.23", "Banados et al. (2023)",
                     "https://iopscience.iop.org/article/10.3847/1538-4365/acb3c7",
                     "PSO", "00:00:19.33", "-18:14:09.64", "",
                     "5.9", "", "", "", "", "", "", "", "",
                     "", "", "", "-25.19", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry431 = np.array([["J0006-2840/P001–28/J001.6–28.67", "Banados et al. (2023)",
                     "https://iopscience.iop.org/article/10.3847/1538-4365/acb3c7",
                     "PSO", "00:06:45.36", "-28:40:42.05", "",
                     "5.95", "", "", "", "", "", "", "", "",
                     "", "", "", "-25.61", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry432 = np.array([["J0010+0303/P002+03/J002.5+03.06", "Banados et al. (2023)",
                     "https://iopscience.iop.org/article/10.3847/1538-4365/acb3c7",
                     "PSO", "00:10:10.30", "+03:03:47.57", "",
                     "5.64", "", "", "", "", "", "", "", "",
                     "", "", "", "-25.67", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry433 = np.array([["J0034+1051/P008+10/J008.6+10.85", "Banados et al. (2023)",
                     "https://iopscience.iop.org/article/10.3847/1538-4365/acb3c7",
                     "PSO", "00:34:26.00", "+10:51:06.70", "",
                     "5.98", "", "", "", "", "", "", "", "",
                     "", "", "", "-26.07", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry434 = np.array([["J0108-1159/P017–11/J017.0–11.99", "Banados et al. (2023)",
                     "https://iopscience.iop.org/article/10.3847/1538-4365/acb3c7",
                     "PSO", "01:08:16.60", "-11:59:31.00", "",
                     "5.8", "", "", "", "", "", "", "", "",
                     "", "", "", "-25.94", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry435 = np.array([["J0200-1737/P030–17/J030.1–17.62", "Banados et al. (2023)",
                     "https://iopscience.iop.org/article/10.3847/1538-4365/acb3c7",
                     "PSO", "02:00:33.30", "-17:37:26.00", "",
                     "6.09", "", "", "", "", "", "", "", "",
                     "", "", "", "-25.36", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry436 = np.array([["J0211-1704/P032–17/J032.9–17.07", "Banados et al. (2023)",
                     "https://iopscience.iop.org/article/10.3847/1538-4365/acb3c7",
                     "PSO", "02:11:40.52", "-17:04:28.74", "",
                     "5.99", "", "", "", "", "", "", "", "",
                     "", "", "", "-25.80", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry437 = np.array([["J0224–3435", "Banados et al. (2023)",
                     "https://iopscience.iop.org/article/10.3847/1538-4365/acb3c7",
                     "VIK", "02:24:56.75", "-34:35:23.00", "",
                     "5.78", "", "", "", "", "", "", "", "",
                     "", "", "", "-24.86", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry438 = np.array([["J0232-1834/P038–18/J038.1–18.57", "Banados et al. (2023)",
                     "https://iopscience.iop.org/article/10.3847/1538-4365/acb3c7",
                     "PSO", "02:32:45.94", "-18:34:24.61", "",
                     "5.68", "", "", "", "", "", "", "", "",
                     "", "", "", "-26.04", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry439 = np.array([["J0252-0237/P043–02/J043.1–02.62", "Banados et al. (2023)",
                     "https://iopscience.iop.org/article/10.3847/1538-4365/acb3c7",
                     "PSO", "02:52:26.68", "-02:37:20.70", "",
                     "6.17", "", "", "", "", "", "", "", "",
                     "", "", "", "-25.69", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry440 = np.array([["J0322-1841/P050–18/J050.5–18.68", "Banados et al. (2023)",
                     "https://iopscience.iop.org/article/10.3847/1538-4365/acb3c7",
                     "PSO", "03:22:14.54", "-18:41:17.43", "",
                     "6.09", "", "", "", "", "", "", "", "",
                     "", "", "", "-26.27", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry441 = np.array([["J0450-0753/P072–07/J072.5–07.89", "Banados et al. (2023)",
                     "https://iopscience.iop.org/article/10.3847/1538-4365/acb3c7",
                     "PSO", "04:50:19.81", "-07:53:30.59", "",
                     "5.75", "", "", "", "", "", "", "", "",
                     "", "", "", "-25.66", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry442 = np.array([["J0504-1053/P076–10/J076.2–10.88", "Banados et al. (2023)",
                     "https://iopscience.iop.org/article/10.3847/1538-4365/acb3c7",
                     "PSO", "05:04:56.27", "-10:53:16.09", "",
                     "5.93", "", "", "", "", "", "", "", "",
                     "", "", "", "-26.13", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry443 = np.array([["J0756+0218/P119+02/J119.0+02.30", "Banados et al. (2023)",
                     "https://iopscience.iop.org/article/10.3847/1538-4365/acb3c7",
                     "PSO", "07:56:22.38", "+02:18:20.16", "",
                     "5.73", "", "", "", "", "", "", "", "",
                     "", "", "", "-26.20", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry444 = np.array([["J0816+1259/P124+12/J124.0+12.99", "Banados et al. (2023)",
                     "https://iopscience.iop.org/article/10.3847/1538-4365/acb3c7",
                     "PSO", "08:16:00.79", "+12:59:56.31", "",
                     "5.8", "", "", "", "", "", "", "", "",
                     "", "", "", "-25.59", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry445 = np.array([["J0929-1121/P142–11/J127.0+26.56", "Banados et al. (2023)",
                     "https://iopscience.iop.org/article/10.3847/1538-4365/acb3c7",
                     "PSO", "09:29:35.77", "-11:21:37.59", "",
                     "5.61", "", "", "", "", "", "", "", "",
                     "", "", "", "-25.99", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry446 = np.array([["J0953+6910/P148+69/J142.3–11.36", "Banados et al. (2023)",
                     "https://iopscience.iop.org/article/10.3847/1538-4365/acb3c7",
                     "PSO", "09:53:55.90", "+69:10:52.62", "",
                     "5.84", "", "", "", "", "", "", "", "",
                     "", "", "", "-26.46", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry447 = np.array([["J1007-1611/P151–16/J151.8-16.18", "Banados et al. (2023)",
                     "https://iopscience.iop.org/article/10.3847/1538-4365/acb3c7",
                     "PSO", "10:07:16.49", "-16:11:07.94", "",
                     "5.84", "", "", "", "", "", "", "", "",
                     "", "", "", "-25.20", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry448 = np.array([["J1025+3857/P156+38/J156.4+38.95", "Banados et al. (2023)",
                     "https://iopscience.iop.org/article/10.3847/1538-4365/acb3c7",
                     "PSO", "10:25:47.19", "+38:57:26.30", "",
                     "5.75", "", "", "", "", "", "", "", "",
                     "", "", "", "-26.78", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry449 = np.array([["J1116+5853/P169+58/J169.1+58.88", "Banados et al. (2023)",
                     "https://iopscience.iop.org/article/10.3847/1538-4365/acb3c7",
                     "PSO", "11:16:33.76", "+58:53:22.19", "",
                     "5.73", "", "", "", "", "", "", "", "",
                     "", "", "", "-26.03", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry450 = np.array([["J1123+2012/P170+20/J170.8+20.20", "Banados et al. (2023)",
                     "https://iopscience.iop.org/article/10.3847/1538-4365/acb3c7",
                     "PSO", "11:23:19.84", "+20:12:29.79", "",
                     "6.41", "", "", "", "", "", "", "", "",
                     "", "", "", "-26.10", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry451 = np.array([["J1133-0656/P173–06/J173.3–06.94", "Banados et al. (2023)",
                     "https://iopscience.iop.org/article/10.3847/1538-4365/acb3c7",
                     "PSO", "11:33:16.78", "-06:56:44.85", "",
                     "5.77", "", "", "", "", "", "", "", "",
                     "", "", "", "-25.97", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry452 = np.array([["J1133+4814/P173+48/J173.4+48.24", "Banados et al. (2023)",
                     "https://iopscience.iop.org/article/10.3847/1538-4365/acb3c7",
                     "PSO", "11:33:50.44", "+48:14:31.21", "",
                     "6.233", "", "", "", "", "", "", "", "",
                     "", "", "", "-25.12", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry453 = np.array([["J1141+7119/P175+71/J175.4+71.32", "Banados et al. (2023)",
                     "https://iopscience.iop.org/article/10.3847/1538-4365/acb3c7",
                     "PSO", "11:41:43.07", "+71:19:25.03", "",
                     "5.86", "", "", "", "", "", "", "", "",
                     "", "", "", "-25.95", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry454 = np.array([["J1153+2830/P178+28/J178.3+28.50", "Banados et al. (2023)",
                     "https://iopscience.iop.org/article/10.3847/1538-4365/acb3c7",
                     "PSO", "11:53:29.60", "+28:30:27.11", "",
                     "5.68", "", "", "", "", "", "", "", "",
                     "", "", "", "-26.77", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry455 = np.array([["J1209+5327/P182+53/J182.3+53.46", "Banados et al. (2023)",
                     "https://iopscience.iop.org/article/10.3847/1538-4365/acb3c7",
                     "PSO", "12:09:14.93", "+53:27:48.05", "",
                     "5.99", "", "", "", "", "", "", "", "",
                     "", "", "", "-25.64", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry456 = np.array([["J1253-0246/P193–02/J193.3–02.78", "Banados et al. (2023)",
                     "https://iopscience.iop.org/article/10.3847/1538-4365/acb3c7",
                     "PSO", "12:53:35.82", "-02:46:55.29", "",
                     "5.8", "", "", "", "", "", "", "", "",
                     "", "", "", "-25.43", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry457 = np.array([["J1305+1523/P196+15/J196.3+15.38", "Banados et al. (2023)",
                     "https://iopscience.iop.org/article/10.3847/1538-4365/acb3c7",
                     "PSO", "13:05:23.43", "+15:23:23.68", "",
                     "5.69", "", "", "", "", "", "", "", "",
                     "", "", "", "-26.17", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry458 = np.array([["J1311+4548/P197+45/J197.8+45.80", "Banados et al. (2023)",
                     "https://iopscience.iop.org/article/10.3847/1538-4365/acb3c7",
                     "PSO", "13:11:28.20", "+45:48:14.69", "",
                     "5.66", "", "", "", "", "", "", "", "",
                     "", "", "", "-25.73", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry459 = np.array([["J1350+3748/P207+37/J207.5+37.80", "Banados et al. (2023)",
                     "https://iopscience.iop.org/article/10.3847/1538-4365/acb3c7",
                     "PSO", "13:50:23.60", "+37:48:35.67", "",
                     "5.69", "", "", "", "", "", "", "", "",
                     "", "", "", "-25.85", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry460 = np.array([["J1351-2111/P207–21/J207.7–21.18", "Banados et al. (2023)",
                     "https://iopscience.iop.org/article/10.3847/1538-4365/acb3c7",
                     "PSO", "13:51:06.72", "-21:11:20.27", "",
                     "5.81", "", "", "", "", "", "", "", "",
                     "", "", "", "-25.95", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry461 = np.array([["J1357-0843/P209–08/J209.3–08.71", "Banados et al. (2023)",
                     "https://iopscience.iop.org/article/10.3847/1538-4365/acb3c7",
                     "PSO", "13:57:31.82", "-08:43:01.74", "",
                     "5.77", "", "", "", "", "", "", "", "",
                     "", "", "", "-25.19", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry462 = np.array([["J1433+2819/P218+28/J218.3+28.33", "Banados et al. (2023)",
                     "https://iopscience.iop.org/article/10.3847/1538-4365/acb3c7",
                     "PSO", "14:33:35.22", "+28:19:50.60", "",
                     "5.91", "", "", "", "", "", "", "", "",
                     "", "", "", "-25.85", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry463 = np.array([["J1435+0449/P218+04/J218.7+04.81", "Banados et al. (2023)",
                     "https://iopscience.iop.org/article/10.3847/1538-4365/acb3c7",
                     "PSO", "14:35:05.15", "+04:49:08.32", "",
                     "6.14", "", "", "", "", "", "", "", "",
                     "", "", "", "-25.90", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry464 = np.array([["J1458+1012/P224+10/J224.6+10.21", "Banados et al. (2023)",
                     "https://iopscience.iop.org/article/10.3847/1538-4365/acb3c7",
                     "PSO", "14:58:36.16", "+10:12:49.67", "",
                     "5.6", "", "", "", "", "", "", "", "",
                     "", "", "", "-26.90", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry465 = np.array([["J1514+0122/P228+01/J228.7+01.38", "Banados et al. (2023)",
                     "https://iopscience.iop.org/article/10.3847/1538-4365/acb3c7",
                     "PSO", "15:14:48.70", "+01:22:52.25", "",
                     "5.76", "", "", "", "", "", "", "", "",
                     "", "", "", "-25.25", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry466 = np.array([["J1724+3718/P261+37/J261.1+37.30", "Banados et al. (2023)",
                     "https://iopscience.iop.org/article/10.3847/1538-4365/acb3c7",
                     "PSO", "17:24:29.94", "+37:18:21.80", "",
                     "5.76", "", "", "", "", "", "", "", "",
                     "", "", "", "-25.60", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry467 = np.array([["J1805+4918/P271+49/J271.4+49.30", "Banados et al. (2023)",
                     "https://iopscience.iop.org/article/10.3847/1538-4365/acb3c7",
                     "PSO", "18:05:46.93", "+49:18:24.23", "",
                     "5.74", "", "", "", "", "", "", "", "",
                     "", "", "", "-26.24", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry468 = np.array([["J1845+5345/P281+53/J281.3+53.76", "Banados et al. (2023)",
                     "https://iopscience.iop.org/article/10.3847/1538-4365/acb3c7",
                     "PSO", "18:45:20.68", "+53:45:47.34", "",
                     "6.18", "", "", "", "", "", "", "", "",
                     "", "", "", "-26.65", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry469 = np.array([["J1914+6314/P288+63/J288.6+63.24", "Banados et al. (2023)",
                     "https://iopscience.iop.org/article/10.3847/1538-4365/acb3c7",
                     "PSO", "19:14:35.44", "+63:14:52.54", "",
                     "5.96", "", "", "", "", "", "", "", "",
                     "", "", "", "-26.04", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry470 = np.array([["J2025-0449/P306-04/J306.3–04.82", "Banados et al. (2023)",
                     "https://iopscience.iop.org/article/10.3847/1538-4365/acb3c7",
                     "PSO", "20:25:24.31", "-04:49:21.88", "",
                     "5.84", "", "", "", "", "", "", "", "",
                     "", "", "", "-25.94", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry471 = np.array([["J2031-0511/P307-05/J307.7–05.19", "Banados et al. (2023)",
                     "https://iopscience.iop.org/article/10.3847/1538-4365/acb3c7",
                     "PSO", "20:31:03.26", "-05:11:45.20", "",
                     "5.8", "", "", "", "", "", "", "", "",
                     "", "", "", "-25.78", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry472 = np.array([["J2216-0500/P334–05/J334.0–05.00", "Banados et al. (2023)",
                     "https://iopscience.iop.org/article/10.3847/1538-4365/acb3c7",
                     "PSO", "22:16:04.36", "-05:00:17.58", "",
                     "6.15", "", "", "", "", "", "", "", "",
                     "", "", "", "-25.66", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry473 = np.array([["J2227–3323", "Banados et al. (2023)",
                     "https://iopscience.iop.org/article/10.3847/1538-4365/acb3c7",
                     "VIK", "22:27:18.58", "-33:23:35.02", "",
                     "6.12", "", "", "", "", "", "", "", "",
                     "", "", "", "-25.41", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry474 = np.array([["J2315–2856", "Banados et al. (2023)",
                     "https://iopscience.iop.org/article/10.3847/1538-4365/acb3c7",
                     "VIK", "23:15:07.39", "-28:56:17.40", "",
                     "5.89", "", "", "", "", "", "", "", "",
                     "", "", "", "-25.35", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry475 = np.array([["(Galaxy) J1237+6212/GOODS-N-4014", "Matthee et al. (2024)",
                     "https://iopscience.iop.org/article/10.3847/1538-4357/ad2345",
                     "JWST", "12:37:12.03", "+62:12:43.36", "",
                     "5.228", "", "", "log7.58", "log0.08", "log0.08", "9.3e44", "0.5e44", "0.5e44",
                     "", "", "", "", "", "", "389.3", "13.4", "13.4",
                     "", "", "", "", "", "", "", "", "",
                     "little red dot"]])

entry476 = np.array([["(Galaxy) J1237+6214/GOODS-N-9771", "Matthee et al. (2024)",
                     "https://iopscience.iop.org/article/10.3847/1538-4357/ad2345",
                     "JWST", "12:37:07.44", "+62:14:50.31", "",
                     "5.538", "", "", "log8.55", "log0.03", "log0.03", "65.8e44", "1.6e44", "1.6e44",
                     "", "", "", "", "", "", "2494.8", "124.7", "124.7",
                     "", "", "", "", "", "", "", "", "",
                     "little red dot"]])

entry477 = np.array([["(Galaxy) J1237+6215/GOODS-N-12839", "Matthee et al. (2024)",
                     "https://iopscience.iop.org/article/10.3847/1538-4357/ad2345",
                     "JWST", "12:37:22.63", "+62:15:48.11", "",
                     "5.241", "", "", "log8.01", "log0.06", "log0.06", "31.2e44", "1.2e44", "1.2e44",
                     "", "", "", "", "", "", "1250.3", "62.5", "62.5",
                     "", "", "", "", "", "", "", "", "",
                     "little red dot"]])

entry478 = np.array([["(Galaxy) J1236+6216/GOODS-N-13733", "Matthee et al. (2024)",
                     "https://iopscience.iop.org/article/10.3847/1538-4357/ad2345",
                     "JWST", "12:36:13.70", "+62:16:08.18", "",
                     "5.236", "", "", "log7.49", "log0.10", "log0.10", "5.2e44", "0.3e44", "0.3e44",
                     "", "", "", "", "", "", "245.8", "12.3", "12.3",
                     "", "", "", "", "", "", "", "", "",
                     "little red dot"]])

entry479 = np.array([["(Galaxy) J1236+6216/GOODS-N-14409", "Matthee et al. (2024)",
                     "https://iopscience.iop.org/article/10.3847/1538-4357/ad2345",
                     "JWST", "12:36:17.30", "+62:16:24.35", "",
                     "5.139", "", "", "log7.21", "log0.14", "log0.14", "7.4e44", "0.9e44", "0.9e44",
                     "", "", "", "", "", "", "224.3", "11.2", "11.2",
                     "", "", "", "", "", "", "", "", "",
                     "little red dot"]])

entry480 = np.array([["(Galaxy) J1237+6216/GOODS-N-15498", "Matthee et al. (2024)",
                     "https://iopscience.iop.org/article/10.3847/1538-4357/ad2345",
                     "JWST", "12:37:08.53", "+62:16:50.82", "",
                     "5.086", "", "", "log7.71", "log0.11", "log0.11", "10.4e44", "1.9e44", "1.9e44",
                     "", "", "", "", "", "", "488.7", "24.4", "24.4",
                     "", "", "", "", "", "", "", "", "",
                     "little red dot"]])

entry481 = np.array([["(Galaxy) J1236+6217/GOODS-N-16813", "Matthee et al. (2024)",
                     "https://iopscience.iop.org/article/10.3847/1538-4357/ad2345",
                     "JWST", "12:36:43.03", "+62:17:33.12", "",
                     "5.355", "", "", "log7.55", "log0.12", "log0.12", "9.1e44", "1.0e44", "1.0e44",
                     "", "", "", "", "", "", "439.2", "22.0", "22.0",
                     "", "", "", "", "", "", "", "", "",
                     "little red dot"]])

entry482 = np.array([["(Galaxy) J1148+5254/J1148-7111", "Matthee et al. (2024)",
                     "https://iopscience.iop.org/article/10.3847/1538-4357/ad2345",
                     "JWST", "11:48:24.41", "+52:54:28.66", "",
                     "4.339", "", "", "log7.92", "log0.10", "log0.10", "10.8e44", "0.8e44", "0.8e44",
                     "", "", "", "", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     "little red dot"]])

entry483 = np.array([["(Galaxy) J1148+5251/J1148-18404", "Matthee et al. (2024)",
                     "https://iopscience.iop.org/article/10.3847/1538-4357/ad2345",
                     "JWST", "11:48:13.91", "+52:51:46.09", "",
                     "5.011", "", "", "log7.79", "log0.14", "log0.14", "6.9e44", "1.4e44", "1.4e44",
                     "", "", "", "", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     "little red dot"]])

entry484 = np.array([["(Galaxy) J1148+5250/J1148-21787", "Matthee et al. (2024)",
                     "https://iopscience.iop.org/article/10.3847/1538-4357/ad2345",
                     "JWST", "11:48:05.14", "+52:50:01.04", "",
                     "4.277", "", "", "log7.59", "log0.18", "log0.18", "6.7e44", "1.6e44", "1.6e44",
                     "", "", "", "", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     "little red dot"]])

entry485 = np.array([["(Galaxy) J0100+2804/J0100-2017", "Matthee et al. (2024)",
                     "https://iopscience.iop.org/article/10.3847/1538-4357/ad2345",
                     "JWST", "01:00:13.93", "+28:04:20.69", "",
                     "4.938", "", "", "log7.44", "log0.11", "log0.11", "6.7e44", "0.8e44", "0.8e44",
                     "", "", "", "", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     "little red dot"]])

entry486 = np.array([["(Galaxy) J0100+2800/J0100-12446", "Matthee et al. (2024)",
                     "https://iopscience.iop.org/article/10.3847/1538-4357/ad2345",
                     "JWST", "01:00:11.58", "+28:00:34.98", "",
                     "4.699", "", "", "log7.46", "log0.06", "log0.06", "12.9e44", "0.6e44", "0.6e44",
                     "", "", "", "", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     "little red dot"]])

entry487 = np.array([["(Galaxy) J0100+2803/J0100-15157", "Matthee et al. (2024)",
                     "https://iopscience.iop.org/article/10.3847/1538-4357/ad2345",
                     "JWST", "01:00:07.26", "+28:03:00.64", "",
                     "4.941", "", "", "log7.35", "log0.08", "log0.08", "6.5e44", "0.6e44", "0.6e44",
                     "", "", "", "", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     "little red dot"]])

entry488 = np.array([["(Galaxy) J0100+2803/J0100-16221", "Matthee et al. (2024)",
                     "https://iopscience.iop.org/article/10.3847/1538-4357/ad2345",
                     "JWST", "01:00:08.17", "+28:03:05.68", "",
                     "4.349", "", "", "log7.53", "log0.07", "log0.07", "7.1e44", "0.6e44", "0.6e44",
                     "", "", "", "", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     "little red dot"]])

entry489 = np.array([["(Galaxy) J0148+0557/J0148-976", "Matthee et al. (2024)",
                     "https://iopscience.iop.org/article/10.3847/1538-4357/ad2345",
                     "JWST", "01:48:35.08", "+05:57:20.97", "",
                     "4.163", "", "", "log7.11", "log0.18", "log0.18", "5.2e44", "0.7e44", "0.7e44",
                     "", "", "", "", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     "little red dot"]])

entry490 = np.array([["(Galaxy) J0148+0559/J0148-4214", "Matthee et al. (2024)",
                     "https://iopscience.iop.org/article/10.3847/1538-4357/ad2345",
                     "JWST", "01:48:33.29", "+05:59:50.04", "",
                     "5.019", "", "", "log7.32", "log0.10", "log0.10", "5.9e44", "0.4e44", "0.4e44",
                     "", "", "", "", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     "little red dot"]])

entry491 = np.array([["(Galaxy) J0148+0600/J0148-12884", "Matthee et al. (2024)",
                     "https://iopscience.iop.org/article/10.3847/1538-4357/ad2345",
                     "JWST", "01:48:41.58", "+06:00:57.30", "",
                     "4.602", "", "", "log6.91", "log0.15", "log0.15", "5.0e44", "0.6e44", "0.6e44",
                     "", "", "", "", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     "little red dot"]])

entry492 = np.array([["(Galaxy) J1119+0639/J1120-7546", "Matthee et al. (2024)",
                     "https://iopscience.iop.org/article/10.3847/1538-4357/ad2345",
                     "JWST", "11:19:59.86", "+06:39:17.01", "",
                     "4.967", "", "", "log7.56", "log0.11", "log0.11", "13.8e44", "1.6e44", "1.6e44",
                     "", "", "", "", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     "little red dot"]])

entry493 = np.array([["(Galaxy) J1120+0643/J1120-14389", "Matthee et al. (2024)",
                     "https://iopscience.iop.org/article/10.3847/1538-4357/ad2345",
                     "JWST", "11:20:00.89", "+06:43:10.42", "",
                     "4.897", "", "", "log7.65", "log0.07", "log0.07", "8.4e44", "0.8e44", "0.8e44",
                     "", "", "", "", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     "little red dot"]])

entry494 = np.array([["J0008+3616", "Ross et al. (2020)",
                     "https://arxiv.org/pdf/1906.06974",
                     "SDWISE", "00:08:51.43", "+36:16:13.48", "",
                     "5.17", "", "", "", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry495 = np.array([["J0012+3632", "Ross et al. (2020)",
                     "https://arxiv.org/pdf/1906.06974",
                     "SDSS", "00:12:32.88", "36:32:16.12", "",
                     "5.44", "", "", "", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry496 = np.array([["J0017-1000", "Ross et al. (2020)",
                     "https://arxiv.org/pdf/1906.06974",
                     "SDSS", "00:17:14.68", "-10:00:55.44", "",
                     "5.01", "", "", "", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry497 = np.array([["J0023-0018", "Ross et al. (2020)",
                     "https://arxiv.org/pdf/1906.06974",
                     "SDSS", "00:23:30.67", "-00:18:36.40", "",
                     "5.06", "", "", "", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry498 = np.array([["J0025-0145", "Ross et al. (2020)",
                     "https://arxiv.org/pdf/1906.06974",
                     "SDWISE", "00:25:26.84", "-01:45:32.51", "",
                     "5.07", "", "", "", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry499 = np.array([["J0031+0710", "Ross et al. (2020)",
                     "https://arxiv.org/pdf/1906.06974",
                     "SDWISE", "00:31:25.86", "+07:10:36.91", "",
                     "5.33", "", "", "", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry500 = np.array([["J0034+3759", "Ross et al. (2020)",
                     "https://arxiv.org/pdf/1906.06974",
                     "SDSS", "00:34:14.35", "37:59:53.99", "",
                     "5.63", "", "", "", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry501 = np.array([["J0026+2516", "Gloudemans et al. (2022)",
                     "https://arxiv.org/pdf/2210.01811",
                     "DESI+LoTSS", "00:26:33.61", "+25:16:53.12", "",
                     "5.06", "0.04", "0.04", "", "", "", "", "", "",
                     "", "", "", "-25.10", "0.14", "0.15", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry502 = np.array([["J0037+2410", "Gloudemans et al. (2022)",
                     "https://arxiv.org/pdf/2210.01811",
                     "DESI+LoTSS", "00:37:05.84", "+24:10:53.30", "",
                     "5.10", "0.05", "0.05", "", "", "", "", "", "",
                     "", "", "", "-26.08", "0.33", "0.04", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry503 = np.array([["J0045+2749", "Gloudemans et al. (2022)",
                     "https://arxiv.org/pdf/2210.01811",
                     "DESI+LoTSS", "00:45:31.82", "+27:49:44.28", "",
                     "5.14", "0.03", "0.03", "", "", "", "", "", "",
                     "", "", "", "-24.85", "0.17", "0.12", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry504 = np.array([["J0121+2940", "Gloudemans et al. (2022)",
                     "https://arxiv.org/pdf/2210.01811",
                     "DESI+LoTSS", "01:21:47.93", "+29:40:32.89", "",
                     "5.34", "0.02", "0.02", "", "", "", "", "", "",
                     "", "", "", "-24.27", "0.05", "0.42", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry505 = np.array([["J0912+6658", "Gloudemans et al. (2022)",
                     "https://arxiv.org/pdf/2210.01811",
                     "DESI+LoTSS", "09:12:07.64", "+66:58:46.95", "",
                     "5.62", "0.02", "0.02", "", "", "", "", "", "",
                     "", "", "", "-26.43", "0.06", "0.03", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry506 = np.array([["J0922+4815", "Gloudemans et al. (2022)",
                     "https://arxiv.org/pdf/2210.01811",
                     "DESI+LoTSS", "09:22:03.57", "+48:15:25.73", "",
                     "5.14", "0.02", "0.02", "", "", "", "", "", "",
                     "", "", "", "-26.16", "0.03", "0.14", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry507 = np.array([["J0952+6311", "Gloudemans et al. (2022)",
                     "https://arxiv.org/pdf/2210.01811",
                     "DESI+LoTSS", "09:52:29.29", "+63:11:37.83", "",
                     "5.21", "0.02", "0.02", "", "", "", "", "", "",
                     "", "", "", "-26.22", "0.52", "0.04", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry508 = np.array([["J1013+3518", "Gloudemans et al. (2022)",
                     "https://arxiv.org/pdf/2210.01811",
                     "DESI+LoTSS", "10:13:37.87", "+35:18:49.81", "",
                     "5.03", "0.04", "0.04", "", "", "", "", "", "",
                     "", "", "", "-26.05", "0.11", "0.03", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry509 = np.array([["J1037+4033", "Gloudemans et al. (2022)",
                     "https://arxiv.org/pdf/2210.01811",
                     "DESI+LoTSS", "10:37:58.18", "+40:33:28.74", "",
                     "6.07", "0.03", "0.03", "", "", "", "", "", "",
                     "", "", "", "-25.25", "0.24", "0.08", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry510 = np.array([["J1043+4048", "Gloudemans et al. (2022)",
                     "https://arxiv.org/pdf/2210.01811",
                     "DESI+LoTSS", "10:43:25.56", "+40:48:49.45", "",
                     "4.89", "0.03", "0.03", "", "", "", "", "", "",
                     "", "", "", "-26.23", "0.02", "0.02", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry511 = np.array([["J1054+4553", "Gloudemans et al. (2022)",
                     "https://arxiv.org/pdf/2210.01811",
                     "DESI+LoTSS", "10:54:04.02", "+45:53:25.31", "",
                     "5.08", "0.03", "0.03", "", "", "", "", "", "",
                     "", "", "", "-26.00", "0.02", "0.04", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry512 = np.array([["J1104+6631", "Gloudemans et al. (2022)",
                     "https://arxiv.org/pdf/2210.01811",
                     "DESI+LoTSS", "11:04:55.18", "+66:31:18.62", "",
                     "5.03", "0.06", "0.06", "", "", "", "", "", "",
                     "", "", "", "-26.72", "0.02", "0.01", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry513 = np.array([["J1330+6224", "Gloudemans et al. (2022)",
                     "https://arxiv.org/pdf/2210.01811",
                     "DESI+LoTSS", "13:30:28.26", "+62:24:12.28", "",
                     "5.43", "0.02", "0.02", "", "", "", "", "", "",
                     "", "", "", "-26.25", "0.04", "0.08", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry514 = np.array([["J1334+4750", "Gloudemans et al. (2022)",
                     "https://arxiv.org/pdf/2210.01811",
                     "DESI+LoTSS", "13:34:22.64", "+47:50:33.50", "",
                     "4.99", "0.03", "0.03", "", "", "", "", "", "",
                     "", "", "", "-27.02", "0.01", "0.01", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry515 = np.array([["J1401+4542", "Gloudemans et al. (2022)",
                     "https://arxiv.org/pdf/2210.01811",
                     "DESI+LoTSS", "14:01:20.86", "+45:42:53.46", "",
                     "5.45", "0.04", "0.04", "", "", "", "", "", "",
                     "", "", "", "-25.50", "0.03", "0.03", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry516 = np.array([["J1419+5718", "Gloudemans et al. (2022)",
                     "https://arxiv.org/pdf/2210.01811",
                     "DESI+LoTSS", "14:19:56.58", "+57:18:40.41", "",
                     "5.35", "0.04", "0.04", "", "", "", "", "", "",
                     "", "", "", "-25.77", "0.08", "0.04", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry517 = np.array([["J1523+2935", "Gloudemans et al. (2022)",
                     "https://arxiv.org/pdf/2210.01811",
                     "DESI+LoTSS", "15:23:30.67", "+29:35:39.67", "",
                     "5.74", "0.03", "0.03", "", "", "", "", "", "",
                     "", "", "", "-26.32", "0.02", "0.02", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry518 = np.array([["J1601+3102", "Gloudemans et al. (2022)",
                     "https://arxiv.org/pdf/2210.01811",
                     "DESI+LoTSS", "16:01:49.45", "+31:02:07.25", "",
                     "4.90", "0.02", "0.02", "", "", "", "", "", "",
                     "", "", "", "-24.75", "0.31", "0.21", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry519 = np.array([["J1650+5457", "Gloudemans et al. (2022)",
                     "https://arxiv.org/pdf/2210.01811",
                     "DESI+LoTSS", "16:50:51.75", "+54:57:01.38", "",
                     "6.06", "0.02", "0.02", "", "", "", "", "", "",
                     "", "", "", "-26.56", "0.04", "0.08", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry520 = np.array([["J2201+2338", "Gloudemans et al. (2022)",
                     "https://arxiv.org/pdf/2210.01811",
                     "DESI+LoTSS", "22:01:07.61", "+23:38:37.95", "",
                     "5.83", "0.02", "0.02", "", "", "", "", "", "",
                     "", "", "", "-26.24", "0.06", "0.11", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry521 = np.array([["J2327+2454", "Gloudemans et al. (2022)",
                     "https://arxiv.org/pdf/2210.01811",
                     "DESI+LoTSS", "23:27:26.89", "+24:54:10.93", "",
                     "5.30", "0.03", "0.03", "", "", "", "", "", "",
                     "", "", "", "-26.07", "0.02", "0.05", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])

entry522 = np.array([["J2336+1842", "Gloudemans et al. (2022)",
                     "https://arxiv.org/pdf/2210.01811",
                     "DESI+LoTSS", "23:36:24.69", "+18:42:48.71", "",
                     "6.60", "0.04", "0.04", "", "", "", "", "", "",
                     "", "", "", "-24.32", "0.13", "-1.44", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])


columnNames = ["Name", "Ref",
               "Link",
               "Inst", "RA", "DEC", "Distance",
               "z", "+dz", "-dz", "M [M_sun]", "+dM", "-dM", "L_bol [erg/s]", "+dL_bol", "-dL_bol",
               "f_Edd", "+df_Edd", "-df_Edd", "M1450", "+dM1450", "-dM1450", "F444W", "+dF44W", "-dF444W",
               "SFR_CII", "+dSFR_CII", "-dSFR_CII", "SFR_TIR", "+dSFR_TIR", "-dSFR_TIR", "Mstar [M_sun]", "+dMstar", "-dMstar",
               "comment"]

'''

This section includes black holes with z < 4, the data within should be ignored:

entry48 = np.array([["J0529-4351", "Wolf et al. (2024), Onken et al. (2023)",
                     "https://arxiv.org/abs/2402.15101, https://arxiv.org/pdf/2209.09342",
                     "SMSS", "05h29m15.82s", "-43°51′52.″20", "",
                     "3.962", "", "", "1.738e10", "8.19e8", "7.82e8", "1.862e48", "2.759e47", "2.403e47",
                     "", "", "", "", "", "", "", "", "",
                     "", "", "", "", "", "", "",
                     "use best estimate results"]])

# coordinates from: https://arxiv.org/pdf/2209.09342 Onken et al. (2023)

entry49 = np.array([["J1144-4308", "Onken et al. (2022)", "https://arxiv.org/abs/2206.04204",
                     "0.8314", "0.0001", "0.0001", "2.6e9", "5.62e9", "1.78e9", "4.7e47", "1e47",
                     "1e47", "1.4", "", "", ""]])

entry50 = np.array([["3C 273 (J1229+0203)", "Peterson et al. (2004)",
                     "https://arxiv.org/abs/astro-ph/0407299",
                     "", "0.158", "", "", "8.86e8", "1.87e8",
                     "1.87e8", "8.21e46", "1.00e46", "8.93e45", "", "", "", "Lbol = 9 λ Lλ"]])

'''

'''

entry = np.array([["", "",
                     "",
                     "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     ""]])


'''

# Inayoshi et al. (2019) All-clear
# Shen et al. (2019) All-clear

# Banados et al. (2016) All-clear

# Look for LRDs if time permits: https://iopscience.iop.org/article/10.3847/1538-4357/ad9920
import numpy as np

# Tool to help convert RA DEC coordinates: https://www.astrouw.edu.pl/~jskowron/ra-dec/?q=d++53.12654+-27.81809

# Arrays are manually populated to include or amend information
# 1a. Some bolometric luminosities need to be converted from units of solar luminosities to ergs per second (1 solar luminosity = 3.846e33 ergs per second)
# 1b. This can be done by adding "S" to the end of the bolometric luminosity
# 2a. Some entries lack a documented black hole mass and is approximated by the formula 10 ** ((-M1450 -3.459) / 2.5)
# 2b. This is done automatically without any input

entry0 = np.array([["J1342+0928", "Banados et al. (2018), Venemans et al. (2017), Onoue et al. (2020), Novak et al. (2019), Yang et al. (2021)",
                    "https://arxiv.org/abs/1712.01860, https://iopscience.iop.org/article/10.3847/2041-8213/aa943a, https://arxiv.org/pdf/2006.16268, https://iopscience.iop.org/article/10.3847/1538-4357/ab2beb, https://iopscience.iop.org/article/10.3847/1538-4357/ac2b32",
                    "ULAS", "13:42:08.097", "+09:28:38.28", "",
                    "7.5413", "0.0007", "0.0007", "9.1e8", "1.4e8", "1.3e8", "13.3e46", "1.1e46", "1.1e46",
                    "1.1", "0.2", "0.2", "-26.57", "0.04", "0.04", "", "", "",
                    "", "", "", "150", "30", "30", "",
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
                    "220", "8", "8", "742", "16", "16", "",
                    "z, SFR from Izumi et al. (2021)"]])

# What does the b in 2019b mean? Have to keep it?
# Updated (newer) redshift and SFR from: https://arxiv.org/pdf/2104.05738### Izumi et al. (2021) pg.6

entry2 = np.array([["J1120+0641", "Mortlock et al.(2011), De Rosa et al. (2014), Yang et al. (2021)",
                    "https://arxiv.org/abs/1106.6088, https://arxiv.org/pdf/1311.3260, https://iopscience.iop.org/article/10.3847/1538-4357/ac2b32",
                    "ULAS", "11:20:01.48", "+06:41:24.30", "",
                    "7.0851", "0.0005", "0.0005", "1.35e9", "0.04e9", "0.04e9", "13.4e46", "1.0e46", "1.0e46",
                    "0.8", "0.1", "0.1", "-26.44", "", "", "", "", "",
                    "", "", "", "", "", "", "",
                    "coordinates from De Rosa et al. (2014), z, M1450, M, L_bol from Yang et al. (2021)"]])

# Coordinates found from: https://arxiv.org/pdf/1311.3260 De Rosa et al. (2014)
# Redshift, M1450, M, L_bol, f_Edd from: https://iopscience.iop.org/article/10.3847/1538-4357/ac2b32 Yang et al. (2021)

entry3 = np.array([["J0038-1527", "Wang et al. (2018)",
                    "https://arxiv.org/abs/1810.11925",
                    "DELS", "00:38:36.10", "-15:27:23.06", "",
                    "7.021", "0.005", "0.005", "1.33e9", "0.25e9", "0.25e9", "2.16e47", "", "",
                    "1.25", "0.19", "0.19", "-27.10", "0.08", "0.08", "", "", "",
                    "", "", "", "", "", "", "",
                    ""]])

entry4 = np.array([["J0252-0503", "Yang et al. (2019), Wang et al (2020)",
                    "https://iopscience.iop.org/article/10.3847/1538-3881/ab1be1/meta, https://arxiv.org/abs/2004.10877",
                    "DES", "02:52:16.64", "-05:03:31.80", "",
                    "7.02", "0.001", "0.001", "1.39e9", "1.6e8", "1.6e8", "1.3e47", "0.1e47", "0.1e47",
                    "0.7", "0.1", "0.1", "-26.50", "0.09", "0.09", "", "", "",
                    "", "", "", "", "", "", "",
                    "M1450 from Yang et al. (2019), z from Wang et al (2020)"]])

# M1450 from: https://iopscience.iop.org/article/10.3847/1538-3881/ab1be1/meta Yang et al. (2019)
# z from: https://arxiv.org/abs/2004.10877 Wang et al (2020)

entry5 = np.array([["J2356+0017", "Matsuoka et al. (2019)",
                    "https://arxiv.org/abs/1908.07910",
                    "HSC", "23:56:46.33", "+00:17:47.30", "",
                    "7.01", "", "", "5.5e8", "2.06e7", "1.99e7", "", "", "",
                    "", "", "", "-25.31", "0.04", "0.04", "", "", "",
                    "", "", "", "", "", "", "",
                    ""]])

# Currently unsure where the mass comes from

entry6 = np.array([["J0313−1806", "Wang et al. (2021)",
                    "https://arxiv.org/abs/2101.03179",
                    "PS1+DELS+VHS+WISE", "03:13:43.84", "-18:06:36.40", "",
                    "7.6423", "0.0013", "0.0013", "1.6e9", "0.4e9", "0.4e9", "1.4e47", "0.1e47", "0.1e47",
                    "0.67", "0.14", "0.14", "-26.13", "0.05", "0.05", "", "", "",
                    "40-240", "", "", "225", "25", "25", "",
                    ""]])

entry7 = np.array([["J1007+2115", "Yang et al. (2020)",
                    "https://arxiv.org/abs/2006.13452",
                    "PS1+DELS+UHS+WISE", "10:07:58.26", "+21:15:29.20", "",
                    "7.5149", "0.0004", "0.0004", "1.5e9", "0.2e9", "0.2e9", "1.9e47", "0.1e47", "0.1e47",
                    "1.06", "0.2", "0.2", "-26.66", "0.07", "0.07", "", "", "",
                    "80-520", "", "", "700", "", "", "",
                    ""]])

entry8 = np.array([["UHZ1", "Bogdan et al. (2023), Castellano et al. (2023), Goulding et al. (2023)",
                    "https://arxiv.org/abs/2305.15458, https://iopscience.iop.org/article/10.3847/2041-8213/accea5/meta, https://arxiv.org/pdf/2308.02750",
                    "JWST", "00:14:16.096", "-30:22:40.285", "",
                    "10.073", "0.002", "0.002", "4e7", "6e7", "3e7", "5e45", "", "",
                    "", "", "", "", "", "", "87.7", "7.2", "7.2",
                    "4.5", "2.9", "2.2", "4.5", "2.9", "2.2", "0.4e8",
                    "F444W, SFR, Mstar from Castellano et al. (2023), z from Goulding et al. (2023)"]])

# F444W, SFR, Mstar from: https://iopscience.iop.org/article/10.3847/2041-8213/accea5/meta Castellano et al. (2023)
# z from: https://arxiv.org/pdf/2308.02750 Goulding et al. (2023)

entry9 = np.array([["GHZ9", "Kovacs et al. (2024), Castellano et al. (2023), Atek et al. (2023)",
                    "https://arxiv.org/abs/2403.14745, https://iopscience.iop.org/article/10.3847/2041-8213/accea5/meta, https://arxiv.org/pdf/2305.01793",
                    "JWST", "00:13:54.90", "-30:20:43.93", "",
                    "10.37", "0.32", "1.09", "8e7", "3.7e7", "3.2e7", "1e46", "0.5e46", "0.4e46",
                    "", "", "", "", "", "", "40.9", "3.9", "3.9",
                    "", "", "", "", "", "", "3.3e8",
                    "F444W, Mstar, SFR [14.4 (+15.0/-7.3)] from Castellano et al. (2023), SFR [0.56 (+0.23/-0.29)] from Atek et al. (2023)"]])

# F444W, Mstar, SFR from: https://iopscience.iop.org/article/10.3847/2041-8213/accea5/meta Castellano et al. (2023)
# SFR from: https://arxiv.org/pdf/2305.01793 Atek et al. (2023)

entry10 = np.array([["GNz11", "Maiolino et al. (2023), Bunker et al. (2023), Oesch et al. (2016)",
                     "https://arxiv.org/abs/2305.12492, https://arxiv.org/pdf/2302.07256, https://arxiv.org/pdf/1603.00461",
                     "JWST", "12:36:25.46", "+62:14:31.40", "",
                     "10.6", "", "", "1.6e6", "1e0.3", "1e0.3", "1.08e45", "", "",
                     "", "", "", "", "", "", "", "", "",
                     "31", "59", "19", "31", "59", "19", "",
                     "SFR from Bunker et al. (2023), coordinates from Oesch et al. (2016)"]])

# SFR from: https://arxiv.org/pdf/2302.07256 Bunker et al. (2023)
# Coordinates from: https://arxiv.org/pdf/1603.00461 Oesch et al. (2016)

entry11 = np.array([["CEERS_1019", "Larson et al. (2023)",
                     "https://arxiv.org/abs/2303.08918",
                     "JWST", "14:20:08.49", "+52:53:26.38", "",
                     "8.679", "0.09", "0.15", "log6.95", "log0.37", "log0.37", "log45.1", "log0.2", "log0.2",
                     "1.2", "0.5", "0.5", "", "", "", "", "", "",
                     "30", "", "", "30", "", "", "",
                     ""]])

entry12 = np.array([["J1205−0000", "Onoue et al. (2019), Sawamura et al. (2025), Izumi et al. (2021)",
                     "https://arxiv.org/abs/1904.07278, https://arxiv.org/pdf/2502.16858, https://iopscience.iop.org/article/10.3847/1538-4357/abd7ef",
                     "HSC", "12:05:05.09", "-00:00:27.90", "",
                     "6.7230", "0.0003", "0.0003", "2.2e9", "0.2e9", "0.6e9", "", "", "",
                     "0.16", "0.04", "0.02", "-24.56", "0.04", "0.04", "", "", "",
                     "122", "5", "5", "528", "8", "8", "",
                     ""]])

# SFR_TIR from: https://arxiv.org/pdf/2502.16858 Sawamura et al. (2025)
# z, SFR_CII from: https://iopscience.iop.org/article/10.3847/1538-4357/abd7ef Izumi et al. (2021)

entry13 = np.array([["J2239+0207", "Onoue et al. (2019), Ishimoto et al. (2020)",
                     "https://arxiv.org/abs/1904.07278, https://iopscience.iop.org/article/10.3847/1538-4357/abb80b/pdf",
                     "HSC", "22:39:47.47", "+02:07:47.50", "",
                     "6.245", "0.008", "0.007", "1.1e9", "0.3e9", "0.2e9", "", "", "",
                     "0.17", "0.04", "0.05", "-24.69", "0.04", "0.04", "", "", "",
                     "", "", "", "", "", "", "",
                     "coordinates from Ishimoto et al. (2020)"]])

# coordinates from: https://iopscience.iop.org/article/10.3847/1538-4357/abb80b/pdf Ishimoto et al. (2020)

entry14 = np.array([["J2216−0016", "Onoue et al. (2019), Ishimoto et al. (2020)",
                     "https://arxiv.org/abs/1904.07278, https://iopscience.iop.org/article/10.3847/1538-4357/abb80b/pdf",
                     "HSC", "22:16:44.47", "-00:16:50.10", "",
                     "6.109", "0.007", "0.008", "0.7e9", "0.14e9", "0.23e9", "", "", "",
                     "0.15", "0.05", "0.03", "-23.82", "0.04", "0.04", "", "", "",
                     "", "", "", "", "", "", "",
                     "coordinates from Ishimoto et al. (2020)"]])

# coordinates from: https://iopscience.iop.org/article/10.3847/1538-4357/abb80b/pdf Ishimoto et al. (2020)

entry15 = np.array([["J1208−0200", "Onoue et al. (2019), Ishimoto et al. (2020)",
                     "https://arxiv.org/abs/1904.07278, https://iopscience.iop.org/article/10.3847/1538-4357/abb80b/pdf",
                     "HSC", "12:08:59.23", "-02:00:34.80", "",
                     "6.144", "0.008", "0.01", "0.71e9", "0.24e9", "0.52e9", "", "", "",
                     "0.24", "0.18", "0.08", "-24.73", "0.02", "0.02", "", "", "",
                     "", "", "", "", "", "", "",
                     "coordinates from Ishimoto et al. (2020)"]])

# coordinates from: https://iopscience.iop.org/article/10.3847/1538-4357/abb80b/pdf Ishimoto et al. (2020)

entry16 = np.array([["J0100+2802", "Wu et al. (2015), D'Odorico et al. (2023), Venemans et al. (2020), Mazzucchelli et al. (2023)",
                     "https://arxiv.org/abs/1502.07418, https://academic.oup.com/mnras/article/523/1/1399/7172883, https://iopscience.iop.org/article/10.3847/1538-4357/abc563, https://arxiv.org/pdf/2306.16474",
                     "SDSS", "01:00:13.02", "+28:02:25.80", "",
                     "6.3269", "0.0002", "0.0002", "log10.1", "log0.2", "log0.1", "log48.15", "log0.04", "log0.04",
                     "0.99", "0.22", "0.22", "-29.26", "0.20", "0.20", "", "", "",
                     "", "", "", "", "", "", "",
                     "coordinates from D'Odorico et al. (2023), distance, z from Venemans et al. (2020), mass, L_bol from Mazzucchelli et al. (2023)"]])

# coordinates from: https://academic.oup.com/mnras/article/523/1/1399/7172883 D'Odorico et al. (2023)
# distance, z from: https://iopscience.iop.org/article/10.3847/1538-4357/abc563 Venemans et al. (2020)
# mass, L_bol from: https://arxiv.org/pdf/2306.16474 Mazzucchelli et al. (2023)

entry17 = np.array([["J158–14", "Eilers et al. (2020)",
                     "https://arxiv.org/abs/2002.01811",
                     "PSO", "10:34:46.509", "-14:25:15.855", "",
                     "6.052", "0.001", "0.001", "1.57e9", "0.12e9", "0.12e9", "2.04e47", "", "",
                     "1.01", "0.08", "0.08", "-27.41", "", "", "", "", "",
                     "230", "", "", "", "", "", "",
                     ""]])

entry18 = np.array([["J0330–4025", "Eilers et al. (2020), Reed et al. (2017)",
                     "https://arxiv.org/abs/2002.01811, https://academic.oup.com/mnras/article/468/4/4702/3089747",
                     "VDES", "03:30:27.920", "-40:25:16.200", "",
                     "6.239", "0.004", "0.004", "4.96e9", "0.51e9", "0.51e9", "8.91e46", "", "",
                     "0.14", "0.01", "0.01", "-26.42", "0.06", "0.06", "", "", "",
                     "", "", "", "", "", "", "",
                     "M1450 from Reed et al. (2017)"]])

# M1450 from: https://academic.oup.com/mnras/article/468/4/4702/3089747 Reed et al. (2017)

entry19 = np.array([["J2100–1715", "Eilers et al. (2020)",
                     "https://arxiv.org/abs/2002.01811",
                     "CFHQS", "21:00:54.616", "-17:15:22.500", "",
                     "6.082", "0.002", "0.002", "2.18e9", "0.21e9", "0.21e9", "4.37e46", "", "",
                     "0.15", "0.02", "0.02", "-25.55", "", "", "", "", "",
                     "170", "", "", "", "", "", "",
                     ""]])

entry20 = np.array([["J2229+1457", "Eilers et al. (2020), Willott et al. (2015)",
                     "https://arxiv.org/abs/2002.01811, https://iopscience.iop.org/article/10.1088/0004-637X/801/2/123#apj509348t2",
                     "CFHQS", "22:29:01.649", "+14:57:08.980", "",
                     "6.144", "0.006", "0.006", "1.44e9", "0.25e9", "0.25e9", "2.29e46", "", "",
                     "0.12", "0.02", "0.02", "-24.78", "", "", "", "", "",
                     "60", "8", "8", "19", "10", "10", "",
                     "SFR from Willott et al. (2015)"]])

# SFR from: https://iopscience.iop.org/article/10.1088/0004-637X/801/2/123#apj509348t2 Willott et al. (2015)

entry21 = np.array([["J004+17", "Eilers et al. (2020), ",
                     "https://arxiv.org/abs/2002.01811",
                     "PSO", "00:17:34.467", "+17:05:10.696", "",
                     "5.8165", "0.0023", "0.0023", "1.05e9", "", "", "", "", "",
                     "", "", "", "-26.01", "", "", "", "", "",
                     "20", "", "", "", "", "", "",
                     ""]])

entry22 = np.array([["J1335+3533", "Eilers et al. (2018), Ishimoto et al. (2020)",
                     "https://arxiv.org/abs/1806.05691, https://iopscience.iop.org/article/10.3847/1538-4357/abb80b/pdf",
                     "SDSS", "13:35:50.81", "+35:33:15.82", "",
                     "5.9012", "0.0019", "0.0019", "4.09e9", "0.58e9", "0.58e9", "1.62e47", "0.03e47", "0.03e47",
                     "0.30", "0.04", "0.04", "-26.67", "", "", "", "", "",
                     "", "", "", "", "", "", "",
                     "coordinates from Ishimoto et al. (2020)"]])

# coordinates from: https://iopscience.iop.org/article/10.3847/1538-4357/abb80b/pdf Ishimoto et al. (2020)

entry23 = np.array([["954", "Maiolino et al. (2024), Juodžbalis et al. (2025)",
                     "https://arxiv.org/abs/2308.01230, https://arxiv.org/html/2504.03551v1",
                     "JWST", "12:36:36.47", "+62:15:34.70", "",
                     "6.759", "", "", "log7.74", "log0.31", "log0.32", "log45.24", "log0.15", "log0.17",
                     "0.25", "0.05", "0.05", "", "", "", "", "", "",
                     "", "", "", "", "", "", "log10.66",
                     "coordinates, z, mass, L_bol, f_Edd from Juodžbalis et al. (2025)"]])

# coordinates, z, mass, L_bol, f_Edd from: https://arxiv.org/html/2504.03551v1 Juodžbalis et al. (2025)

entry24 = np.array([["1093", "Maiolino et al. (2024), Juodžbalis et al. (2025)",
                     "https://arxiv.org/abs/2308.01230, https://arxiv.org/html/2504.03551v1",
                     "JWST", "12:36:43.14", "+62:13:28.67", "",
                     "5.594", "", "", "log7.07", "log0.34", "log0.33", "log44.52", "log0.18", "log0.16",
                     "0.15", "0.06", "0.04", "", "", "", "", "", "",
                     "", "", "", "", "", "", "log8.34",
                     "coordinates, z, mass, L_bol, f_Edd from Juodžbalis et al. (2025)"]])

# coordinates, z, mass, L_bol, f_Edd from: https://arxiv.org/html/2504.03551v1 Juodžbalis et al. (2025)

entry25 = np.array([["3608", "Maiolino et al. (2024)",
                     "https://arxiv.org/abs/2308.01230",
                     "JWST", "", "", "",
                     "5.26894", "", "", "6.60693e6", "9.242e6", "3.51664e6", "1.e44", "", "",
                     "0.11", "", "", "", "", "", "", "", "",
                     "", "", "", "", "", "", "log8.38",
                     "tentative source according to https://arxiv.org/html/2504.03551v1 Juodžbalis et al. (2025)"]])

entry26 = np.array([["8083", "Maiolino et al. (2024), Juodžbalis et al. (2025)",
                     "https://arxiv.org/abs/2308.01230, https://arxiv.org/html/2504.03551v1",
                     "JWST", "03:32:31.88", "-27:48:06.70", "",
                     "4.753", "", "", "log7.11", "log0.31", "log0.31", "log44.06", "log0.05", "log0.05",
                     "0.07", "0.01", "0.01", "", "", "", "", "", "",
                     "", "", "", "", "", "", "log8.45",
                     "coordinates, z, mass, L_bol, f_Edd from Juodžbalis et al. (2025)"]])

# coordinates, z, mass, L_bol, f_Edd from: https://arxiv.org/html/2504.03551v1 Juodžbalis et al. (2025)

entry27 = np.array([["11836", "Maiolino et al. (2024), Juodžbalis et al. (2025)",
                     "https://arxiv.org/abs/2308.01230, https://arxiv.org/html/2504.03551v1",
                     "JWST", "12:36:52.94", "+62:15:49.25", "",
                     "4.409", "", "", "log7.00", "log0.32", "log0.32", "log44.20", "log0.05", "log0.05",
                     "0.13", "0.03", "0.02", "", "", "", "", "", "",
                     "", "", "", "", "", "", "log7.79",
                     "coordinates, z, mass, L_bol, f_Edd from Juodžbalis et al. (2025)"]])

# coordinates, z, mass, L_bol, f_Edd from: https://arxiv.org/html/2504.03551v1 Juodžbalis et al. (2025)

entry28 = np.array([["20621", "Maiolino et al. (2024), Juodžbalis et al. (2025)",
                     "https://arxiv.org/abs/2308.01230, https://arxiv.org/html/2504.03551v1",
                     "JWST", "12:36:29.40", "+62:17:34.26", "",
                     "4.682", "", "", "log7.09", "log0.35", "log0.34", "log44.24", "log0.23", "log0.19",
                     "0.11", "0.06", "0.03", "", "", "", "", "", "",
                     "", "", "", "", "", "", "log8.06",
                     "coordinates, z, mass, L_bol, f_Edd from Juodžbalis et al. (2025)"]])

# coordinates, z, mass, L_bol, f_Edd from: https://arxiv.org/html/2504.03551v1 Juodžbalis et al. (2025)

entry29 = np.array([["53757", "Maiolino et al. (2024), Juodžbalis et al. (2025)",
                     "https://arxiv.org/abs/2308.01230, https://arxiv.org/html/2504.03551v1",
                     "JWST", "12:37:04.75", "+62:11:39.16", "",
                     "4.447", "", "", "log7.33", "log0.31", "log0.31", "log44.29", "log0.02", "log0.02",
                     "0.07", "0.01", "0.009", "", "", "", "", "", "",
                     "", "", "", "", "", "", "log10.18",
                     "coordinates, z, mass, L_bol, f_Edd from Juodžbalis et al. (2025)"]])

# coordinates, z, mass, L_bol, f_Edd from: https://arxiv.org/html/2504.03551v1 Juodžbalis et al. (2025)

entry30 = np.array([["61888", "Maiolino et al. (2024), Juodžbalis et al. (2025)",
                     "https://arxiv.org/abs/2308.01230, https://arxiv.org/html/2504.03551v1",
                     "JWST", "12:36:40.32", "+62:13:01.24", "",
                     "5.874", "", "", "log7.08", "log0.33", "log0.32", "log44.46", "log0.13", "log0.10",
                     "0.20", "0.06", "0.03", "", "", "", "", "", "",
                     "", "", "", "", "", "", "log8.11",
                     "coordinates, z, mass, L_bol, f_Edd from Juodžbalis et al. (2025)"]])

# coordinates, z, mass, L_bol, f_Edd from: https://arxiv.org/html/2504.03551v1 Juodžbalis et al. (2025)

entry31 = np.array([["62309", "Maiolino et al. (2024), Juodžbalis et al. (2025)",
                     "https://arxiv.org/abs/2308.01230, https://arxiv.org/html/2504.03551v1",
                     "JWST", "12:36:59.76", "+62:13:06.06", "",
                     "5.172", "", "", "log6.30", "log0.36", "log0.33", "log43.57", "log0.13", "log0.12",
                     "0.15", "0.05", "0.05", "", "", "", "", "", "",
                     "", "", "", "", "", "", "log8.12",
                     "coordinates, z, mass, L_bol, f_Edd from Juodžbalis et al. (2025)"]])

# coordinates, z, mass, L_bol, f_Edd from: https://arxiv.org/html/2504.03551v1 Juodžbalis et al. (2025)

entry32 = np.array([["73488", "Maiolino et al. (2024), Juodžbalis et al. (2025)",
                     "https://arxiv.org/abs/2308.01230, https://arxiv.org/html/2504.03551v1",
                     "JWST", "12:36:47.38", "+62:10:38.03", "",
                     "4.133", "", "", "log7.95", "log0.30", "log0.30", "log45.45", "log0.07", "log0.05",
                     "0.25", "0.02", "0.02", "", "", "", "", "", "",
                     "", "", "", "", "", "", "log9.78",
                     "coordinates, z, mass, L_bol, f_Edd from Juodžbalis et al. (2025)"]])

# coordinates, z, mass, L_bol, f_Edd from: https://arxiv.org/html/2504.03551v1 Juodžbalis et al. (2025)

entry33 = np.array([["77652", "Maiolino et al. (2024), Juodžbalis et al. (2025)",
                     "https://arxiv.org/abs/2308.01230, https://arxiv.org/html/2504.03551v1",
                     "JWST", "12:37:10.38", "+62:11:56.40", "",
                     "5.229", "", "", "log6.62", "log0.34", "log0.32", "log44.11", "log0.04", "log0.05",
                     "0.24", "0.09", "0.08", "", "", "", "", "", "",
                     "", "", "", "", "", "", "log7.87",
                     "coordinates, z, mass, L_bol, f_Edd from Juodžbalis et al. (2025)"]])

# coordinates, z, mass, L_bol, f_Edd from: https://arxiv.org/html/2504.03551v1 Juodžbalis et al. (2025)

entry34 = np.array([["10013704", "Maiolino et al. (2024), Juodžbalis et al. (2025)",
                     "https://arxiv.org/abs/2308.01230, https://arxiv.org/html/2504.03551v1",
                     "JWST", "03:32:30.37", "-27:49:05.12", "",
                     "5.919", "", "", "log7.44", "log0.31", "log0.31", "log44.29", "log0.02", "log0.02",
                     "0.055", "0.007", "0.006", "", "", "", "", "", "",
                     "", "", "", "", "", "", "log8.88",
                     "coordinates, z, mass, L_bol, f_Edd from Juodžbalis et al. (2025)"]])

# coordinates, z, mass, L_bol, f_Edd from: https://arxiv.org/html/2504.03551v1 Juodžbalis et al. (2025)

entry35 = np.array([["GS_3073", "Ubler et al. (2023), Barchiesi et al. (2022)",
                     "https://arxiv.org/abs/2302.06647, https://arxiv.org/pdf/2212.00038",
                     "JWST", "03:32:18.93", "-27:53:02.96", "",
                     "5.55", "", "", "1.58489e8", "2.39618e8", "9.53936e7", "5.0e45", "1.08e46", "3.43e45",
                     "0.25", "1.35", "0.15", "", "", "", "", "", "",
                     "16", "14", "7", "", "", "", "",
                     "use H-alpha for mass, use geometric mean of two method for L_bol, SFR [90 (+30/-30)] from Barchiesi et al. (2022)"]])

# SFR from: https://arxiv.org/pdf/2212.00038 Barchiesi et al. (2022)

entry36 = np.array([["CEERS_01244", "Harikane et al. (2023)",
                     "https://arxiv.org/pdf/2303.11946",
                     "JWST", "14:20:57.76", "+53:02:09.80", "",
                     "4.478", "", "", "3.2e7", "0.3e7", "0.2e7", "1.9e45", "3.8e45", "0.6e45",
                     "0.46", "1.04", "0.16", "", "", "", "", "", "",
                     "", "", "", "", "", "", "",
                     ""]])

entry37 = np.array([["GLASS_160133", "Harikane et al. (2023)",
                     "https://arxiv.org/pdf/2303.11946",
                     "JWST", "00:14:19.27", "-30:25:27.80", "",
                     "4.015", "", "", "2.3e6", "0.1e6", "0.1e6", "1.1e45", "6.1e45", "0.9e45",
                     "3.68", "21.21", "2.84", "", "", "", "", "", "",
                     "", "", "", "", "", "", "",
                     ""]])

entry38 = np.array([["GLASS_150029", "Harikane et al. (2023)",
                     "https://arxiv.org/pdf/2303.11946",
                     "JWST", "00:14:18.52", "-30:25:21.30", "",
                     "4.583", "", "", "3.7e6", "0.2e6", "0.3e6", "9.1e44", "13.8e44", "7.1e44",
                     "1.89", "3.31", "1.49", "", "", "", "", "", "",
                     "", "", "", "", "", "", "",
                     ""]])

entry39 = np.array([["CEERS_00746", "Harikane et al. (2023)",
                     "https://arxiv.org/pdf/2303.11946",
                     "JWST", "14:19:14.19", "+52:52:06.05", "",
                     "5.624", "", "", "5.8e7", "1.5e7", "1.3e7", "1.1e46", "0.1e46", "0.2e46",
                     "1.47", "0.60", "0.52", "", "", "", "", "", "",
                     "", "", "", "", "", "", "",
                     ""]])

entry40 = np.array([["CEERS_01665", "Harikane et al. (2023)",
                     "https://arxiv.org/pdf/2303.11946",
                     "JWST", "14:20:42.77", "+53:03:33.07", "",
                     "4.483", "", "", "1.9e7", "0.8e7", "0.5e7", "4.8e45", "7.2e45", "3.6e45",
                     "1.93", "4.61", "1.59", "", "", "", "", "", "",
                     "", "", "", "", "", "", "",
                     ""]])

entry41 = np.array([["CEERS_00672", "Harikane et al. (2023)",
                     "https://arxiv.org/pdf/2303.11946",
                     "JWST", "14:19:33.52", "+52:49:58.07", "",
                     "5.666", "", "", "5.0e7", "1.7e7", "1.3e7", "4.3e45", "0.4e45", "1.4e45",
                     "0.65", "0.31", "0.33", "", "", "", "", "", "",
                     "", "", "", "", "", "", "",
                     ""]])

entry42 = np.array([["CEERS_02782", "Harikane et al. (2023)",
                    "https://arxiv.org/pdf/2303.11946",
                     "JWST", "14:19:17.63", "+52:49:49.00", "",
                     "5.241", "", "", "4.2e7", "1.2e7", "1.0e7", "2.8e45", "2.3e45", "1.4e45",
                     "0.51", "0.71", "0.32", "", "", "", "", "", "",
                     "", "", "", "", "", "", "",
                     ""]])

entry43 = np.array([["CEERS_00397", "Harikane et al. (2023)",
                     "https://arxiv.org/pdf/2303.11946",
                     "JWST", "14:19:20.69", "+52:52:57.07", "",
                     "6.000", "", "", "1.0e7", "0.8e7", "0.5e7", "2.8e45", "14.2e45", "2.2e45",
                     "2.02", "20.68", "1.80", "", "", "", "", "", "",
                     "", "", "", "", "", "", "",
                     ""]])

entry44 = np.array([["CEERS_00717", "Harikane et al. (2023)",
                     "https://arxiv.org/pdf/2303.11946",
                     "JWST", "14:20:19.54", "+52:58:19.09", "",
                     "6.936", "", "", "9.8e7", "4.4e7", "3.2e7", "7.1e44", "51.8e44", "4.3e44",
                     "0.06", "0.63", "0.04", "", "", "", "", "", "",
                     "", "", "", "", "", "", "",
                     ""]])

entry45 = np.array([["CEERS_01236", "Harikane et al. (2023)",
                     "https://arxiv.org/pdf/2303.11946",
                     "JWST", "14:20:34.87", "+52:58:02.02", "",
                     "4.484", "", "", "1.8e7", "1.0e7", "0.6e7", "1.8e44", "2.6e44", "0.5e44",
                     "0.08", "0.20", "0.04", "", "", "", "", "", "",
                     "", "", "", "", "", "", "",
                     ""]])

entry46 = np.array([["J172+18", "Banados et al. (2021)",
                     "https://www.mpg.de/16498963/mpia-pr_banados_quasar_2021_preprint.pdf",
                     "PSO", "11:29:25.37", "+18:46:24.29", "",
                     "6.823", "0.003", "0.001", "2.9e8", "0.7e8", "0.6e8", "6.5e46", "", "",
                     "2.2", "0.6", "0.4", "-25.81", "0.10", "0.10", "", "", "",
                     "", "", "", "", "", "", "",
                     ""]])

entry47 = np.array([["J2157-3602", "Wolf et al. (2018), Onken et al. (2020), Lai et al. (2023)",
                     "https://arxiv.org/abs/1805.04317, https://arxiv.org/pdf/2005.06868, https://arxiv.org/pdf/2302.10397",
                     "SMSS", "21:57:28.23", "-36:02:15.21", "",
                     "4.692", "", "", "log10.31", "log0.17", "log0.14", "log47.87", "log0.10", "log0.10",
                     "0.29", "0.11", "0.10", "", "", "", "", "", "",
                     "", "", "", "", "", "", "",
                     "z from Onken et al. (2020), mass, L_bol, f_Edd from Lai et al. (2023)"]])

# z from: https://arxiv.org/pdf/2005.06868 Onken et al. (2020)
# mass, L_bol, f_Edd from: https://arxiv.org/pdf/2302.10397 Lai et al. (2023)

entry48 = np.array([["J1609+5328", "Matsuoka et al. (2019)",
                     "https://arxiv.org/pdf/1908.07910",
                     "HSC", "16:09:53.03", "+53:28:21.00", "",
                     "6.92", "", "", "", "", "", "", "", "",
                     "", "", "", "-22.75", "1.67", "1.67", "", "", "",
                     "", "", "", "", "", "", "",
                     ""]])

entry49 = np.array([["J0839+3900", "Wang et al. (2019), Yang et al. (2021)",
                     "https://iopscience.iop.org/article/10.3847/1538-4357/ab2be5/pdf, https://iopscience.iop.org/article/10.3847/1538-4357/ac2b32",
                     "DELS", "08:39:46.88", "+39:00:11.50", "",
                     "6.905", "0.01", "0.01", "0.671e9", "0.003e9", "0.003e9", "1.78e46", "0.7e46", "0.7e46",
                     "2.1", "0.1", "0.1", "-26.29", "0.20", "0.20", "", "", "",
                     "", "", "", "", "", "", "",
                     "mass, L_bol, f_Edd from Yang et al. (2019)"]])

# mass, L_bol, f_Edd from: https://iopscience.iop.org/article/10.3847/1538-4357/ac2b32 Yang et al. (2019)

entry50 = np.array([["J2348-3054", "Banados et al. (2016), Venemans et al. (2020), Venemens et al. (2015), Venemans et al. (2013)",
                     "https://arxiv.org/pdf/1608.03279, https://iopscience.iop.org/article/10.3847/1538-4357/abc563, https://iopscience.iop.org/article/10.3847/0004-637X/816/1/37/meta, https://iopscience.iop.org/article/10.1088/0004-637X/779/1/24",
                     "VIK", "23:48:33.34", "-30:54:10.24", "",
                     "6.9007", "0.0005", "0.0005", "2.1e9", "0.5e9", "0.5e9", "", "", "",
                     "", "", "", "-25.72", "0.14", "0.14", "", "", "",
                     "100-680", "", "", "", "", "", "",
                     "z from Venemans et al. (2020), SFR from Venemens et al. (2015), mass, M1450 from Venemans et al. (2013)"]])        

# z from: https://iopscience.iop.org/article/10.3847/1538-4357/abc563 Venemans et al. (2020)
# SFR from: https://iopscience.iop.org/article/10.3847/0004-637X/816/1/37/meta Venemans et al. (2015)
# mass, M1450 from: https://iopscience.iop.org/article/10.1088/0004-637X/779/1/24 Venemans et al. (2013)

entry51 = np.array([["J2210+0304", "Matsuoka et al. (2018)",
                     "https://arxiv.org/pdf/1803.01861",
                     "HSC", "22:10:27.24", "+03:04:28.50", "",
                     "6.9", "", "", "", "", "", "", "", "",
                     "", "", "", "-24.44", "0.06", "0.06", "", "", "",
                     "", "", "", "", "", "", "",
                     ""]])

entry52 = np.array([["J2211-6320", "Yang et al. (2021), Wang et al. (2024)",
                     "https://iopscience.iop.org/article/10.3847/1538-4357/ac2b32, https://arxiv.org/html/2404.15413v1#S1",
                     "DES", "22:11:00.60", "-63:20:55.90", "",
                     "6.8449", "0.0003", "0.0003", "0.55e9", "0.24e9", "0.24e9", "5.9e46", "0.2e46", "0.2e46",
                     "0.8", "0.4", "0.4", "-25.38", "", "", "", "", "",
                     "132-828", "", "", "", "", "", "",
                     "coordinates, SFR_CII from Wang et al. (2024)"]])

# coordinates, SFR_CII from: https://arxiv.org/html/2404.15413v1#S1 Wang et al. (2024)

entry53 = np.array([["J0246-5219", "Yang et al. (2021), Wang et al. (2024)",
                     "https://iopscience.iop.org/article/10.3847/1538-4357/ac2b32, https://arxiv.org/html/2404.15413v1#S1",
                     "DES", "02:46:55.90", "-52:19:49.90", "",
                     "6.8876", "0.0003", "0.0003", "1.05e9", "0.37e9", "0.37e9", "10.2e46", "1.0e46", "1.0e46",
                     "0.8", "0.3", "0.3", "-25.36", "", "", "", "", "",
                     "193-1210", "", "", "", "", "", "",
                     "coordinates, SFR_CII from Wang et al. (2024)"]])

# coordinates, SFR_CII from: https://arxiv.org/html/2404.15413v1#S1 Wang et al. (2024)

entry54 = np.array([["J0020-3653", "Reed et al. (2019)",
                     "https://academic.oup.com/mnras/article/487/2/1874/5505847",
                     "VDES", "00:20:31.47", "-36:53:41.80", "",
                     "6.834", "0.0004", "0.0004", "1.67e9", "0.32e9", "0.32e9", "1.35e47", "0.03e47", "0.03e47",
                     "0.62", "0.12", "0.12", "-26.92", "0.03", "0.03", "", "", "",
                     "", "", "", "", "", "", "",
                     ""]])

entry55 = np.array([["J0319-1008", "Yang et al. (2021), Wang et al. (2024)",
                     "https://iopscience.iop.org/article/10.3847/1538-4357/ac2b32, https://arxiv.org/html/2404.15413v1#S1",
                     "DES", "03:19:41.66", "-10:08:46.00", "",
                     "6.8275", "0.0021", "0.0021", "0.40e9", "0.03e9", "0.03e9", "9.6e46", "1.4e46", "1.4e46",
                     "1.9", "0.3", "0.3", "-25.36", "", "", "", "", "",
                     "146-916", "", "", "", "", "", "",
                     "coordinates, SFR_CII from Wang et al. (2024)"]])

# coordinates, SFR_CII from: https://arxiv.org/html/2404.15413v1#S1 Wang et al. (2024)

entry56 = np.array([["J0112+0110", "Matsuoka et al. (2019)",
                     "https://arxiv.org/pdf/1908.07910",
                     "HSC", "01:12:57.84", "+01:10:42.40", "",
                     "6.82", "", "", "", "", "", "", "", "",
                     "", "", "", "-24.07", "0.35", "0.35", "", "", "",
                     "", "", "", "", "", "", "",
                     ""]])

entry57 = np.array([["J0411-0907", "Yang et al. (2021), Wang et al. (2024), Wang et al. (2019)",
                     "https://iopscience.iop.org/article/10.3847/1538-4357/ac2b32, https://arxiv.org/html/2404.15413v1#S1, https://iopscience.iop.org/article/10.3847/1538-4357/ab2be5/pdf",
                     "DELS", "04:11:28.63", "-09:07:49.70", "",
                     "6.8260", "0.0007", "0.0007", "0.95e9", "0.09e9", "0.09e9", "15.9e46", "1.0e46", "1.0e46",
                     "1.3", "0.2", "0.2", "-26.61", "0.12", "0.12", "", "", "",
                     "119-745", "", "", "", "", "", "",
                     "coordinates, SFR_CII from Wang et al. (2024), M1450 from Wang et al. (2019)"]])

# coordinates, SFR_CII from: https://arxiv.org/html/2404.15413v1#S1 Wang et al. (2024)
# M1450 from: https://iopscience.iop.org/article/10.3847/1538-4357/ab2be5/pdf Wang et al. (2019)

entry58 = np.array([["J1429-0104", "Matsuoka et al. (2018)",
                     "https://arxiv.org/pdf/1704.05854",
                     "HSC", "14:29:03.08", "-01:04:43.40", "",
                     "6.8", "", "", "", "", "", "", "", "",
                     "", "", "", "-23.00", "0.26", "0.26", "", "", "",
                     "", "", "", "", "", "", "",
                     ""]])

entry59 = np.array([["J0109-3047", "Banados et al. (2016), Venemans et al. (2020)",
                     "https://arxiv.org/pdf/1608.03279, https://iopscience.iop.org/article/10.3847/1538-4357/abc563",
                     "VIK", "01:09:53.13", "-30:47:26.31", "",
                     "6.7904", "0.0003", "0.0003", "", "", "", "", "", "",
                     "", "", "", "-25.64", "", "", "", "", "",
                     "", "", "", "", "", "", "",
                     "z from Venemans et al. (2020)"]])

# z from: https://iopscience.iop.org/article/10.3847/1538-4357/abc563 Venemans et al. (2020)

entry60 = np.array([["J1612+5559", "Matsuoka et al. (2019)",
                     "https://arxiv.org/pdf/1908.07910",
                     "HSC", "16:12:07.12", "+55:59:19.20", "",
                     "6.78", "", "", "", "", "", "", "", "",
                     "", "", "", "-23.02", "0.32", "0.32", "", "", "",
                     "", "", "", "", "", "", "",
                     ""]])

entry61 = np.array([["J0829+4117", "Wang et al. (2019), Yang et al. (2021)",
                     "https://iopscience.iop.org/article/10.3847/1538-4357/ab2be5/pdf, https://iopscience.iop.org/article/10.3847/1538-4357/ac2b32",
                     "DELS", "08:29:31.98", "+41:17:40.90", "",
                     "6.768", "0.006", "0.006", "0.71e9", "0.02e9", "0.02e9", "12.8e46", "1.2e46", "1.2e46",
                     "1.4", "0.1", "0.1", "-26.36", "0.15", "0.15", "", "", "",
                     "<19-122", "", "", "", "", "", "",
                     "mass, L_bol, f_Edd from Yang et al. (2021), coordinates, SFR_CII from Wang et al. (2024)"]])

# mass, L_bol, f_Edd from: https://iopscience.iop.org/article/10.3847/1538-4357/ac2b32 Yang et al. (2021)
# coordinates, SFR_CII from: https://arxiv.org/html/2404.15413v1#S1 Wang et al. (2024)

entry62 = np.array([["J1104+2134", "Yang et al. (2021), Wang et al. (2024), Wang et al. (2019)",
                     "https://iopscience.iop.org/article/10.3847/1538-4357/ac2b32, https://arxiv.org/html/2404.15413v1#S1, https://iopscience.iop.org/article/10.3847/1538-4357/ab2be5/pdf",
                     "DELS", "11:04:21.58", "+21:34:28.90", "",
                     "6.7662", "0.0009", "0.0009", "1.69e9", "0.15e9", "0.15e9", "15.1e46", "0.9e46", "0.9e46",
                     "0.7", "0.1", "0.1", "-26.67", "0.13", "0.13", "", "", "",
                     "", "", "", "", "", "", "",
                     "coordinates, SFR_CII from Wang et al. (2024), M1450 from Wang et al. (2019)"]])

# coordinates, SFR_CII from: https://arxiv.org/html/2404.15413v1#S1 Wang et al. (2024)
# M1450 from: https://iopscience.iop.org/article/10.3847/1538-4357/ab2be5/pdf Wang et al. (2019)

entry63 = np.array([["J0244-5008", "Reed et al. (2019)",
                     "https://academic.oup.com/mnras/article/487/2/1874/5505847",
                     "VDES", "02:44:01.02", "-50:08:53.70", "",
                     "6.724", "0.0008", "0.0008", "1.15e9", "0.39e9", "0.39e9", "1.44e47", "0.02e47", "0.02e47",
                     "0.96", "0.33", "0.33", "-26.72", "0.05", "0.05", "", "", "",
                     "", "", "", "", "", "", "",
                     ""]])

entry64 = np.array([["J0910+1656", "Yang et al. (2021), Wang et al. (2024), Wang et al. (2019)",
                     "https://iopscience.iop.org/article/10.3847/1538-4357/ac2b32, https://arxiv.org/html/2404.15413v1#S1, https://iopscience.iop.org/article/10.3847/1538-4357/ab2be5/pdf",
                     "DELS", "09:10:13.65", "+16:56:30.20", "",
                     "6.7289", "0.0005", "0.0005", "0.41e9", "0.03e9", "0.03e9", "5.3e46", "0.6e46", "0.6e46",
                     "1.0", "0.1", "0.1", "-25.57", "0.14", "0.14", "", "", "",
                     "105-658", "", "", "", "", "", "",
                     "coordinates, SFR_CII from Wang et al. (2024), M1450 from Wang et al. (2019)"]])

# coordinates, SFR_CII from: https://arxiv.org/html/2404.15413v1#S1 Wang et al. (2024)
# M1450 from: https://iopscience.iop.org/article/10.3847/1538-4357/ab2be5/pdf Wang et al. (2019)

entry65 = np.array([["J1344+0128", "Matusuka et al. (2019)",
                     "https://arxiv.org/pdf/1908.07910",
                     "HSC", "13:44:00.87", "+01:28:27.80", "",
                     "6.72", "", "", "", "", "", "", "", "",
                     "", "", "", "-23.46", "0.15", "0.15", "", "", "",
                     "", "", "", "", "", "", "",
                     ""]])

entry66 = np.array([["J0213-0626", "Matsuoka et al. (2018), Wang et al. (2024)",
                     "https://arxiv.org/pdf/1803.01861, https://arxiv.org/html/2404.15413v1#S1",
                     "HSC", "02:13:16.94", "-06:26:15.20", "",
                     "6.72", "", "", "", "", "", "log44.18", "log0.02", "log0.02",
                     "", "", "", "-25.24", "0.02", "0.02", "", "", "",
                     "13-86", "", "", "", "", "", "",
                     ""]])

# SFR_CII from: https://arxiv.org/html/2404.15413v1#S1 Wang et al. (2024)

entry67 = np.array([["J0837+4929", "Yang et al. (2021), Wang et al. (2024), Wang et al. (2019)",
                     "https://iopscience.iop.org/article/10.3847/1538-4357/ac2b32, https://arxiv.org/html/2404.15413v1#S1, https://iopscience.iop.org/article/10.3847/1538-4357/ab2be5/pdf",
                     "DELS", "08:37:37.83", "+49:29:00.60", "",
                     "6.710", "0.008", "0.008", "0.81e9", "0.01e9", "0.01e9", "14.5e46", "0.4e46", "0.4e46",
                     "1.4", "0.1", "0.1", "-26.42", "0.18", "0.18", "", "", "",
                     "36-229", "", "", "", "", "", "",
                     "coordinates, SFR_CII from Wang et al. (2024), M1450 from Wang et al. (2019)"]])

# M1450 from: https://iopscience.iop.org/article/10.3847/1538-4357/ab2be5/pdf Wang et al. (2019)
# coordinates, SFR_CII from: https://arxiv.org/html/2404.15413v1#S1 Wang et al. (2024)

entry68 = np.array([["J0001+0000", "Matsuoka et al. (2019)",
                     "https://arxiv.org/pdf/1908.07910",
                     "HSC", "00:01:42.54", "+00:00:57.50", "",
                     "6.69", "", "", "", "", "", "", "", "",
                     "", "", "", "-24.49", "0.59", "0.59", "", "", "",
                     "", "", "", "", "", "", "",
                     ""]])

entry69 = np.array([["J1231+0052", "Matsuoka et al. (2019)",
                     "https://arxiv.org/pdf/1908.07910",
                     "HSC", "12:31:37.77", "+00:52:30.30", "",
                     "6.69", "", "", "", "", "", "", "", "",
                     "", "", "", "-24.39", "0.09", "0.09", "", "", "",
                     "", "", "", "", "", "", "",
                     ""]])

entry70 = np.array([["J2232+2930/J338.2+29.50", "Banados et al. (2016), Wang et al. (2019)",
                     "https://arxiv.org/pdf/1608.03279, https://iopscience.iop.org/article/10.3847/1538-4357/ab2be5/pdf",
                     "PSO", "22:32:55.14", "+29:30:32.31", "",
                     "6.666", "0.0004", "0.0004", "", "", "", "", "", "",
                     "", "", "", "-26.31", "0.15", "0.15", "", "", "",
                     "", "", "", "", "", "", "",
                     "z, M1450 from Wang et al. (2019)"]])

# z, M1450 from: https://iopscience.iop.org/article/10.3847/1538-4357/ab2be5/pdf Wang et al. (2019)

entry71 = np.array([["J1216+4519", "Wang et al. (2019), Yang et al. (2021), Wang et al. (2024)",
                     "https://iopscience.iop.org/article/10.3847/1538-4357/ab2be5/pdf, https://iopscience.iop.org/article/10.3847/1538-4357/ac2b32, https://arxiv.org/html/2404.15413v1#S1",
                     "DELS", "12:16:27.58", "+45:19:10.70", "",
                     "6.654", "0.01", "0.01", "0.61e9", "0.20e9", "0.20e9", "5.8e46", "1.2e46", "1.2e46",
                     "0.8", "0.3", "0.3", "-25.58", "0.14", "0.14", "", "", "",
                     "<16-104", "", "", "", "", "", "",
                     "mass, L_bol, f_Edd from Yang et al. (2021), coordinates, SFR_CII from Wang et al. (2024)"]])

# mass, L_bol, f_Edd from: https://iopscience.iop.org/article/10.3847/1538-4357/ac2b32 Yang et al. (2021)
# coordinates, SFR_CII from: https://arxiv.org/html/2404.15413v1#S1 Wang et al. (2024)

entry72 = np.array([["J2102-1458", "Wang et al. (2019), Yang et al. (2021), Wang et al. (2024)",
                     "https://iopscience.iop.org/article/10.3847/1538-4357/ab2be5/pdf, https://iopscience.iop.org/article/10.3847/1538-4357/ac2b32, https://arxiv.org/html/2404.15413v1#S1",
                     "VHS", "21:02:19.23", "-14:58:53.90", "",
                     "6.6645", "0.0002", "0.0002", "0.74e9", "0.11e9", "0.11e9", "6.0e46", "0.5e46", "0.5e46",
                     "0.6", "0.1", "0.1", "-25.50", "0.2", "0.2", "", "", "",
                     "81-511", "", "", "", "", "", "",
                     "z, mass, L_bol, f_Edd from Yang et al. (2021), coordinates, SFR_CII from Wang et al. (2024)"]])

# z, mass, L_bol, f_Edd from: https://iopscience.iop.org/article/10.3847/1538-4357/ac2b32 Yang et al. (2021)
# coordinates, SFR_CII from: https://arxiv.org/html/2404.15413v1#S1 Wang et al. (2024)

entry73 = np.array([["J0910-0414", "Wang et al. (2019), Yang et al. (2021), Wang et al. (2024)",
                     "https://iopscience.iop.org/article/10.3847/1538-4357/ab2be5/pdf, https://iopscience.iop.org/article/10.3847/1538-4357/ac2b32, https://arxiv.org/html/2404.15413v1#S1",
                     "DELS", "09:10:54.54", "-04:14:06.90", "",
                     "6.6363", "0.0003", "0.0003", "3.59e9", "0.61e9", "0.61e9", "15.0e46", "1.1e46", "1.1e46",
                     "0.3", "0.1", "0.1", "-26.36", "0.15", "0.15", "", "", "",
                     "271-1697	", "", "", "", "", "", "",
                     "z, mass, L_bol, f_Edd from Yang et al. (2021), coordinates, SFR_CII from Wang et al. (2024)"]])

# z, mass, L_bol, f_Edd from: https://iopscience.iop.org/article/10.3847/1538-4357/ac2b32 Yang et al. (2021)
# coordinates, SFR_CII from: https://arxiv.org/html/2404.15413v1#S1 Wang et al. (2024)

entry74 = np.array([["J1048-0109", "Venemans et al. (2020), Wang et al. (2019), ",
                     "https://iopscience.iop.org/article/10.3847/1538-4357/abc563, https://iopscience.iop.org/article/10.3847/1538-4357/ab2be5/pdf",
                     "DELS", "10:48:19.077", "-01:09:40.42", "",
                     "6.6759", "0.0002", "0.0002", "", "", "", "", "", "",
                     "", "", "", "-25.97", "0.18", "0.18", "", "", "",
                     "", "", "", "", "", "", "",
                     "M1450 from Wang et al. (2019)"]])

# M1450 from: https://iopscience.iop.org/article/10.3847/1538-4357/ab2be5/pdf Wang et al. (2019)

entry75 = np.array([["J0024+3913/J006.1+39.22", "Tang et al. (2017), Koptelova et al. (2019)",
                     "https://academic.oup.com/mnras/article/466/4/4568/2712523, https://arxiv.org/pdf/1907.07458",
                     "PSO", "00:24:29.77", "+39:13:18.95", "",
                     "6.61", "0.02", "0.02", "2.19e8", "0.30e8", "0.30e8", "", "", "",
                     "", "", "", "-25.96", "0.08", "0.08", "", "", "",
                     "", "", "", "", "", "", "",
                     "mass from Koptelova et al. (2019)"]])

# mass from: https://arxiv.org/pdf/1907.07458 Koptelova et al. (2019)

entry76 = np.array([["J0305-3150", "Banados et al. (2016)",
                     "https://arxiv.org/pdf/1608.03279",
                     "VIK", "03:05:16.92", "-31:50:55.90", "",
                     "6.6145", "", "", "", "", "", "", "", "",
                     "", "", "", "-26.18", "", "", "", "", "",
                     "", "", "", "", "", "", "",
                     ""]])

entry77 = np.array([["J0923+0402", "Yang et al. (2021), Wang et al. (2024), Wang et al. (2019)",
                     "https://iopscience.iop.org/article/10.3847/1538-4357/ac2b32, https://arxiv.org/html/2404.15413v1#S1, https://iopscience.iop.org/article/10.3847/1538-4357/ab2be5/pdf",
                     "DELS/HSC", "09:23:47.12", "+04:02:54.40", "",
                     "6.6330", "0.0003", "0.0003", "1.77e9", "0.02e9", "0.02e9", "21.7e46", "3.0e46", "3.0e46",
                     "1.0", "0.1", "0.1", "-26.61", "0.11", "0.11", "", "", "",
                     "116-729", "", "", "", "", "", "",
                     "coordinates, SFR_CII from Wang et al. (2024), M1450 from Wang et al. (2019), additional information here: https://arxiv.org/pdf/2306.16474  Mazzucchelli et al. (2023)"]])

# coordinates, SFR_CII from: https://arxiv.org/html/2404.15413v1#S1 Wang et al. (2024)
# M1450 from: https://iopscience.iop.org/article/10.3847/1538-4357/ab2be5/pdf Wang et al. (2019)

entry78 = np.array([["J2132+1217/J323.1+12.29", "Mazzucchelli et al. (2017), Wang et al. (2019)",
                     "https://arxiv.org/pdf/1710.01251, https://iopscience.iop.org/article/10.3847/1538-4357/ab2be5/pdf",
                     "PSO", "21:32:33.191", "+12:17:55.26", "",
                     "6.5881", "0.0003", "0.0003", "1.39e9", "0.32e9", "0.51e9", "0.81e47", "0.07e47", "0.50e47",
                     "0.44", "1.09", "3.19", "-27.04", "0.12", "0.12", "", "", "",
                     "", "", "", "", "", "", "",
                     "M1450 from Wang et al. (2019)"]])

# M1450 from: https://iopscience.iop.org/article/10.3847/1538-4357/ab2be5/pdf Wang et al. (2019)
# How is it possible that the f_Edd is negative?

entry79 = np.array([["J1526-2050/J231.6-20.83", "Mazzucchelli et al. (2017)",
                     "https://arxiv.org/pdf/1710.01251",
                     "PSO", "15:26:37.841", "-20:50:00.66", "",
                     "6.5864", "0.0005", "0.0005", "3.05e9", "0.44e9", "2.24e9", "1.89e47", "0.34e47", "0.45e47",
                     "0.48", "0.11", "0.39", "-27.14", "", "", "", "", "",
                     "", "", "", "", "", "", "",
                     ""]])

entry80 = np.array([["J0706+2921", "Yang et al. (2021), Wang et al. (2024), Wang et al. (2019)",
                     "https://iopscience.iop.org/article/10.3847/1538-4357/ac2b32, https://arxiv.org/html/2404.15413v1#S1, https://iopscience.iop.org/article/10.3847/1538-4357/ab2be5/pdf",
                     "DELS", "07:06:26.38", "+29:21:05.50", "",
                     "6.6037", "0.0003", "0.0003", "2.11e9", "0.16e9", "0.16e9", "33.9e46", "1.5e46", "1.5e46",
                     "1.3", "0.1", "0.1", "-27.51", "0.08", "0.08", "", "", "",
                     "129-808", "", "", "", "", "", "",
                     "coordinates, SFR_CII from Wang et al. (2024), M1450 from Wang et al. (2019), additional information here: https://arxiv.org/pdf/2306.16474  Mazzucchelli et al. (2023)"]])

# coordinates, SFR_CII from: https://arxiv.org/html/2404.15413v1#S1 Wang et al. (2024)
# M1450 from: https://iopscience.iop.org/article/10.3847/1538-4357/ab2be5/pdf Wang et al. (2019)

entry81 = np.array([["J1135+5011", "Yang et al. (2021), Wang et al. (2024), Wang et al. (2019)",
                     "https://iopscience.iop.org/article/10.3847/1538-4357/ac2b32, https://arxiv.org/html/2404.15413v1#S1, https://iopscience.iop.org/article/10.3847/1538-4357/ab2be5/pdf",
                     "DELS", "11:35:08.92", "+50:11:32.60", "",
                     "6.5851", "0.0008", "0.0008", "1.49e9", "0.05e9", "0.05e9", "10.8e46", "0.8e46", "0.8e46",
                     "0.6", "0.1", "0.1", "-26.19", "0.17", "0.17", "", "", "",
                     "107-669", "", "", "", "", "", "",
                     "coordinates, SFR_CII from Wang et al. (2024), M1450 from Wang et al. (2019)"]])

# coordinates, SFR_CII from: https://arxiv.org/html/2404.15413v1#S1 Wang et al. (2024)
# M1450 from: https://iopscience.iop.org/article/10.3847/1538-4357/ab2be5/pdf Wang et al. (2019)

entry82 = np.array([["J0921+0007", "Yang et al. (2021), Matsuoka et al. (2018), Wang et al. (2024)",
                     "https://iopscience.iop.org/article/10.3847/1538-4357/ac2b32, https://arxiv.org/pdf/1803.01861, https://arxiv.org/html/2404.15413v1#S1",
                     "HSC", "09:21:20.56", "+00:07:22.90", "",
                     "6.5646", "0.0003", "0.0003", "0.26e9", "0.01e9", "0.01e9", "6.1e46", "0.6e46", "0.6e46",
                     "1.9", "0.2", "0.2", "-24.79", "0.10", "0.10", "", "", "",
                     "62-389", "", "", "", "", "", "",
                     "coordinates, SFR_CII from Wang et al. (2024), M1450 from Matsuoka et al. (2018)"]])

# coordinates, SFR_CII from: https://arxiv.org/html/2404.15413v1#S1 Wang et al. (2024)
# M1450 from: https://arxiv.org/pdf/1803.01861 Matsuoka et al. (2018)

entry83 = np.array([["J0226+0302/J036.5+03.04", "Banados et al. (2016), Mazzucchelli et al. (2017), ",
                     "https://arxiv.org/pdf/1608.03279, https://arxiv.org/pdf/1710.01251",
                     "PSO", "02:26:01.87", "+03:02:59.42", "",
                     "6.541", "0.002", "0.002", "3.00e9", "0.92e9", "0.77e9", "2.0e47", "0.22e47", "0.64e47",
                     "0.51", "0.17", "0.21", "-27.18", "0.12", "0.12", "", "", "",
                     "", "", "", "", "", "", "",
                     "z, mass, L_bol, f_Edd from Mazzucchelli et al. (2017), M1450 from Wang et al. (2019)"]])

# z, mass, L_bol, f_Edd from: https://arxiv.org/pdf/1710.01251 Mazzucchelli et al. (2017)
# M1450 from: https://iopscience.iop.org/article/10.3847/1538-4357/ab2be5/pdf Wang et al. (2019)

entry84 = np.array([["J0224-4711", "Reed et al. (2019), Wang et al. (2024)",
                     "https://academic.oup.com/mnras/article/487/2/1874/5505847, https://arxiv.org/html/2404.15413v1#S1",
                     "VDES", "02:24:26.54", "-47:11:29.40", "",
                     "6.526", "0.0003", "0.0003", "2.12e9", "0.42e9", "0.42e9", "3.13e47", "0.04e47", "0.04e47",
                     "1.13", "0.22", "0.22", "-26.72", "0.05", "0.05", "", "", "",
                     "370-2316", "", "", "", "", "", "",
                     "SFR_CII from Wang et al. (2024), additional information here: https://arxiv.org/pdf/2306.16474  Mazzucchelli et al. (2023)"]])

# SFR_CII from: https://arxiv.org/html/2404.15413v1#S1 Wang et al. (2024)

entry85 = np.array([["J0439+1634", "Yang et al. (2021), Wang et al. (2024)",
                     "https://iopscience.iop.org/article/10.3847/1538-4357/ac2b32, https://arxiv.org/html/2404.15413v1#S1",
                     "UHS", "04:39:47.10", "+16:34:15.80", "",
                     "6.5188", "0.0004", "0.0004", "0.63e9", "0.02e9", "0.02e9", "4.6e46", "0.1e46", "0.1e46",
                     "0.6", "0.1", "0.1", "-25.31", "", "", "", "", "",
                     "", "", "", "", "", "", "",
                     "coordinates from Wang et al. (2024), additional information here: https://arxiv.org/pdf/2306.16474  Mazzucchelli et al. (2023)"]])

# coordinates from: https://arxiv.org/html/2404.15413v1#S1 Wang et al. (2024)

entry86 = np.array([["J1110-1329/J167.6-13.49", "Banados et al. (2016), Decarli et al. (2018), Mazzucchelli et al. (2017)",
                     "https://arxiv.org/pdf/1608.03279, https://iopscience.iop.org/article/10.3847/1538-4357/aaa5aa, https://arxiv.org/pdf/1710.01251",
                     "PSO", "11:10:33.976", "-13:29:45.60", "",
                     "6.508", "0.001", "0.001", "0.30e9", "0.08e9", "0.12e9", "0.47e47", "0.16e47", "0.22e47",
                     "1.22", "0.51", "0.75", "-25.62", "", "", "", "", "",
                     "", "", "", "", "", "", "",
                     "coordinates, z errors from Decarli et al. (2018), mass, L_bol, f_Edd from Mazzucchelli et al. (2017)"]])

# coordinates, z errors from: https://iopscience.iop.org/article/10.3847/1538-4357/aaa5aa Decarli et al. (2018)
# mass, L_bol, f_Edd from: https://arxiv.org/pdf/1710.01251 Mazzucchelli et al. (2017)

entry87 = np.array([["J1545+4232", "Matsuoka et al. (2018), Ishimoto et al. (2020)",
                     "https://arxiv.org/pdf/1803.01861, https://iopscience.iop.org/article/10.3847/1538-4357/abb80b/pdf",
                     "HSC", "15:45:05.62", "+42:32:11.60", "",
                     "6.511", "0.003", "0.004", "", "", "", "log44.68", "log0.03", "log0.03",
                     "", "", "", "-24.76", "0.17", "0.17", "", "", "",
                     "", "", "", "", "", "", "",
                     "z, M1450 from Ishimoto et al. (2020)"]])

# z, M1450 from: https://iopscience.iop.org/article/10.3847/1538-4357/abb80b/pdf Ishimoto et al. (2020)

entry88 = np.array([["J1350-0027", "Matsuoka et al. (2019)",
                     "https://arxiv.org/pdf/1908.07910",
                     "HSC", "13:50:12.04", "-00:27:05.20", "",
                     "6.49", "", "", "", "", "", "", "", "",
                     "", "", "", "-24.38", "0.19", "0.19", "", "", "",
                     "", "", "", "", "", "", "",
                     ""]])

entry89 = np.array([["J1629+2407/J247.2+24.12", "Mazzucchelli et al. (2017)",
                     "https://arxiv.org/pdf/1710.01251",
                     "PSO", "16:29:11.296", "+24:07:39.74", "",
                     "6.476", "0.004", "0.004", "0.52e9", "0.22e9", "0.25e9", "1.77e47", "0.06e47", "0.76e47",
                     "2.60", "0.08", "0.15", "-26.53", "", "", "", "", "",
                     "", "", "", "", "", "", "",
                     ""]])

entry90 = np.array([["J2131-4359", "Yang et al. (2019)",
                     "https://iopscience.iop.org/article/10.3847/1538-3881/ab1be1/meta",
                     "DES", "21:31:10.29", "-43:59:02.50", "",
                     "6.45", "", "", "", "", "", "", "", "",
                     "", "", "", "-24.93", "0.25", "0.25", "", "", "",
                     "", "", "", "", "", "", "",
                     ""]])

entry91 = np.array([["J1724+1901/J261.0+19.02", "Mazzucchelli et al. (2017), Wang et al. (2019)",
                     "https://arxiv.org/pdf/1710.01251, https://iopscience.iop.org/article/10.3847/1538-4357/ab2be5/pdf",
                     "PSO", "17:24:08.743", "+19:01:43.12", "",
                     "6.44", "0.05", "0.05", "", "", "", "", "", "",
                     "", "", "", "-25.51", "0.19", "0.19", "", "", "",
                     "", "", "", "", "", "", "",
                     "M1450 from Wang et al. (2019)"]])

# M1450 from: https://iopscience.iop.org/article/10.3847/1538-4357/ab2be5/pdf Wang et al. (2019)

entry92 = np.array([["J1212+0505/J183.1+05.09", "Mazzucchelli et al. (2017), Wang et al. (2019)",
                     "https://arxiv.org/pdf/1710.01251, https://iopscience.iop.org/article/10.3847/1538-4357/ab2be5/pdf",
                     "PSO", "12:12:26.981", "+05:05:33.49", "",
                     "6.4386", "0.0004", "0.0004", "", "", "", "", "", "",
                     "", "", "", "-26.80", "0.10", "0.10", "", "", "",
                     "", "", "", "", "", "", "",
                     ""]])

# M1450 from: https://iopscience.iop.org/article/10.3847/1538-4357/ab2be5/pdf Wang et al. (2019)

entry93 = np.array([["J2318-3113", "Decarli et al. (2018)",
                     "https://iopscience.iop.org/article/10.3847/1538-4357/aaa5aa",
                     "VIK", "23:18:18.351", "-31:13:46.35", "",
                     "6.444", "0.005", "0.005", "", "", "", "", "", "",
                     "", "", "", "-26.11", "", "", "", "", "",
                     "", "", "", "", "", "", "",
                     ""]])

entry94 = np.array([["J0210-0456", "Banados et al. (2016), Willott et al. (2015)",
                     "https://arxiv.org/pdf/1608.03279, https://iopscience.iop.org/article/10.1088/0004-637X/801/2/123#apj509348t2",
                     "CFHQS", "02:10:13.19", "-04:56:20.90", "",
                     "6.4323", "0.0005", "0.0005", "0.8e8", "1.0e8", "0.6e8", "", "", "",
                     "", "", "", "-24.53", "", "", "", "", "",
                     "", "", "", "", "", "", "",
                     "z, mass from Willott et al. (2015)"]])

# z, mass from: https://iopscience.iop.org/article/10.1088/0004-637X/801/2/123#apj509348t2 Willott et al. (2015)

entry95 = np.array([["J0045+0901/J011.3+09.03", "Mazzucchelli et al. (2017)",
                     "https://arxiv.org/pdf/1710.01251",
                     "PSO", "00:45:33.568", " +09:01:56.96", "",
                     "6.42", "0.05", "0.05", "", "", "", "", "", "",
                     "", "", "", "-25.95", "", "", "", "", "",
                     "", "", "", "", "", "", "",
                     ""]])

entry96 = np.array([["J1148+5251", "Banados et al. (2016), Willott et al. (2015)",
                     "https://arxiv.org/pdf/1608.03279, https://iopscience.iop.org/article/10.1088/0004-637X/801/2/123#apj509348t2",
                     "SDSS", "11:48:16.65", "+52:51:50.39", "",
                     "6.4189", "0.0006", "0.0006", "4.9e9", "4.9e9", "2.5e9", "", "", "",
                     "", "", "", "-27.62", "", "", "", "", "",
                     "", "", "", "", "", "", "",
                     "z, mass from Willott et al. (2015)"]])

# z, mass from: https://iopscience.iop.org/article/10.1088/0004-637X/801/2/123#apj509348t2 Willott et al. (2015)

entry97 = np.array([["J2329-0301", "Banados et al. (2016), ishimoto et al. (2020)",
                     "https://arxiv.org/pdf/1608.03279, https://iopscience.iop.org/article/10.3847/1538-4357/abb80b/pdf",
                     "CFHQS", "23:29:08.28", "-03:01:58.80", "",
                     "6.4164", "0.0008", "0.0008", "", "", "", "", "", "",
                     "", "", "", "-25.25", "", "", "", "", "",
                     "", "", "", "", "", "", "",
                     "z from Ishimoto et al. (2020)"]])

# z from: https://iopscience.iop.org/article/10.3847/1538-4357/abb80b/pdf Ishimoto et al. (2020)

entry98 = np.array([["J0216-5226", "Yang et al. (2019)",
                     "https://iopscience.iop.org/article/10.3847/1538-3881/ab1be1/meta",
                     "DES", "02:16:38.85", "-52:26:20.60", "",
                     "6.41", "", "", "", "", "", "", "", "",
                     "", "", "", "-25.19", "0.19", "0.19", "", "", "",
                     "", "", "", "", "", "", "",
                     ""]])

entry99 = np.array([["J1004+0239", "Matsuoka et al. (2018)",
                     "https://arxiv.org/pdf/1803.01861",
                     "HSC", "10:04:01.36", "+02:39:30.70", "",
                     "6.41", "", "", "", "", "", "log44.27", "log0.01", "log0.01",
                     "", "", "", "-24.52", "0.03", "0.03", "", "", "",
                     "", "", "", "", "", "", "",
                     ""]])

entry100 = np.array([["J1535+1943", "Wang et al. (2019), Yang et al. (2021), D'Odorico et al. (2023)",
                     "https://iopscience.iop.org/article/10.3847/1538-4357/ab2be5/pdf, https://iopscience.iop.org/article/10.3847/1538-4357/ac2b32, https://academic.oup.com/mnras/article/523/1/1399/7172883",
                     "DELS", "15:35:32.87", "+19:43:20.10", "",
                     "6.370", "0.001", "0.001", "3.53e9", "0.33e9", "0.33e9", "33.5e46", "1.7e46", "1.7e46",
                     "0.8", "0.1", "0.1", "-27.01", "0.13", "0.13", "", "", "",
                     "", "", "", "", "", "", "",
                     "z, mass, L_bol, f_Edd from Yang et al. (2021), coordinates from D'Odorico et al. (2023), additional information here: https://arxiv.org/pdf/2306.16474  Mazzucchelli et al. (2023)"]])

# z, mass, L_bol, f_Edd from: https://iopscience.iop.org/article/10.3847/1538-4357/ac2b32 Yang et al. (2021)
# coordinates from: https://academic.oup.com/mnras/article/523/1/1399/7172883 D'Odorico et al. (2023)

entry101 = np.array([["J1137+0045", "Matsuoka et al. (2019)",
                     "https://arxiv.org/pdf/1908.07910",
                     "HSC", "11:37:53.64", "+00:45:09.70", "",
                     "6.4", "", "", "", "", "", "", "", "",
                     "", "", "", "-24.20", "0.13", "0.13", "", "", "",
                     "", "", "", "", "", "", "",
                     ""]])

entry102 = np.array([["J0844+0226", "Matsuoka et al. (2019)",
                     "https://arxiv.org/pdf/1908.07910",
                     "HSC", "08:44:56.62", "+02:26:40.50", "",
                     "6.40", "", "", "", "", "", "", "", "",
                     "", "", "", "-21.57", "0.47", "0.47", "", "", "",
                     "", "", "", "", "", "", "",
                     ""]])

entry103 = np.array([["J2236+0032", "Banados et al. (2016), Matsuoka et al. (2016)",
                     "https://arxiv.org/pdf/1608.03279, https://iopscience.iop.org/article/10.3847/0004-637X/828/1/26",
                     "HSC", "22:36:44.58", "+00:32:56.90", "",
                     "6.40", "", "", "", "", "", "", "", "",
                     "", "", "", "-23.66", "0.10", "0.10", "", "", "",
                     "", "", "", "", "", "", "",
                     "M1450 from Matsuoka et al. (2016)"]])

# M1450 from: https://iopscience.iop.org/article/10.3847/0004-637X/828/1/26 Matsuoka et al. (2016)

entry104 = np.array([["J0859+0022", "Banados et al. (2016), Ishimoto et al. (2020), Onoue et al. (2019)",
                     "https://arxiv.org/pdf/1608.03279, https://iopscience.iop.org/article/10.3847/1538-4357/abb80b/pdf, https://arxiv.org/pdf/1904.07278",
                     "HSC", "08:59:07.19", "+00:22:55.90", "",
                     "6.3903", "0.0005", "0.0005", "0.38e8", "0.10e8", "0.18e8", "", "", "",
                     "1.1", "0.5", "0.3", "-23.10", "0.27", "0.27", "", "", "",
                     "", "", "", "", "", "", "",
                     "z from Ishimoto et al. (2020), M1450, mass, f_Edd from Onoue et al. (2019), L_bol (LyA) from Matsuoka et al. (2018)"]])

# z from: https://iopscience.iop.org/article/10.3847/1538-4357/abb80b/pdf Ishimoto et al. (2020)
# M1450, mass, f_Edd from: https://arxiv.org/pdf/1904.07278 Onoue et al. (2019)


entry105 = np.array([["J1036-0232/J159.2-02.54/P195-02", "Banados et al. (2016), Decarli et al. (2018)",
                     "https://arxiv.org/pdf/1608.03279, https://iopscience.iop.org/article/10.3847/1538-4357/aaa5aa",
                     "PSO", "10:36:54.191", "-02:32:37.94", "",
                     "6.38", "0.05", "0.05", "", "", "", "", "", "",
                     "", "", "", "-26.80", "", "", "", "", "",
                     "", "", "", "", "", "", "",
                     "z, coordinates from Decarli et al. (2018)"]])

# z, coordinates from: https://iopscience.iop.org/article/10.3847/1538-4357/aaa5aa Decarli et al. (2018)

entry106 = np.array([["J0803+3138", "Wang et al. (2019), Yang et al. (2021)",
                     "https://iopscience.iop.org/article/10.3847/1538-4357/ab2be5/pdf, https://iopscience.iop.org/article/10.3847/1538-4357/ac2b32",
                     "DELS", "08:03:05.42", "+31:38:34.20", "",
                     "6.377", "0.006", "0.006", "1.40e9", "0.18e9", "0.18e9", "13.4e46", "1.1e46", "1.1e46",
                     "0.8", "0.1", "0.1", "-26.51", "0.14", "0.14", "", "", "",
                     "", "", "", "", "", "", "",
                     "mass, L_bol, f_Edd from Yang et al. (2021)"]])

# mass, L_bol, f_Edd from: https://iopscience.iop.org/article/10.3847/1538-4357/ac2b32 Yang et al. (2021)

entry107 = np.array([["J1152+0055", "Banados et al. (2016), Ishimoto et al. (2020), Onoue et al. (2019)",
                     "https://arxiv.org/pdf/1608.03279, https://iopscience.iop.org/article/10.3847/1538-4357/abb80b/pdf, https://arxiv.org/pdf/1904.07278",
                     "VIK/HSC", "11:52:21.27", "+00:55:36.69", "",
                     "6.3637", "0.0005", "0.0005", "6.3e8", "0.8e8", "1.2e8", "", "", "",
                     "0.43", "0.08", "0.05", "-25.08", "0.07", "0.07", "", "", "",
                     "", "", "", "", "", "", "",
                     "z, mass from Ishimoto et al. (2020), mass, f_Edd from Onoue et al. (2019), L_bol from Matsuoka et al. (2018)"]])

# z, M1450 from: https://iopscience.iop.org/article/10.3847/1538-4357/abb80b/pdf Ishimoto et al. (2020)
# mass, f_Edd from: https://arxiv.org/pdf/1904.07278 Onoue et al. (2019)


entry108 = np.array([["J0211-0203", "Matsuoka et al. (2018)",
                     "https://arxiv.org/pdf/1803.01861",
                     "HSC", "02:11:44.53", "-02:03:03.90", "",
                     "6.37", "", "", "", "", "", "", "", "",
                     "", "", "", "-23.36", "0.06", "0.06", "43.64", "0.04", "0.04",
                     "", "", "", "", "", "", "",
                     ""]])

entry109 = np.array([["J2304+0045", "Matsuoka et al. (2018), Ishimoto et al. (2020)",
                     "https://arxiv.org/pdf/1803.01861, https://iopscience.iop.org/article/10.3847/1538-4357/abb80b/pdf	",
                     "HSC", "23:04:22.97", "+00:45:05.40", "",
                     "6.3504", "0.0002", "0.0002", "", "", "", "log43.79", "log0.03", "log0.03",
                     "", "", "", "-24.28", "0.03", "0.03", "", "", "",
                     "", "", "", "", "", "", "",
                     "z from Ishimoto et al. (2020)"]])

# z from: https://iopscience.iop.org/article/10.3847/1538-4357/abb80b/pdf Ishimoto et al. (2020)

entry110 = np.array([["J1316+1028", "Wang et al. (2019), Yang et al. (2021)",
                     "https://iopscience.iop.org/article/10.3847/1538-4357/ab2be5/pdf, https://iopscience.iop.org/article/10.3847/1538-4357/ac2b32",
                     "DELS", "13:16:08.14", "+10:28:32.80", "",
                     "6.35", "0.04", "0.04", "1.01e9", "0.37e9", "0.37e9", "14.8e46", "3.3e46", "3.3e46",
                     "1.2", "0.5", "0.5", "-25.73", "0.17", "0.17", "", "", "",
                     "", "", "", "", "", "", "",
                     "mass, L_bol, f_Edd from Yang et al. (2021)"]])

# mass, L_bol, f_Edd from: https://iopscience.iop.org/article/10.3847/1538-4357/ac2b32 Yang et al. (2021)

entry111 = np.array([["J0857+0056", "Matsuoka et al. (2018)",
                     "https://arxiv.org/pdf/1704.05854",
                     "HSC", "08:57:38.53", "+00:56:12.70", "",
                     "6.35", "", "", "", "", "", "", "", "",
                     "", "", "", "-23.01", "0.07", "0.07", "", "", "",
                     "", "", "", "", "", "", "",
                     ""]])

entry112 = np.array([["J2255+0251", "Matsuoka et al. (2018)",
                     "https://arxiv.org/pdf/1803.01861",
                     "HSC", "22:55:38.04", "+02:51:26.60", "",
                     "6.34", "", "", "", "", "", "", "", "",
                     "", "", "", "-23.87", "0.04", "0.04", "", "", "",
                     "", "", "", "", "", "", "",
                     ""]])

entry113 = np.array([["J2211-3206/J332.8-32.10", "Decarli et al. (2018), Mazzucchelli et al. (2023)",
                     "https://iopscience.iop.org/article/10.3847/1538-4357/aaa5aa, https://arxiv.org/pdf/2306.16474",
                     "VIK/VST-ATLAS", "22:11:12.391", "-32:06:12.94", "",
                     "6.3394", "0.0010", "0.0010", "log9.27", "log0.06", "log0.07", "log47.44", "0.04", "0.05",
                     "1.15", "0.2", "0.2", "-26.71", "", "", "", "", "",
                     "", "", "", "", "", "", "",
                     "mass(CIV), L_bol, f_Edd(CIV) from Mazzucchelli et al. (2023), additional information here: https://iopscience.iop.org/article/10.3847/1538-4357/ab2f75#apjab2f75fn1 Mazzucchelli et al. (2019), https://academic.oup.com/mnras/article/478/2/1649/4944228 Chehade et al. (2018)"]])

# mass(CIV), L_bol, f_Edd(CIV) from: https://arxiv.org/pdf/2306.16474 Mazzucchelli et al. (2023)

entry114 = np.array([["J1406-0116", "Matsuoka et al. (2018), Ishimoto et al. (2020)",
                     "https://arxiv.org/pdf/1803.01861, https://iopscience.iop.org/article/10.3847/1538-4357/abb80b/pdf",
                     "HSC", "14:06:29.12", "-01:16:11.20", "",
                     "6.292", "0.002", "0.002", "", "", "", "", "", "",
                     "", "", "", "-24.76", "0.18", "0.18", "", "", "",
                     "", "", "", "", "", "", "",
                     ""]])

# z, M1450 from: https://iopscience.iop.org/article/10.3847/1538-4357/abb80b/pdf Ishimoto et al. (2020)

entry115 = np.array([["J1148+0702", "Decarli et al. (2018)",
                     "https://iopscience.iop.org/article/10.3847/1538-4357/aaa5aa",
                     "ULAS", "11:48:03.286", "+07:02:08.33", "",
                     "6.339", "0.001", "0.001", "", "", "", "", "", "",
                     "", "", "", "-26.49", "", "", "", "", "",
                     "", "", "", "", "", "", "",
                     ""]])

entry116 = np.array([["J0142-3327/J025.6-33.46", "Carnall et al. (2015)",
                     "https://academic.oup.com/mnrasl/article/451/1/L16/954689",
                     "ATLAS", "01:42:43.70", "-33:27:45.72", "",
                     "6.31", "0.03", "0.03", "", "", "", "", "", "",
                     "", "", "", "-27.8", "0.2", "0.2", "", "", "",
                     "", "", "", "", "", "", "",
                     ""]])

entry117 = np.array([["J1030+0524", "Banados et al. (2016), D'Odorico et al. (2023), Yue et al. (2024)",
                     "https://arxiv.org/pdf/1608.03279, https://academic.oup.com/mnras/article/523/1/1399/7172883, https://arxiv.org/pdf/2309.04614",
                     "SDSS", "10:30:27.11", "+05:24:55.06", "",
                     "6.304", "0.002", "0.002", "log9.187", "log0.004", "log0.003", "", "", "",
                     "0.94", "", "", "-26.99", "", "", "", "", "",
                     "", "", "", "", "", "", "",
                     "z from D'Odorico et al. (2023), mass, f_Edd from Yue et al. (2024)"]])

# z from: https://academic.oup.com/mnras/article/523/1/1399/7172883 D'Odorico et al. (2023)
# mass, f_Edd from: https://arxiv.org/pdf/2309.04614 Yue et al. (2024)

entry118 = np.array([["J1146-0005", "Matsuoka et al. (2018)",
                     "https://arxiv.org/pdf/1803.01861",
                     "HSC", "11:46:58.89", "-00:05:37.70", "",
                     "6.30", "", "", "", "", "", "", "", "",
                     "", "", "", "-21.46", "0.63", "0.63", "", "", "",
                     "", "", "", "", "", "", "",
                     ""]])

entry119 = np.array([["J1525+4303", "Matsuoka et al. (2019)",
                     "https://arxiv.org/pdf/1908.07910",
                     "HSC", "15:25:55.79", "+43:03:24.00", "",
                     "6.27", "", "", "", "", "", "", "", "",
                     "", "", "", "-23.61", "0.06", "0.06", "", "", "",
                     "", "", "", "", "", "", "",
                     ""]])

entry120 = np.array([["J0905+0300", "Matsuoka et al. (2018)",
                     "https://arxiv.org/pdf/1704.05854",
                     "HSC", "09:05:44.65", "+03:00:58.80", "",
                     "6.27", "", "", "", "", "", "", "", "",
                     "", "", "", "-22.55", "0.11", "0.11", "", "", "",
                     "", "", "", "", "", "", "",
                     ""]])

entry121 = np.array([["J1146+0124", "Matsuoka et al. (2018)",
                     "https://arxiv.org/pdf/1803.01861",
                     "HSC", "11:46:48.42", "+01:24:20.10", "",
                     "6.27", "", "", "", "", "", "", "", "",
                     "", "", "", "-23.71", "0.07", "0.07", "", "", "",
                     "", "", "", "", "", "", "",
                     ""]])

entry122 = np.array([["J1623+3112", "Ishimoto et al. (2020), Eilers et al. (2017)",
                     "https://iopscience.iop.org/article/10.3847/1538-4357/abb80b/pdf, https://iopscience.iop.org/article/10.3847/1538-4357/aa6c60",
                     "SDSS", "16:23:31.81", "+31:12:00.53", "",
                     "6.2572", "0.0024", "0.0024", "", "", "", "", "", "",
                     "", "", "", "-26.55", "", "", "", "", "",
                     "", "", "", "", "", "", "",
                     "Instrument from Eilers et al. (2017)"]])

# Instrument from: https://iopscience.iop.org/article/10.3847/1538-4357/aa6c60 Eilers et al. (2017)

entry123 = np.array([["J0050+3445", "Ishimoto et al. (2020), Eilers et al. (2017)",
                     "https://iopscience.iop.org/article/10.3847/1538-4357/abb80b/pdf, https://iopscience.iop.org/article/10.3847/1538-4357/aa6c60",
                     "CFHQS", "00:55:02.91", "+34:45:21.65", "",
                     "6.253", "0.003", "0.003", "", "", "", "", "", "",
                     "", "", "", "-26.70", "", "", "", "", "",
                     "", "", "", "", "", "", "",
                     "Instrument from Eilers et al. (2017)"]])

# Instrument from: https://iopscience.iop.org/article/10.3847/1538-4357/aa6c60 Eilers et al. (2017)

entry124 = np.array([["J0323-4701", "Eilers et al. (2020), Reed et al. (2017)",
                     "https://arxiv.org/pdf/2002.01811, https://academic.oup.com/mnras/article/468/4/4702/3089747",
                     "VDES", "03:23:40.340", "-47:11:29.400", "",
                     "6.241", "0.002", "0.002", "0.28e9", "0.20e9", "0.20e9", "log46.81", "", "",
                     "1.76", "1.24", "1.24", "-26.02", "0.07", "0.07", "", "", "",
                     "", "", "", "", "", "", "",
                     "M1450 from Reed et al. (2017)"]])

# M1450 from: https://academic.oup.com/mnras/article/468/4/4702/3089747 Reed et al. (2017)

entry125 = np.array([["J0143-5545", "Reed et al. (2017)",
                     "https://academic.oup.com/mnras/article/468/4/4702/3089747",
                     "VDES", "01:43:10.24", "-55:45:10.68", "",
                     "6.25", "0.01", "0.01", "", "", "", "", "", "",
                     "", "", "", "-25.65", "0.12", "0.12", "", "", "",
                     "", "", "", "", "", "", "",
                     ""]])

entry126 = np.array([["J0844-0052", "Matsuoka et al. (2018)",
                     "https://arxiv.org/pdf/1704.05854",
                     "HSC", "08:44:31.60", "-00:52:54.60", "",
                     "6.25", "", "", "", "", "", "", "", "",
                     "", "", "", "-23.74", "0.23", "0.23", "", "", "",
                     "", "", "", "", "", "", "",
                     ""]])

entry127 = np.array([["J2032-2114/P308-21/J308.0-21.23", "Banados et al. (2016), Decarli et al. (2018)",
                     "https://arxiv.org/pdf/1608.03279, https://iopscience.iop.org/article/10.3847/1538-4357/aaa5aa",
                     "PSO", "20:32:09.996", "-21:14:02.31", "",
                     "6.24", "0.05", "0.05", "", "", "", "", "", "",
                     "", "", "", "-26.35", "", "", "", "", "",
                     "", "", "", "", "", "", "",
                     "coordinates, z from Decarli et al. (2018)"]])

# coordinates, z from: https://iopscience.iop.org/article/10.3847/1538-4357/aaa5aa Decarli et al. (2018)

entry128 = np.array([["J1048+4637", "Banados et al. (2016)",
                     "https://arxiv.org/pdf/1608.03279",
                     "SDSS", "10:48:45.07", "+46:37:18.55", "",
                     "6.2284", "", "", "", "", "", "", "", "",
                     "", "", "", "-27.24", "", "", "", "", "",
                     "", "", "", "", "", "", "",
                     ""]])

entry129 = np.array([["J0410-4414", "Reed et al. (2017)",
                     "https://academic.oup.com/mnras/article/468/4/4702/3089747",
                     "VDES", "04:10:03.23", "-44:14:40.70", "",
                     "6.21", "0.01", "0.01", "", "", "", "", "", "",
                     "", "", "", "-26.14", "0.09", "0.09", "", "", "",
                     "", "", "", "", "", "", "",
                     ""]])

entry130 = np.array([["J0136+0226", "Banados et al. (2016), Shen et al. (2019)",
                     "https://arxiv.org/pdf/1608.03279, https://iopscience.iop.org/article/10.3847/1538-4357/ab03d9/pdf",
                     "CFHQS", "01:36:03.17", "+02:26:05.70", "",
                     "6.206", "0.009", "0.009", "", "", "", "", "", "",
                     "", "", "", "-24.66", "", "", "", "", "",
                     "", "", "", "", "", "", "",
                     "z from Shen et al. (2019)"]])

# z from: https://iopscience.iop.org/article/10.3847/1538-4357/ab03d9/pdf Shen et al. (2019)

entry131 = np.array([["J0217-0208", "Matsuoka et al. (2018)",
                     "https://arxiv.org/pdf/1704.05854",
                     "HSC", "02:17:21.59", "-02:08:52.60", "",
                     "6.20", "", "", "", "", "", "", "", "",
                     "", "", "", "-23.19", "0.04", "0.04", "", "", "",
                     "", "", "", "", "", "", "",
                     ""]])

entry132 = np.array([["J1217+0131/J184.3+01.52", "Banados et al. (2016), Wang et al. (2018)",
                     "https://arxiv.org/pdf/1608.03279, https://arxiv.org/pdf/1703.07490",
                     "PSO", "12:17:21.34", "+01:31:42.47", "",
                     "6.17", "0.05", "0.05", "", "", "", "", "", "",
                     "", "", "", "-25.37", "", "", "", "", "",
                     "", "", "", "", "", "", "",
                     "z from Wang et al. (2018)"]])

# z from: https://arxiv.org/pdf/1703.07490 Wang et al. (2018)

entry133 = np.array([["J0227-0605", "Banados et al. (2016), Shen et al. (2019)",
                     "https://arxiv.org/pdf/1608.03279, https://iopscience.iop.org/article/10.3847/1538-4357/ab03d9/pdf",
                     "CFHQS/HSC/VIK", "02:27:43.29", "-06:05:30.20", "",
                     "6.212", "0.007", "0.007", "", "", "", "", "", "",
                     "", "", "", "-25.28", "", "", "", "", "",
                     "", "", "", "", "", "", "",
                     ""]])

# Instrument from: https://iopscience.iop.org/article/10.3847/1538-4357/ab03d9/pdf Shen et al. (2019)

entry134 = np.array([["J1512+4422", "Matsuoka et al. (2019)",
                     "https://arxiv.org/pdf/1908.07910",
                     "HSC", "15:12:48.71", "+44:22:17.50", "",
                     "6.19", "", "", "", "", "", "", "", "",
                     "", "", "", "-22.07", "0.04", "0.04", "", "", "",
                     "", "", "", "", "", "", "",
                     ""]])

entry135 = np.array([["J0918+0139", "Matsuoka et al. (2018)",
                     "https://arxiv.org/pdf/1803.01861",
                     "HSC", "09:18:33.17", "+01:39:23.30", "",
                     "6.19", "", "", "", "", "", "", "", "",
                     "", "", "", "-23.71", "0.04", "0.04", "", "", "",
                     "", "", "", "", "", "", "",
                     ""]])

entry136 = np.array([["J1429+5447", "Banados et al. (2016)",
                     "https://arxiv.org/pdf/1608.03279",
                     "CFHQS", "14:29:52.17", "+54:47:17.70", "",
                     "6.1831", "", "", "", "", "", "", "", "",
                     "", "", "", "-26.10", "", "", "", "", "",
                     "", "", "", "", "", "", "",
                     ""]])

entry137 = np.array([["J2255+0503", "Matsuoka et al. (2019)",
                     "https://arxiv.org/pdf/1908.07910",
                     "HSC", "22:55:20.78", "+05:03:43.30", "",
                     "6.18", "", "", "", "", "", "", "", "",
                     "", "", "", "-24.43", "0.02", "0.02", "", "", "",
                     "", "", "", "", "", "", "",
                     ""]])

entry138 = np.array([["J1425-0015", "Matsuoka et al. (2018)",
                     "https://arxiv.org/pdf/1704.05854	",
                     "HSC", "14:25:17.72", "-00:15:40.90", "",
                     "6.18", "", "", "", "", "", "", "", "",
                     "", "", "", "-23.44", "0.02", "0.02", "", "", "",
                     "", "", "", "", "", "", "",
                     ""]])

entry139 = np.array([["J0402+2451/P060+24/J060.5+24.85", "Banados et al. (2016), Shen et al. (2019)",
                     "https://arxiv.org/pdf/1608.03279, https://iopscience.iop.org/article/10.3847/1538-4357/ab03d9/pdf",
                     "PSO", "04:02:12.69", "+24:51:24.43", "",
                     "6.170", "0.006", "0.006", "", "", "", "", "", "",
                     "", "", "", "-26.95", "", "", "", "", "",
                     "", "", "", "", "", "", "",
                     "z from Shen et al. (2019)"]])

# z from: https://iopscience.iop.org/article/10.3847/1538-4357/ab03d9/pdf Shen et al. (2019)

entry140 = np.array([["J0844-0132", "Matsuoka et al. (2018)",
                     "https://arxiv.org/pdf/1803.01861",
                     "HSC", "08:44:08.61", "-01:32:16.50", "",
                     "6.18", "", "", "", "", "", "", "", "",
                     "", "", "", "-23.97", "0.11", "0.11", "", "", "",
                     "", "", "", "", "", "", "",
                     ""]])

entry141 = np.array([["J2232+0012", "Matsuoka et al. (2018)",
                     "https://arxiv.org/pdf/1704.05854",
                     "HSC", "22:32:12.03", "+00:12:38.40", "",
                     "6.18", "", "", "", "", "", "", "", "",
                     "", "", "", "-22.81", "0.10", "0.10", "", "", "",
                     "", "", "", "", "", "", "",
                     ""]])

entry142 = np.array([["J0221-0802", "Banados et al. (2016), Shen et al. (2019)",
                     "https://arxiv.org/pdf/1608.03279, https://iopscience.iop.org/article/10.3847/1538-4357/ab03d9/pdf",
                     "CFHQS", "02:21:22.71", "-08:02:51.50", "",
                     "6.161", "0.054", "0.054", "", "", "", "", "", "",
                     "", "", "", "-24.70", "", "", "", "", "",
                     "", "", "", "", "", "", "",
                     "z from Shen et al. (2019)"]])

# z from: https://iopscience.iop.org/article/10.3847/1538-4357/ab03d9/pdf Shen et al. (2019)

entry143 = np.array([["J2201+0155", "Matsuoka et al. (2018)",
                     "https://arxiv.org/pdf/1704.05854",
                     "HSC", "22:01:32.07", "+01:55:29.00", "",
                     "6.16", "", "", "", "", "", "", "", "",
                     "", "", "", "-22.97", "0.04", "0.04", "", "", "",
                     "", "", "", "", "", "", "",
                     ""]])

entry144 = np.array([["J1146-0154", "Matsuoka et al. (2016)",
                     "https://arxiv.org/pdf/1803.01861",
                     "HSC", "11:46:32.66", "-01:54:38.30", "",
                     "6.16", "", "", "", "", "", "", "", "",
                     "", "", "", "-23.43", "0.07", "0.07", "", "", "",
                     "", "", "", "", "", "", "",
                     ""]])

entry145 = np.array([["J2219+0102/VIMOS2911001793", "Kashikawa et al. (2015)",
                     "https://arxiv.org/pdf/1410.7401",
                     "HSC", "22:19:17.22", "+01:02:48.90", "",
                     "6.156", "", "", "", "", "", "", "", "",
                     "", "", "", "-23.10", "0.11", "0.11", "", "", "",
                     "", "", "", "", "", "", "",
                     ""]])

entry146 = np.array([["J1347-0157", "Matsuoka et al. (2019)",
                     "https://arxiv.org/pdf/1908.07910",
                     "HSC", "13:47:33.69", "-01:57:50.60", "",
                     "6.15", "", "", "", "", "", "", "", "",
                     "", "", "", "-24.73", "0.02", "0.02", "", "", "",
                     "", "", "", "", "", "", "",
                     ""]])

entry147 = np.array([["J2356-0622/P359–06/J359.1-06.38", "Decarli et al. (2018), Wang et al. (2016)",
                     "https://iopscience.iop.org/article/10.3847/1538-4357/aaa5aa, https://arxiv.org/pdf/1602.04659",
                     "PSO", "23:56:32.455s", "-06:22:59.26", "",
                     "6.15", "0.02", "0.02", "", "", "", "", "", "",
                     "", "", "", "-26.79", "", "", "", "", "",
                     "", "", "", "", "", "", "",
                     "z from Wang et al. (2016)"]])

# z from: https://arxiv.org/pdf/1602.04659 Wang et al. (2016)

entry148 = np.array([["J1250+3130", "Banados et al. (2016), Ishimoto et al. (2020)",
                     "https://arxiv.org/pdf/1608.03279, https://iopscience.iop.org/article/10.3847/1538-4357/abb80b/pdf",
                     "SDSS", "12:50:51.93", "+31:30:21.90", "",
                     "6.138", "0.005", "0.005", "", "", "", "", "", "",
                     "", "", "", "-26.53", "", "", "", "", "",
                     "", "", "", "", "", "", "",
                     "z from Ishimoto et al. (2020)"]])

# z from: https://iopscience.iop.org/article/10.3847/1538-4357/abb80b/pdf Ishimoto et al. (2020)

entry149 = np.array([["J0909+0440", "Matsuoka et al. (2018)",
                     "https://arxiv.org/pdf/1803.01861",
                     "HSC", "09:09:21.50", "+04:40:42.90", "",
                     "6.15", "", "", "", "", "", "", "", "",
                     "", "", "", "-24.88", "0.02", "0.02", "", "", "",
                     "", "", "", "", "", "", "",
                     ""]])

entry150 = np.array([["J0834+0211", "Matsuoka et al. (2018)",
                     "https://arxiv.org/pdf/1803.01861",
                     "HSC", "08:34:00.88", "+02:11:46.90", "",
                     "6.15", "", "", "", "", "", "", "", "",
                     "", "", "", "-24.05", "0.09", "0.09", "", "", "",
                     "", "", "", "", "", "", "",
                     ""]])

entry151 = np.array([["J2318-3029", "Venemans et al. (2020), Decarli et al. (2018)",
                     "https://iopscience.iop.org/article/10.3847/1538-4357/abc563, https://iopscience.iop.org/article/10.3847/1538-4357/aaa5aa",
                     "VIK", "23:18:33.099", "-30:29:33.58", "",
                     "6.1456", "0.0002", "0.0002", "", "", "", "", "", "",
                     "", "", "", "-26.21", "", "", "", "", "",
                     "", "", "", "", "", "", "",
                     "M1450 from Decarli et al. (2018)"]])

# M1450 from: https://iopscience.iop.org/article/10.3847/1538-4357/aaa5aa Decarli et al. (2018)

entry152 = np.array([["J1448+4333", "Matsuoka et al. (2019)",
                     "https://arxiv.org/pdf/1908.07910",
                     "HSC", "14:48:23.33", "+43:33:05.90", "",
                     "6.14", "", "", "", "", "", "", "", "",
                     "", "", "", "-24.36", "0.04", "0.04", "", "", "",
                     "", "", "", "", "", "", "",
                     ""]])

entry153 = np.array([["J0421-2657/P065–26/J065.4-26.95", "Decarli et al. (2018), Banados et al. (2016)",
                     "https://iopscience.iop.org/article/10.3847/1538-4357/aaa5aa, https://arxiv.org/pdf/1608.03279",
                     "PSO", "04:21:38.052", "-26:57:15.60", "",
                     "6.14", "0.05", "0.05", "", "", "", "", "", "",
                     "", "", "", "-27.25", "", "", "", "", "",
                     "", "", "", "", "", "", "",
                     "M1450 from Banados et al. (2016)"]])

# M1450 from: https://arxiv.org/pdf/1608.03279 Banados et al. (2016)

entry154 = np.array([["J1401+2749/J210.4+27.82", "Banados et al. (2016)",
                     "https://arxiv.org/pdf/1608.03279",
                     "PSO", "14:01:47.34", "+27:49:35.03", "",
                     "6.14", "", "", "", "", "", "", "", "",
                     "", "", "", "-26.54", "", "", "", "", "",
                     "", "", "", "", "", "", "",
                     ""]])

entry155 = np.array([["J1609+3041", "Banados et al. (2016)",
                     "https://arxiv.org/pdf/1608.03279",
                     "ULAS", "16:09:37.27", "+30:41:47.78", "",
                     "6.14", "", "", "", "", "", "", "", "",
                     "", "", "", "-26.38", "", "", "", "", "",
                     "", "", "", "", "", "", "",
                     ""]])

entry156 = np.array([["J1431-0724/J217.9-07.41", "Banados et al. (2016)",
                     "https://arxiv.org/pdf/1608.03279",
                     "PSO", "14:31:40.45", "-07:24:43.47", "",
                     "6.14", "", "", "", "", "", "", "", "",
                     "", "", "", "-26.35", "", "", "", "", "",
                     "", "", "", "", "", "", "",
                     ""]])

entry157 = np.array([["J1319+0950", "D'Odorico et al. (2023), Venemans et al. (2020), Banados et al. (2016)",
                     "https://academic.oup.com/mnras/article/523/1/1399/7172883, https://iopscience.iop.org/article/10.3847/1538-4357/abc563, https://arxiv.org/pdf/1608.03279",
                     "ULAS", "13:19:11.291", "+09:50:51.49", "",
                     "6.1347", "0.0005", "0.0005", "log9.53", "log0.05", "log0.05", "", "", "",
                     "", "", "", "-27.05", "", "", "", "", "",
                     "", "", "", "", "", "", "",
                     "coordinates from Venemans et al. (2020), M1450 from Banados et al. (2016)"]])

# coordinates from: https://iopscience.iop.org/article/10.3847/1538-4357/abc563 Venemans et al. (2020)
# M1450 from: https://arxiv.org/pdf/1608.03279 Banados et al. (2016)

entry158 = np.array([["J1516+4228", "Matsuoka et al. (2019)",
                     "https://arxiv.org/pdf/1908.07910",
                     "HSC", "15:16:57.87", "+42:28:52.90", "",
                     "6.13", "", "", "", "", "", "", "", "",
                     "", "", "", "-24.35", "0.01", "0.01", "", "", "",
                     "", "", "", "", "", "", "",
                     ""]])

entry159 = np.array([["J0001+0006", "Matsuoka et al. (2019)",
                     "https://arxiv.org/pdf/1908.07910",
                     "HSC", "00:01:33.30", "+00:06:05.40", "",
                     "6.13", "", "", "", "", "", "", "", "",
                     "", "", "", "-23.72", "0.06", "0.06", "", "", "",
                     "", "", "", "", "", "", "",
                     ""]])

entry160 = np.array([["J1254-0014", "Matsuoka et al. (2019)",
                     "https://arxiv.org/pdf/1908.07910",
                     "HSC", "12:54:37.08", "-00:14:10.70", "",
                     "6.13", "", "", "", "", "", "", "", "",
                     "", "", "", "-20.91", "0.32", "0.32", "", "", "",
                     "", "", "", "", "", "", "",
                     ""]])

entry161 = np.array([["J1440-0107", "Matsuoka et al. (2018)",
                     "https://arxiv.org/pdf/1704.05854",
                     "HSC", "14:40:01.30", "-01:07:02.20", "",
                     "6.13", "", "", "", "", "", "", "", "",
                     "", "", "", "-22.59", "0.10", "0.10", "", "", "",
                     "", "", "", "", "", "", "",
                     ""]])

entry162 = np.array([["J1423-0018", "Matsuoka et al. (2018)",
                     "https://arxiv.org/pdf/1704.05854",
                     "HSC", "14:23:31.71", "-00:18:09.10", "",
                     "6.13", "", "", "", "", "", "", "", "",
                     "", "", "", "-21.88", "0.20", "0.20", "", "", "",
                     "", "", "", "", "", "", "",
                     ""]])

entry163 = np.array([["J0033-0125", "Banados et al. (2016), Shen et al. (2019)",
                     "https://arxiv.org/pdf/1608.03279, https://iopscience.iop.org/article/10.3847/1538-4357/ab03d9/pdf",
                     "CFHQS", "00:33:11.40", "-01:25:24.90", "",
                     "5.978", "0.010", "0.010", "", "", "", "", "", "",
                     "", "", "", "-25.14", "", "", "", "", "",
                     "", "", "", "", "", "", "",
                     "z from Shen et al. (2019)"]])

# z from: https://iopscience.iop.org/article/10.3847/1538-4357/ab03d9/pdf Shen et al. (2019)

entry164 = np.array([["J1509-1749", "Decarli et al. (2018), D'Odorico et al. (2023)",
                     "https://iopscience.iop.org/article/10.3847/1538-4357/aaa5aa, https://academic.oup.com/mnras/article/523/1/1399/7172883",
                     "CFHQS", "15:09:41.778", "-17:49:26.80", "",
                     "6.1225", "0.0007", "0.0006", "log9.30", "log0.15", "log0.22", "", "", "",
                     "", "", "", "-27.14", "", "", "", "", "",
                     "", "", "", "", "", "", "",
                     "mass from D'Odorico et al. (2023)"]])

# mass from: https://academic.oup.com/mnras/article/523/1/1399/7172883 D'Odorico et al. (2023)

entry165 = np.array([["J0422-1927/P065–19/J065.5-19.45", "Decarli et al. (2018)",
                     "https://iopscience.iop.org/article/10.3847/1538-4357/aaa5aa",
                     "PSO", "04:22:00.994", "-19:27:28.68", "",
                     "6.12", "0.05", "0.05", "", "", "", "", "", "",
                     "", "", "", "-26.62", "", "", "", "", "",
                     "", "", "", "", "", "", "",
                     ""]])

entry166 = np.array([["J1427+3312", "Banados et al. (2016), Khusanova et al. (2022)",
                     "https://arxiv.org/pdf/1608.03279, https://www.aanda.org/articles/aa/full_html/2022/08/aa43660-22/aa43660-22.html",
                     "FIRST", "14:27:38.59", "+33:12:42.00", "",
                     "6.12", "", "", "", "", "", "", "", "",
                     "", "", "", "-26.10", "", "", "", "", "",
                     "30-90", "", "", "", "", "", "",
                     "SFR_CII from Khusanova et al. (2022)"]])

# SFR_CII from: https://www.aanda.org/articles/aa/full_html/2022/08/aa43660-22/aa43660-22.html Khusanova et al. (2022)

entry167 = np.array([["J2315-0023", "Banados et al. (2016), Jiang et al. (2008)",
                     "https://arxiv.org/pdf/1608.03279, https://iopscience.iop.org/article/10.1088/0004-6256/135/3/1057",
                     "SDSS", "23:15:46.57", "-00:23:58.10", "",
                     "6.117", "0.006", "0.006", "", "", "", "", "", "",
                     "", "", "", "-25.14", "", "", "", "", "",
                     "", "", "", "", "", "", "",
                     "z from Jiang et al. (2008)"]])

# z from: https://iopscience.iop.org/article/10.1088/0004-6256/135/3/1057 Jiang et al. (2008)

entry168 = np.array([["J2252+0225", "Matsuoka et al. (2018)",
                     "https://arxiv.org/pdf/1803.01861",
                     "HSC", "22:52:05.44", "+02:25:31.90", "",
                     "6.12", "", "", "", "", "", "", "", "",
                     "", "", "", "-22.74", "0.06", "0.06", "", "", "",
                     "", "", "", "", "", "", "",
                     ""]])

entry169 = np.array([["J1558-0724/J239.7-07.40", "Banados et al. (2016)",
                     "https://arxiv.org/pdf/1608.03279",
                     "PSO", "15:58:50.99", "-07:24:09.59", "",
                     "6.11", "", "", "", "", "", "", "", "",
                     "", "", "", "-27.46", "", "", "", "", "",
                     "", "", "", "", "", "", "",
                     ""]])

entry170 = np.array([["J1428-1602/P217–16/J217.0-16.04", "Decarli et al. (2018)",
                     "https://iopscience.iop.org/article/10.3847/1538-4357/aaa5aa",
                     "PSO", "14:28:21.394", "-16:02:43.29", "",
                     "6.11", "0.05", "0.05", "", "", "", "", "", "",
                     "", "", "", "-26.93", "", "", "", "", "",
                     "", "", "", "", "", "", "",
                     ""]])

entry171 = np.array([["J0004-0049", "Matsuoka et al. (2019)",
                     "https://arxiv.org/pdf/1908.07910",
                     "HSC", "00:04:45.81", "-00:49:44.30", "",
                     "6.10", "", "", "", "", "", "", "", "",
                     "", "", "", "-23.90", "0.06", "0.06", "", "", "",
                     "", "", "", "", "", "", "",
                     ""]])

entry172 = np.array([["J0454-4448", "Reed et al. (2017), Decarli et al. (2018)",
                     "https://academic.oup.com/mnras/article/468/4/4702/3089747, https://iopscience.iop.org/article/10.3847/1538-4357/aaa5aa",
                     "VDES", "04:54:01.79", "-44:48:31.10", "",
                     "6.0581", "0.0006", "0.0006", "", "", "", "", "", "",
                     "", "", "", "-26.36", "0.05", "0.05", "", "", "",
                     "", "", "", "", "", "", "",
                     "z from Decarli et al. (2018)"]])

# z from: https://iopscience.iop.org/article/10.3847/1538-4357/aaa5aa Decarli et al. (2018)

entry173 = np.array([["J0009+3252/J002.3+32.87", "Banados et al. (2016)",
                     "https://arxiv.org/pdf/1608.03279",
                     "PSO", "00:09:30.89", "+32:52:12.94", "",
                     "6.10", "", "", "", "", "", "", "", "",
                     "", "", "", "-25.65", "", "", "", "", "",
                     "", "", "", "", "", "", "",
                     ""]])

entry174 = np.array([["J1406-0144", "Matsuoka et al. (2018)",
                     "https://arxiv.org/pdf/1803.01861",
                     "HSC", "14:06:46.88", "-01:44:02.60", "",
                     "6.10", "", "", "", "", "", "", "", "",
                     "", "", "", "-23.37", "0.16", "0.16", "", "", "",
                     "", "", "", "", "", "", "",
                     ""]])

entry175 = np.array([["J0235-0532", "Matsuoka et al. (2018)",
                     "https://arxiv.org/pdf/1704.05854",
                     "HSC", "02:35:42.42", "-05:32:41.60", "",
                     "6.09", "", "", "", "", "", "", "", "",
                     "", "", "", "-23.01", "0.05", "0.05", "", "", "",
                     "", "", "", "", "", "", "",
                     ""]])

entry176 = np.array([["J1602+4228", "Banados et al. (2016), Ishimoto et al. (2020)",
                     "https://arxiv.org/pdf/1608.03279, https://iopscience.iop.org/article/10.3847/1538-4357/abb80b/pdf",
                     "SDSS", "16:02:53.98", "+42:28:24.94", "",
                     "6.083", "0.005", "0.005", "", "", "", "", "", "",
                     "", "", "", "-26.94", "", "", "", "", "",
                     "", "", "", "", "", "", "",
                     ""]])

# z from: https://iopscience.iop.org/article/10.3847/1538-4357/abb80b/pdf Ishimoto et al. (2020)

entry177 = np.array([["J0935-0110", "Matsuoka et al. (2019)",
                     "https://arxiv.org/pdf/1908.07910",
                     "HSC", "09:35:43.32", "-01:10:33.30", "",
                     "6.08", "", "", "", "", "", "", "", "",
                     "", "", "", "-21.97", "0.18", "0.28", "", "", "",
                     "", "", "", "", "", "", "",
                     ""]])

entry178 = np.array([["J2228+0152", "Matsuoka et al. (2018), Ishimoto et al. (2020)",
                     "https://arxiv.org/pdf/1704.05854, https://iopscience.iop.org/article/10.3847/1538-4357/abb80b/pdf",
                     "HSC", "22:28:47.71", "+01:52:40.50", "",
                     "6.0805", "0.0004", "0.0004", "", "", "", "", "", "",
                     "", "", "", "-24.00", "0.04", "0.04", "", "", "",
                     "", "", "", "", "", "", "",
                     "z from Ishimoto et al. (2020)"]])

# z from: https://iopscience.iop.org/article/10.3847/1538-4357/abb80b/pdf Ishimoto et al. (2020)

entry179 = np.array([["J1932+7139/J293.0+71.65", "Banados et al. (2016)",
                     "https://arxiv.org/pdf/1608.03279",
                     "PSO", "19:32:07.62", "+71:39:08.41", "",
                     "6.08", "", "", "", "", "", "", "", "",
                     "", "", "", "-26.92", "", "", "", "", "",
                     "", "", "", "", "", "", "",
                     ""]])

entry180 = np.array([["J0303-0019", "Banados et al. (2016), Kurk et al. (2009), Ishimoto et al. (2020)",
                     "https://arxiv.org/pdf/1608.03279, https://iopscience.iop.org/article/10.1088/0004-637X/702/2/833, https://iopscience.iop.org/article/10.3847/1538-4357/abb80b/pdf",
                     "SDSS", "03:03:31.40", "-00:19:12.90", "",
                     "6.078", "0.007", "0.007", "2e8", "1e8", "0.5e8", "", "", "",
                     "1.6", "0.4", "0.6", "-25.56", "", "", "", "", "",
                     "", "", "", "", "", "", "",
                     "mass, f_Edd from Kurk et al. (2009), z from Ishimoto et al. (2020)"]])

# mass, f_Edd from: https://iopscience.iop.org/article/10.1088/0004-637X/702/2/833 Kurk et al. (2009)
# z from: https://iopscience.iop.org/article/10.3847/1538-4357/abb80b/pdf Ishimoto et al. (2020)

entry181 = np.array([["J0353+0104", "Banados et al. (2016), Shen et al. 92019",
                     "https://arxiv.org/pdf/1608.03279, https://iopscience.iop.org/article/10.3847/1538-4357/ab03d9/pdf",
                     "SDSS", "03:53:49.73:", "01:04:04.66", "",
                     "6.057", "0.005", "0.005", "", "", "", "", "", "",
                     "", "", "", "-26.43", "", "", "", "", "",
                     "", "", "", "", "", "", "",
                     "z from Shen et al. (2019), additional information (mass, f_Edd) here: https://iopscience.iop.org/article/10.1088/0004-637X/739/2/56#apj398369fd4 De Rosa et al. (2011)"]])

# z from: https://iopscience.iop.org/article/10.3847/1538-4357/ab03d9/pdf Shen et al. (2019)

entry182 = np.array([["J1034-1425/J158.6-14.42", "Chehade et al. (2018)",
                     "https://academic.oup.com/mnras/article/478/2/1649/4944228",
                     "VST-ATLAS", "10:34:46.51", "-14:25:15.96", "",
                     "6.07", "0.03", "0.03", "", "", "", "", "", "",
                     "", "", "", "-27.23", "0.08", "0.08", "", "", "",
                     "", "", "", "", "", "", "",
                     ""]])

entry183 = np.array([["J1559+2212", "Wang et al. (2018)",
                     "https://arxiv.org/pdf/1703.07490",
                     "DELS", "15:59:09.09", "+22:12:14.43", "",
                     "6.07", "0.02", "0.02", "", "", "", "", "", "",
                     "", "", "", "-25.83", "", "", "", "", "",
                     "", "", "", "", "", "", "",
                     ""]])

entry184 = np.array([["J0420-4453", "Reed et al. (2017)",
                     "https://academic.oup.com/mnras/article/468/4/4702/3089747",
                     "VDES", "04:20:11.34", "-44:53:23.80", "",
                     "6.07", "0.01", "0.01", "", "", "", "", "", "",
                     "", "", "", "-26.25", "0.06", "0.06", "", "", "",
                     "", "", "", "", "", "", "",
                     ""]])

entry185 = np.array([["J0911+0152", "Matsuoka et al. (2018)",
                     "https://arxiv.org/pdf/1704.05854",
                     "HSC", "09:11:14.27", "+01:52:19.40", "",
                     "6.07", "", "", "", "", "", "", "", "",
                     "", "", "", "-22.09", "0.07", "0.07", "", "", "",
                     "", "", "", "", "", "", "",
                     ""]])

entry186 = np.array([["J1416+0147", "Matsuoka et al. (2018)",
                     "https://arxiv.org/pdf/1803.01861",
                     "HSC", "14:16:53.01", "+01:47:02.20", "",
                     "6.07", "", "", "", "", "", "", "", "",
                     "", "", "", "-23.27", "0.10", "0.10", "", "", "",
                     "", "", "", "", "", "", "",
                     ""]])

entry187 = np.array([["J0842+1218", "Banados et al. (2016), Venemans et al. (2020), D'Odorico et al. (2023), Mazzucchelli et al. (2023)",
                     "https://arxiv.org/pdf/1608.03279, https://iopscience.iop.org/article/10.3847/1538-4357/abc563, https://academic.oup.com/mnras/article/523/1/1399/7172883, https://arxiv.org/pdf/2306.16474",
                     "SDSS/UHS", "08:42:29.438", "+12:18:50.47", "",
                     "6.0754", "0.0005", "0.0005", "log9.30", "log0.07", "log0.09", "log47.25", "log0.05", "log0.05",
                     "0.68", "0.15", "0.15", "-26.91", "", "", "", "", "",
                     "", "", "", "", "", "", "",
                     "coordinates, z from Venemans et al. (2020), mass from D'Odorico et al. (2023), L_bol, f_Edd (MgII) from Mazzucchelli et al. (2023), instrument from Shen et al. (2019)"]])

# coordinates, z from: https://iopscience.iop.org/article/10.3847/1538-4357/abc563 Venemans et al. (2020)
# mass from: https://academic.oup.com/mnras/article/523/1/1399/7172883 D'Odorico et al. (2023)
# L_bol, f_Edd (MgII) from: https://arxiv.org/pdf/2306.16474 Mazzucchelli et al. (2023)
# instrument from: https://iopscience.iop.org/article/10.3847/1538-4357/ab03d9/pdf Shen et al. (2019)

entry188 = np.array([["J1630+4012", "Banados et al. (2016), Ishimoto et al. (2020)",
                     "https://arxiv.org/pdf/1608.03279, https://iopscience.iop.org/article/10.3847/1538-4357/abb80b/pdf",
                     "SDSS", "16:30:33.90", "+40:12:09.69", "",
                     "6.065", "0.007", "0.007", "", "", "", "", "", "",
                     "", "", "", "-26.19", "", "", "", "", "",
                     "", "", "", "", "", "", "",
                     "z from Ishimoto et al. (2020)"]])

# z from: https://iopscience.iop.org/article/10.3847/1538-4357/abb80b/pdf Ishimoto et al. (2020)

entry189 = np.array([["J0106-0030", "Matsuoka et al. (2019)",
                     "https://arxiv.org/pdf/1908.07910",
                     "HSC", "01:06:03.68", "-00:30:15.20", "",
                     "6.06", "", "", "", "", "", "", "", "",
                     "", "", "", "-23.53", "0.05", "0.05", "", "", "",
                     "", "", "", "", "", "", "",
                     ""]])

entry190 = np.array([["J1201+0133", "Matsuoka et al. (2018)",
                     "https://arxiv.org/pdf/1704.05854",
                     "HSC", "12:01:03.02", "+01:33:56.40", "",
                     "6.06", "", "", "", "", "", "", "", "",
                     "", "", "", "-23.85", "0.02", "0.02", "", "", "",
                     "", "", "", "", "", "", "",
                     ""]])

entry191 = np.array([["J0559-1534/J089.9-15.58", "Banados et al. (2016)",
                     "https://arxiv.org/pdf/1608.03279",
                     "PSO", "05:59:45.47", "-15:35:00.20", "",
                     "6.05", "", "", "", "", "", "", "", "",
                     "", "", "", "-26.93", "", "", "", "", "",
                     "", "", "", "", "", "", "",
                     ""]])

entry192 = np.array([["J0828+2633", "Banados et al. (2016)",
                     "https://arxiv.org/pdf/1608.03279",
                     "ULAS", "08:28:13.41", "+26:33:55.49", "",
                     "6.05", "", "", "", "", "", "", "", "",
                     "", "", "", "-26.37", "", "", "", "", "",
                     "", "", "", "", "", "", "",
                     ""]])

entry193 = np.array([["J2223+0326", "Matsuoka et al. (2018)",
                     "https://arxiv.org/pdf/1803.01861",
                     "HSC", "22:23:09.51", "+03:26:20.30", "",
                     "6.05", "", "", "", "", "", "", "", "",
                     "", "", "", "-25.20", "0.02", "0.02", "", "", "",
                     "", "", "", "", "", "", "",
                     ""]])

entry194 = np.array([["J2318-0246", "Banados et al. (2016)",
                     "https://arxiv.org/pdf/1608.03279",
                     "CFHQS", "23:18:02.80", "-02:46:34.00", "",
                     "6.05", "", "", "", "", "", "", "", "",
                     "", "", "", "-25.10", "", "", "", "", "",
                     "", "", "", "", "", "", "",
                     ""]])

entry195 = np.array([["J0957+0053", "Matsuoka et al. (2018)",
                     "https://arxiv.org/pdf/1803.01861",
                     "HSC", "09:57:40.39", "+00:53:33.60", "",
                     "6.05", "", "", "", "", "", "", "", "",
                     "", "", "", "-22.98", "0.04", "0.04", "", "", "",
                     "", "", "", "", "", "", "",
                     ""]])

entry196 = np.array([["J1641+3755", "Banados et al. (2016), Willott et al. (2010)",
                     "https://arxiv.org/pdf/1608.03279, https://iopscience.iop.org/article/10.1088/0004-6256/140/2/546",
                     "CFHQS", "16:41:21.73", "+37:55:20.15", "",
                     "6.047", "0.003", "0.003", "2.4e8", "1.0e8", "0.8e8", "", "", "",
                     "2.3", "", "", "-25.67", "", "", "", "", "",
                     "", "", "", "", "", "", "",
                     "z, mass, f_Edd from Willott et al. (2010)"]])

# z, mass, f_Edd from: https://iopscience.iop.org/article/10.1088/0004-6256/140/2/546 Willott et al. (2010)

entry197 = np.array([["J1603+5510/ELAIS1091000446", "Kashikawa et al. (2015)",
                     "https://iopscience.iop.org/article/10.1088/0004-637X/798/1/28",
                     "HSC", "16:03:49.07", "+55:10:32.30", "",
                     "6.041", "", "", "", "", "", "", "", "",
                     "", "", "", "-22.58", "0.13", "0.13", "", "", "",
                     "", "", "", "", "", "", "",
                     ""]])

entry198 = np.array([["J1429-0002", "Matsuoka et al. (2018)",
                     "https://arxiv.org/pdf/1704.05854",
                     "HSC", "14:29:20.22", "-00:02:07.40", "",
                     "6.04", "", "", "", "", "", "", "", "",
                     "", "", "", "-23.42", "0.04", "0.04", "", "", "",
                     "", "", "", "", "", "", "",
                     ""]])

entry199 = np.array([["J1207+0630", "Decarli et al. (2018), Banados et al. (2016)",
                     "https://iopscience.iop.org/article/10.3847/1538-4357/aaa5aa, https://arxiv.org/pdf/1608.03279",
                     "ULAS", "12:07:37.440", "+06:30:10.37", "",
                     "6.040", "0.003", "0.003", "", "", "", "", "", "",
                     "", "", "", "-26.63", "", "", "", "", "",
                     "", "", "", "", "", "", "",
                     "M1450 from Banados et al. (2016)"]])

# M1450 from: https://arxiv.org/pdf/1608.03279 Banados et al. (2016)

entry200 = np.array([["J1402+4024/J210.7+40.40", "Banados et al. (2016)",
                     "https://arxiv.org/pdf/1608.03279",
                     "PSO", "14:02:54.67", "+40:24:03.19", "",
                     "6.04", "", "", "", "", "", "", "", "",
                     "", "", "", "-25.86", "", "", "", "", "",
                     "", "", "", "", "", "", "",
                     ""]])

entry201 = np.array([["J1400-0125", "Matsuoka et al. (2018)",
                     "https://arxiv.org/pdf/1803.01861",
                     "HSC", "14:00:29.99", "-01:25:21.00", "",
                     "6.04", "", "", "", "", "", "", "", "",
                     "", "", "", "-23.70", "0.05", "0.05", "", "", "",
                     "", "", "", "", "", "", "",
                     ""]])

entry202 = np.array([["J1400-0011", "Matsuoka et al. (2018)",
                     "https://arxiv.org/pdf/1803.01861",
                     "HSC", "14:00:28.79", "-00:11:51.50", "",
                     "6.04", "", "", "", "", "", "", "", "",
                     "", "", "", "-22.95", "0.11", "0.11", "", "", "",
                     "", "", "", "", "", "", "",
                     ""]])

entry203 = np.array([["J2054-0005", "Banados et al. (2020), Wang et al. (2013), Willott et al. (2015)",
                     "https://arxiv.org/pdf/1608.03279, https://iopscience.iop.org/article/10.1088/0004-637X/773/1/44, https://iopscience.iop.org/article/10.1088/0004-637X/801/2/123#apj509348t2",
                     "SDSS", "20:54:06.49", "-00:05:14.80", "",
                     "6.0391", "0.0001", "0.0001", "0.9e9", "1.6e9", "0.6e9", "", "", "",
                     "", "", "", "-26.21", "", "", "", "", "",
                     "", "", "", "", "", "", "",
                     "z from Wang et al. (2013), mass from Willott et al. (2015)"]])

# z from: https://iopscience.iop.org/article/10.1088/0004-637X/773/1/44 Wang et al. (2013)
# mass from: https://iopscience.iop.org/article/10.1088/0004-637X/801/2/123#apj509348t2 Willott et al. (2015)

entry204 = np.array([["J0408-5632", "D'Odorico et al. (2023), Mazzucchelli et al. (2023), Reed et al. (2017)",
                     "https://academic.oup.com/mnras/article/523/1/1399/7172883, https://arxiv.org/pdf/2306.16474, https://academic.oup.com/mnras/article/468/4/4702/3089747",
                     "VDES", "04:08:19.23", "-56:32:28.80", "",
                     "6.033", "0.004", "0.004", "log9.31", "log0.08", "log0.09", "log47.19", "log0.08", "log0.1",
                     "0.57", "0.16", "0.16", "-26.51", "0.05", "0.05", "", "", "",
                     "", "", "", "", "", "", "",
                     "L_bol, f_Edd (Mg II) from Mazzucchelli et al. (2023), M1450 from Reed et al. (2017)"]])

# L_bol, f_Edd (Mg II) from: https://arxiv.org/pdf/2306.16474 Mazzucchelli et al. (2023)
# M1450 from: https://academic.oup.com/mnras/article/468/4/4702/3089747 Reed et al. (2017)

entry205 = np.array([["J0206-0255", "Mastuoka et al. (2018)",
                     "https://arxiv.org/pdf/1704.05854",
                     "HSC/DELS", "02:06:11.20", "-02:55:37.80", "",
                     "6.03", "", "", "", "", "", "", "", "",
                     "", "", "", "-24.91", "0.03", "0.03", "", "", "",
                     "", "", "", "", "", "", "",
                     "additional information here: https://iopscience.iop.org/article/10.3847/1538-4357/ab2be5/pdf Wang et al. (2019)"]])

entry206 = np.array([["J0202-0251", "Matsuoka et al. (2018)",
                     "https://arxiv.org/pdf/1704.05854	",
                     "HSC", "02:02:58.21", "-02:51:53.60", "",
                     "6.03", "", "", "", "", "", "", "", "",
                     "", "", "", "-23.39", "0.07", "0.07", "", "", "",
                     "", "", "", "", "", "", "",
                     ""]])

entry207 = np.array([["J1416+0015", "Matsuoka et al. (2018)",
                     "https://arxiv.org/pdf/1704.05854",
                     "HSC", "14:16:12.71", "+00:15:46.20", "",
                     "6.03", "", "", "", "", "", "", "", "",
                     "", "", "", "-22.39", "0.10", "0.10", "", "", "",
                     "", "", "", "", "", "", "",
                     ""]])

entry208 = np.array([["J1137+3549", "Banados et al. (2016), Ishimoto et al. (2020), Shen et al. (2019)",
                     "https://arxiv.org/pdf/1608.03279, https://iopscience.iop.org/article/10.3847/1538-4357/abb80b/pdf, https://iopscience.iop.org/article/10.3847/1538-4357/ab03d9/pdf",
                     "SDSS/UHS", "11:37:17.73", "+35:49:56.85", "",
                     "6.009", "0.010", "0.010", "", "", "", "", "", "",
                     "", "", "", "-27.36", "", "", "", "", "",
                     "", "", "", "", "", "", "",
                     "z from Ishimoto et al. (2020), instrument from Shen et al. (2019)"]])

# z from: https://iopscience.iop.org/article/10.3847/1538-4357/abb80b/pdf Ishimoto et al. (2020)
# instrument from: https://iopscience.iop.org/article/10.3847/1538-4357/ab03d9/pdf Shen et al. (2019)

entry209 = np.array([["J2215+2606/J333.9+26.10", "Banados et al. (2016)",
                     "https://arxiv.org/pdf/1608.03279",
                     "PSO", "22:15:56.63", "+26:06:29.41", "",
                     "6.03", "", "", "", "", "", "", "", "",
                     "", "", "", "-26.44", "", "", "", "", "",
                     "", "", "", "", "", "", "",
                     ""]])

entry210= np.array([["J1417+0117", "Matsuoka et al. (2018)",
                     "https://arxiv.org/pdf/1704.05854",
                     "HSC", "14:17:28.67", "+01:17:12.40", "",
                     "6.02", "", "", "", "", "", "", "", "",
                     "", "", "", "-22.83", "0.05", "0.05", "", "", "",
                     "", "", "", "", "", "", "",
                     ""]])

entry211 = np.array([["J0818+1722", "Banados et al. (2016), D'Odorico et al. (2023)",
                     "https://arxiv.org/pdf/1608.03279, https://academic.oup.com/mnras/article/523/1/1399/7172883",
                     "SDSS", "08:18:27.40", "+17:22:52.01", "",
                     "5.960", "0.010", "0.010", "log9.76", "log0.06", "log0.08", "", "", "",
                     "", "", "", "-27.52", "", "", "", "", "",
                     "", "", "", "", "", "", "",
                     "z, mass from D'Odorico et al. (2023)"]])

# z, mass from: https://academic.oup.com/mnras/article/523/1/1399/7172883 D'Odorico et al. (2023)

entry212 = np.array([["J0159-3633/J029.9-36.56", "Carnall et al. (2015), Chehade et al. (2018)",
                     "https://academic.oup.com/mnrasl/article/451/1/L16/954689, https://academic.oup.com/mnras/article/478/2/1649/4944228",
                     "ATLAS", "01:59:57.96", "-36:33:56.88", "",
                     "6.02", "0.03", "0.03", "", "", "", "", "", "",
                     "", "", "", "-26.97", "0.08", "0.08", "", "", "",
                     "", "", "", "", "", "", "",
                     "M1450 from Chehade et al. (2018)"]])

# M1450 from: https://academic.oup.com/mnras/article/478/2/1649/4944228 Chehade et al. (2018)

entry213 = np.array([["J1257+6349", "Banados et al. (2016), Jiang et al. (2015)",
                     "https://arxiv.org/pdf/1608.03279, https://iopscience.iop.org/article/10.1088/0004-6256/149/6/188",
                     "SDSS", "12:57:57.48", "+63:49:37.16", "",
                     "6.02", "0.03", "0.03", "", "", "", "", "", "",
                     "", "", "", "-26.14", "0.12", "0.12", "", "", "",
                     "", "", "", "", "", "", "",
                     "z, M1450 from Jiang et al. (2015)"]])

# z, M1450 from: https://iopscience.iop.org/article/10.1088/0004-6256/149/6/188 Jiang et al. (2015)

entry214 = np.array([["J1306+0356", "Venemans et al. (2020), Banados et al. (2016), D'Odorico et al. (2023)",
                     "https://iopscience.iop.org/article/10.3847/1538-4357/abc563, https://arxiv.org/pdf/1608.03279, https://academic.oup.com/mnras/article/523/1/1399/7172883",
                     "SDSS", "13:06:08.259", "+03:56:26.19", "",
                     "6.0330", "0.0002", "0.0002", "log9.29", "log0.09", "log0.12", "", "", "",
                     "", "", "", "-26.81", "", "", "", "", "",
                     "", "", "", "", "", "", "",
                     "M1450 from Banados et al. (2016), mass from D'Odorico et al. (2023)"]])

# M1450 from: https://arxiv.org/pdf/1608.03279 Banados et al. (2016)
# mass from: https://academic.oup.com/mnras/article/523/1/1399/7172883 D'Odorico et al. (2023)

entry215 = np.array([["J0902+0155", "Matsuoka et al. (2018)",
                     "https://arxiv.org/pdf/1704.05854",
                     "HSC", "09:02:54.87", "+01:55:10.90", "",
                     "6.01", "", "", "", "", "", "", "", "",
                     "", "", "", "-22.51", "0.04", "0.04", "", "", "",
                     "", "", "", "", "", "", "",
                     ""]])

entry216 = np.array([["J0853+0139", "Matsuoka et al. (2018)",
                     "https://arxiv.org/pdf/1704.05854",
                     "HSC", "08:53:48.84", "+01:39:11.00", "",
                     "6.01", "", "", "", "", "", "", "", "",
                     "", "", "", "-22.51", "0.14", "0.14", "", "", "",
                     "", "", "", "", "", "", "",
                     ""]])

entry217 = np.array([["J2240-1839/P340–18/J340.2-18.66", "Decarli et al. (2018), Chehade etal. (2018)",
                     "https://iopscience.iop.org/article/10.3847/1538-4357/aaa5aa, https://academic.oup.com/mnras/article/478/2/1649/4944228",
                     "PSO", "22:40:48.997", "−18:39:43.81", "",
                     "6.01", "0.05", "0.05", "", "", "", "", "", "",
                     "", "", "", "-26.42", "0.10", "0.10", "", "", "",
                     "", "", "", "", "", "", "",
                     "M1450 from Chehade et al. (2018)"]])

# M1450 from: https://academic.oup.com/mnras/article/478/2/1649/4944228 Chehade et al. (2018)

entry218 = np.array([["J1219+0050", "Matsuoka et al. (2018)",
                     "https://arxiv.org/pdf/1803.01861",
                     "HSC", "12:19:05.34", "+00:50:37.50", "",
                     "6.01", "", "", "", "", "", "", "", "",
                     "", "", "", "-23.85", "0.05", "0.05", "", "", "",
                     "", "", "", "", "", "", "",
                     ""]])

entry219 = np.array([["J1207-0005", "Matsuoka et al. (2016)",
                     "https://iopscience.iop.org/article/10.3847/0004-637X/828/1/26",
                     "HSC", "12:07:54.14", "-00:05:53.30", "",
                     "6.01", "", "", "", "", "", "", "", "",
                     "", "", "", "-22.59", "0.08", "0.08", "", "", "",
                     "", "", "", "", "", "", "",
                     ""]])

entry220 = np.array([["J0216-0455", "Willott et al. (2009), Banados et al. (2016)",
                     "https://iopscience.iop.org/article/10.1088/0004-6256/137/3/3541, https://arxiv.org/pdf/1608.03279",
                     "CFHQS", "02:16:27.81", "-04:55:34.10", "",
                     "6.01", "", "", "", "", "", "", "", "",
                     "", "", "", "-22.49", "", "", "", "", "",
                     "", "", "", "", "", "", "",
                     ""]])

# M1450 from: https://arxiv.org/pdf/1608.03279 Banados et al. (2016)

entry221 = np.array([["J2228+0128", "Matsuoka et al. (2016)",
                     "https://iopscience.iop.org/article/10.3847/0004-637X/828/1/26",
                     "HSC", "22:28:27.83", "+01:28:09.50", "",
                     "6.01", "", "", "", "", "", "", "", "",
                     "", "", "", "-22.40", "0.12", "0.12", "", "", "",
                     "", "", "", "", "", "", "",
                     ""]])

entry222 = np.array([["J1426-0128", "Matsuoka et al. (2019)",
                     "https://arxiv.org/pdf/1908.07910",
                     "HSC", "14:26:11.33", "-01:28:22.80", "",
                     "6.01", "", "", "", "", "", "", "", "",
                     "", "", "", "-23.75", "0.10", "0.10", "", "", "",
                     "", "", "", "", "", "", "",
                     ""]])

entry223 = np.array([["J0055+0146", "Willott et al. (2015), Willott et al. (2009), Banados et al. (2016)",
                     "https://iopscience.iop.org/article/10.1088/0004-637X/801/2/123#apj50934, https://iopscience.iop.org/article/10.1088/0004-6256/137/3/3541, https://arxiv.org/pdf/1608.03279",
                     "CFHQS", "00:55:02.91", "+01:46:18.30", "",
                     "6.0060", "0.0008", "0.0008", "2.4e8", "2.6e8", "1.4e8", "", "", "",
                     "1.2", "", "", "-24.81", "", "", "", "", "",
                     "83", "13", "13", "", "", "", "",
                     "coordinates from Willott et al. (2009), f_Edd from Willott et al. (2010), M1450 from Banados et al. (2016)"]])

# coordinates from: https://iopscience.iop.org/article/10.1088/0004-6256/137/3/3541 Willott et al. (2009)
# f_Edd from: https://iopscience.iop.org/article/10.1088/0004-6256/140/2/546 Willott et al. (2010)
# M1450 from: https://arxiv.org/pdf/1608.03279 Banados et al. (2016)

entry224 = np.array([["J2310+1855", "Wang et al. (2013), D'Odorico et al. (2023), Banados et al. (2016)",
                     "https://iopscience.iop.org/article/10.1088/0004-637X/773/1/44, https://academic.oup.com/mnras/article/523/1/1399/7172883, https://arxiv.org/pdf/1608.03279",
                     "SDSS", "23:10:38.89", "+18:55:19.70", "",
                     "6.0031", "0.0002", "0.0002", "log9.67", "log0.06", "log0.08", "9.3e13S", "", "",
                     "", "", "", "-27.80", "", "", "", "", "",
                     "", "", "", "", "", "", "",
                     "coordinates, mass from D'Odorico et al. (2023), M1450 from Banados et al. (2016)"]])

# coordinates, mass from: https://academic.oup.com/mnras/article/523/1/1399/7172883 D'Odorico et al. (2023)
# M1450 from: https://arxiv.org/pdf/1608.03279 Banados et al. (2016)

entry225 = np.array([["J2250-5015", "D'Odorico et al. (2023), Mazzucchelli et al. (2023), Reed et al. (2017)",
                     "https://academic.oup.com/mnras/article/523/1/1399/7172883, https://arxiv.org/pdf/2306.16474, https://academic.oup.com/mnras/article/468/4/4702/3089747",
                     "VDES", "22:50:02.01", "-50:15:42.20", "",
                     "5.985", "0.003", "0.003", "log9.66", "log0.41", "log0.41", "log47.44", "log0.07", "log0.08",
                     "0.46", "0.72", "0.72", "-26.80", "0.04", "0.04", "", "", "",
                     "", "", "", "", "", "", "",
                     "L_bol, f_Edd from Mazzucchelli et al. (2023), M1450 from Reed et al. (2017)"]])

# L_bol, f_Edd from: https://arxiv.org/pdf/2306.16474 Mazzucchelli et al. (2023)
# M1450 from: https://academic.oup.com/mnras/article/468/4/4702/3089747 Reed et al. (2017)
# f_Edd can somehow be negative again?

entry226 = np.array([["J0028+0457/J007.0+04.95", "Banados et al. (2016), Jiang et al. (2015), Shen et al. (2019)",
                     "https://arxiv.org/pdf/1608.03279, https://iopscience.iop.org/article/10.1088/0004-6256/149/6/188, https://iopscience.iop.org/article/10.3847/1538-4357/ab03d9/pdf",
                     "PSO/SDSS", "00:28:06.56", "+04:57:25.64", "",
                     "5.982", "0.012", "0.012", "", "", "", "", "", "",
                     "", "", "", "-26.38", "0.10", "0.10", "", "", "",
                     "", "", "", "", "", "", "",
                     "M1450 from Jiang et al. (2015), z from Shen et al. (2019)"]])

# M1450 from: https://iopscience.iop.org/article/10.1088/0004-6256/149/6/188 Jiang et al. (2015)
# z from: https://iopscience.iop.org/article/10.3847/1538-4357/ab03d9/pdf Shen et al. (2019)

entry227 = np.array([["J0231-2850/J037.9-28.83", "Banados et al. (2016)",
                     "https://arxiv.org/pdf/1608.03279",
                     "PSO", "02:31:52.96", "-28:50:20.08", "",
                     "6.00", "", "", "", "", "", "", "", "",
                     "", "", "", "-26.23", "", "", "", "", "",
                     "", "", "", "", "", "", "",
                     ""]])

entry228 = np.array([["J2356+0023", "Banados et al. (2016)",
                     "https://arxiv.org/pdf/1608.03279",
                     "SDSS", "23:56:51.58", "+00:23:33.30", "",
                     "6.00", "", "", "", "", "", "", "", "",
                     "", "", "", "-25.50", "", "", "", "", "",
                     "", "", "", "", "", "", "",
                     ""]])

entry229 = np.array([["J0001+2650/P000+26", "Shen et al. (2019)",
                     "https://iopscience.iop.org/article/10.3847/1538-4357/ab03d9/pdf",
                     "PSO/UHS", "00:01:21.63", "+26:50:09.20", "",
                     "5.733", "0.007", "0.007", "", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     "", "", "", "", "", "", "",
                     ""]])

entry230 = np.array([["J0002+2550", "Ishimoto et al. (2020)",
                     "https://iopscience.iop.org/article/10.3847/1538-4357/abb80b/pdf",
                     "SDSS/UHS", "00:02:39.39", "+25:50:34.96", "",
                     "5,818", "0.007", "0.007", "", "", "", "", "", "",
                     "", "", "", "-27.31", "", "", "", "", "",
                     "", "", "", "", "", "", "",
                     ""]])

entry231 = np.array([["J0008−0626", "Shen at al. (2019), Jiang et al. (2015)",
                     "https://iopscience.iop.org/article/10.3847/1538-4357/ab03d9/pdf, https://iopscience.iop.org/article/10.1088/0004-6256/149/6/188",
                     "SDSS", "00:08:25.77", "-06:26:04.60", "",
                     "5.929", "0.003", "0.003", "", "", "", "", "", "",
                     "", "", "", "-26.04", "0.09", "0.09", "", "", "",
                     "", "", "", "", "", "", "",
                     "z, M1450 from Jiang et al. (2015)"]])

# z, M1450 from: https://iopscience.iop.org/article/10.1088/0004-6256/149/6/188 Jiang et al. (2015)

entry232 = np.array([["J0203+0012", "Shen et al. (2019), Eilers et al. (2017), Jiang et al. (2008)",
                     "https://iopscience.iop.org/article/10.3847/1538-4357/ab03d9/pdf, https://iopscience.iop.org/article/10.3847/1538-4357/aa6c60, https://iopscience.iop.org/article/10.1088/0004-6256/135/3/1057",
                     "SDSS/ULAS", "02:03:32.38", "+00:12:29.27", "",
                     "5.709", "0.010", "0.010", "", "", "", "", "", "",
                     "", "", "", "-25.72", "0.10", "0.10", "", "", "",
                     "", "", "", "", "", "", "",
                     "coordinates from Eilers et al. (2017), M1450 from Jiang et al. (2008)"]])

# coordinates from: https://iopscience.iop.org/article/10.3847/1538-4357/aa6c60 Eilers et al. (2017)
# M1450 from: https://iopscience.iop.org/article/10.1088/0004-6256/135/3/1057 Jiang et al. (2008)

entry233 = np.array([["J0300−2232/J045.1–22.54", "Banados et al. (2016), Shen et al. (2019)",
                     "https://arxiv.org/pdf/1608.03279, https://iopscience.iop.org/article/10.3847/1538-4357/ab03d9/pdf",
                     "PSO", "03:00:44.18", "-22:32:27.19", "",
                     "5.684", "0.008", "0.008", "", "", "", "", "", "",
                     "", "", "", "-26.26", "", "", "", "", "",
                     "", "", "", "", "", "", "",
                     ""]])

# z from: https://iopscience.iop.org/article/10.3847/1538-4357/ab03d9/pdf Shen et al. (2019)

entry234 = np.array([["J0810+5105", "Banados et al. (2016), Shen et al. (2019)",
                     "https://arxiv.org/pdf/1608.03279, https://iopscience.iop.org/article/10.3847/1538-4357/ab03d9/pdf",
                     "SDSS", "08:10:54.31", "+51:05:40.10", "",
                     "5.805", "0.010", "0.010", "", "", "", "", "", "",
                     "", "", "", "-26.82", "", "", "", "", "",
                     "", "", "", "", "", "", "",
                     "z from Shen et al. (2019)"]])

# z from: https://iopscience.iop.org/article/10.3847/1538-4357/ab03d9/pdf Shen et al. (2019)

entry235 = np.array([["J0835+3217", "Shen et al. (2019), Jiang et al. (2016)",
                     "https://iopscience.iop.org/article/10.3847/1538-4357/ab03d9/pdf, https://iopscience.iop.org/article/10.3847/1538-4357/833/2/222",
                     "SDSS", "08:35:25.76", "+32:17:52.60", "",
                     "5.902", "0.009", "0.009", "", "", "", "", "", "",
                     "", "", "", "-25.76", "", "", "", "", "",
                     "", "", "", "", "", "", "",
                     "M1450 from Jiang et al. (2016)"]])

# M1450 from: https://iopscience.iop.org/article/10.3847/1538-4357/833/2/222 Jiang et al. (2016)

entry236 = np.array([["J0836+0054", "Banados et al. (2016), Shen et al. (2019), D'Odorico et al. (2023)",
                     "https://arxiv.org/pdf/1608.03279, https://iopscience.iop.org/article/10.3847/1538-4357/ab03d9/pdf, https://academic.oup.com/mnras/article/523/1/1399/7172883",
                     "SDSS", "08:36:43.86", "+00:54:53.26", "",
                     "5.834", "0.007", "0.007", "log9.59", "log0.13", "log0.20", "", "", "",
                     "", "", "", "-27.75", "", "", "", "", "",
                     "", "", "", "", "", "", "",
                     "z from Shen et al. (2019), mass from D'Odorico et al. (2023)"]])

# z from: https://iopscience.iop.org/article/10.3847/1538-4357/ab03d9/pdf Shen et al. (2019)
# mass from: https://academic.oup.com/mnras/article/523/1/1399/7172883 D'Odorico et al. (2023)

entry237 = np.array([["J0840+5624", "Shen et al. (2019), Banados et al. (2016)",
                     "https://iopscience.iop.org/article/10.3847/1538-4357/ab03d9/pdf, https://arxiv.org/pdf/1608.03279",
                     "SDSS", "08:40:35.09", "+56:24:19.90", "",
                     "5.816", "0.010", "0.010", "", "", "", "", "", "",
                     "", "", "", "-27.24", "", "", "", "", "",
                     "", "", "", "", "", "", "",
                     "M1450 from Banados et al. (2016)"]])

# M1450 from: https://arxiv.org/pdf/1608.03279 Banados et al. (2016)

entry238 = np.array([["J0841+2905", "Banados et al. (2016), Shen et al. (2019)",
                     "https://arxiv.org/pdf/1608.03279, https://iopscience.iop.org/article/10.3847/1538-4357/ab03d9/pdf",
                     "SDSS", "08:41:19.52", "+29:05:04.55", "",
                     "5.954", "0.005", "0.005", "", "", "", "", "", "",
                     "", "", "", "-26.50", "", "", "", "", "",
                     "", "", "", "", "", "", "",
                     "z from Shen et al. (2019)"]])

# z from: https://iopscience.iop.org/article/10.3847/1538-4357/ab03d9/pdf Shen et al. (2019)

entry239 = np.array([["J0850+3246", "Banados et al. (2016), Shen et al. (2019), Jiang et al. (2015)",
                     "https://arxiv.org/pdf/1608.03279, https://iopscience.iop.org/article/10.3847/1538-4357/ab03d9/pdf, https://iopscience.iop.org/article/10.1088/0004-6256/149/6/188",
                     "SDSS/UHS", "08:50:48.25", "+32:46:47.94", "",
                     "5.730", "0.013", "0.013", "", "", "", "", "", "",
                     "", "", "", "-26.74", "0.08", "0.08", "", "", "",
                     "", "", "", "", "", "", "",
                     "z from Shen et al. (2019), M1450 from Jiang et al. (2015)"]])

# z from: https://iopscience.iop.org/article/10.3847/1538-4357/ab03d9/pdf Shen et al. (2019)
# M1450 from: https://iopscience.iop.org/article/10.1088/0004-6256/149/6/188 Jiang et al. (2015)

entry240 = np.array([["J0927+2001", "Ishimoto et al. (2020), D'Odorico et al. (2023), Mazzucchelli et al. (2023)",
                     "https://iopscience.iop.org/article/10.3847/1538-4357/abb80b/pdf, https://academic.oup.com/mnras/article/523/1/1399/7172883, https://arxiv.org/pdf/2306.16474",
                     "SDSS/UHS", "09:27:2182", "+20:01:23.64", "",
                     "5.7722", "0.0006", "0.0006", "log9.11", "log0.10", "log0.13", "log47.08", "log0.15", "log0.24",
                     "", "", "", "-26.76", "", "", "", "", "",
                     "", "", "", "", "", "", "",
                     "mass from D'Odorico et al. (2023), L_bol from Mazzucchelli et al. (2023), additional information here: https://arxiv.org/pdf/2306.16474 Mazzucchelli et al. (2023)"]])

# mass from: https://academic.oup.com/mnras/article/523/1/1399/7172883 D'Odorico et al. (2023)
# L_bol from: https://arxiv.org/pdf/2306.16474 Mazzucchelli et al. (2023)

entry241 = np.array([["J1044−0125", "Venemans et al. (2020), Willott et al. (2015), Wang et al. (2013), Banados et al. (2016)",
                     "https://iopscience.iop.org/article/10.3847/1538-4357/abc563, https://iopscience.iop.org/article/10.1088/0004-637X/801/2/123#apj509348t2, https://iopscience.iop.org/article/10.1088/0004-637X/773/1/44, https://arxiv.org/pdf/1608.03279",
                     "SDSS", "10:44:33.040", "-01:25:02.08", "",
                     "5.7846", "0.0005", "0.0005", "1.1e10", "1.9e10", "0.7e10", "11.6e13S", "", "",
                     "", "", "", "-27.38", "", "", "", "", "",
                     "", "", "", "", "", "", "",
                     "mass from Willott et al. (2015), L_bol from Wang et al. (2013), M1450 from Banados et al. (2016)"]])

# mass from: https://iopscience.iop.org/article/10.1088/0004-637X/801/2/123#apj509348t2 Willott et al. (2015)
# L_bol from: https://iopscience.iop.org/article/10.1088/0004-637X/773/1/44 Wang et al. (2013)
# M1450 from: https://arxiv.org/pdf/1608.03279 Banados et al. (2016)

entry242 = np.array([["J1143+3808", "Eilers et al. (2020)",
                     "https://arxiv.org/pdf/2002.01811",
                     "SDSS", "11:43:38.347", "+38:08:28.823", "",
                     "5.8366", "0.0023", "0.0023", "", "", "", "", "", "",
                     "", "", "", "-26.69", "", "", "", "", "",
                     "", "", "", "", "", "", "",
                     ""]])

columnNames = ["Name", "Ref",
               "Link",
               "Inst", "RA", "DEC", "Distance",
               "z", "+dz", "-dz", "M [M_sun]", "+dM", "-dM", "L_bol [erg/s]", "+dL_bol", "-dL_bol",
               "f_Edd", "+df_Edd", "-df_Edd", "M1450", "+dM1450", "-dM1450", "F444W", "+dF44W", "-dF444W",
               "SFR_CII", "+dSFR_CII", "-dSFR_CII", "SFR_TIR", "+dSFR_TIR", "-dSFR_TIR", "Mstar"
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
                     "", "", "", "", "", "", "",
                     ""]])


'''

# Inayoshi et al. (2019) All-clear


# Banados et al. (2016) Not sure
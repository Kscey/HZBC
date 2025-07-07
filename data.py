import numpy as np

# Tool to help convert RA DEC coordinates: https://www.astrouw.edu.pl/~jskowron/ra-dec/?q=d++53.12654+-27.81809

# Arrays are manually populated to include or amend information
# 1a. Some bolometric luminosities need to be converted from units of solar luminosities to ergs per second (1 solar luminosity = 3.846e33 ergs per second)
# 1b. This can be done by adding "S" to the end of the bolometric luminosity
# 2a. Some entries lack a documented black hole mass and is approximated by the formula 10 ** ((-M1450 -3.459) / 2.5)
# 2b. This is done automatically without any input

entry0 = np.array([["J1342+0928", "Banados et al. (2018), Venemans et al. (2017), Onoue et al. (2020), Novak et al. (2019), Yang et al. (2021)",
                    "https://arxiv.org/abs/1712.01860, https://iopscience.iop.org/article/10.3847/2041-8213/aa943a, https://arxiv.org/pdf/2006.16268, https://iopscience.iop.org/article/10.3847/1538-4357/ab2beb, https://iopscience.iop.org/article/10.3847/1538-4357/ac2b32",
                    "ULAS", "13h42m08s.097", "+09°28′38″28", "",
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
                    "HSC", "12h43m53s.93", "+01°00′38″5", "",
                    "7.0749", "0.001", "0.001", "3.3e8", "2e8", "2e8", "1.4e46", "0.1e46", "0.1e46",
                    "0.34", "0.2", "0.2", "-24.13", "0.08", "0.08", "", "", "",
                    "220", "8", "8", "742", "16", "16", "",
                    "z, SFR from Izumi et al. (2021)"]])

# What does the b in 2019b mean? Have to keep it?
# Updated (newer) redshift and SFR from: https://arxiv.org/pdf/2104.05738### Izumi et al. (2021) pg.6

entry2 = np.array([["J1120+0641", "Mortlock et al.(2011), De Rosa et al. (2014), Yang et al. (2021)",
                    "https://arxiv.org/abs/1106.6088, https://arxiv.org/pdf/1311.3260, https://iopscience.iop.org/article/10.3847/1538-4357/ac2b32",
                    "ULAS", " 11h20m01s.48", "+06°41′24.″3", "",
                    "7.0851", "0.0005", "0.0005", "1.35e9", "0.04e9", "0.04e9", "13.4e46", "1.0e46", "1.0e46",
                    "0.8", "0.1", "0.1", "-26.44", "", "", "", "", "",
                    "", "", "", "", "", "", "",
                    "coordinates from De Rosa et al. (2014), z, M1450, M, L_bol from Yang et al. (2021)"]])

# Coordinates found from: https://arxiv.org/pdf/1311.3260 De Rosa et al. (2014)
# Redshift, M1450, M, L_bol, f_Edd from: https://iopscience.iop.org/article/10.3847/1538-4357/ac2b32 Yang et al. (2021)

entry3 = np.array([["J0038-1527", "Wang et al. (2018)",
                    "https://arxiv.org/abs/1810.11925",
                    "DELS", "00h38m36s.10", "-15°27′23.″06", "",
                    "7.021", "0.005", "0.005", "1.33e9", "0.25e9", "0.25e9", "2.16e47", "", "",
                    "1.25", "0.19", "0.19", "-27.10", "0.08", "0.08", "", "", "",
                    "", "", "", "", "", "", "",
                    ""]])

entry4 = np.array([["J0252-0503", "Yang et al. (2019), Wang et al (2020)",
                    "https://iopscience.iop.org/article/10.3847/1538-3881/ab1be1/meta, https://arxiv.org/abs/2004.10877",
                    "DES", "02h52m16.s64", "-05°03′31.″80", "",
                    "7.02", "0.001", "0.001", "1.39e9", "1.6e8", "1.6e8", "1.3e47", "0.1e47", "0.1e47",
                    "0.7", "0.1", "0.1", "-26.50", "0.09", "0.09", "", "", "",
                    "", "", "", "", "", "", "",
                    "M1450 from Yang et al. (2019), z from Wang et al (2020)"]])

# M1450 from: https://iopscience.iop.org/article/10.3847/1538-3881/ab1be1/meta Yang et al. (2019)
# z from: https://arxiv.org/abs/2004.10877 Wang et al (2020)

entry5 = np.array([["J2356+0017", "Matsuoka et al. (2019)",
                    "https://arxiv.org/abs/1908.07910",
                    "HSC", "23h56m46.s33", "+00°17′47.″30", "",
                    "7.01", "", "", "5.5e8", "2.06e7", "1.99e7", "", "", "",
                    "", "", "", "-25.31", "0.04", "0.04", "", "", "",
                    "", "", "", "", "", "", "",
                    ""]])

# Currently unsure where the mass comes from

entry6 = np.array([["J0313−1806", "Wang et al. (2021)",
                    "https://arxiv.org/abs/2101.03179",
                    "PS1+DELS+VHS+WISE", "03h13m43s.84", "-18°06′36.″4", "",
                    "7.6423", "0.0013", "0.0013", "1.6e9", "0.4e9", "0.4e9", "1.4e47", "0.1e47", "0.1e47",
                    "0.67", "0.14", "0.14", "-26.13", "0.05", "0.05", "", "", "",
                    "40-240", "", "", "225", "25", "25", "",
                    ""]])

entry7 = np.array([["J1007+2115", "Yang et al. (2020)",
                    "https://arxiv.org/abs/2006.13452",
                    "PS1+DELS+UHS+WISE", "10h07m58.s26", "+21°15′29.″20", "",
                    "7.5149", "0.0004", "0.0004", "1.5e9", "0.2e9", "0.2e9", "1.9e47", "0.1e47", "0.1e47",
                    "1.06", "0.2", "0.2", "-26.66", "0.07", "0.07", "", "", "",
                    "80-520", "", "", "700", "", "", "",
                    ""]])

entry8 = np.array([["UHZ1", "Bogdan et al. (2023), Castellano et al. (2023), Goulding et al. (2023)",
                    "https://arxiv.org/abs/2305.15458, https://iopscience.iop.org/article/10.3847/2041-8213/accea5/meta, https://arxiv.org/pdf/2308.02750",
                    "JWST", "0h14m16.s096", "-30°22′40.″285", "",
                    "10.073", "0.002", "0.002", "4e7", "6e7", "3e7", "5e45", "", "",
                    "", "", "", "", "", "", "87.7", "7.2", "7.2",
                    "4.5", "2.9", "2.2", "4.5", "2.9", "2.2", "0.4e8",
                    "F444W, SFR, Mstar from Castellano et al. (2023), z from Goulding et al. (2023)"]])

# F444W, SFR, Mstar from: https://iopscience.iop.org/article/10.3847/2041-8213/accea5/meta Castellano et al. (2023)
# z from: https://arxiv.org/pdf/2308.02750 Goulding et al. (2023)

entry9 = np.array([["GHZ9", "Kovacs et al. (2024), Castellano et al. (2023), Atek et al. (2023)",
                    "https://arxiv.org/abs/2403.14745, https://iopscience.iop.org/article/10.3847/2041-8213/accea5/meta, https://arxiv.org/pdf/2305.01793",
                    "JWST", "00h13m54.s90", "-30°20′43.″93", "",
                    "10.37", "0.32", "1.09", "8e7", "3.7e7", "3.2e7", "1e46", "0.5e46", "0.4e46",
                    "", "", "", "", "", "", "40.9", "3.9", "3.9",
                    "", "", "", "", "", "", "3.3e8",
                    "F444W, Mstar, SFR [14.4 (+15.0/-7.3)] from Castellano et al. (2023), SFR [0.56 (+0.23/-0.29)] from Atek et al. (2023)"]])

# F444W, Mstar, SFR from: https://iopscience.iop.org/article/10.3847/2041-8213/accea5/meta Castellano et al. (2023)
# SFR from: https://arxiv.org/pdf/2305.01793 Atek et al. (2023)

entry10 = np.array([["GNz11", "Maiolino et al. (2023), Bunker et al. (2023), Oesch et al. (2016)",
                     "https://arxiv.org/abs/2305.12492, https://arxiv.org/pdf/2302.07256, https://arxiv.org/pdf/1603.00461",
                     "JWST", "12h36m25.s46", "+62°14′31.″4", "",
                     "10.6", "", "", "1.6e6", "1e0.3", "1e0.3", "1.08e45", "", "",
                     "", "", "", "", "", "", "", "", "",
                     "31", "59", "19", "31", "59", "19", "",
                     "SFR from Bunker et al. (2023), coordinates from Oesch et al. (2016)"]])

# SFR from: https://arxiv.org/pdf/2302.07256 Bunker et al. (2023)
# Coordinates from: https://arxiv.org/pdf/1603.00461 Oesch et al. (2016)

entry11 = np.array([["CEERS_1019", "Larson et al. (2023)",
                     "https://arxiv.org/abs/2303.08918",
                     "JWST", "215d02m07.s41", "+52°53′26.″38", "",
                     "8.679", "0.09", "0.15", "log6.95", "log0.37", "log0.37", "log45.1", "log0.2", "log0.2",
                     "1.2", "0.5", "0.5", "", "", "", "", "", "",
                     "30", "", "", "30", "", "", "",
                     ""]])

entry12 = np.array([["J1205−0000", "Onoue et al. (2019), Sawamura et al. (2025), Izumi et al. (2021)",
                     "https://arxiv.org/abs/1904.07278, https://arxiv.org/pdf/2502.16858, https://iopscience.iop.org/article/10.3847/1538-4357/abd7ef",
                     "HSC", "12h05m05.s09", "-00°00′27.″90", "",
                     "6.7230", "0.0003", "0.0003", "2.2e9", "0.2e9", "0.6e9", "", "", "",
                     "0.16", "0.04", "0.02", "-24.56", "0.04", "0.04", "", "", "",
                     "122", "5", "5", "528", "8", "8", "",
                     ""]])

# SFR_TIR from: https://arxiv.org/pdf/2502.16858 Sawamura et al. (2025)
# z, SFR_CII from: https://iopscience.iop.org/article/10.3847/1538-4357/abd7ef Izumi et al. (2021)

entry13 = np.array([["J2239+0207", "Onoue et al. (2019), Ishimoto et al. (2020)",
                     "https://arxiv.org/abs/1904.07278, https://iopscience.iop.org/article/10.3847/1538-4357/abb80b/pdf",
                     "HSC", "22h39m47.s47", "+02°07′47.″5", "",
                     "6.245", "0.008", "0.007", "1.1e9", "0.3e9", "0.2e9", "", "", "",
                     "0.17", "0.04", "0.05", "-24.69", "0.04", "0.04", "", "", "",
                     "", "", "", "", "", "", "",
                     "coordinates from Ishimoto et al. (2020)"]])

# coordinates from: https://iopscience.iop.org/article/10.3847/1538-4357/abb80b/pdf Ishimoto et al. (2020)

entry14 = np.array([["J2216−0016", "Onoue et al. (2019), Ishimoto et al. (2020)",
                     "https://arxiv.org/abs/1904.07278, https://iopscience.iop.org/article/10.3847/1538-4357/abb80b/pdf",
                     "HSC", "22h16m44.s47", "−00°16′50.″1", "",
                     "6.109", "0.007", "0.008", "0.7e9", "0.14e9", "0.23e9", "", "", "",
                     "0.15", "0.05", "0.03", "-23.82", "0.04", "0.04", "", "", "",
                     "", "", "", "", "", "", "",
                     "coordinates from Ishimoto et al. (2020)"]])

# coordinates from: https://iopscience.iop.org/article/10.3847/1538-4357/abb80b/pdf Ishimoto et al. (2020)

entry15 = np.array([["J1208−0200", "Onoue et al. (2019), Ishimoto et al. (2020)",
                     "https://arxiv.org/abs/1904.07278, https://iopscience.iop.org/article/10.3847/1538-4357/abb80b/pdf",
                     "HSC", "12h08m59.s23", "−02°00′34.″8", "",
                     "6.144", "0.008", "0.01", "0.71e9", "0.24e9", "0.52e9", "", "", "",
                     "0.24", "0.18", "0.08", "-24.73", "0.02", "", "", "", "",
                     "", "", "", "", "", "", "",
                     "coordinates from Ishimoto et al. (2020)"]])

# coordinates from: https://iopscience.iop.org/article/10.3847/1538-4357/abb80b/pdf Ishimoto et al. (2020)

entry16 = np.array([["J0100+2802", "Wu et al. (2015), D'Odorico et al. (2023), Venemans et al. (2020), Mazzucchelli et al. (2023)",
                     "https://arxiv.org/abs/1502.07418, https://academic.oup.com/mnras/article/523/1/1399/7172883, https://iopscience.iop.org/article/10.3847/1538-4357/abc563, https://arxiv.org/pdf/2306.16474",
                     "SDSS", "01h00m13.s02", "+28°02′25.″80", "",
                     "6.3269", "0.0002", "0.0002", "log10.1", "log0.2", "log0.1", "log48.15", "log0.04", "log0.04",
                     "0.99", "0.22", "0.22", "-29.26", "0.20", "0.20", "", "", "",
                     "", "", "", "", "", "", "",
                     "coordinates from D'Odorico et al. (2023), distance, z from Venemans et al. (2020), mass, L_bol from Mazzucchelli et al. (2023)"]])

# coordinates from: https://academic.oup.com/mnras/article/523/1/1399/7172883 D'Odorico et al. (2023)
# distance, z from: https://iopscience.iop.org/article/10.3847/1538-4357/abc563 Venemans et al. (2020)
# mass, L_bol from: https://arxiv.org/pdf/2306.16474 Mazzucchelli et al. (2023)

entry17 = np.array([["J158–14", "Eilers et al. (2020)",
                     "https://arxiv.org/abs/2002.01811",
                     "PSO", "10h34m46.s509", "–14°25′15.″855", "",
                     "6.052", "0.001", "0.001", "1.57e9", "0.12e9", "0.12e9", "2.04e47", "", "",
                     "1.01", "0.08", "0.08", "-27.41", "", "", "", "", "",
                     "230", "", "", "", "", "", "",
                     ""]])

entry18 = np.array([["J0330–4025", "Eilers et al. (2020)",
                     "https://arxiv.org/abs/2002.01811",
                     "VDES", "03h30m27.s920", "–40°25′16.″200", "",
                     "6.239", "0.004", "0.004", "4.96e9", "0.51e9", "0.51e9", "8.91e46", "", "",
                     "0.14", "0.01", "0.01", "-26.42", "", "", "", "", "",
                     "", "", "", "", "", "", "",
                     ""]])

entry19 = np.array([["J2100–1715", "Eilers et al. (2020)",
                     "https://arxiv.org/abs/2002.01811",
                     "CFHQS", "21h00m54.s616", "–17°15′22.″500", "",
                     "6.082", "0.002", "0.002", "2.18e9", "0.21e9", "0.21e9", "4.37e46", "", "",
                     "0.15", "0.02", "0.02", "-25.55", "", "", "", "", "",
                     "170", "", "", "", "", "", "",
                     ""]])

entry20 = np.array([["J2229+1457", "Eilers et al. (2020), Willott et al. (2015)",
                     "https://arxiv.org/abs/2002.01811, https://iopscience.iop.org/article/10.1088/0004-637X/801/2/123#apj509348t2",
                     "CFHQS", "22h29m01.s649", "+14°57′08.″980", "",
                     "6.144", "0.006", "0.006", "1.44e9", "0.25e9", "0.25e9", "2.29e46", "", "",
                     "0.12", "0.02", "0.02", "-24.78", "", "", "", "", "",
                     "60", "8", "8", "19", "10", "10", "",
                     "SFR from Willott et al. (2015)"]])

# SFR from: https://iopscience.iop.org/article/10.1088/0004-637X/801/2/123#apj509348t2 Willott et al. (2015)

entry21 = np.array([["J004+17", "Eilers et al. (2020), ",
                     "https://arxiv.org/abs/2002.01811",
                     "PSO", "00h17m34.s467", "+17°05′10.″696", "",
                     "5.8165", "0.0023", "0.0023", "1.05e9", "", "", "", "", "",
                     "", "", "", "-26.01", "", "", "", "", "",
                     "20", "", "", "", "", "", "",
                     ""]])

entry22 = np.array([["J1335+3533", "Eilers et al. (2018), Ishimoto et al. (2020)",
                     "https://arxiv.org/abs/1806.05691, https://iopscience.iop.org/article/10.3847/1538-4357/abb80b/pdf",
                     "SDSS", "13h35m50.s81", "+35°33′15.″82", "",
                     "5.9012", "0.0019", "0.0019", "4.09e9", "0.58e9", "0.58e9", "1.62e47", "0.03e47", "0.03e47",
                     "0.30", "0.04", "0.04", "-26.67", "", "", "", "", "",
                     "", "", "", "", "", "", "",
                     "coordinates from Ishimoto et al. (2020)"]])

# coordinates from: https://iopscience.iop.org/article/10.3847/1538-4357/abb80b/pdf Ishimoto et al. (2020)

entry23 = np.array([["954", "Maiolino et al. (2024), Juodžbalis et al. (2025)",
                     "https://arxiv.org/abs/2308.01230, https://arxiv.org/html/2504.03551v1",
                     "JWST", "12h36m36.s47", "+62°15′34.″70", "",
                     "6.759", "", "", "log7.74", "log0.31", "log0.32", "log45.24", "log0.15", "log0.17",
                     "0.25", "0.05", "0.05", "", "", "", "", "", "",
                     "", "", "", "", "", "", "log10.66",
                     "coordinates, z, mass, L_bol, f_Edd from Juodžbalis et al. (2025)"]])

# coordinates, z, mass, L_bol, f_Edd from: https://arxiv.org/html/2504.03551v1 Juodžbalis et al. (2025)

entry24 = np.array([["1093", "Maiolino et al. (2024), Juodžbalis et al. (2025)",
                     "https://arxiv.org/abs/2308.01230, https://arxiv.org/html/2504.03551v1",
                     "JWST", "12h36m43.s14", "+62°13′28.″67", "",
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
                     "JWST", "03h32m31.s88", "-27°48′06.″70", "",
                     "4.753", "", "", "log7.11", "log0.31", "log0.31", "log44.06", "log0.05", "log0.05",
                     "0.07", "0.01", "0.01", "", "", "", "", "", "",
                     "", "", "", "", "", "", "log8.45",
                     "coordinates, z, mass, L_bol, f_Edd from Juodžbalis et al. (2025)"]])

# coordinates, z, mass, L_bol, f_Edd from: https://arxiv.org/html/2504.03551v1 Juodžbalis et al. (2025)

entry27 = np.array([["11836", "Maiolino et al. (2024), Juodžbalis et al. (2025)",
                     "https://arxiv.org/abs/2308.01230, https://arxiv.org/html/2504.03551v1",
                     "JWST", "12h36m52.s94", "+62°15′49.″25", "",
                     "4.409", "", "", "log7.00", "log0.32", "log0.32", "log44.20", "log0.05", "log0.05",
                     "0.13", "0.03", "0.02", "", "", "", "", "", "",
                     "", "", "", "", "", "", "log7.79",
                     "coordinates, z, mass, L_bol, f_Edd from Juodžbalis et al. (2025)"]])

# coordinates, z, mass, L_bol, f_Edd from: https://arxiv.org/html/2504.03551v1 Juodžbalis et al. (2025)

entry28 = np.array([["20621", "Maiolino et al. (2024), Juodžbalis et al. (2025)",
                     "https://arxiv.org/abs/2308.01230, https://arxiv.org/html/2504.03551v1",
                     "JWST", "12h36m29.s40", "+62°17′34.″26", "",
                     "4.682", "", "", "log7.09", "log0.35", "log0.34", "log44.24", "log0.23", "log0.19",
                     "0.11", "0.06", "0.03", "", "", "", "", "", "",
                     "", "", "", "", "", "", "log8.06",
                     "coordinates, z, mass, L_bol, f_Edd from Juodžbalis et al. (2025)"]])

# coordinates, z, mass, L_bol, f_Edd from: https://arxiv.org/html/2504.03551v1 Juodžbalis et al. (2025)

entry29 = np.array([["53757", "Maiolino et al. (2024), Juodžbalis et al. (2025)",
                     "https://arxiv.org/abs/2308.01230, https://arxiv.org/html/2504.03551v1",
                     "JWST", "12h37m04.s75", "+62°11′39.″16", "",
                     "4.447", "", "", "log7.33", "log0.31", "log0.31", "log44.29", "log0.02", "log0.02",
                     "0.07", "0.01", "0.009", "", "", "", "", "", "",
                     "", "", "", "", "", "", "log10.18",
                     "coordinates, z, mass, L_bol, f_Edd from Juodžbalis et al. (2025)"]])

# coordinates, z, mass, L_bol, f_Edd from: https://arxiv.org/html/2504.03551v1 Juodžbalis et al. (2025)

entry30 = np.array([["61888", "Maiolino et al. (2024), Juodžbalis et al. (2025)",
                     "https://arxiv.org/abs/2308.01230, https://arxiv.org/html/2504.03551v1",
                     "JWST", "12h36m40.s32", "+62°13′01.″24", "",
                     "5.874", "", "", "log7.08", "log0.33", "log0.32", "log44.46", "log0.13", "log0.10",
                     "0.20", "0.06", "0.03", "", "", "", "", "", "",
                     "", "", "", "", "", "", "log8.11",
                     "coordinates, z, mass, L_bol, f_Edd from Juodžbalis et al. (2025)"]])

# coordinates, z, mass, L_bol, f_Edd from: https://arxiv.org/html/2504.03551v1 Juodžbalis et al. (2025)

entry31 = np.array([["62309", "Maiolino et al. (2024), Juodžbalis et al. (2025)",
                     "https://arxiv.org/abs/2308.01230, https://arxiv.org/html/2504.03551v1",
                     "JWST", "12h36m59.s76", "+62°13′06.″06", "",
                     "5.172", "", "", "log6.30", "log0.36", "log0.33", "log43.57", "log0.13", "log0.12",
                     "0.15", "0.05", "0.05", "", "", "", "", "", "",
                     "", "", "", "", "", "", "log8.12",
                     "coordinates, z, mass, L_bol, f_Edd from Juodžbalis et al. (2025)"]])

# coordinates, z, mass, L_bol, f_Edd from: https://arxiv.org/html/2504.03551v1 Juodžbalis et al. (2025)

entry32 = np.array([["73488", "Maiolino et al. (2024), Juodžbalis et al. (2025)",
                     "https://arxiv.org/abs/2308.01230, https://arxiv.org/html/2504.03551v1",
                     "JWST", "12h36m47.s38", "+62°10′38.″03", "",
                     "4.133", "", "", "log7.95", "log0.30", "log0.30", "log45.45", "log0.07", "log0.05",
                     "0.25", "0.02", "0.02", "", "", "", "", "", "",
                     "", "", "", "", "", "", "log9.78",
                     "coordinates, z, mass, L_bol, f_Edd from Juodžbalis et al. (2025)"]])

# coordinates, z, mass, L_bol, f_Edd from: https://arxiv.org/html/2504.03551v1 Juodžbalis et al. (2025)

entry33 = np.array([["77652", "Maiolino et al. (2024), Juodžbalis et al. (2025)",
                     "https://arxiv.org/abs/2308.01230, https://arxiv.org/html/2504.03551v1",
                     "JWST", "12h37m10.s38", "+62°11′56.″40", "",
                     "5.229", "", "", "log6.62", "log0.34", "log0.32", "log44.11", "log0.04", "log0.05",
                     "0.24", "0.09", "0.08", "", "", "", "", "", "",
                     "", "", "", "", "", "", "log7.87",
                     "coordinates, z, mass, L_bol, f_Edd from Juodžbalis et al. (2025)"]])

# coordinates, z, mass, L_bol, f_Edd from: https://arxiv.org/html/2504.03551v1 Juodžbalis et al. (2025)

entry34 = np.array([["10013704", "Maiolino et al. (2024), Juodžbalis et al. (2025)",
                     "https://arxiv.org/abs/2308.01230, https://arxiv.org/html/2504.03551v1",
                     "JWST", "03h32m30.s37", "-27°49′05.″12", "",
                     "5.919", "", "", "log7.44", "log0.31", "log0.31", "log44.29", "log0.02", "log0.02",
                     "0.055", "0.007", "0.006", "", "", "", "", "", "",
                     "", "", "", "", "", "", "log8.88",
                     "coordinates, z, mass, L_bol, f_Edd from Juodžbalis et al. (2025)"]])

# coordinates, z, mass, L_bol, f_Edd from: https://arxiv.org/html/2504.03551v1 Juodžbalis et al. (2025)

entry35 = np.array([["GS_3073", "Ubler et al. (2023), Barchiesi et al. (2022)",
                     "https://arxiv.org/abs/2302.06647, https://arxiv.org/pdf/2212.00038",
                     "JWST", "03h32m18.s93", "−27◦53′02.″96", "",
                     "5.55", "", "", "1.58489e8", "2.39618e8", "9.53936e7", "5.0e45", "1.08e46", "3.43e45",
                     "0.25", "1.35", "0.15", "", "", "", "", "", "",
                     "16", "14", "7", "", "", "", "",
                     "use H-alpha for mass, use geometric mean of two method for L_bol, SFR [90 (+30/-30)] from Barchiesi et al. (2022)"]])

# SFR from: https://arxiv.org/pdf/2212.00038 Barchiesi et al. (2022)

entry36 = np.array([["CEERS_01244", "Harikane et al. (2023)",
                     "https://arxiv.org/pdf/2303.11946",
                     "JWST", "14h20m57.s76 ", "+53◦02′09.″08", "",
                     "4.478", "", "", "3.2e7", "0.3e7", "0.2e7", "1.9e45", "3.8e45", "0.6e45",
                     "0.46", "1.04", "0.16", "", "", "", "", "", "",
                     "", "", "", "", "", "", "",
                     ""]])

entry37 = np.array([["GLASS_160133", "Harikane et al. (2023)",
                     "https://arxiv.org/pdf/2303.11946",
                     "JWST", "00h14m19.s27", "−30◦25′27.″8", "",
                     "4.015", "", "", "2.3e6", "0.1e6", "0.1e6", "1.1e45", "6.1e45", "0.9e45",
                     "3.68", "21.21", "2.84", "", "", "", "", "", "",
                     "", "", "", "", "", "", "",
                     ""]])

entry38 = np.array([["GLASS_150029", "Harikane et al. (2023)",
                     "https://arxiv.org/pdf/2303.11946",
                     "JWST", "00h14m18.s52", "−30◦25′21.″3", "",
                     "4.583", "", "", "3.7e6", "0.2e6", "0.3e6", "9.1e44", "13.8e44", "7.1e44",
                     "1.89", "3.31", "1.49", "", "", "", "", "", "",
                     "", "", "", "", "", "", "",
                     ""]])

entry39 = np.array([["CEERS_00746", "Harikane et al. (2023)",
                     "https://arxiv.org/pdf/2303.11946",
                     "JWST", "14h19m14.s19", "+52◦52′06.″05", "",
                     "5.624", "", "", "5.8e7", "1.5e7", "1.3e7", "1.1e46", "0.1e46", "0.2e46",
                     "1.47", "0.60", "0.52", "", "", "", "", "", "",
                     "", "", "", "", "", "", "",
                     ""]])

entry40 = np.array([["CEERS_01665", "Harikane et al. (2023)",
                     "https://arxiv.org/pdf/2303.11946",
                     "JWST", "14h20m42.s77", "+53◦03′33.″07", "",
                     "4.483", "", "", "1.9e7", "0.8e7", "0.5e7", "4.8e45", "7.2e45", "3.6e45",
                     "1.93", "4.61", "1.59", "", "", "", "", "", "",
                     "", "", "", "", "", "", "",
                     ""]])

entry41 = np.array([["CEERS_00672", "Harikane et al. (2023)",
                     "https://arxiv.org/pdf/2303.11946",
                     "JWST", "14h19m33.s52", "+52◦49′58.″07", "",
                     "5.666", "", "", "5.0e7", "1.7e7", "1.3e7", "4.3e45", "0.4e45", "1.4e45",
                     "0.65", "0.31", "0.33", "", "", "", "", "", "",
                     "", "", "", "", "", "", "",
                     ""]])

entry42 = np.array([["CEERS_02782", "Harikane et al. (2023)",
                    "https://arxiv.org/pdf/2303.11946",
                     "JWST", "14h19m17.s63", "+52◦49′49.″00", "",
                     "5.241", "", "", "4.2e7", "1.2e7", "1.0e7", "2.8e45", "2.3e45", "1.4e45",
                     "0.51", "0.71", "0.32", "", "", "", "", "", "",
                     "", "", "", "", "", "", "",
                     ""]])

entry43 = np.array([["CEERS_00397", "Harikane et al. (2023)",
                     "https://arxiv.org/pdf/2303.11946",
                     "JWST", "14h19m20.s69", "+52◦52′57.″07", "",
                     "6.000", "", "", "1.0e7", "0.8e7", "0.5e7", "2.8e45", "14.2e45", "2.2e45",
                     "2.02", "20.68", "1.80", "", "", "", "", "", "",
                     "", "", "", "", "", "", "",
                     ""]])

entry44 = np.array([["CEERS_00717", "Harikane et al. (2023)",
                     "https://arxiv.org/pdf/2303.11946",
                     "JWST", "14h20m19.s54", "+52◦58′19.″09", "",
                     "6.936", "", "", "9.8e7", "4.4e7", "3.2e7", "7.1e44", "51.8e44", "4.3e44",
                     "0.06", "0.63", "0.04", "", "", "", "", "", "",
                     "", "", "", "", "", "", "",
                     ""]])

entry45 = np.array([["CEERS_01236", "Harikane et al. (2023)",
                     "https://arxiv.org/pdf/2303.11946",
                     "JWST", "14h20m34.s87", "+52◦58′02.″02", "",
                     "4.484", "", "", "1.8e7", "1.0e7", "0.6e7", "1.8e44", "2.6e44", "0.5e44",
                     "0.08", "0.20", "0.04", "", "", "", "", "", "",
                     "", "", "", "", "", "", "",
                     ""]])

entry46 = np.array([["J172+18", "Banados et al. (2021)",
                     "https://www.mpg.de/16498963/mpia-pr_banados_quasar_2021_preprint.pdf",
                     "PSO", "11h29m25.s37", "+18◦46′24.″29", "",
                     "6.823", "0.003", "0.001", "2.9e8", "0.7e8", "0.6e8", "6.5e46", "", "",
                     "2.2", "0.6", "0.4", "-25.81", "0.10", "0.10", "", "", "",
                     "", "", "", "", "", "", "",
                     ""]])

entry47 = np.array([["J2157-3602", "Wolf et al. (2018), Onken et al. (2020), Lai et al. (2023)",
                     "https://arxiv.org/abs/1805.04317, https://arxiv.org/pdf/2005.06868, https://arxiv.org/pdf/2302.10397",
                     "SMSS", "21h57m28.s23", "-36°02′15.″21", "",
                     "4.692", "", "", "log10.31", "log0.17", "log0.14", "log47.87", "log0.10", "log0.10",
                     "0.29", "0.11", "0.10", "", "", "", "", "", "",
                     "", "", "", "", "", "", "",
                     "z from Onken et al. (2020), mass, L_bol, f_Edd from Lai et al. (2023)"]])

# z from: https://arxiv.org/pdf/2005.06868 Onken et al. (2020)
# mass, L_bol, f_Edd from: https://arxiv.org/pdf/2302.10397 Lai et al. (2023)

entry48 = np.array([["J1609+5328", "Matsuoka et al. (2019)",
                     "https://arxiv.org/pdf/1908.07910",
                     "HSC", "16h09m53.s03", "+53°28′21.″00", "",
                     "6.92", "", "", "", "", "", "", "", "",
                     "", "", "", "-22.75", "1.67", "1.67", "", "", "",
                     "", "", "", "", "", "", "",
                     ""]])

entry49 = np.array([["J0839+3900", "Wang et al. (2019)",
                     "https://iopscience.iop.org/article/10.3847/1538-4357/ab2be5/pdf",
                     "DELS", "08h39m46.s88", "+39°00′11.″50", "",
                     "6.905", "0.01", "0.01", "", "", "", "", "", "",
                     "", "", "", "-26.29", "0.20", "0.20", "", "", "",
                     "", "", "", "", "", "", "",
                     ""]])

entry50 = np.array([["J2348-3054", "Banados et al. (2016), Venemans et al. (2020), Venemens et al. (2015), Venemans et al. (2013)",
                     "https://arxiv.org/pdf/1608.03279, https://iopscience.iop.org/article/10.3847/1538-4357/abc563, https://iopscience.iop.org/article/10.3847/0004-637X/816/1/37/meta, https://iopscience.iop.org/article/10.1088/0004-637X/779/1/24",
                     "VIK", "23h48m33.s34", "−30°54′10.″24", "",
                     "6.9007", "0.0005", "0.0005", "2.1e9", "0.5e9", "0.5e9", "", "", "",
                     "", "", "", "-25.72", "0.14", "0.14", "", "", "",
                     "100-680", "", "", "", "", "", "",
                     "z from Venemans et al. (2020), SFR from Venemens et al. (2015), mass, M1450 from Venemans et al. (2013)"]])        

# z from: https://iopscience.iop.org/article/10.3847/1538-4357/abc563 Venemans et al. (2020)
# SFR from: https://iopscience.iop.org/article/10.3847/0004-637X/816/1/37/meta Venemans et al. (2015)
# mass, M1450 from: https://iopscience.iop.org/article/10.1088/0004-637X/779/1/24 Venemans et al. (2013)

entry51 = np.array([["J2210+0304", "Matsuoka et al. (2018)",
                     "https://arxiv.org/pdf/1803.01861",
                     "HSC", "22h10m27.s24", "+03°04′28.″5", "",
                     "6.9", "", "", "", "", "", "", "", "",
                     "", "", "", "-24.44", "0.06", "0.06", "", "", "",
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
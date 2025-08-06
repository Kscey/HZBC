import numpy as np

entry8 = np.array([["J0014-3022/UHZ1", "Bogdan et al. (2023), Castellano et al. (2023), Goulding et al. (2023)",
                    "https://arxiv.org/abs/2305.15458, https://iopscience.iop.org/article/10.3847/2041-8213/accea5/meta, https://arxiv.org/pdf/2308.02750",
                    "JWST", "00:14:16.096", "-30:22:40.285", "",
                    "10.073", "0.002", "0.002", "4e7", "6e7", "3e7", "5e45", "", "",
                    "", "", "", "", "", "", "87.7", "7.2", "7.2",
                    "4.5", "2.9", "2.2", "4.5", "2.9", "2.2", "0.4e8", "1.8e8", "0.2e8",
                    "F444W, SFR, Mstar from Castellano et al. (2023), z from Goulding et al. (2023)"]])

# F444W, SFR, Mstar from: https://iopscience.iop.org/article/10.3847/2041-8213/accea5/meta Castellano et al. (2023)
# z from: https://arxiv.org/pdf/2308.02750 Goulding et al. (2023)

entry9 = np.array([["J0013-3020/GHZ9", "Kovacs et al. (2024), Castellano et al. (2023), Atek et al. (2023)",
                    "https://arxiv.org/abs/2403.14745, https://iopscience.iop.org/article/10.3847/2041-8213/accea5/meta, https://arxiv.org/pdf/2305.01793",
                    "JWST", "00:13:54.90", "-30:20:43.93", "",
                    "10.37", "0.32", "1.09", "8e7", "3.7e7", "3.2e7", "1e46", "0.5e46", "0.4e46",
                    "", "", "", "", "", "", "40.9", "3.9", "3.9",
                    "", "", "", "", "", "", "3.3e8", "2.9e8", "2.4e8",
                    "F444W, Mstar, SFR [14.4 (+15.0/-7.3)] from Castellano et al. (2023), SFR [0.56 (+0.23/-0.29)] from Atek et al. (2023)"]])

# F444W, Mstar, SFR from: https://iopscience.iop.org/article/10.3847/2041-8213/accea5/meta Castellano et al. (2023)
# SFR from: https://arxiv.org/pdf/2305.01793 Atek et al. (2023)

entry10 = np.array([["GNz11", "Maiolino et al. (2023), Bunker et al. (2023), Oesch et al. (2016)",
                     "https://arxiv.org/abs/2305.12492, https://arxiv.org/pdf/2302.07256, https://arxiv.org/pdf/1603.00461",
                     "JWST", "12:36:25.46", "+62:14:31.40", "",
                     "10.6", "", "", "1.6e6", "1e0.3", "1e0.3", "1.08e45", "", "",
                     "", "", "", "", "", "", "", "", "",
                     "31", "59", "19", "31", "59", "19", "", "", "",
                     "SFR from Bunker et al. (2023), coordinates from Oesch et al. (2016)"]])

# SFR from: https://arxiv.org/pdf/2302.07256 Bunker et al. (2023)
# Coordinates from: https://arxiv.org/pdf/1603.00461 Oesch et al. (2016)

entry11 = np.array([["J1420+5253/CEERS_01019/CEERS_1019", "Larson et al. (2023)",
                     "https://arxiv.org/abs/2303.08918",
                     "JWST", "14:20:08.49", "+52:53:26.38", "",
                     "8.679", "0.09", "0.15", "log6.95", "log0.37", "log0.37", "log45.1", "log0.2", "log0.2",
                     "1.2", "0.5", "0.5", "", "", "", "", "", "",
                     "30", "", "", "30", "", "", "", "", "",
                     ""]])

entry36 = np.array([["J1420+5302/CEERS_01244", "Harikane et al. (2023)",
                     "https://arxiv.org/pdf/2303.11946",
                     "JWST", "14:20:57.76", "+53:02:09.80", "",
                     "4.478", "", "", "3.2e7", "0.3e7", "0.2e7", "1.9e45", "3.8e45", "0.6e45",
                     "0.46", "1.04", "0.16", "", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     "+df_Edd may be unusually large because Harikane et al. (2023) estimates L_bol and -dL_bol using equation 17 but estimates +dL_bol using equation 18"]])

entry37 = np.array([["J0014-3025/GLASS_160133", "Harikane et al. (2023)",
                     "https://arxiv.org/pdf/2303.11946",
                     "JWST", "00:14:19.27", "-30:25:27.80", "",
                     "4.015", "", "", "2.3e6", "0.1e6", "0.1e6", "1.1e45", "6.1e45", "0.9e45",
                     "3.68", "21.21", "2.84", "", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     "+df_Edd may be unusually large because Harikane et al. (2023) estimates L_bol and -dL_bol using equation 17 but estimates +dL_bol using equation 18"]])

entry38 = np.array([["J0014-3025/GLASS_150029", "Harikane et al. (2023)",
                     "https://arxiv.org/pdf/2303.11946",
                     "JWST", "00:14:18.52", "-30:25:21.30", "",
                     "4.583", "", "", "3.7e6", "0.2e6", "0.3e6", "9.1e44", "13.8e44", "7.1e44",
                     "1.89", "3.31", "1.49", "", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     "+df_Edd may be unusually large because Harikane et al. (2023) estimates L_bol and -dL_bol using equation 17 but estimates +dL_bol using equation 18"]])

entry39 = np.array([["J1419+5252/CEERS_00746/CEERS 3210", "Harikane et al. (2023)",
                     "https://arxiv.org/pdf/2303.11946",
                     "JWST", "14:19:14.19", "+52:52:06.05", "",
                     "5.624", "", "", "5.8e7", "1.5e7", "1.3e7", "1.1e46", "0.1e46", "0.2e46",
                     "1.47", "0.60", "0.52", "", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     "+df_Edd may be unusually large because Harikane et al. (2023) estimates L_bol and -dL_bol using equation 17 but estimates +dL_bol using equation 18"]])

entry40 = np.array([["J1420+5303/CEERS_01665", "Harikane et al. (2023)",
                     "https://arxiv.org/pdf/2303.11946",
                     "JWST", "14:20:42.77", "+53:03:33.07", "",
                     "4.483", "", "", "1.9e7", "0.8e7", "0.5e7", "4.8e45", "7.2e45", "3.6e45",
                     "1.93", "4.61", "1.59", "", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     "+df_Edd may be unusually large because Harikane et al. (2023) estimates L_bol and -dL_bol using equation 17 but estimates +dL_bol using equation 18"]])

entry41 = np.array([["J1419+5249/CEERS_00672", "Harikane et al. (2023)",
                     "https://arxiv.org/pdf/2303.11946",
                     "JWST", "14:19:33.52", "+52:49:58.07", "",
                     "5.666", "", "", "5.0e7", "1.7e7", "1.3e7", "4.3e45", "0.4e45", "1.4e45",
                     "0.65", "0.31", "0.33", "", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     "+df_Edd may be unusually large because Harikane et al. (2023) estimates L_bol and -dL_bol using equation 17 but estimates +dL_bol using equation 18"]])

entry42 = np.array([["J1419+5249/CEERS_02782/CEERS 1670", "Harikane et al. (2023)",
                    "https://arxiv.org/pdf/2303.11946",
                     "JWST", "14:19:17.63", "+52:49:49.00", "",
                     "5.241", "", "", "4.2e7", "1.2e7", "1.0e7", "2.8e45", "2.3e45", "1.4e45",
                     "0.51", "0.71", "0.32", "", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     "+df_Edd may be unusually large because Harikane et al. (2023) estimates L_bol and -dL_bol using equation 17 but estimates +dL_bol using equation 18"]])

entry43 = np.array([["J1419+5252/CEERS_00397", "Harikane et al. (2023)",
                     "https://arxiv.org/pdf/2303.11946",
                     "JWST", "14:19:20.69", "+52:52:57.07", "",
                     "6.000", "", "", "1.0e7", "0.8e7", "0.5e7", "2.8e45", "14.2e45", "2.2e45",
                     "2.02", "20.68", "1.80", "", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     "+df_Edd may be unusually large because Harikane et al. (2023) estimates L_bol and -dL_bol using equation 17 but estimates +dL_bol using equation 18"]])

entry44 = np.array([["J1420+5258/CEERS_00717", "Harikane et al. (2023)",
                     "https://arxiv.org/pdf/2303.11946",
                     "JWST", "14:20:19.54", "+52:58:19.09", "",
                     "6.936", "", "", "9.8e7", "4.4e7", "3.2e7", "7.1e44", "51.8e44", "4.3e44",
                     "0.06", "0.63", "0.04", "", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     "+df_Edd may be unusually large because Harikane et al. (2023) estimates L_bol and -dL_bol using equation 17 but estimates +dL_bol using equation 18"]])

entry45 = np.array([["J1420+5258/CEERS_01236", "Harikane et al. (2023)",
                     "https://arxiv.org/pdf/2303.11946",
                     "JWST", "14:20:34.87", "+52:58:02.02", "",
                     "4.484", "", "", "1.8e7", "1.0e7", "0.6e7", "1.8e44", "2.6e44", "0.5e44",
                     "0.08", "0.20", "0.04", "", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     "+df_Edd may be unusually large because Harikane et al. (2023) estimates L_bol and -dL_bol using equation 17 but estimates +dL_bol using equation 18"]])

entry313 = np.array([["J0014-3022/GHZ1", "Castellano et al. (2023)",
                     "https://iopscience.iop.org/article/10.3847/2041-8213/accea5/meta",
                     "JWST", "00:14:02.86", "-30:22:18.69", "",
                     "10.47", "0.38", "0.89", "", "", "", "", "", "",
                     "", "", "", "", "", "", "111.8", "4.4", "4.4",
                     "10.7", "42.7", "4.7", "10.7", "42.7", "4.7", "11.5e8", "7.1e8", "10.3e8",
                     ""]])

entry314 = np.array([["J0014-3021/GHZ4", "Castellano et al. (2023)",
                     "https://iopscience.iop.org/article/10.3847/2041-8213/accea5/meta",
                     "JWST", "00:14:03.30", "-30:21:05.62", "",
                     "10.27", "1.2", "1.4", "", "", "", "", "", "",
                     "", "", "", "", "", "", "41.7", "3.1", "3.1",
                     "2.0", "14.2", "0.4", "2.0", "14.2", "0.4", "4.3e8", "1.5e8", "3.9e8",
                     ""]])

entry315 = np.array([["J0013-3019/GHZ7", "Castellano et al. (2023)",
                     "https://iopscience.iop.org/article/10.3847/2041-8213/accea5/meta",
                     "JWST", "00:13:48.33", "-30:19:14.58", "",
                     "10.62", "0.55", "1.02", "", "", "", "", "", "",
                     "", "", "", "", "", "", "28.8", "3.6", "3.6",
                     "3.2", "10.0", "0.5", "3.2", "10.0", "0.5", "2.1e8", "1.8e8", "1.7e8",
                     ""]])

entry316 = np.array([["J0013-3019/GHZ8", "Castellano et al. (2023)",
                     "https://iopscience.iop.org/article/10.3847/2041-8213/accea5/meta",
                     "JWST", "00:13:48.34", "-30:19:18.47", "",
                     "10.85", "0.45", "0.57", "", "", "", "", "", "",
                     "", "", "", "", "", "", "53.7", "5.2", "5.2",
                     "17.5", "13.6", "12.3", "17.5", "13.6", "12.3", "0.8e8", "6.4e8", "0.16e8",
                     ""]])

entry317 = np.array([["J0014-3025/DHZ1", "Castellano et al. (2023)",
                     "https://iopscience.iop.org/article/10.3847/2041-8213/accea5/meta",
                     "JWST", "00:14:28.14", "-30:25:32.03", "",
                     "9.3127", "0.0002", "0.0002", "", "", "", "", "", "",
                     "", "", "", "", "", "", "353.3", "17.9", "17.9",
                     "25.4", "3.2", "4.3", "25.4", "3.2", "4.3", "25e8", "6.6e8", "5.0e8",
                     ""]])

entry475 = np.array([["J1237+6212/GOODS-N-4014", "Matthee et al. (2024)",
                     "https://iopscience.iop.org/article/10.3847/1538-4357/ad2345",
                     "JWST", "12:37:12.03", "+62:12:43.36", "",
                     "5.228", "", "", "log7.58", "log0.08", "log0.08", "9.3e44", "0.5e44", "0.5e44",
                     "", "", "", "", "", "", "389.3", "13.4", "13.4",
                     "", "", "", "", "", "", "", "", "",
                     "little red dot"]])

entry476 = np.array([["J1237+6214/GOODS-N-9771", "Matthee et al. (2024)",
                     "https://iopscience.iop.org/article/10.3847/1538-4357/ad2345",
                     "JWST", "12:37:07.44", "+62:14:50.31", "",
                     "5.538", "", "", "log8.55", "log0.03", "log0.03", "65.8e44", "1.6e44", "1.6e44",
                     "", "", "", "", "", "", "2494.8", "124.7", "124.7",
                     "", "", "", "", "", "", "", "", "",
                     "little red dot"]])

entry477 = np.array([["J1237+6215/GOODS-N-12839", "Matthee et al. (2024)",
                     "https://iopscience.iop.org/article/10.3847/1538-4357/ad2345",
                     "JWST", "12:37:22.63", "+62:15:48.11", "",
                     "5.241", "", "", "log8.01", "log0.06", "log0.06", "31.2e44", "1.2e44", "1.2e44",
                     "", "", "", "", "", "", "1250.3", "62.5", "62.5",
                     "", "", "", "", "", "", "", "", "",
                     "little red dot"]])

entry478 = np.array([["J1236+6216/GOODS-N-13733", "Matthee et al. (2024)",
                     "https://iopscience.iop.org/article/10.3847/1538-4357/ad2345",
                     "JWST", "12:36:13.70", "+62:16:08.18", "",
                     "5.236", "", "", "log7.49", "log0.10", "log0.10", "5.2e44", "0.3e44", "0.3e44",
                     "", "", "", "", "", "", "245.8", "12.3", "12.3",
                     "", "", "", "", "", "", "", "", "",
                     "little red dot"]])

entry479 = np.array([["J1236+6216/GOODS-N-14409", "Matthee et al. (2024)",
                     "https://iopscience.iop.org/article/10.3847/1538-4357/ad2345",
                     "JWST", "12:36:17.30", "+62:16:24.35", "",
                     "5.139", "", "", "log7.21", "log0.14", "log0.14", "7.4e44", "0.9e44", "0.9e44",
                     "", "", "", "", "", "", "224.3", "11.2", "11.2",
                     "", "", "", "", "", "", "", "", "",
                     "little red dot"]])

entry480 = np.array([["J1237+6216/GOODS-N-15498", "Matthee et al. (2024)",
                     "https://iopscience.iop.org/article/10.3847/1538-4357/ad2345",
                     "JWST", "12:37:08.53", "+62:16:50.82", "",
                     "5.086", "", "", "log7.71", "log0.11", "log0.11", "10.4e44", "1.9e44", "1.9e44",
                     "", "", "", "", "", "", "488.7", "24.4", "24.4",
                     "", "", "", "", "", "", "", "", "",
                     "little red dot"]])

entry481 = np.array([["J1236+6217/GOODS-N-16813", "Matthee et al. (2024)",
                     "https://iopscience.iop.org/article/10.3847/1538-4357/ad2345",
                     "JWST", "12:36:43.03", "+62:17:33.12", "",
                     "5.355", "", "", "log7.55", "log0.12", "log0.12", "9.1e44", "1.0e44", "1.0e44",
                     "", "", "", "", "", "", "439.2", "22.0", "22.0",
                     "", "", "", "", "", "", "", "", "",
                     "little red dot"]])

entry482 = np.array([["J1148+5254/J1148-7111", "Matthee et al. (2024)",
                     "https://iopscience.iop.org/article/10.3847/1538-4357/ad2345",
                     "JWST", "11:48:24.41", "+52:54:28.66", "",
                     "4.339", "", "", "log7.92", "log0.10", "log0.10", "10.8e44", "0.8e44", "0.8e44",
                     "", "", "", "", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     "little red dot"]])

entry483 = np.array([["J1148+5251/J1148-18404", "Matthee et al. (2024)",
                     "https://iopscience.iop.org/article/10.3847/1538-4357/ad2345",
                     "JWST", "11:48:13.91", "+52:51:46.09", "",
                     "5.011", "", "", "log7.79", "log0.14", "log0.14", "6.9e44", "1.4e44", "1.4e44",
                     "", "", "", "", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     "little red dot"]])

entry484 = np.array([["J1148+5250/J1148-21787", "Matthee et al. (2024)",
                     "https://iopscience.iop.org/article/10.3847/1538-4357/ad2345",
                     "JWST", "11:48:05.14", "+52:50:01.04", "",
                     "4.277", "", "", "log7.59", "log0.18", "log0.18", "6.7e44", "1.6e44", "1.6e44",
                     "", "", "", "", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     "little red dot"]])

entry485 = np.array([["J0100+2804/J0100-2017", "Matthee et al. (2024)",
                     "https://iopscience.iop.org/article/10.3847/1538-4357/ad2345",
                     "JWST", "01:00:13.93", "+28:04:20.69", "",
                     "4.938", "", "", "log7.44", "log0.11", "log0.11", "6.7e44", "0.8e44", "0.8e44",
                     "", "", "", "", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     "little red dot"]])

entry486 = np.array([["J0100+2800/J0100-12446", "Matthee et al. (2024)",
                     "https://iopscience.iop.org/article/10.3847/1538-4357/ad2345",
                     "JWST", "01:00:11.58", "+28:00:34.98", "",
                     "4.699", "", "", "log7.46", "log0.06", "log0.06", "12.9e44", "0.6e44", "0.6e44",
                     "", "", "", "", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     "little red dot"]])

entry487 = np.array([["J0100+2803/J0100-15157", "Matthee et al. (2024)",
                     "https://iopscience.iop.org/article/10.3847/1538-4357/ad2345",
                     "JWST", "01:00:07.26", "+28:03:00.64", "",
                     "4.941", "", "", "log7.35", "log0.08", "log0.08", "6.5e44", "0.6e44", "0.6e44",
                     "", "", "", "", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     "little red dot"]])

entry488 = np.array([["J0100+2803/J0100-16221", "Matthee et al. (2024)",
                     "https://iopscience.iop.org/article/10.3847/1538-4357/ad2345",
                     "JWST", "01:00:08.17", "+28:03:05.68", "",
                     "4.349", "", "", "log7.53", "log0.07", "log0.07", "7.1e44", "0.6e44", "0.6e44",
                     "", "", "", "", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     "little red dot"]])

entry489 = np.array([["J0148+0557/J0148-976", "Matthee et al. (2024)",
                     "https://iopscience.iop.org/article/10.3847/1538-4357/ad2345",
                     "JWST", "01:48:35.08", "+05:57:20.97", "",
                     "4.163", "", "", "log7.11", "log0.18", "log0.18", "5.2e44", "0.7e44", "0.7e44",
                     "", "", "", "", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     "little red dot"]])

entry490 = np.array([["J0148+0559/J0148-4214", "Matthee et al. (2024)",
                     "https://iopscience.iop.org/article/10.3847/1538-4357/ad2345",
                     "JWST", "01:48:33.29", "+05:59:50.04", "",
                     "5.019", "", "", "log7.32", "log0.10", "log0.10", "5.9e44", "0.4e44", "0.4e44",
                     "", "", "", "", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     "little red dot"]])

entry491 = np.array([["J0148+0600/J0148-12884", "Matthee et al. (2024)",
                     "https://iopscience.iop.org/article/10.3847/1538-4357/ad2345",
                     "JWST", "01:48:41.58", "+06:00:57.30", "",
                     "4.602", "", "", "log6.91", "log0.15", "log0.15", "5.0e44", "0.6e44", "0.6e44",
                     "", "", "", "", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     "little red dot"]])

entry492 = np.array([["J1119+0639/J1120-7546", "Matthee et al. (2024)",
                     "https://iopscience.iop.org/article/10.3847/1538-4357/ad2345",
                     "JWST", "11:19:59.86", "+06:39:17.01", "",
                     "4.967", "", "", "log7.56", "log0.11", "log0.11", "13.8e44", "1.6e44", "1.6e44",
                     "", "", "", "", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     "little red dot"]])

entry493 = np.array([["J1120+0643/J1120-14389", "Matthee et al. (2024)",
                     "https://iopscience.iop.org/article/10.3847/1538-4357/ad2345",
                     "JWST", "11:20:00.89", "+06:43:10.42", "",
                     "4.897", "", "", "log7.65", "log0.07", "log0.07", "8.4e44", "0.8e44", "0.8e44",
                     "", "", "", "", "", "", "", "", "",
                     "", "", "", "", "", "", "", "", "",
                     "little red dot"]])
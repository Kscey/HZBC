import math
import functions

# A calculator to check fEdd from https://iopscience.iop.org/article/10.3847/1538-4357/aa9185/pdf Mazzucchelli et al. (2017) and https://arxiv.org/pdf/2306.16474 Mazzuchelli et al. (2023)

# format: BH# = ["BH name", "L_bol", "+dL_bol", "-dL_bol", "BHM", "+dBHM", "-dBHM"]

# Mazzuchelli et al. (2017):

BH1 = ["VIK J0109–3047", 0.51e47, 0.05e47, 0.06e47, 1.33e9, 0.38e9, 0.62e9]

# the rest are done elsewhere

# Mazzucchelli et al. (2023):

BH2 = ["PSOJ007+04", functions.unLog(47.12), functions.unLogUp(47.12, 0.15), functions.unLogDown(47.12, 0.22), functions.unLog(9.89), functions.unLogUp(9.89, 0.09), functions.unLogDown(9.89, 0.11)]

BH3 = ["PSOJ009-10", functions.unLog(47.34), functions.unLogUp(47.34, 0.08), functions.unLogDown(47.34, 0.09), functions.unLog(9.9), functions.unLogUp(9.9, 0.08), functions.unLogDown(9.9, 0.1)]

BH4 = ["PSOJ023-02", functions.unLog(47.33), functions.unLogUp(47.33, 0.06), functions.unLogDown(47.33, 0.07), functions.unLog(9.39), functions.unLogUp(9.39, 0.05), functions.unLogDown(9.39, 0.06)]

BH5 = ["PSOJ025-11", functions.unLog(47.27), functions.unLogUp(47.27, 0.09), functions.unLogDown(47.27, 0.11), functions.unLog(9.34), functions.unLogUp(9.34, 0.06), functions.unLogDown(9.34, 0.07)]

BH6 = ["PSOJ029-29", functions.unLog(47.49), functions.unLogUp(47.49, 0.07), functions.unLogDown(47.49, 0.08), functions.unLog(9.34), functions.unLogUp(9.34, 0.07), functions.unLogDown(9.34, 0.09)]

BH7 = ["ATLASJ029-36", functions.unLog(47.1), functions.unLogUp(47.1, 0.03), functions.unLogDown(47.1, 0.03), functions.unLog(9.2), functions.unLogUp(9.2, 0.06), functions.unLogDown(9.2, 0.07)]

BH8 = ["VDESJ0224-4711", functions.unLog(47.54), functions.unLogUp(47.54, 0.06), functions.unLogDown(47.54, 0.06), functions.unLog(9.19), functions.unLogUp(9.19, 0.06), functions.unLogDown(9.19, 0.08)]

BH9 = ["PSOJ060+24", functions.unLog(47.3), functions.unLogUp(47.3, 0.08), functions.unLogDown(47.3, 0.1), functions.unLog(9.18), functions.unLogUp(9.18, 0.07), functions.unLogDown(9.18, 0.09)]

BH10 = ["J0408-5632", functions.unLog(47.19), functions.unLogUp(47.19, 0.08), functions.unLogDown(47.19, 0.1), functions.unLog(9.31), functions.unLogUp(9.31, 0.08), functions.unLogDown(9.31, 0.09)]

BH11 = ["PSOJ065-26", functions.unLog(47.35), functions.unLogUp(47.35, 0.04), functions.unLogDown(47.35, 0.04), functions.unLog(9.56), functions.unLogUp(9.56, 0.13), functions.unLogDown(9.56, 0.18)]

BH12 = ["PSOJ065+01", functions.unLog(47.2), functions.unLogUp(47.2, 0.08), functions.unLogDown(47.2, 0.1), functions.unLog(9.6), functions.unLogUp(9.6, 0.12), functions.unLogDown(9.6, 0.17)]

BH13 = ["PSOJ089-15", functions.unLog(47.57), functions.unLogUp(47.57, 0.05), functions.unLogDown(47.57, 0.06), functions.unLog(9.57), functions.unLogUp(9.57, 0.08), functions.unLogDown(9.57, 0.1)]

BH14 = ["PSOJ108+08", functions.unLog(47.46), functions.unLogUp(47.46, 0.1), functions.unLogDown(47.46, 0.13), functions.unLog(9.49), functions.unLogUp(9.49, 0.08), functions.unLogDown(9.49, 0.1)]

BH15 = ["SDSSJ0842+1218", functions.unLog(47.25), functions.unLogUp(47.25, 0.05), functions.unLogDown(47.25, 0.05), functions.unLog(9.3), functions.unLogUp(9.3, 0.07), functions.unLogDown(9.3, 0.09)]

BH16 = ["J0923+0402", functions.unLog(47.51), functions.unLogUp(47.51, 0.07), functions.unLogDown(47.51, 0.08), functions.unLog(9.42), functions.unLogUp(9.42, 0.16), functions.unLogDown(9.42, 0.24)]

BH17 = ["PSOJ158-14", functions.unLog(47.56), functions.unLogUp(47.56, 0.1), functions.unLogDown(47.56, 0.13), functions.unLog(9.31), functions.unLogUp(9.31, 0.07), functions.unLogDown(9.31, 0.09)]

BH18 = ["PSOJ183+05", functions.unLog(47.2), functions.unLogUp(47.2, 0.16), functions.unLogDown(47.2, 0.25), functions.unLog(9.41), functions.unLogUp(9.41, 0.21), functions.unLogDown(9.41, 0.41)]

BH19 = ["PSOJ183-12", functions.unLog(47.41), functions.unLogUp(47.41, 0.06), functions.unLogDown(47.41, 0.07), functions.unLog(9.22), functions.unLogUp(9.22, 0.12), functions.unLogDown(9.22, 0.17)]

BH20 = ["PSOJ217-16", functions.unLog(47.26), functions.unLogUp(47.26, 0.08), functions.unLogDown(47.26, 0.1), functions.unLog(9.02), functions.unLogUp(9.02, 0.19), functions.unLogDown(9.02, 0.34)]

BH21 = ["PSOJ217-07", functions.unLog(47.13), functions.unLogUp(47.13, 0.15), functions.unLogDown(47.13, 0.23), functions.unLog(8.9), functions.unLogUp(8.9, 0.16), functions.unLogDown(8.9, 0.27)]

BH22 = ["PSOJ231-20", functions.unLog(47.36), functions.unLogUp(47.36, 0.04), functions.unLogDown(47.36, 0.04), functions.unLog(9.52), functions.unLogUp(9.52, 0.04), functions.unLogDown(9.52, 0.04)]

BH23 = ["J1535+1943", functions.unLog(47.6), functions.unLogUp(47.6, 0.1), functions.unLogDown(47.6, 0.13), functions.unLog(9.8), functions.unLogUp(9.8, 0.06), functions.unLogDown(9.8, 0.07)]

BH24 = ["PSOJ239-07", functions.unLog(47.46), functions.unLogUp(47.46, 0.1), functions.unLogDown(47.46, 0.13), functions.unLog(9.42), functions.unLogUp(9.42, 0.05), functions.unLogDown(9.42, 0.06)]

BH25 = ["PSOJ242-12", functions.unLog(47.26), functions.unLogUp(47.26, 0.12), functions.unLogDown(47.26, 0.17), functions.unLog(9.51), functions.unLogUp(9.51, 0.1), functions.unLogDown(9.51, 0.13)]

BH26 = ["PSOJ308-27", functions.unLog(47.35), functions.unLogUp(47.35, 0.06), functions.unLogDown(47.35, 0.07), functions.unLog(9.09), functions.unLogUp(9.09, 0.05), functions.unLogDown(9.09, 0.05)]

BH27 = ["PSOJ323+12", functions.unLog(47.27), functions.unLogUp(47.27, 0.06), functions.unLogDown(47.27, 0.07), functions.unLog(8.92), functions.unLogUp(8.92, 0.09), functions.unLogDown(8.92, 0.12)]

BH28 = ["VIK J2211-3206", functions.unLog(47.44), functions.unLogUp(47.44, 0.04), functions.unLogDown(47.44, 0.05), functions.unLog(9.3), functions.unLogUp(9.3, 0.15), functions.unLogDown(9.3, 0.24)]

BH29 = ["VDES J2250-5051", functions.unLog(47.44), functions.unLogUp(47.44, 0.07), functions.unLogDown(47.44, 0.08), functions.unLog(9.66), functions.unLogUp(9.66, 0.41), functions.unLogDown(9.66, 0.41)]

BH30 = ["SDSSJ2310+18", functions.unLog(47.49), functions.unLogUp(47.49, 0.1), functions.unLogDown(47.49, 0.13), functions.unLog(9.67), functions.unLogUp(9.67, 0.06), functions.unLogDown(9.67, 0.08)]

BH31 = ["PSOJ359-06", functions.unLog(47.3), functions.unLogUp(47.3, 0.13), functions.unLogDown(47.3, 0.19), functions.unLog(9.0), functions.unLogUp(9.0, 0.09), functions.unLogDown(9.0, 0.12)]

BH32 = ["SDSSJ0100+28", functions.unLog(48.15), functions.unLogUp(48.15, 0.04), functions.unLogDown(48.15, 0.04), functions.unLog(10.1), functions.unLogUp(10.1, 0.2), functions.unLogDown(10.1, 0.1)]

BH33 = ["ATLASJ025-33", functions.unLog(47.66), functions.unLogUp(47.66, 0.02), functions.unLogDown(47.66, 0.02), functions.unLog(9.37), functions.unLogUp(9.37, 0.17), functions.unLogDown(9.37, 0.1)]

BH34 = ["ULASJ0148+06", functions.unLog(47.46), functions.unLogUp(47.46, 0.04), functions.unLogDown(47.46, 0.04), functions.unLog(9.58), functions.unLogUp(9.58, 0.08), functions.unLogDown(9.58, 0.06)]

BH35 = ["PSOJ036+03", functions.unLog(47.5), functions.unLogUp(47.5, 0.04), functions.unLogDown(47.5, 0.05), functions.unLog(9.43), functions.unLogUp(9.43, 0.08), functions.unLogDown(9.43, 0.07)]

BH36 = ["QSOJ0439+1634", functions.unLog(48.33), functions.unLogUp(48.33, 0.03), functions.unLogDown(48.33, 0.03), functions.unLog(9.72), functions.unLogUp(9.72, 0.07), functions.unLogDown(9.72, 0.09)]

BH37 = ["SDSSJ0818+17", functions.unLog(47.56), functions.unLogUp(47.56, 0.08), functions.unLogDown(47.56, 0.1), functions.unLog(9.76), functions.unLogUp(9.76, 0.06), functions.unLogDown(9.76, 0.07)]

BH38 = ["SDSSJ0836+00 (L_bol missing error)", functions.unLog(47.85), functions.unLogUp(47.85, 0), functions.unLogDown(47.85, 0), functions.unLog(9.59), functions.unLogUp(9.59, 0.13), functions.unLogDown(9.59, 0.08)]

BH39 = ["SDSSJ0927+20", functions.unLog(47.08), functions.unLogUp(47.08, 0.15), functions.unLogDown(47.08, 0.24), functions.unLog(9.11), functions.unLogUp(9.11, 0.1), functions.unLogDown(9.11, 0.09)]

BH40 = ["SDSSJ1030+05", functions.unLog(47.32), functions.unLogUp(47.32, 0.11), functions.unLogDown(47.32, 0.14), functions.unLog(9.27), functions.unLogUp(9.27, 0.09), functions.unLogDown(9.27, 0.09)]

BH41 = ["SDSSJ1306+03", functions.unLog(47.24), functions.unLogUp(47.24, 0.05), functions.unLogDown(47.24, 0.06), functions.unLog(9.29), functions.unLogUp(9.29, 0.09), functions.unLogDown(9.29, 0.18)]

BH42 = ["ULASJ1319+09", functions.unLog(47.3), functions.unLogUp(47.3, 0.07), functions.unLogDown(47.3, 0.08), functions.unLog(9.53), functions.unLogUp(9.53, 0.05), functions.unLogDown(9.53, 0.11)]

BH43 = ["CFHQSJ1509-1", functions.unLog(47.37), functions.unLogUp(47.37, 0.06), functions.unLogDown(47.37, 0.08), functions.unLog(9.3), functions.unLogUp(9.3, 0.15), functions.unLogDown(9.3, 0.17)]




for i in range(1, 100000):

    try:

        currentBH = eval(f'BH{i}')

        LEdd = 1.3 * (10 ** 38) * currentBH[4]

        fEdd = currentBH[1] / LEdd

        fEddUp = fEdd * math.sqrt((currentBH[2] / currentBH [1]) **2 + (currentBH[5] / currentBH [4]) ** 2) 

        fEddDown = fEdd * math.sqrt((currentBH[3] / currentBH [1]) **2 + (currentBH[6] / currentBH [4]) ** 2)

        print("{}: {}, {}, {}".format(currentBH[0], round(fEdd, 6), round(fEddUp, 6), round(fEddDown, 6)))


    except:

        break


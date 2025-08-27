import numpy as np
import pandas as pd
import functions
import dataMain
import dataTentative
import dataGalaxy

def conversion():

        # Converts the bolometric luminosities from units of solar luminosities to ergs per second

        if "S" in currentEntry[0, 13]:

            currentEntry[0, 13] = functions.solarLuminosityToErgsPerS(
                currentEntry[0, 13])

        if "S" in currentEntry[0, 14]:

            currentEntry[0, 14] = functions.solarLuminosityToErgsPerS(
                currentEntry[0, 14])

        if "S" in currentEntry[0, 15]:

            currentEntry[0, 15] = functions.solarLuminosityToErgsPerS(
                currentEntry[0, 15])

        # Calculates the black hole mass if it is missing and M1450 is provided

        if currentEntry[0, 10] == "" and currentEntry[0, 19] != "":

            if currentEntry[0, 11] == "" and currentEntry[0, 21] != "":

                currentEntry[0, 11] = functions.estimateMassUpperError(currentEntry[0, 19], currentEntry[0, 21])

            if currentEntry[0, 12] == "" and currentEntry[0, 20] != "":

                currentEntry[0, 12] = functions.estimateMassLowerError(currentEntry[0, 19], currentEntry[0, 20])

            currentEntry[0, 10] = functions.estimateMassBlackHole(currentEntry[0, 19])

            if currentEntry[0, 34] == "":

                currentEntry[0, 34] += "mass using formula [1]"

            else:

                currentEntry[0, 34] += ", mass using formula [1]"
            
        # Converts the log values and errors of BHM, L_bol, Mstar, f_Edd to non-log values

        if "log" in currentEntry[0, 11]:

            currentEntry[0, 11] = functions.logToUpperError(currentEntry[0, 10], currentEntry[0, 11])

        if "log" in currentEntry[0, 12]:

            currentEntry[0, 12] = functions.logToLowerError(currentEntry[0, 10], currentEntry[0, 12])

        if "log" in currentEntry[0, 10]:

            currentEntry[0, 10] = functions.logToValue(currentEntry[0, 10])

        if "log" in currentEntry[0, 14]:

            currentEntry[0, 14] = functions.logToUpperError(currentEntry[0, 13], currentEntry[0, 14])

        if "log" in currentEntry[0, 15]:

            currentEntry[0, 15] = functions.logToLowerError(currentEntry[0, 13], currentEntry[0, 15])

        if "log" in currentEntry[0, 13]:

            currentEntry[0, 13] = functions.logToValue(currentEntry[0, 13])

        if "log" in currentEntry[0, 32]:

            currentEntry[0, 32] = functions.logToUpperError(currentEntry[0, 31], currentEntry[0, 32])

        if "log" in currentEntry[0, 33]:

            currentEntry[0, 33] = functions.logToLowerError(currentEntry[0, 31], currentEntry[0, 33])
        
        if "log" in currentEntry[0, 31]:

            currentEntry[0, 31] = functions.logToValue(currentEntry[0, 31])

        if "log" in currentEntry[0, 17]:

            currentEntry[0, 17] = functions.logToUpperError(currentEntry[0, 16], currentEntry[0, 17])

        if "log" in currentEntry[0, 18]:

            currentEntry[0, 18] = functions.logToLowerError(currentEntry[0, 16], currentEntry[0, 18])

        if "log" in currentEntry[0, 16]:

            currentEntry[0, 16] = functions.logToValuef_Edd(currentEntry[0, 16])


# Column names respectively stand for:
# Name = Name
# Ref = Reference
# link = Online link
# Inst = Observational instrument
# AC = Right ascension coordinates (***NEW)
# DEC = Declination coordinates (***NEW)
# distance = distance (*** NEW)
# z = Redshift
# +dz = Redshift upper bound
# -dz = Redshift lower bound
# M [M_sun] = Mass (in units of solar mass)
# +dM = Mass upper bound
# -dM = Mass lower bound
# L_bol [ergs/s] = Bolometric luminosity (in units of ergs per second)
# +dL_bol = Bolometric luminosity upper bound
# -dL_bol = Bolometric luminosity lower bound
# f_Edd = Eddington luminosity
# +dF_Edd = Eddington luminosity upper bound
# -df_Edd = Eddington luminosity lower bound
# M1450 = M1450 (***NEW)
# +dM1450 = M1450 upper bound (***NEW)
# -dM1450 = M1450 lower bound (***NEW)
# F444W = F444W (***NEW)
# +dF44W = F444W upper bound (***NEW)
# -dF444W = F444W lower bound (***NEW)
# SFR_TIR = Star formation rate (TIR) (***NEW)
# +dSFR_TIR = Star formation rate (TIR) upper bound (***NEW)
# -dSFR_TIR = Star formation rate (TIR) lower bound (***NEW)
# comment = comments (e.g. origins of data)

columnNames = ["Name", "Ref",
               "Link",
               "Inst", "RA", "DEC", "Distance",
               "z", "+dz", "-dz", "M [M_sun]", "+dM", "-dM", "L_bol [erg/s]", "+dL_bol", "-dL_bol",
               "f_Edd", "+df_Edd", "-df_Edd", "M1450", "+dM1450", "-dM1450", "F444W", "+dF44W", "-dF444W",
               "SFR_CII", "+dSFR_CII", "-dSFR_CII", "SFR_TIR", "+dSFR_TIR", "-dSFR_TIR", "Mstar [M_sun]", "+dMstar", "-dMstar",
               "comment"]

arrListMain = dataMain.entry0

for i in range(1, 10000):

    try:

        currentEntry = eval(f'dataMain.entry{i}')

        conversion()

        arrListMain = np.vstack((arrListMain, currentEntry))

    except:
        continue

dataframe = pd.DataFrame(data=arrListMain, columns=columnNames)

dataframe.to_csv("catalogMain.csv")

print(dataframe)

arrListTentative = dataTentative.entry25

for i in range(26, 10000):

    try:

        currentEntry = eval(f'dataTentative.entry{i}')

        conversion()

        arrListTentative = np.vstack((arrListTentative, currentEntry))

    except:
        continue

dataframe = pd.DataFrame(data=arrListTentative, columns=columnNames)

dataframe.to_csv("catalogTentative.csv")

print(dataframe)

arrListGalaxy = dataGalaxy.entry9

for i in range(9, 10000):

    try:

        currentEntry = eval(f'dataGalaxy.entry{i}')

        conversion()

        arrListGalaxy = np.vstack((arrListGalaxy, currentEntry))

    except:
        continue

dataframe = pd.DataFrame(data=arrListGalaxy, columns=columnNames)

dataframe.to_csv("catalogGalaxy.csv")

print(dataframe)


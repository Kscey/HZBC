import numpy as np
import pandas as pd
import functions
import data


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
               "SFR_CII", "+dSFR_CII", "-dSFR_CII", "SFR_TIR", "+dSFR_TIR", "-dSFR_TIR", "Mstar",
               "comment"]

arrList = data.entry0

for i in range(1, 10000):

    try:

        currentEntry = eval(f'data.entry{i}')

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

            currentEntry[0, 10] = functions.estimateMassBlackHole(currentEntry[0, 19])

            if currentEntry[0, 11] == "" and currentEntry[0, 20] != "":

                currentEntry[0, 11] = functions.estimateMassBlackHole(currentEntry[0, 20])

            if currentEntry[0, 12] == "" and currentEntry[0, 21] != "":

                currentEntry[0, 12] = functions.estimateMassBlackHole(currentEntry[0, 21])


        arrList = np.vstack((arrList, currentEntry))

    except:
        break

dataframe = pd.DataFrame(data=arrList, columns=columnNames)

print(dataframe)

dataframe.to_csv("out.csv")

# Consider implementing sorting (by z), dropping duplicates, adding csv for looking at review articles

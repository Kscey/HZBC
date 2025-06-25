import numpy as np
import pandas as pd

# Calculator function for automatic unit conversion:


def solarLuminosityToErgsPerS(x):

    x = x.strip("S")

    x = x.split("e")

    luminosity = float(x[0]) * (10 ** int(x[1]))

    print(luminosity)

    return luminosity * 3.846e33


def removePositiveSciNotation(x):

    exponent = int(np.log10(np.abs(x)))
    mantissa = x/10**exponent
    y = f'{mantissa:.3f}e{exponent:.0f}'

    return y


# Column names respectively stand for:
# Name = Name
# Ref = Reference
# link = Online link
# Inst = Observational instrument
# AC = Right ascension coordinates (***NEW)
# DEC = Declination coordinates (***NEW)
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
# comment = comments (e,g. High z)

columnNames = ["Name", "Ref", "link", "Inst", "RA", "DEC", "z", "+dz", "-dz", "M [M_sun]", "+dM", "-dM",
               "L_bol [erg/s]", "+dL_bol", "-dL_bol", "f_Edd", "+df_Edd", "-df_Edd", "comment"]


# Arrays are manually populated to include or amend information
# Some bolometric luminosities need to be converted from units of solar luminosities to ergs per second (1 solar luminosity = 3.846e33 ergs per second)

entry0 = np.array([["J1342+0928", "Banados et al. (2018)", "https://arxiv.org/abs/1712.01860", "ULAS", "13h42m08s.097", "+09°28′38″28",
                  "7.5413", "0.0007", "0.0007", "7.8e8", "3.3e8", "1.9e8", "1.54e47", "", "", "1.5", "0.5", "0.4", "High z"]])

# Coordinates found from: https://iopscience.iop.org/article/10.3847/2041-8213/aa943a Venemans et al. (2017)


entry1 = np.array([["J1243+0100", "Matsuoka et al. (2019b)", "https://arxiv.org/abs/1901.10487", "HSC", "12h43m53s.93", "+01°00′38″5",
                  "7.07", "0.01", "0.01", "3.3e8", "2e8", "2e8", "1.4e46", "0.1e46", "0.1e46", "0.34", "0.2", "0.2", "High z"]])

# What does the b in 2019b mean?

entry2 = np.array([["J1120+0641", "Mortlock et al.(2011)", "https://arxiv.org/abs/1106.6088", "ULAS", " 11h20m01s.48", "+06°41′24.″3",
                    "7.085", "0.003", "0.003", "2e9", "1.5e9", "0.7e9", "6.3e13S", "0.6e13S", "0.6e13S", "1.2", "0.6", "0.5", "High z"]])

# Coordinates found from: https://arxiv.org/pdf/1311.3260 De Rosa et al. (2014)

arrList = entry0

for i in range(1, 10000):

    try:

        currentEntry = eval(f'entry{i}')

        if "S" in currentEntry[0, 12]:

            currentEntry[0, 12] = solarLuminosityToErgsPerS(
                currentEntry[0, 12])

            currentEntry[0, 12] = removePositiveSciNotation(
                currentEntry[0, 12].astype(float))

        if "S" in currentEntry[0, 13]:

            currentEntry[0, 13] = solarLuminosityToErgsPerS(
                currentEntry[0, 13])

            currentEntry[0, 13] = removePositiveSciNotation(
                currentEntry[0, 13].astype(float))

        if "S" in currentEntry[0, 14]:

            currentEntry[0, 14] = solarLuminosityToErgsPerS(
                currentEntry[0, 14])

            currentEntry[0, 14] = removePositiveSciNotation(
                currentEntry[0, 14].astype(float))

        arrList = np.vstack((arrList, currentEntry))

    except:
        break

dataframe = pd.DataFrame(data=arrList, columns=columnNames)

print(dataframe)

dataframe.to_csv("out.csv")

# Consider implementing sorting (by z), dropping duplicates

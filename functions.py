import numpy as np

# Calculator function for automatic unit conversion:

def solarLuminosityToErgsPerS(x):

    x = x.strip("S")

    x = x.split("e")

    luminosity = float(x[0]) * (10 ** int(x[1]))

    y = float(luminosity * 3.846e33)

    exponent = int(np.log10(np.abs(y)))
    mantissa = y/10**exponent
    z = f'{mantissa:.3f}e{exponent:.0f}'

    return z

# Calculator function for estimating black hole mass from M1450:

def estimateMassBlackHole(x):

    mass = 10 ** ((-float(x) -3.459) / 2.5)

    exponent = int(np.log10(np.abs(mass)))
    mantissa = mass/10**exponent
    y = f'{mantissa:.3f}e{exponent:.0f}'
    
    return y
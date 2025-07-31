import numpy as np

def removeSciNotion(x):
    
    exponent = int(np.log10(np.abs(x)))
    mantissa = x/10**exponent
    y = f'{mantissa:.3f}e{exponent:.0f}'

    return y

# Calculator function for automatic unit conversion:

def solarLuminosityToErgsPerS(x):

    x = x.strip("S")

    x = x.split("e")

    luminosity = float(x[0]) * (10 ** int(x[1]))

    y = float(luminosity * 3.846e33)

    return removeSciNotion(y)

# Calculator function for estimating black hole mass from M1450:

def estimateMassBlackHole(x):

    mass = 10 ** ((-float(x) -3.459) / 2.5)

    return removeSciNotion(mass)

def estimateMassUpperError(x, y):

    mass = 10 ** ((-(float(x) - float(y))-3.459) / 2.5) - 10 ** ((-float(x) -3.459) / 2.5)

    return removeSciNotion(mass)

def estimateMassLowerError(x, y):

    mass = 10 ** ((-float(x) -3.459) / 2.5) - 10 ** ((-(float(x) + float(y))-3.459) / 2.5)

    return removeSciNotion(mass)

def logToValue(x):

    x = x.strip("log")

    value = 10 ** float(x)

    return removeSciNotion(value)

def logToUpperError(x, y):

    x = x.strip("log")
    y = y.strip("log")

    value = 10 ** (float(x) + float(y)) - 10 ** float(x)

    return removeSciNotion(value)
    
def logToLowerError(x, y):

    x = x.strip("log")
    y = y.strip("log")

    value = 10 ** float(x) - 10 ** (float(x) - float(y))

    return removeSciNotion(value)

def logToValuef_Edd(x):

    x = x.strip("log")

    value = 10 ** float(x)

    return value

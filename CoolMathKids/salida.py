import numpy as np
import math

def g( x ):
    return x ** 2

def graficar():
    function = np.frompyfunc(g, 1, 1)
    return function([1, 2, 3])

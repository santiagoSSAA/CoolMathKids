import numpy as np
import math

def g( x ):
    if ( x < 10 ):
        return x
    else:
        return x ** 2

def graficar():
    function = np.frompyfunc(g, 1, 1)
    return function([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])

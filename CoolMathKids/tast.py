import numpy as np
import math

def myadd(x):
    if x <= 2:
        return x **2
    else:
        return x

function = np.frompyfunc(myadd, 1, 1)

print(function([1, 2, 3, 4]))
print(math.sin(2))
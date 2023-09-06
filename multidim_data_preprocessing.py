import numpy as np
import math

def log(input):
    return np.log(input)

def exp(input):
    return np.exp(input)

def stand(input):
    buffer = list()
    for dim in input:
        mean = np.mean(dim)
        std = np.std(dim)
        buffer.append ((dim-mean)/std)
    return np.array(buffer)




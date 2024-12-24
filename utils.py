import numpy as np
import random

def setseed(seed = 0):
    random.seed(seed)
    np.random.seed(seed)

def getdata(para, n=1, distribution = "exp"):
    x = [0 for _ in range(n)]
    if distribution == "normal":
        x = np.random.normal(para[0],para[1],n)
    elif distribution == "exp":
        x = np.random.exponential(1/para[0], size=n)
    elif distribution == "uni":
        x = np.random.uniform(para[0], para[1], n)
    elif distribution == "bi":
        x = np.random.binomial(para[0], para[1], n)
    elif distribution == "poi":
        x = np.random.poisson(para[0], n)
    return x

def getf(_x):
    res =  (np.exp((-0.5)*_x**2) / np.sqrt(2*np.pi))
    return res
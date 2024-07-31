import matplotlib.pyplot as plt
import numpy as np

from fuzlab.trimf import trimf
from fuzlab.gaussmf import gaussmf
from fuzlab.trapmf import trapmf

def evalmf(mf, x):
    
    if mf.Type == 'trimf':
        y = trimf(x, mf.Parameters)
    if mf.Type == 'trapmf':
        y = trapmf(x, mf.Parameters)
    elif mf.Type == 'gaussmf':
        y = gaussmf(x, mf.Parameters)

    return y
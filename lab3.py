import numpy as np
import sympy as sp
import scipy as sc
from scipy.linalg import lu
from scipy.stats import mode, chisquare
from lab1 import X, fmt, print_matrix

#1
a = X

#2
p, l, u = lu(a)

#3
detA = np.linalg.det(p) * np.linalg.det(u)


#4
uniform = np.round(np.random.uniform(low=0, high=200, size=100))
normal = np.round(np.random.normal(loc=100, scale=33, size=100))

#5
meanUniform = np.mean(uniform)
meanNormal = np.mean(normal)

modeUniform = mode(uniform)
modeNormal = mode(normal)

medianUniform = np.median(uniform)
medianNormal = np.median(normal)

maxUniform = np.max(uniform)
maxNormal = np.max(normal)

minUniform = np.min(uniform)
minNormal = np.min(normal)

stdUniform = np.std(uniform)
stdNormal = np.std(normal)

#6
k = 10

bins = np.linspace(min(min(uniform), min(normal)), max(max(uniform), max(normal)), k+1)

obs_u, _ = np.histogram(uniform, bins=bins)
obs_n, _ = np.histogram(normal,  bins=bins)

N_u = obs_u.sum()
N_n = obs_n.sum()
expected_u = np.full_like(obs_u, fill_value=N_u / obs_u.size, dtype=float)
expected_n = np.full_like(obs_n, fill_value=N_n / obs_n.size, dtype=float)

chiU, pU = chisquare(obs_u, f_exp=expected_u)
chiN, pN = chisquare(obs_n, f_exp=expected_n)




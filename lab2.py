import numpy as np
from scipy.optimize import minimize
import sympy as sp
from scipy.differentiate import derivative
import numdifftools as ndt

def fmt(x, eps=1e-9):
    xf = float(x)
    if abs(xf - round(xf)) < eps:
        return str(int(round(xf)))
    s = ('{:.12f}'.format(xf)).rstrip('0').rstrip('.')
    return s if s != '' else '0'

def y_func(x: float) -> float:
    return 2.0 / (np.sin(x) + 4.0)

x0 = 2.0
a = 3.0
b = 6.0

# 1
x = sp.symbols('x')
y = 2/(sp.sin(x) + 4)
first_derivative = sp.diff(y, x, 1)
second_derivative = sp.diff(y, x, 2)
sotaya_derivative = sp.diff(y, x, 10)

# 2
y_diff = sp.diff(y, x)

# 3
def rectangle(f, a, b, n=1000):
    h = (b - a) / n 
    sum = 0
    for i in range(n):
        x = a + i * h
        sum += f(x) * h 
    return sum


# 4
indef_int = sp.integrate(y, x)

# 5
def objective(x):
    return (x[0] - 4)**2 + (x[1] - 2)**2

def constraint1(x):
    return 4*x[0] + 2*x[1] - 11

def constraint2(x):
    return -2*x[0] - 7
# в задании -2???
constraints = [
    {'type': 'ineq', 'fun': constraint1},
    {'type': 'ineq', 'fun': constraint2}
]

bounds = [(0, None), (0, None)]

result = minimize(objective, [0, 0], method='SLSQP', bounds=bounds, constraints=constraints)



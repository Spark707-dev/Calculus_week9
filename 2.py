import numpy as np
from scipy.integrate import quad
import matplotlib.pyplot as plt

def f(x):
    return np.sin(x)

def g(x):
    return - (3 / (7 * np.pi)) * x  # Line from (0,0) to (7π/6, -1/2)

# 1. Definite Integral Method
a = 0
b = 7 * np.pi / 6

def area_between(x):
    return abs(f(x) - g(x))

area_integral, _ = quad(area_between, a, b)

# 2. Monte Carlo Simulation
np.random.seed(0)
N = 100000
x_rand = np.random.uniform(a, b, N)
y_min = min(np.sin(b), g(b))
y_max = max(np.sin(a), g(a))
y_rand = np.random.uniform(y_min, y_max, N)

f_vals = f(x_rand)
g_vals = g(x_rand)
y_curve = abs(f_vals - g_vals)
count_under = np.sum(y_rand < y_curve)
area_rect = (b - a) * (y_max - y_min)
area_mc = area_rect * count_under / N

print(f"Area using definite integral: {area_integral:.6f}")
print(f"Area using Monte Carlo (N={N}): {area_mc:.6f}")


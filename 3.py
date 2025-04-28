import numpy as np
from scipy.integrate import quad

# Define the function to integrate
def integrand(x):
    ln_x = np.log(x)
    return (1 + ln_x) * np.sqrt(1 + (x * ln_x)**2)

# Compute the definite integral from x = 0.2 to x = 1
result, error = quad(integrand, 0.2, 1)

print(f"Integral result: {result}")
print(f"Estimated error: {error}")

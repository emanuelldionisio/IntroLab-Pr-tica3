import numpy as np

def func_seno_amortecido(t, gamma, omega, theta, phi, c):
    return theta * np.e**(-gamma*t/2) * np.cos(
        (1 - (gamma**2)/(4*omega**2))**0.5 * omega * t + phi
    ) + c
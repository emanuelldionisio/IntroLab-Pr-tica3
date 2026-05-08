import numpy as np

def func_seno_amortecido(t, A, gamma, omega, phi, C):
    radicando = 1 - (gamma**2) / (4 * omega**2)
    
    if radicando < 0:
        return np.inf 
        
    omega_d = omega * np.sqrt(radicando)

    exp_term = np.exp(-gamma * t / 2)
    
    termo_cos = ((gamma**2)/2 - omega**2) * np.cos(omega_d * t + phi)
    termo_sin = (gamma * omega_d) * np.sin(omega_d * t + phi)
    
    return A * exp_term * (termo_cos + termo_sin) + C
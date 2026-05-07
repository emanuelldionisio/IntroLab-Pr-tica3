import numpy as np

def func_seno(t: float, A: float, omega: float, phi: float, c: float):
    '''
    Essa função aceita os seguintes parâmetros:
    - t: tempo
    - A: amplitude 
    - omega: frequência angular
    - phi: fase
    - c: deslocamento vertical
    
    A função retorna o valor do seno para os parâmetros fornecidos.
    '''
    return A * np.sin(omega * t + phi) + c
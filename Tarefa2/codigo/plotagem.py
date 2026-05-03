import matplotlib.pyplot as plt
import numpy as np
import scipy.optimize as opt
from func_seno import func_seno
import csv

data = []
with open('Tarefa2/data/SemDissipacao.csv', 'r') as file:
    reader = csv.reader(file)
    data = list(reader)
#Cabeçalho: [Tempo, Posição em X, Posição em Y, Energia cinética]
for i in range(1, len(data)):
    data[i] = [i if i != '' else None for i in data[i]]
data = np.array(data[1:], dtype=float)  

def plotagemPosx():
    tempo = data[:,0]
    posx = data[:,1]
    
    popt, pcov = opt.curve_fit(func_seno, tempo, posx)
    posxAjustada = func_seno(tempo, *popt)
        
    plt.title("Posição em X em função do tempo")
    plt.xlabel("Tempo (s)")
    plt.ylabel("Posição em X (m)")
    plt.plot(tempo, posx, 'o', label='Dados experimentais', markersize=1)
    plt.plot(tempo, posxAjustada, 'r-', label=f'Ajuste de curvas - g = {popt[1]**2:.2f} m/s²')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    plotagemPosx()


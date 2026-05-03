import matplotlib.pyplot as plt
import numpy as np
import scipy.optimize as opt
from func_seno import func_seno
import csv

diretorioImgs = "Tarefa2/imgs/semDissipacao"

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
    
    popt, pcov = opt.curve_fit(func_seno, tempo, posx, p0=[1, 3, 0, 0])
    posxAjustada = func_seno(tempo, *popt)
    erro = np.diag(pcov)**0.5
    print(erro[1])    
    plt.figure(figsize=(19.2, 10.8))
    plt.title("Posição em X em função do tempo")
    plt.xlabel("Tempo (s)")
    plt.ylabel("Posição em X (m)")
    plt.plot(tempo, posx, 'o', label='Dados experimentais', markersize=1)
    plt.plot(tempo, posxAjustada, 'r-', label=f'Ajuste de curvas - g = {popt[1]**2:.4f} m/s²')
    plt.legend()
    plt.savefig(diretorioImgs + "/posx.png")
    plt.close()

def plotagemPosy():
    tempo = data[:,0]
    posy = data[:,2]
    popt, pcov = opt.curve_fit(func_seno, tempo, posy, p0=[(np.max(posy)-np.min(posy))/2, 3, 0, 0.01])
    posyAjustada = func_seno(tempo, *popt)
    erro = np.diag(pcov)**0.5
    print(erro[1])    
    plt.figure(figsize=(19.2, 10.8))
    plt.title("Posição em Y em função do tempo")
    plt.xlabel("Tempo (s)")
    plt.ylabel("Posição em Y (m)")
    plt.plot(tempo, posy, 'o', label='Dados experimentais', markersize=1)
    plt.plot(tempo, posyAjustada, 'r-', label=f'Ajuste de curvas - g = {popt[1]**2:.4f} m/s²')
    plt.legend()
    plt.savefig(diretorioImgs + "/posy.png")
    plt.close()

def plotagemAng():
    tempo = data[:,0]
    posx = data[:,1]
    posy = data[:,2]
    y0 = np.min(posy)

    ang = np.arctan2(posx, 1 - (posy - y0))
    
    popt, pcov = opt.curve_fit(func_seno, tempo, ang, p0=[(np.max(ang)-np.min(ang))/2, 3, 0, 0])
    angAjustada = func_seno(tempo, *popt)
    erro = np.diag(pcov)**0.5
    print(erro[1])    
    plt.figure(figsize=(19.2, 10.8))
    plt.title("Ângulo em função do tempo")
    plt.xlabel("Tempo (s)")
    plt.ylabel("Ângulo (rad)")
    plt.plot(tempo, ang, 'o', label='Dados experimentais', markersize=1)
    plt.plot(tempo, angAjustada, 'r-', label=f'Ajuste de curvas - g = {popt[1]**2:.4f} m/s²')
    plt.legend()
    plt.savefig(diretorioImgs + "/ang.png")
    plt.close()

if __name__ == "__main__":
    plotagemPosx()
    plotagemPosy()
    plotagemAng()


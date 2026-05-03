import matplotlib.pyplot as plt
import numpy as np
import scipy.optimize as opt
from func_seno import func_seno
import csv

diretorioImgs = "Tarefa2/imgs/semDissipacao"
diretorioData = "Tarefa2/data/semDissipacao"

data = []
with open(diretorioData + '/SemDissipacao.csv', 'r') as file:
    reader = csv.reader(file)
    data = list(reader)
#Cabeçalho: [Tempo, Posição em X, Posição em Y, Energia cinética]
for i in range(1, len(data)):
    data[i] = [i if i != '' else None for i in data[i]]
data = np.array(data[1:], dtype=float)  

tempo = data[:,0]
posx = data[:,1]
posy = data[:,2]
energiaK = data[:,3]
y0 = np.min(posy)
ang = -np.arctan2(posx, 1 - (posy - y0))
ang0 = ang[0]

def plotagemPosx():
    
    popt, pcov = opt.curve_fit(func_seno, tempo, posx, p0=[1, 3, 0, 0])
    posxAjustada = func_seno(tempo, *popt)
    erro = np.diag(pcov)**0.5
    with open(diretorioData + "/ajustePosx.txt", 'w') as f:
        f.write(f"Parâmetros do ajuste: {popt}\n")
        f.write(f"Erro dos parâmetros: {erro}\n")
     
    plt.title("Posição em X em função do tempo")
    plt.xlabel("Tempo (s)")
    plt.ylabel("Posição em X (m)")
    plt.plot(tempo, posx, 'o', label='Dados experimentais', markersize=1)
    plt.plot(tempo, posxAjustada, 'r-', label=f'Ajuste de curvas')
    plt.legend(loc='upper right')
    plt.savefig(diretorioImgs + "/posx.png")
    plt.close()

def plotagemPosy():
    popt, pcov = opt.curve_fit(func_seno, tempo, posy, p0=[0.013, 2 * np.pi, np.pi/2, 0.021])
    posyAjustada = func_seno(tempo, *popt)
    erro = np.diag(pcov)**0.5
    with open(diretorioData + "/ajustePosy.txt", 'w') as f:
        f.write(f"Parâmetros do ajuste: {popt}\n")
        f.write(f"Erro dos parâmetros: {erro}\n")  
    plt.title("Posição em Y em função do tempo")
    plt.xlabel("Tempo (s)")
    plt.ylabel("Posição em Y (m)")
    plt.plot(tempo, posy, 'o', label='Dados experimentais', markersize=1)
    plt.plot(tempo, posyAjustada, 'r-', label=f'Ajuste de curvas')
    plt.legend(loc='upper right')
    plt.savefig(diretorioImgs + "/posy.png")
    plt.close()

def plotagemAng():
    
    popt, pcov = opt.curve_fit(func_seno, tempo, ang, p0=[(np.max(ang)-np.min(ang))/2, 3, 0, 0])
    angAjustada = func_seno(tempo, *popt)
    erro = np.diag(pcov)**0.5
    with open(diretorioData + "/ajusteAng.txt", 'w') as f:
        f.write(f"Parâmetros do ajuste: {popt}\n")
        f.write(f"Erro dos parâmetros: {erro}\n")
    plt.title("Ângulo em função do tempo")
    plt.xlabel("Tempo (s)")
    plt.ylabel("Ângulo (rad)")
    plt.plot(tempo, ang, 'o', label='Dados experimentais', markersize=1)
    plt.plot(tempo, angAjustada, 'r-', label=f'Ajuste de curvas - g = {popt[1]**2:.4f} m/s²')
    plt.legend(loc='upper right')
    plt.savefig(diretorioImgs + "/ang.png")
    plt.close()

def plotagemEnergia():
    
    m = 0.0518
    vx = np.gradient(posx, tempo)
    vy = np.gradient(posy, tempo)
    ax = np.gradient(vx, tempo)
    ay = np.gradient(vy, tempo)
    
    
    energiaPot = 9.8 * (posy - y0) * m
    energiaMec = energiaK + energiaPot
    
    plt.figure(figsize=(10, 6))
    plt.title("Energia em função do tempo")
    plt.xlabel("Tempo (s)")
    plt.ylabel("Energia (J)")
    plt.plot(tempo, energiaPot, 'o', label='Dados experimentais - Energia Potencial', markersize=1)
    plt.plot(tempo, energiaK, 'o', label='Dados experimentais - Energia Cinética', markersize=1)
    plt.plot(tempo, energiaMec, 'o', label='Dados experimentais - Energia Mecânica', markersize=1)
    
    plt.legend(loc='upper right')
    plt.savefig(diretorioImgs + "/energia.png")
    plt.close()

if __name__ == "__main__":
    plotagemPosx()
    plotagemPosy()
    plotagemAng()
    plotagemEnergia()


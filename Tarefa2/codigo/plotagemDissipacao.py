import matplotlib.pyplot as plt
import numpy as np
import scipy.optimize as opt
from func_seno_amortecido import func_seno_amortecido
from func_seno import func_seno
import csv
import pandas as pd

diretorioImgs = "Tarefa2/imgs/comDissipacao"
diretorioData = "Tarefa2/data/comDissipacao"

data = []
with open(diretorioData + '/ComDissipacao.csv', 'r') as file:
    reader = csv.reader(file)
    data = list(reader)
#Cabeçalho: [Tempo, Posição em X, Posição em Y, Energia cinética]
for i in range(1, len(data)):
    data[i] = [i if i != '' else None for i in data[i]]
data = np.array(data[1:], dtype=float)  

tempo = data[:,0]
posx = data[:,1]
posy = data[:,2]
posy = pd.DataFrame(posy).rolling(window=21).mean()
posy = posy.bfill().to_numpy().flatten()
y0 = np.min(posy)
posy = posy - y0
energiaK = data[:,3] * 0.0518
ang = -np.arctan2(posx, 1.107 - (posy))
ang0 = ang[0]

def plotagemAng():
    
    popt, pcov = opt.curve_fit(func_seno_amortecido, tempo, ang, p0=[1, 1, 3, 0.1, 0.1])
    semDissipacao = func_seno_amortecido(tempo, 0, popt[1], popt[2], popt[3], popt[4])
    angAjustada = func_seno_amortecido(tempo, *popt)
    erro = np.diag(pcov)**0.5
    with open(diretorioData + "/ajusteAng.txt", 'w') as f:
        f.write(f"Parâmetros do ajuste: {popt}\n")
        f.write(f"Erro dos parâmetros: {erro}\n")
    plt.title("Ângulo em função do tempo")
    plt.xlabel("Tempo (s)")
    plt.ylabel("Ângulo (rad)")
    plt.plot(tempo, ang, 'o', label='Dados experimentais', markersize=1)
    plt.plot(tempo, angAjustada, '--', color="red", label=f'Ajuste de curvas')
    plt.plot(tempo, semDissipacao, '-.', color="green", label=f'Ajuste sem dissipação')
    plt.legend(loc='upper right')
    plt.savefig(diretorioImgs + "/ang.png")
    plt.close()

def plotagemPosx():
    
    popt, pcov = opt.curve_fit(func_seno_amortecido, tempo, posx, p0=[1, 1, 3, 0.1, 0.1])
    posxAjustada = func_seno_amortecido(tempo, *popt)
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
    popt, pcov = opt.curve_fit(func_seno_amortecido, tempo, posy, p0=[0.11847116,5.6,0.0004,-1.48361739,0.0001])
    posyAjustada = func_seno_amortecido(tempo, *popt)
    erro = np.diag(pcov)**0.5
    with open(diretorioData + "/ajustePosy.txt", 'w') as f:
        f.write(f"Parâmetros do ajuste: {popt}\n")
        f.write(f"Erro dos parâmetros: {erro}\n")
    plt.title("Posição em Y em função do tempo")
    plt.xlabel("Tempo (s)")
    plt.ylabel("Posição em Y (m)")
    plt.plot(tempo, posy, 'o', label='Dados experimentais', markersize=1)
    plt.plot(tempo, posyAjustada, '--', color='red', label=f'Ajuste de curvas')
    plt.legend(loc='upper right')
    plt.savefig(diretorioImgs + "/posy.png")
    plt.close()

def plotagemEnergia():
    
    m = 0.0518
    
    
    energiaPot = 9.8 * (posy)
    energiaMec = energiaK + energiaPot
    
    plt.figure(figsize=(10, 6))
    plt.title("Energia em função do tempo")
    plt.xlabel("Tempo (s)")
    plt.ylabel("Energia (J)")
    plt.plot(tempo, energiaPot, 'o', label='Dados experimentais - Energia Potencial', markersize=1)
    plt.plot(tempo, energiaK, 'o', label='Dados experimentais - Energia Cinética', markersize=1)
    plt.plot(tempo, energiaMec, 'o', label='Dados experimentais - Energia Mecânica', markersize=1)
    # plt.ylim(0, 0.0001)
    
    plt.legend(loc='upper right')
    plt.savefig(diretorioImgs + "/energia.png")
    plt.close()

if __name__ == "__main__":
    plotagemAng()
    plotagemPosx()
    plotagemPosy()
    plotagemEnergia()


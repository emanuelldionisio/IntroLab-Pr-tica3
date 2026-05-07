import matplotlib.pyplot as plt
import numpy as np
import scipy.optimize as opt
import pandas as pd

diretorioImgs = "Tarefa3/imgs"
diretorioData = "Tarefa3/data"

data = pd.read_csv(diretorioData + '/laser.csv')

def plotarHistograma(dados, titulo, qtBins, nomeArquivo):
    desvioPadrao = np.std(dados)
    media = np.mean(dados)
    gravidade = 4 * (np.pi / (media/10**6))**2
    incertezaTempo = desvioPadrao / np.sqrt(len(dados))
    with open(diretorioData + f"/{nomeArquivo}.txt", "w") as f:
        f.write(f"Desvio Padrão: {desvioPadrao:.4f} µs\n")
        f.write(f"Média: {media:.4f} µs\n")
        f.write(f"Gravidade: {gravidade:.4f} m/s²\n")
        f.write(f"Incerteza do Tempo: {incertezaTempo:.4f} µs\n")
    plt.title(titulo)
    plt.xlabel("Tempo (µs)")
    plt.ylabel("Frequência")
    plt.hist(dados, bins=qtBins, edgecolor='black')
    plt.savefig(diretorioImgs + f"/{nomeArquivo}.png")
    plt.close()

    

if __name__ == "__main__":
    plotarHistograma(data["sDissipacao"], "Período sem dissipação", 5, "histograma_sDissipacao")
    plotarHistograma(data["cDissipacao"], "Período com dissipação", 4, "histograma_comDissipacao")

import pandas as pd
import matplotlib.pyplot as plt
import scipy.optimize as opt
from scipy import signal
import numpy as np
from func_seno import func_seno

diretorioImgs = "Tarefa4/imgs/oscilacoesLongas"
diretorioData = "Tarefa4/data/oscilacoesLongas"

df = pd.read_csv(diretorioData + '/dados.csv')

tempo = df['t']
ax = df['x']
ay = df['y']
az = df['z']

popt, pcov = opt.curve_fit(func_seno, tempo, ax, p0=[np.max(ax), 3.14, 0, 0])
a_ajustada = func_seno(tempo, *popt)
erro = np.diag(pcov)**0.5

with open(diretorioData + "/ajusteAcel.txt", 'w') as f:
    f.write(f"Formato: A * sin(Bt + C) + D\n")
    f.write(f"Parâmetros do ajuste: {popt}\n")
    f.write(f"Erro dos parâmetros: {erro}\n")
    f.write(f"Gravidade obtida: {(popt[1]) ** 2}")

plt.title("Aceleração em cada eixo")
plt.xlabel("Tempo (s)")
plt.ylabel("Aceleração (m/s²)")
plt.plot(tempo, ax, 'o', label='Eixo X', markersize=.5)
plt.plot(tempo, ay, 'o', label='Eixo Y', markersize=.5)
plt.plot(tempo, az, 'o', label='Eixo Z', markersize=.5)
plt.legend(loc='upper right')
plt.savefig(diretorioImgs + "/acel_por_eixo.png")
plt.close()

plt.title("Aceleração total")
plt.xlabel("Tempo (s)")
plt.ylabel("Aceleração (m/s²)")
plt.plot(tempo, ax, 'o', label='Dados brutos', markersize=.5)
plt.plot(tempo, a_ajustada, '--', label='Ajuste senoidal', linewidth='1')
plt.legend(loc='upper right')
plt.savefig(diretorioImgs + "/acel.png")
plt.close()

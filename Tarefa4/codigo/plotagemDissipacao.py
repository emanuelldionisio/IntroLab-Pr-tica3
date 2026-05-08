import pandas as pd
import matplotlib.pyplot as plt
import scipy.optimize as opt
import numpy as np
from func_seno_amortecido import func_seno_amortecido

diretorioImgs = "Tarefa4/imgs/comDissipacao"
diretorioData = "Tarefa4/data/comDissipacao"

df = pd.read_csv(diretorioData + '/dados.csv')

tempo = df['t']
ax = df['x']
ay = df['y']
az = df['z']

from scipy.signal import find_peaks

ax_centered = ax - np.mean(ax)

pico_estimado = np.max(ax_centered) * 0.5
peaks, _ = find_peaks(ax_centered, height=pico_estimado)

t_peaks = tempo[peaks]
a_peaks = ax_centered[peaks]

valid_indices = a_peaks > 0
t_final = t_peaks[valid_indices]
a_final = a_peaks[valid_indices]

slope, intercept = np.polyfit(t_final, np.log(a_final), 1)
gamma_inicial = -slope
A_inicial = np.exp(intercept)

p0 = [A_inicial, gamma_inicial, 3.14, 0, .1]

inferior = [0, 0, 0.1, -np.pi, -np.inf]
superior = [np.inf, 2.0, 20.0, np.pi, np.inf]

popt, pcov = opt.curve_fit(func_seno_amortecido, tempo, ax, p0=p0, bounds=(inferior, superior))
a_ajustada = func_seno_amortecido(tempo, *popt)
erro = np.diag(pcov)**0.5

with open(diretorioData + "/ajusteAcel.txt", 'w') as f:
    f.write(f"Formato: A * sin(Bt + C) + D\n")
    f.write(f"Parâmetros do ajuste: {popt}\n")
    f.write(f"Erro dos parâmetros: {erro}\n")
    f.write(f"Gravidade obtida: {(popt[2])**2}")

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
plt.ylabel("Aceleração (rad/s²)")
plt.plot(tempo, ax, 'o', label='Dados brutos', markersize=.5)
plt.plot(tempo, a_ajustada, '--', label='Ajuste senoidal', linewidth='1')
plt.legend(loc='upper right')
plt.savefig(diretorioImgs + "/acel.png")
plt.close()

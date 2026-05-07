import pandas as pd
import matplotlib.pyplot as plt
import scipy.optimize as opt
import numpy as np
from func_seno_amortecido import func_seno_amortecido

diretorioImgs = "Tarefa4/imgs/comDissipacao"
diretorioData = "Tarefa4/data/comDissipacao"

df = pd.read_csv(diretorioData + '/dados.csv')
rolling_window = 15

df['abs_movel'] = df['abs'].rolling(window=rolling_window).mean()
df['x_movel'] = df['x'].rolling(window=rolling_window).mean()
df['y_movel'] = df['y'].rolling(window=rolling_window).mean()
df['z_movel'] = df['z'].rolling(window=rolling_window).mean()

df = df.dropna()

tempo = df['t']
acel = df['abs_movel']
acel_x = df['x_movel']
acel_y = df['y_movel']
acel_z = df['z_movel']
     
popt, pcov = opt.curve_fit(func_seno_amortecido, tempo, acel, p0=[0.85, 6.28, 1, 0.75, 0])
acel_ajustada = func_seno_amortecido(tempo, *popt)
erro = np.diag(pcov)**0.5

with open(diretorioData + "/ajusteAcel.txt", 'w') as f:
    f.write(f"Formato: A * sin(Bt + C) + D\n")
    f.write(f"Parâmetros do ajuste: {popt}\n")
    f.write(f"Erro dos parâmetros: {erro}\n")
    f.write(f"Gravidade obtida: {(popt[1]/2) ** 2}")

plt.title("Aceleração em cada eixo")
plt.xlabel("Tempo (s)")
plt.ylabel("Aceleração (m/s²)")
plt.plot(tempo, acel_x, 'o', label='Eixo X', markersize=.5)
plt.plot(tempo, acel_y, 'o', label='Eixo Y', markersize=.5)
plt.plot(tempo, acel_z, 'o', label='Eixo Z', markersize=.5)
plt.legend(loc='upper right')
plt.savefig(diretorioImgs + "/acel_por_eixo.png")
plt.close()

plt.title("Aceleração total")
plt.xlabel("Tempo (s)")
plt.ylabel("Aceleração (m/s²)")
plt.plot(tempo, acel, 'o', label='Dados brutos', markersize=.5)
plt.plot(tempo, acel_ajustada, '--', label='Ajuste senoidal', linewidth='1')
plt.legend(loc='upper right')
plt.savefig(diretorioImgs + "/acel.png")
plt.close()

import pandas as pd
import matplotlib.pyplot as plt
import scipy.optimize as opt
import numpy as np
from func_seno import func_seno

diretorioImgs = "Tarefa4/imgs/"
diretorioData = "Tarefa4/data/"

df = pd.read_csv(diretorioData + '/dados.csv')

tempo = df['t'] / 10 ** 9
tempo = tempo - np.min(tempo)
acel_x = df['x'] / 10 ** 9
acel_y = df['y'] / 10 ** 9
acel_z = df['z'] / 10 ** 9
     
popt, pcov = opt.curve_fit(func_seno, tempo, acel_x, p0=[1.6, 3, 0, 0])
acel_x_ajustada = func_seno(tempo, *popt)

with open(diretorioData + "/ajusteAcex.txt", 'w') as f:
    f.write(f"Parâmetros do ajuste: {popt}\n")

popt2, pcov = opt.curve_fit(func_seno, tempo, acel_z, p0=[.3, 6, 0, 0])
acel_z_ajustada = func_seno(tempo, *popt2)

with open(diretorioData + "/ajusteAcez.txt", 'w') as f:
    f.write(f"Parâmetros do ajuste: {popt2}\n")

plt.title("Graficos bobinhos")
plt.xlabel("Tempo (s)")
plt.ylabel("Aceleração (m/s²)")
plt.plot(tempo, acel_x, 'o', label='Eixo X', markersize=1)
plt.plot(tempo, acel_x_ajustada, 'r-', label='ajuste', markersize=1)
plt.plot(tempo, acel_z_ajustada, 'r-', label='ajustez', markersize=1)
plt.plot(tempo, acel_z, 'o', label='Eixo Z', markersize=1)
plt.legend(loc='upper right')
plt.savefig(diretorioImgs + "/acel.png")
plt.close()


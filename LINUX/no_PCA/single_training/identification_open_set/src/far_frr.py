import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Carica il tuo file CSV
df = pd.read_csv('./file_csv/risultati.csv')
th = df['threshold'].values
far = df['FAR'].values
cdir = df['CDIR'].values
frr = 1 - cdir

# Plot delle curve FAR e FRR
plt.plot(th, far, label='FAR')
plt.plot(th, frr, label='FRR')

# Individuazione del punto di intersezione
intersection_point = np.argmin(np.abs(far - frr))

# Calcolo dell'ERR
err_value = far[intersection_point]

# Estrai il threshold corrispondente al punto di intersezione
optimal_threshold = th[intersection_point]

# Aggiunta di marcatori per indicare il punto di intersezione
plt.scatter(optimal_threshold, err_value, color='red', label='ERR Intersection Point')

# Annotazioni
plt.annotate(f"ERR: {err_value:.2f}", (optimal_threshold, err_value), xytext=(optimal_threshold + 0.1, err_value + 0.1), arrowprops=dict(facecolor='black', shrink=0.05))
plt.annotate(f"Threshold: {optimal_threshold:.2f}", (optimal_threshold, err_value), xytext=(optimal_threshold + 0.1, err_value + 0.2), arrowprops=dict(facecolor='black', shrink=0.05))

plt.yticks([0.01,0.05, 0.10,0.15,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9])

# Etichette e titoli
plt.xlabel('Threshold')
plt.ylabel('Rate')
plt.title('FAR and FRR Curves')
plt.legend()
plt.savefig('./output/FAR_FRR.png')
plt.close()

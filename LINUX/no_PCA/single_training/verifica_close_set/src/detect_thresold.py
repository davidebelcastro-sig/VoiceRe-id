import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Carica il tuo file CSV
df = pd.read_csv('./file_csv/risultati.csv')

# Estrai le colonne di interesse
thresholds = df['threshold']
far_values = df['far']
frr_values = df['frr']


# Plot delle curve FAR e FRR
plt.plot(thresholds, far_values, label='FAR')
plt.plot(thresholds, frr_values, label='FRR')

# Individuazione del punto di intersezione
intersection_point = np.argmin(np.abs(far_values - frr_values))

# Calcolo dell'ERR
err_value = far_values[intersection_point]



# Estrai il threshold corrispondente al punto di intersezione
optimal_threshold = thresholds[intersection_point]




# Se ci sono più valori in cui FRR è zero, prendi il primo
# Aggiunta di marcatori per indicare il punto di intersezione
plt.scatter(optimal_threshold, err_value, color='red', label='ERR Intersection Point')

plt.annotate(f"ERR: {err_value:.2f}", (thresholds[intersection_point], err_value), xytext=(thresholds[intersection_point] + 0.1, err_value + 0.1), arrowprops=dict(facecolor='black', shrink=0.05))
plt.annotate(f"Threshold: {optimal_threshold:.2f}", (thresholds[intersection_point], err_value), xytext=(thresholds[intersection_point] + 0.1, err_value + 0.2), arrowprops=dict(facecolor='black', shrink=0.05))

# Etichette e titoli
plt.xlabel('Threshold')
plt.ylabel('Rate')
plt.title('FAR and FRR Curves')
plt.legend()
plt.savefig('./output/FAR_FRR.png')
plt.close()


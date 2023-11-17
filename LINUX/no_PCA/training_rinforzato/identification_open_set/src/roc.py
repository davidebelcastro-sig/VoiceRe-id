import pandas as pd
import matplotlib.pyplot as plt

# Carica il tuo file CSV
df = pd.read_csv('./csv/accuracy.csv')
th = df['threshold'].values
far = df['FAR'].values
cdir = df['CDIR'].values



# Plotta la curva ROC
plt.figure(figsize=(8, 8))
plt.plot(far, cdir, label='WatchList ROC Curve')

# Plotta i punti della curva ROC
plt.scatter(far, cdir, c=th, cmap='viridis', label='Threshold Values', s=30, edgecolors='black', linewidths=0.5)

# Etichette e titoli
plt.title('Receiver Operating Characteristic (ROC) Curve')
plt.xlabel('False Alarm Rate (FAR)')
plt.ylabel('Detect and Identification Rate (DIR)')
plt.legend()

# Aggiungi una barra dei colori per i valori di threshold
cbar = plt.colorbar()
cbar.set_label('Threshold Values')

# Salva il grafico
plt.savefig('./output/Watch_ROC.png')
plt.close()
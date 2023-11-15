import pandas as pd
import matplotlib.pyplot as plt

# Carica i dati dai file CSV
df1 = pd.read_csv('../single_training/file_csv/risultati.csv')
df2 = pd.read_csv('../training_rinforzato/csv/accuracy.csv')

thresholds = df1['threshold']
#frr
frr1 = df1['frr']
far1 = df1['far']
acc1 = df1['acc']
frr2 = df2['frr']
far2 = df2['far']
acc2 = df2['acc']

# Plot
plt.plot(thresholds, frr1, label='FRR')
plt.plot(thresholds, far1, label='FAR')
plt.plot(thresholds, acc1, label='ACC')
plt.plot(thresholds, frr2, label='FRR rinforzato')
plt.plot(thresholds, far2, label='FAR rinforzato')
plt.plot(thresholds, acc2, label='ACC rinforzato')
plt.xlabel('Threshold')
plt.ylabel('Percentuale')
# Specifica i valori sull'asse y (modifica questa lista in base alle tue esigenze)
plt.yticks([0, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.50, 0.55, 0.6, 0.65, 0.7, 0.75, 0.8, 0.85, 0.9, 0.95, 0.99])
plt.title('FRR, FAR, ACC')
plt.legend()
plt.show()

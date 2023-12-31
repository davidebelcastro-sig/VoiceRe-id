import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Carica il tuo file CSV
df = pd.read_csv('./csv/accuracy_combined.csv')

# Estrai le colonne di interesse
thresholds = df['threshold']
far_values = df['far']
frr_values = df['frr']

# Plotta la curva DET in forma logaritmica
plt.figure(figsize=(8, 8))
plt.loglog(far_values, frr_values, label='DET Curve')

# Etichette e titoli
plt.title('Detection Error TradeOff (DET) Curve (Log Scale)')
plt.xlabel('False Positive Rate (FAR)')
plt.ylabel('False Reject Rate (FRR)')
plt.legend()
plt.savefig('./output/DET.png')
plt.close() 

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Carica il tuo file CSV
df = pd.read_csv('./output/risultati.csv')

# Estrai le colonne di interesse
far_values = df['far']
tpr_values = df['Recall']

# Funzione per calcolare l'area sotto la curva ROC
def calculate_auc(far, tpr):
    n = len(far)
    auc = np.sum((far[1:] - far[:-1]) * (tpr[:-1] + tpr[1:]) / 2)
    return auc

# Calcola l'area sotto la curva ROC
area_under_curve = calculate_auc(far_values, tpr_values)

# Plotta la curva ROC
plt.figure(figsize=(8, 8))
plt.plot(far_values, tpr_values, label='ROC Curve')  

# Evidenzia l'area sotto la curva ROC
plt.fill_between(far_values, tpr_values, color='lightblue', alpha=0.3)

# Aggiungi il valore dell'area direttamente nel grafico
#plt.text(0.6, 0.3, f'AUC = {area_under_curve:.2f}', fontsize=12, color='darkblue')

# Etichette e titoli
plt.title('Receiver Operating Characteristic (ROC) Curve')
plt.xlabel('False Positive Rate (FAR)')
plt.ylabel('True Positive Rate (TPR)')
plt.legend()

# Salva il grafico come immagine
plt.savefig('./output/ROC.png')
plt.close()


import pandas as pd
import matplotlib.pyplot as plt

# Carica il tuo file CSV
df = pd.read_csv('./file_csv/risultati.csv')

# Estrai le colonne di interesse
far_values = df['far']
frr_values = df['frr']

# Calcola True Positive Rate (TPR) o Sensitivity (1-FRR)
#tpr_values = 1 - frr_values #GAR
tpr_values = df['Recall']
# Plotta la curva ROC
plt.figure(figsize=(8, 8))
plt.plot(far_values, tpr_values, label='ROC Curve')  




# Etichette e titoli
plt.title('Receiver Operating Characteristic (ROC) Curve')
plt.xlabel('False Positive Rate (FAR)')
plt.ylabel('True Positive Rate (TPR)')
plt.legend()
plt.savefig('./output/ROC.png')
plt.close()

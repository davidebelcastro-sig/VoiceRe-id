import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pickle
import os
import zipfile
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import precision_score, recall_score
import csv

print("Accuracy calculation...")

# Carica i dati di addestramento e test
train_data = pd.read_csv('./file_csv/features_train.csv')
test_data = pd.read_csv('./file_csv/features_test.csv')

# Separa le etichette dai dati
X_train = train_data.drop('label', axis=1)
y_train = train_data['label']

X_test = test_data.drop('label', axis=1)
y_test = test_data['label']


#Controllo che il file pkl non esista già
if os.path.exists('modello_random_forest.pkl'):
    # Caricamento del modello da un file pickle
    with open('modello_random_forest.pkl', 'rb') as file:
        rf_model = pickle.load(file)
else:
    #c'è il zip?
    zip_file_path = "modello_random_forest.zip"
    if os.path.exists(zip_file_path):
        # Apri il file ZIP in modalità lettura
        with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
            # Estrai tutti i file contenuti nel file ZIP nella cartella di destinazione
            zip_ref.extractall(".")
        # Caricamento del modello da un file pickle
        with open('modello_random_forest.pkl', 'rb') as file:
            rf_model = pickle.load(file)
    else:
        rf_model = RandomForestClassifier()
        rf_model.fit(X_train, y_train)
        # Salvataggio del modello in formato pickle
        with open('modello_random_forest.pkl', 'wb') as file:
            pickle.dump(rf_model, file)


rf_probabilities = rf_model.predict_proba(X_test)
cmc_probs = []

for x in range(1, 61):
    total_correct_matches = 0
    for i in range(len(rf_probabilities)):
        rf_prob  = rf_probabilities[i]
        # Creazione di una lista di tuple (valore, indice)
        lista_di_tuple = list(enumerate(rf_prob))
        # Ordinamento della lista di tuple in base al valore in modo decrescente
        rf_sorted = sorted(lista_di_tuple, key=lambda x: x[1], reverse=True)
        #solo il primo elemento per ogni riga
        rf_sorted = [x[0] + 1  for x in rf_sorted]
        #capire dove è uguale ytest[i] in rf_sorted
        index = rf_sorted.index(y_test[i]) + 1 
        if index <= x:
            total_correct_matches += 1
    cmc_probs.append(total_correct_matches / len(rf_probabilities))

accuracy_at_rank1 = cmc_probs[0]
plt.plot(range(1, 61), cmc_probs)
plt.xticks(np.arange(1, 61, 4))
plt.xlabel('Rank (k)')
plt.ylabel('Probability of Correct Match')
plt.title('Cumulative Match Characteristic (CMC) Curve')
# Annotazione dell'accuracy al rank 1
plt.annotate(f'Recognition Rate: {accuracy_at_rank1:.2%}',
             xy=(1, accuracy_at_rank1), xycoords='data',
             xytext=(20, 30), textcoords='offset points',
             arrowprops=dict(facecolor='black', arrowstyle='->', connectionstyle='arc3,rad=.2'))
plt.savefig('./output/cmc_curve.png')
plt.close()


rf_result = rf_model.predict(X_test)
precision = precision_score(y_test, rf_result, average='weighted')
recall = recall_score(y_test, rf_result, average='weighted')
f1_score = 2 * (precision * recall) / (precision + recall)


# Percorso del file CSV
csv_file_path = "./output/accuracy.csv"

# Scrivi i valori nel file CSV
with open(csv_file_path, mode='w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    # Scrivi l'intestazione
    writer.writerow(['Precision', 'Recall', 'F1 Score'])
    # Scrivi i valori
    writer.writerow([precision, recall, f1_score])


print("Accuracy calculation completed, you can see the result in the output folder")
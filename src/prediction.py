import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pickle
import os
import numpy as np

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
    rf_model = RandomForestClassifier()
    rf_model.fit(X_train, y_train)
    # Salvataggio del modello in formato pickle
    with open('modello_random_forest.pkl', 'wb') as file:
        pickle.dump(rf_model, file)



rf_predictions = rf_model.predict_proba(X_test)

# Simula la dichiarazione dell'utente: vero (50%) o falso (50%)
np.random.seed(42)  # Per riproducibilità
user_truthfulness = np.random.choice([True, False], len(y_test), p=[0.5, 0.5])
true_labels = np.where(user_truthfulness, y_test, -1) #-1 se non è vero
utente_dichiara = [x if x != -1 else np.random.randint(1, 61) for x in true_labels]


#dovrei abbassare y_test e utente_dichiara di 1
y_test = [x-1 for x in y_test]
utente_dichiara = [x-1 for x in utente_dichiara]

# Creazione di un DataFrame con le colonne desiderate
df = pd.DataFrame({
    'y_test': y_test,
    'utente_dichiara': utente_dichiara,
    'rf_predictions': rf_predictions.tolist()  # Converti le previsioni in formato lista
})

# Salva il DataFrame in un file CSV
df.to_csv('./file_csv/accessi.csv', index=False)

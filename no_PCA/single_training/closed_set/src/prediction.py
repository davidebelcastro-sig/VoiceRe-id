import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pickle
import os
import zipfile

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


rf_predictions = rf_model.predict(X_test)
accuracy = rf_model.score(X_test, y_test)
print("Accuracy: ", accuracy)



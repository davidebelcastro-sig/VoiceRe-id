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
if os.path.exists('./modelli/modello_combinato.pkl'):
    # Caricamento del modello da un file pickle
    with open('./modelli/modello_combinato.pkl', 'rb') as file:
        rf_model = pickle.load(file)
    rf_predictions = rf_model.predict(X_test)
    accuracy = rf_model.score(X_test, y_test)
    print("Accuracy: ", accuracy)
else:
    print("Il file non esiste")






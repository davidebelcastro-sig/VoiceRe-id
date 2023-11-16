import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pickle
import os
import zipfile


print("Accuracy calculation...")

# Carica i dati di addestramento e test
test_data = pd.read_csv('./file_csv/features_test.csv')


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






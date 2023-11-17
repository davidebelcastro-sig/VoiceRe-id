import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pickle
import os
import numpy as np
import  crea_feature_test

# Carica i dati di addestramento e test
train_data = pd.read_csv('./file_csv/features_train.csv')


# Separa le etichette dai dati
X_train = train_data.drop('label', axis=1)
y_train = train_data['label']




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


#dovrei crearmi un feature_test che ha record con label -1 e feature diverse(posso prendere la mia voce e fare variaizoni)

#crea_feature_test.crea_feature_test('./file_csv/features_test_open_set.csv') #-> già fatto
test_data = pd.read_csv('./file_csv/features_test_open_set.csv')
X_test = test_data.drop('label', axis=1)
y_test = test_data['label']
rf_predictions = rf_model.predict_proba(X_test)



#dovrei abbassare y_test e utente_dichiara di 1
y_test = [x-1 for x in y_test]


# Creazione di un DataFrame con le colonne desiderate
df = pd.DataFrame({
    'y_test': y_test,
    'rf_predictions': rf_predictions.tolist()  # Converti le previsioni in formato lista
})

# Salva il DataFrame in un file CSV
df.to_csv('./file_csv/accessi.csv', index=False)

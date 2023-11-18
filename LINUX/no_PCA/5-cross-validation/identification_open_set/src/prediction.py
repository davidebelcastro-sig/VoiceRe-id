import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pickle
import os


def pred(feature_train,feature_test,modello,accessi):
   
    # Carica i dati di addestramento e test
    train_data = pd.read_csv(feature_train)
    test_data = pd.read_csv(feature_test)

    # Separa le etichette dai dati
    X_train = train_data.drop('label', axis=1)
    y_train = train_data['label']

    X_test = test_data.drop('label', axis=1)
    y_test = test_data['label']


    #Controllo che il file pkl non esista già
    if os.path.exists(modello):
        # Caricamento del modello da un file pickle
        with open(modello, 'rb') as file:
            rf_model = pickle.load(file)
    else:
        rf_model = RandomForestClassifier()
        rf_model.fit(X_train, y_train)
        # Salvataggio del modello in formato pickle
        with open(modello, 'wb') as file:
            pickle.dump(rf_model, file)

    rf_predictions = rf_model.predict_proba(X_test)

    #dovrei abbassare y_test e utente_dichiara di 1
    y_test = [x-1 for x in y_test]


    # Creazione di un DataFrame con le colonne desiderate
    df = pd.DataFrame({
        'y_test': y_test,
        'rf_predictions': rf_predictions.tolist()  # Converti le previsioni in formato lista
    })

    # Salva il DataFrame in un file CSV
    df.to_csv(accessi, index=False)


if __name__ == '__main__':
    pred("./csv/features_train.csv", "./csv/features_test_open_set.csv", "./modelli/modello_combinato.pkl", "./csv/accessi_combined.csv")
    pred("./csv/features_train.csv", "./csv/features_test_open_set.csv", "./modelli/modello_0.pkl", "./csv/accessi_0.csv")
    pred("./csv/features_train.csv", "./csv/features_test_open_set.csv", "./modelli/modello_1.pkl", "./csv/accessi_1.csv")
    pred("./csv/features_train.csv", "./csv/features_test_open_set.csv", "./modelli/modello_2.pkl", "./csv/accessi_2.csv")
    pred("./csv/features_train.csv", "./csv/features_test_open_set.csv", "./modelli/modello_3.pkl", "./csv/accessi_3.csv")
    pred("./csv/features_train.csv", "./csv/features_test_open_set.csv", "./modelli/modello_4.pkl", "./csv/accessi_4.csv")
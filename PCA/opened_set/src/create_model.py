import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pickle





def create(nome):
    # Carica i dati di addestramento e test
    train_data = pd.read_csv('features_train.csv')
    test_data = pd.read_csv('features_test.csv')

    # Separa le etichette dai dati
    X_train = train_data.drop('label', axis=1)
    y_train = train_data['label']

    X_test = test_data.drop('label', axis=1)
    y_test = test_data['label']


    rf_model = RandomForestClassifier()
    rf_model.fit(X_train, y_train)
    # Salvataggio del modello in formato pickle
    with open(nome, 'wb') as file:
        pickle.dump(rf_model, file)





import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pickle
import os
import numpy as np
from PCA import PCA_analysis




def pred(modello,accessi):
   


    X_train_pca, pca_model, X_val_pca, y_train, y_val = PCA_analysis("dataset.csv","combinato")

    #Controllo che il file pkl non esista già
    if os.path.exists(modello):
        # Caricamento del modello da un file pickle
        with open(modello, 'rb') as file:
            rf_model = pickle.load(file)
    else:
        rf_model = RandomForestClassifier()
        rf_model.fit(X_train_pca, y_train)
        # Salvataggio del modello in formato pickle
        with open(modello, 'wb') as file:
            pickle.dump(rf_model, file)

    rf_predictions = rf_model.predict_proba(X_val_pca)

    # Simula la dichiarazione dell'utente: vero (50%) o falso (50%)
    np.random.seed(42)  # Per riproducibilità
    user_truthfulness = np.random.choice([True, False], len(y_val), p=[0.5, 0.5])
    true_labels = np.where(user_truthfulness, y_val, -1) #-1 se non è vero
    utente_dichiara = [x if x != -1 else np.random.randint(1, 61) for x in true_labels]


    #dovrei abbassare y_test e utente_dichiara di 1
    y_test = [x-1 for x in y_val]
    utente_dichiara = [x-1 for x in utente_dichiara]

    # Creazione di un DataFrame con le colonne desiderate
    df = pd.DataFrame({
        'y_test': y_test,
        'utente_dichiara': utente_dichiara,
        'rf_predictions': rf_predictions.tolist()  # Converti le previsioni in formato lista
    })

    # Salva il DataFrame in un file CSV
    df.to_csv(accessi, index=False)


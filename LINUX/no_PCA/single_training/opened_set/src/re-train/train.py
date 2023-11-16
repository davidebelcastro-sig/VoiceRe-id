import pandas as pd
import joblib
import zipfile
import os.path
import pickle


def new_training(path_label):

    # Percorso del file ZIP da decomprimere
    zip_file_path = "modello_random_forest.zip"

    # Percorso della cartella di destinazione per l'estrazione
    extracted_folder = "."


    #controllo che non sia gia stato estratto
    
    if os.path.exists(extracted_folder+"modello_random_forest.pkl"):
        pass
    else:
        # Apri il file ZIP in modalità lettura
        with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
            # Estrai tutti i file contenuti nel file ZIP nella cartella di destinazione
            zip_ref.extractall(extracted_folder)


    # Carica il tuo modello esistente
    with open('modello_random_forest.pkl', 'rb') as file:
        model = pickle.load(file)

    # Carica il file di train esistente
    df_train_esistente = pd.read_csv(path_label)
    df_nuove_righe = pd.read_csv('re-train.csv') 


    # Aggiungi le nuove righe al file di train esistente
    # Supponiamo che df_nuove_righe sia il DataFrame con le nuove righe
    df_nuovo_train = pd.concat([df_train_esistente, df_nuove_righe])


    # Dividi il dataset in features (X) e target (y)
    # Separa le etichette dai dati
    X_train = df_nuovo_train.drop('label', axis=1)

    y_train = df_nuovo_train['label']


    # Esegui il re-train del modello sul dataset esteso
    model.fit(X_train, y_train)

    # Salva il nuovo modello addestrato
    with open('nuovo_modello.pkl', 'wb') as file:
        pickle.dump(model, file)
import speak as sp
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pickle
import os
import numpy as np
import reg as re
import detect_last_label as dll
import train as tr
import zipfile

def reidentificazione(path_label,modello_path):
    features = sp.main()
    row =  [features["mfccs"][i] for i in range(0, 13)] + [features["spectral_centroid_mean"][i] for i in range(0, 94)] + \
                    [features["chroma"][i] for i in range(0, 12)] + [features['zero_crossings'], features["rms_energy"]] + \
                    [features["spectral_contrast"][i] for i in range(0, 7)] + [features["spectral_bandwidth_mean"][i] for i in range(0, 94)] + \
                    [features["spectral_rolloff"], features["spectral_flatness"], features["total_duration"], features["average_segment_duration"]]
    # Carica i dati di addestramento e test
    train_data = pd.read_csv(path_label)
    # Separa le etichette dai dati
    X_train = train_data.drop('label', axis=1)
    y_train = train_data['label']
    print("Calcolo delle probabilità di appartenenza alle classi...")

    # Controllo che il file pkl non esista già
    if os.path.exists(modello_path):
        # Caricamento del modello da un file pickle
        with open(modello_path, 'rb') as file:
            rf_model = pickle.load(file)
    else:
        rf_model = RandomForestClassifier()
        rf_model.fit(X_train, y_train)
        # Salvataggio del modello in formato pickle
        with open(modello_path, 'wb') as file:
            pickle.dump(rf_model, file)


    # Ottieni le previsioni di probabilità
    row = np.array(row)
    row = row.reshape(1, -1)
    rf_predictions = rf_model.predict_proba(row)

    # Stampa le previsioni
    result = rf_predictions[0]
    return result



    



if __name__ == "__main__":

    thresold = 0.40
    path_label = "./file_csv/features_train.csv"
    modello1 = '../../modello_random_forest.pkl'
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
    modello2 = "nuovo_modello.pkl"
    result = reidentificazione(path_label,modello1)
    massimo = max(result)
    indice = np.where(result == massimo)
    indice = indice[0][0] + 1
    print("Expected: No person")
    if massimo >= thresold:
        print("La persona è la numero: " + str(indice))
    else:
        print("La persona non è presente nel dataset")

    path = "re-train.csv"
    label = dll.detect(path_label)
    label = int(label)
    label = label + 1

    #acquisisco i dati della persona
    print("Acquisizione dati in corso...")
    re.main(path,str(label))

    #faccio il re-train
    print("Re-train in corso...")
    tr.new_training(path_label)

    #rifaccio re-id
    print("Re-id in corso...")
    result = reidentificazione(path_label,modello2)
    massimo = max(result)
    indice = np.where(result == massimo)
    indice = indice[0][0] + 1
    print("Expected: 61")
    if massimo >= thresold:
        print("La persona è la numero: " + str(indice))
    else:
        print("La persona non è presente nel dataset")

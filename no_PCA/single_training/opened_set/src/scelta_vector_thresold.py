import pandas as pd
from collections import Counter


def vector_thresold(path):
    # Carica il file CSV
    df = pd.read_csv(path)

    # Inizializza una lista per salvare tutte le percentuali di risultati
    all_percentages = []


    # Itera sul DataFrame e aggiorna la matrice di confusione
    for index, row in df.iterrows():
        y_test = row['y_test']
        utente_dichiara = row['utente_dichiara']
        rf_predictions = eval(row['rf_predictions'])  # Converte la stringa in una lista
        # prendo tutti i valori maggiori di 0.0
        filtered_predictions = [x for x in rf_predictions if x > 0.0]
        all_percentages.extend(filtered_predictions)
        

    # Trova i 10 valori di threshold più frequenti
    threshold_counts = Counter(all_percentages)
    most_common_thresholds = [item[0] for item in threshold_counts.most_common(80)]

    return most_common_thresholds #ritorna una lista con i 20 valori di threshold più frequenti
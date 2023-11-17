import pandas as pd
import speak
import csv
import numpy as np




def modifica_miavoce(my_voice):
    for j in range(1,len(my_voice)):
        my_voice[j] = my_voice[j] + np.random.randint(0,200)  # Aggiunge un numero casuale
    return my_voice



def crea_feature_test(path,my_voice):
    test_data = pd.read_csv("./file_csv/features_test.csv")
    # Lista degli header delle colonne
    headers = ['label'] + [f'mfccs_{i}' for i in range(1, 14)] + [f'centroid_mean_{i}' for i in range(1, 95)] + \
          [f'chroma_{i}' for i in range(1, 13)] + ['zero_crossing', 'rms_energy'] + \
          [f'contrast_{i}' for i in range(1, 8)] + [f'bandwidth_mean_{i}' for i in range(1, 95)] + \
          ['rolloff', 'flatness', 'duration', 'average_duration']

    with open("file_appo.csv", mode='w', newline='') as file:
            writer = csv.writer(file)
            # Scrivi l'header
            writer.writerow(headers)


    for i in range(100):
        record = modifica_miavoce(my_voice)
        with open("file_appo.csv", mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(record)

    
 
    nuovi_dati = pd.read_csv("file_appo.csv")

    #nuove_righe = pd.DataFrame(nuove_righe)
    # Aggiungi le nuove righe al DataFrame esistente
    test_data_extended = pd.concat([test_data, nuovi_dati], ignore_index=True)

    # Salva il DataFrame esteso in un nuovo file CSV
    test_data_extended.to_csv(path, index=False)


if __name__ == '__main__':
    features = speak.main()
    features = {k: 0 if v is None else v for k, v in features.items()}
    row = ["-1"] + [features["mfccs"][i] for i in range(0, 13)] + [features["spectral_centroid_mean"][i] for i in range(0, 94)] + \
                        [features["chroma"][i] for i in range(0, 12)] + [features['zero_crossings'], features["rms_energy"]] + \
                        [features["spectral_contrast"][i] for i in range(0, 7)] + [features["spectral_bandwidth_mean"][i] for i in range(0, 94)] + \
                        [features["spectral_rolloff"], features["spectral_flatness"], features["total_duration"], features["average_segment_duration"]]
    crea_feature_test('./file_csv/features_test_open_set.csv',row)
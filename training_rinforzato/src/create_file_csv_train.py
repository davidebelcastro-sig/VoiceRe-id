# extract_features_audio.py

import os
import csv
from extract_features_audio import extract_features_from_file  # Importa la funzione da extract_features.py
import numpy as np

csv_file_train_path = "features_train.csv"
# Lista degli header delle colonne
headers = ['label'] + [f'mfccs_{i}' for i in range(1, 14)] + [f'centroid_mean_{i}' for i in range(1, 95)] + \
          [f'chroma_{i}' for i in range(1, 13)] + ['zero_crossing', 'rms_energy'] + \
          [f'contrast_{i}' for i in range(1, 8)] + [f'bandwidth_mean_{i}' for i in range(1, 95)] + \
          ['rolloff', 'flatness', 'duration', 'average_duration']


def process_audio_files(data_dir):
        # Scrivi i dati nel file CSV
        with open(csv_file_train_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            
            # Scrivi l'header
            writer.writerow(headers)

        for i in range(1,61):
            if i < 10:
                label = '0' + str(i)
            else:
                label = str(i)
            path = os.path.join(data_dir, label)
            for file in os.listdir(path):
                if file.endswith('.wav'):
                    audio_file_path = os.path.join(path, file)
                    features = extract_features_from_file(audio_file_path)
                    row = [label] + [features["mfccs"][i] for i in range(0, 13)] + [features["spectral_centroid_mean"][i] for i in range(0, 94)] + \
                    [features["chroma"][i] for i in range(0, 12)] + [features['zero_crossings'], features["rms_energy"]] + \
                    [features["spectral_contrast"][i] for i in range(0, 7)] + [features["spectral_bandwidth_mean"][i] for i in range(0, 94)] + \
                    [features["spectral_rolloff"], features["spectral_flatness"], features["total_duration"], features["average_segment_duration"]]
                    with open(csv_file_train_path, mode='a', newline='') as file:
                        writer = csv.writer(file)
                        writer.writerow(row)
                    
            print("fine label: " + label)


                    


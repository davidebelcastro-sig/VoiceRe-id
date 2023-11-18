import sounddevice as sd
import wave
import extract_features_audio as efa
import detect_last_label as dll
import csv
import os
from pydub import AudioSegment
import numpy as np



def check_audio(file_path,livello_voce):
    # Carica il file audio WAV
    audio = AudioSegment.from_file(file_path, format="wav")

    # Converte l'audio in un array numpy
    audio_array = np.array(audio.get_array_of_samples())

    # Calcola il valore assoluto di ciascun campione
    audio_array = np.abs(audio_array)

    # Calcola la media dell'intensità
    media_intensita = np.mean(audio_array)
    if media_intensita > 999 and media_intensita < 2500 and livello_voce <= 3:
        return 1
    elif media_intensita >= 2500 and media_intensita <= 3500 and livello_voce > 3 and livello_voce <= 6:
        return 1
    elif media_intensita > 3500 and livello_voce > 6:
        return 1
    else:
        return 0
    


def record_voice(duration,number, sample_rate=44100):
    print("To say: ",str(number))
    audio_data = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1, dtype='int16')
    sd.wait()
    return audio_data.flatten()

def save_audio_to_wav(audio_data, file_path, sample_rate=44100):
    with wave.open(file_path, 'wb') as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(sample_rate)
        wf.writeframes(audio_data.tobytes())


def main(csv_file_retrain_path,label):

    # Lista degli header delle colonne
    headers = ['label'] + [f'mfccs_{i}' for i in range(1, 14)] + [f'centroid_mean_{i}' for i in range(1, 95)] + \
          [f'chroma_{i}' for i in range(1, 13)] + ['zero_crossing', 'rms_energy'] + \
          [f'contrast_{i}' for i in range(1, 8)] + [f'bandwidth_mean_{i}' for i in range(1, 95)] + \
          ['rolloff', 'flatness', 'duration', 'average_duration']

    with open(csv_file_retrain_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            # Scrivi l'header
            writer.writerow(headers)


    duration = 1.5  # durata della registrazione in secondi
    # Registra la voce
    livello_voce = -1
    for number in range(0,10):
        livello_voce +=1
        is_correct = 0
        while is_correct == 0:
            if livello_voce <= 3:
                 print("Speak with low voice")
            elif livello_voce > 3 and livello_voce <= 6:
                    print("Speak with medium voice")
            elif livello_voce > 6:
                    print("Speak with high voice")
            input("You can start recording. Press Enter to continue...")      
            audio_data = record_voice(duration,number)
        # Salva la registrazione su file wav
            save_audio_to_wav(audio_data, "audio.wav")
            is_correct = check_audio("audio.wav",livello_voce)
            if is_correct == 0:
                 print("Registration not completed. Please repeat.")
            else:
                 print("Registration completed.")

        features = efa.extract_features_from_file("audio.wav")
        #i nan vengono sostituiti con 0
        features = {k: 0 if v is None else v for k, v in features.items()}
        row = [label] + [features["mfccs"][i] for i in range(0, 13)] + [features["spectral_centroid_mean"][i] for i in range(0, 94)] + \
                        [features["chroma"][i] for i in range(0, 12)] + [features['zero_crossings'], features["rms_energy"]] + \
                        [features["spectral_contrast"][i] for i in range(0, 7)] + [features["spectral_bandwidth_mean"][i] for i in range(0, 94)] + \
                        [features["spectral_rolloff"], features["spectral_flatness"], features["total_duration"], features["average_segment_duration"]]
        with open(csv_file_retrain_path, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(row)



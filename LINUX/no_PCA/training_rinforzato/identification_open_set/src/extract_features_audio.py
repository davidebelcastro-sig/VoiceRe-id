import librosa
import numpy as np


def extract_features_from_file(audio_file_path):
    # Carica il file audio
    audio_signal, sample_rate = librosa.load(audio_file_path, sr=None)

    # Estrai le MFCC (Mel-frequency cepstral coefficients)
    mfccs = librosa.feature.mfcc(y=audio_signal, sr=sample_rate, n_mfcc=13)

    # Estrai il centro spettrale
    spectral_centroid = librosa.feature.spectral_centroid(y=audio_signal, sr=sample_rate)

    # Estrai la Chroma feature
    chroma = librosa.feature.chroma_stft(y=audio_signal, sr=sample_rate)

    # Estrai il tasso di attraversamento dello zero
    zero_crossings = librosa.feature.zero_crossing_rate(audio_signal)

    # Estrai l'energia RMS
    rms_energy = librosa.feature.rms(y=audio_signal)

    # Estrai il contrasto spettrale
    spectral_contrast = librosa.feature.spectral_contrast(y=audio_signal, sr=sample_rate)

    # Estrai la larghezza di banda spettrale
    spectral_bandwidth = librosa.feature.spectral_bandwidth(y=audio_signal, sr=sample_rate)

    # Estrai il roll-off spettrale
    spectral_rolloff = librosa.feature.spectral_rolloff(y=audio_signal, sr=sample_rate)

    # Altre feature comuni
    spectral_flatness = librosa.feature.spectral_flatness(y=audio_signal)
    


     #size di ogni feature
    centroid_size = spectral_centroid.size
    bandwidth_size = spectral_bandwidth.size

    # Calcola il padding necessario
    padding_size1 = max(0, 94 - centroid_size) #94 è la dimensione che ha il max
    padding_size3 = max(0, 94 - bandwidth_size) #94 è la dimensione che ha il max
    spectral_centroid = np.pad(spectral_centroid, (0, padding_size1), 'constant')
    spectral_bandwidth = np.pad(spectral_bandwidth, (0, padding_size3), 'constant')
   
    spectral_centroid_mean = np.mean(np.expand_dims(spectral_centroid, axis=0), axis=1)
    spectral_bandwidth_mean = np.mean(np.expand_dims(spectral_bandwidth, axis=0), axis=1)


    # Feature aggiuntive per audio brevi
    total_duration = len(audio_signal) / sample_rate  # Lunghezza totale dell'audio in secondi
    average_segment_duration = total_duration / mfccs.shape[1] if mfccs.shape[1] > 0 else 0  # Durata media di ciascun segmento

    


    # Restituisci un dizionario di features
    features = {
        "mfccs": mfccs.mean(axis=1),
        "spectral_centroid_mean": spectral_centroid_mean.flatten(),
        "chroma": chroma.mean(axis=1),
        "zero_crossings": zero_crossings.mean(),
        "rms_energy": rms_energy.mean(),
        "spectral_contrast": spectral_contrast.mean(axis=1),
        "spectral_bandwidth_mean": spectral_bandwidth_mean.flatten(),
        "spectral_rolloff": spectral_rolloff.mean(),
        "spectral_flatness": spectral_flatness.mean(),
        "total_duration": total_duration,
        "average_segment_duration": average_segment_duration
    }

    return features

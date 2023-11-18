from pydub import AudioSegment
import numpy as np
import sounddevice as sd
import wave

def record_voice(duration,number, sample_rate=44100):
    print("To say: ",str(number))
    audio_data = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1, dtype='int16')
    sd.wait()
    print("Registration completed.")
    return audio_data.flatten()

def save_audio_to_wav(audio_data, file_path, sample_rate=44100):
    with wave.open(file_path, 'wb') as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(sample_rate)
        wf.writeframes(audio_data.tobytes())




def check_audio(file_path):
    # Carica il file audio WAV
    audio = AudioSegment.from_file(file_path, format="wav")

    # Converte l'audio in un array numpy
    audio_array = np.array(audio.get_array_of_samples())

    # Calcola il valore assoluto di ciascun campione
    audio_array = np.abs(audio_array)

    # Calcola la media dell'intensità
    media_intensita = np.mean(audio_array)
    if media_intensita < 2000:
        level = "piano"
    elif media_intensita > 2000 and media_intensita < 3000:
        level = "media"
    else:
        level = "forte"
    return level


if __name__ == '__main__':
    duration = 1.5  # durata della registrazione in secondi

    audio_data = record_voice(duration, 0)
    # Salva l'audio in formato WAV
    save_audio_to_wav(audio_data, 'prova.wav')
    # Calcola il livello di intensità
    livello_intensita = check_audio('prova.wav')
    print(livello_intensita)
    
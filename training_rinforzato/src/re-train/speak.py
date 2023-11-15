import sounddevice as sd
import wave
import extract_features_audio as efa


def record_voice(duration, sample_rate=44100):
    #print("Dire un numero da 0 a 9...")
    print("You can start speaking for 1.5s(example a number between 0 and 9)...")
    audio_data = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1, dtype='int16')
    sd.wait()
    print("Registrazione completata.")
    return audio_data.flatten()

def save_audio_to_wav(audio_data, file_path, sample_rate=44100):
    with wave.open(file_path, 'wb') as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(sample_rate)
        wf.writeframes(audio_data.tobytes())

def main():
    duration = 1.5  # durata della registrazione in secondi
    # Registra la voce
    audio_data = record_voice(duration)
    # Salva la registrazione su file wav
    save_audio_to_wav(audio_data, "audio.wav")
    features = efa.extract_features_from_file("audio.wav")
    #i nan vengono sostituiti con 0
    features = {k: 0 if v is None else v for k, v in features.items()}
    return features




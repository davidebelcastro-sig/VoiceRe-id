import os
import glob

def delete_pkl_files(directory):
    # Per ogni elemento nella directory
    for root, dirs, files in os.walk(directory):
        for file in files:
            # Verifica se il file ha estensione .pkl
            if file.endswith(".pkl") or file.endswith(".wav") or file.endswith("modello_combinato.zip"):
                # Costruisci il percorso completo del file
                file_path = os.path.join(root, file)
                # Elimina il file
                os.remove(file_path)
                

# Specifica la directory da cui iniziare la ricerca
starting_directory = "."

# Chiama la funzione per eliminare i file .pkl
delete_pkl_files(starting_directory)

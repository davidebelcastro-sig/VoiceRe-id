import zipfile

# Percorso del file ZIP da decomprimere
zip_file_path = "modello_random_forest.zip"

# Percorso della cartella di destinazione per l'estrazione
extracted_folder = "."


#controllo che non sia gia stato estratto
import os.path
if os.path.exists(extracted_folder+"modello_random_forest.pkl"):
    pass
else:
    # Apri il file ZIP in modalità lettura
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        # Estrai tutti i file contenuti nel file ZIP nella cartella di destinazione
        zip_ref.extractall(extracted_folder)

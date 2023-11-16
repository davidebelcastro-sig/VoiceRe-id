import zipfile
import os.path

# Percorso del file ZIP da decomprimere
zip_file_path1 = "./modelli/modello_0.zip"
zip_file_path2 = "./modelli/modello_1.zip"
zip_file_path3 = "./modelli/modello_2.zip"
zip_file_path4 = "./modelli/modello_3.zip"
zip_file_path5 = "./modelli/modello_4.zip"
#zip_file_path6 = "modello_combinato.zip"

# Percorso della cartella di destinazione per l'estrazione
extracted_folder = "./modelli"


#controllo che non sia gia stato estratto

if os.path.exists(extracted_folder+"modello_0.pkl"):
    pass
else:
    # Apri il file ZIP in modalità lettura
    with zipfile.ZipFile(zip_file_path1, 'r') as zip_ref:
        # Estrai tutti i file contenuti nel file ZIP nella cartella di destinazione
        zip_ref.extractall(extracted_folder)

if os.path.exists(extracted_folder+"modello_1.pkl"):
    pass
else:
    # Apri il file ZIP in modalità lettura
    with zipfile.ZipFile(zip_file_path2, 'r') as zip_ref:
        # Estrai tutti i file contenuti nel file ZIP nella cartella di destinazione
        zip_ref.extractall(extracted_folder)
    
if os.path.exists(extracted_folder+"modello_2.pkl"):
    pass
else:
    # Apri il file ZIP in modalità lettura
    with zipfile.ZipFile(zip_file_path3, 'r') as zip_ref:
        # Estrai tutti i file contenuti nel file ZIP nella cartella di destinazione
        zip_ref.extractall(extracted_folder)

if os.path.exists(extracted_folder+"modello_3.pkl"):
    pass
else:
    # Apri il file ZIP in modalità lettura
    with zipfile.ZipFile(zip_file_path4, 'r') as zip_ref:
        # Estrai tutti i file contenuti nel file ZIP nella cartella di destinazione
        zip_ref.extractall(extracted_folder)

if os.path.exists(extracted_folder+"modello_4.pkl"):
    pass
else:
    # Apri il file ZIP in modalità lettura
    with zipfile.ZipFile(zip_file_path5, 'r') as zip_ref:
        # Estrai tutti i file contenuti nel file ZIP nella cartella di destinazione
        zip_ref.extractall(extracted_folder)


import dividi_dataset
import create_file_csv_train
import create_file_csv_test
import create_model
import pickle
import os
import copy




input_directory = "./data"  # Sostituisci con il percorso reale
train_directory = "train_data"  # Sostituisci con il percorso desiderato per i dati di addestramento
test_directory = "test_data"  # Sostituisci con il percorso desiderato per i dati di test



num_iter = 5
for i in range(num_iter):
    if os.path.exists(train_directory):
        os.system("rm -rf " + train_directory)
    if os.path.exists(test_directory):
        os.system("rm -rf " + test_directory)
    print("Iterazione numero: ", i)
    dividi_dataset.split_data(input_directory, train_directory, test_directory, split_ratio=0.8, random_seed=42)
    print("Creazione file csv train")
    create_file_csv_train.process_audio_files(train_directory)
    print("Creazione file csv test")
    create_file_csv_test.process_audio_files(test_directory)
    print("Creazione modello")
    create_model.create("modello_" + str(i) + ".pkl")
    with open("./modelli/modello_" + str(i) + ".pkl", 'rb') as file:
        model = pickle.load(file)



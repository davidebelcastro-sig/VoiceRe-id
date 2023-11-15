import RF_training
import prediction
import combina_modelli
import extract
import remove_model

def main():
    dataset = "dataset.csv"
    file_name = "training_results"
    #extrai i modelli
    extract.estrai("./modelli")
    #RF_training.main(dataset,file_name,iterazioni) -> crea i modelli che però gia esistono
    combina_modelli.start() #crea il modello combinato
    file_name = "training_results_combinati"
    prediction.prediction(dataset,file_name)
    #visualizza grafici
    # Specifica la directory da cui iniziare la ricerca
    starting_directory = "."
    # Chiama la funzione per eliminare i file .pkl
    remove_model.delete_pkl_files(starting_directory)


if __name__ == "__main__":
    main()
import combina_modelli
import extract
import remove_model
import prediction
import remove_img
import accuracy
import roc
import det
import detect_thresold

def main():

    #extrai i modelli
    print("-Extracting models")
    extract.estrai("./modelli")
    #RF_training.main(dataset,file_name,iterazioni) -> crea i modelli che però gia esistono
    print("-Combining models")
    combina_modelli.start() #crea il modello combinato
    #prediction
    print("-Prediction")
    prediction.pred("./modelli/modello_combinato.pkl", "./csv/accessi.csv")
    remove_img.rem() #elimina le immagini
    print("-Performance Evaluation")
    accuracy.get_accuracy("./csv/accessi.csv", "./csv/accuracy.csv")
    print("-Curva ROC")
    roc.roc("./csv/accuracy.csv", "./output/roc.png")
    print("-Curva DET")
    det.det("./csv/accuracy.csv", "./output/det.png")
    print("-Detect Thresold")
    detect_thresold.detect_th("./csv/accuracy.csv", "./output/detect_thresold.png")
    starting_directory = "."
    # Chiama la funzione per eliminare i file .pkl
    remove_model.delete_pkl_files(starting_directory)


if __name__ == "__main__":
    main()
import os
import pickle
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score, precision_score, recall_score, f1_score
from pathlib import Path
from PCA import PCA_analysis

def prediction(data, file_name):
    #output_dir = r"C:\Users\susan\Documents\VSCode\BiometricSystems\output_file"
    output_dir = Path("output")
    if not output_dir.exists():
        output_dir.mkdir()
    output_path = os.path.join(output_dir, file_name +".txt")
    output_file = open(output_path, "w")

    X_train_pca, pca_model, X_val_pca, y_train, y_val = PCA_analysis(data,"combinato")


    with open("./modelli/modello_combinato.pkl", 'rb') as file:
        best_model = pickle.load(file)

    y_pred = best_model.predict(X_val_pca)
    #rf_accuracy = accuracy_score(y_val, y_pred)
    #print("\nRandom Forest Accuracy: {:.2f}%".format(rf_accuracy * 100))

    classification_rep = classification_report(y_val, y_pred)
    conf_matrix = confusion_matrix(y_val, y_pred)

    #scrivo su file
    # Stampa le altre metriche di valutazione
    print("Classification Report:", file=output_file)
    print(classification_rep, file=output_file)

    # confusion matrix
    print("\nConfusion Matrix:", file=output_file)
    print(conf_matrix, file=output_file)

    # precision, recall, f1
    precision = precision_score(y_val, y_pred, average='weighted')
    recall = recall_score(y_val, y_pred, average='weighted')
    f1 = f1_score(y_val, y_pred, average='weighted')
    print("\nPrecision:", file=output_file)
    print(precision, file=output_file)
    print("Recall:", file=output_file)
    print(recall, file=output_file)
    print("F1-Score:", file=output_file)
    print(f1, file=output_file)
    print("Finished, you can see the output in output/training_results_combinati.txt")
    output_file.close()  




if __name__ == '__main__':
    dataset = "dataset.csv"
    file_name = "training_results_combinati"
    prediction(dataset,file_name)

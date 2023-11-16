import os
import pickle
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score, precision_score, recall_score, f1_score
from pathlib import Path
from PCA import PCA_analysis
import matplotlib.pyplot as plt
import numpy as np

def curva_cmc(model, X_val_pca, y_val):

    rf_probabilities = model.predict_proba(X_val_pca)
    cmc_probs = []
    for x in range(1, 61):
        total_correct_matches = 0
        for i in range(len(rf_probabilities)):
            rf_prob  = rf_probabilities[i]
            # Creazione di una lista di tuple (valore, indice)
            lista_di_tuple = list(enumerate(rf_prob))
            # Ordinamento della lista di tuple in base al valore in modo decrescente
            rf_sorted = sorted(lista_di_tuple, key=lambda x: x[1], reverse=True)
            #solo il primo elemento per ogni riga
            rf_sorted = [x[0] + 1  for x in rf_sorted]
            #capire dove è uguale ytest[i] in rf_sorted
            appo = y_val.iloc[i]
            index = rf_sorted.index(appo) + 1 
            if index <= x:
                total_correct_matches += 1
        cmc_probs.append(total_correct_matches / len(rf_probabilities))

    accuracy_at_rank1 = cmc_probs[0]
    plt.plot(range(1, 61), cmc_probs)
    plt.xticks(np.arange(1, 61, 4))
    plt.xlabel('Rank (k)')
    plt.ylabel('Probability of Correct Match')
    plt.title('Cumulative Match Characteristic (CMC) Curve')
    # Annotazione dell'accuracy al rank 1
    plt.annotate(f'Accuracy at Rank 1: {accuracy_at_rank1:.2%}',
                xy=(1, accuracy_at_rank1), xycoords='data',
                xytext=(20, 30), textcoords='offset points',
                arrowprops=dict(facecolor='black', arrowstyle='->', connectionstyle='arc3,rad=.2'))
    plt.savefig('./output/cmc_curve.png')
    plt.close()
    print("Accuracy calculation completed, you can see the result in the output folder")




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

    curva_cmc(best_model, X_val_pca, y_val)



if __name__ == '__main__':
    dataset = "dataset.csv"
    file_name = "training_results_combinati"
    prediction(dataset,file_name)

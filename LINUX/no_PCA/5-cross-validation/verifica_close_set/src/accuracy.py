import pandas as pd
import csv


def get_accuracy(path_accessi,path_output):


    df = pd.read_csv(path_accessi)
    #apri file csv "risultat" e prendi colonna threshold
    threshold_values = pd.read_csv("./csv/risultati.csv")
    threshold_values = threshold_values['threshold'].tolist()
    threshold_values = sorted(threshold_values)
    with open(path_output, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["threshold", "far", "frr", "acc", "Recall", "tnr", "Precision", "npv", "f1_score"])

    for threshold in threshold_values:
    

        # Inizializza la matrice di confusione
        conf_matrix = [[0, 0], [0, 0]]

        # Itera sul DataFrame e aggiorna la matrice di confusione
        for index, row in df.iterrows():
            y_test = row['y_test']
            utente_dichiara = row['utente_dichiara']
            rf_predictions = eval(row['rf_predictions'])  # Converte la stringa in una lista
            
            # Confronta le condizioni descritte
            if y_test == utente_dichiara and rf_predictions[y_test] >= threshold:
                # Vero Positivo (l'utente dichiara correttamente e la previsione è corretta)
                conf_matrix[1][1] += 1
            elif y_test == utente_dichiara and rf_predictions[y_test] < threshold:
                # Falso Negativo (l'utente dichiara correttamente ma la previsione è errata)
                conf_matrix[1][0] += 1
            elif y_test != utente_dichiara and rf_predictions[utente_dichiara] >= threshold:
                # Falso Positivo (l'utente dichiara erroneamente ma la previsione consente l'accesso)
                conf_matrix[0][1] += 1
            else:
                # Vero Negativo (l'utente dichiara erroneamente e la previsione è corretta)
                conf_matrix[0][0] += 1


        #print(pd.DataFrame(conf_matrix, columns=['Previsto Negativo', 'Previsto Positivo'], index=['Reale Negativo', 'Reale Positivo']))
        # Calcola il FAR (False Acceptance Rate) percentuale in cui il sistema accetta un utente non autorizzato,piu è basso meglio è
        far = conf_matrix[0][1] / (conf_matrix[0][1] + conf_matrix[0][0])
        # Calcola il FRR (False Rejection Rate) percentuale in cui il sistema rifiuta un utente autorizzato,piu è basso meglio è
        frr = conf_matrix[1][0] / (conf_matrix[1][0] + conf_matrix[1][1])
        # Calcola l'ACC (Accuracy) percentuale di accessi correttamente autorizzati,piu è alto meglio è
        acc = (conf_matrix[0][0] + conf_matrix[1][1]) / (conf_matrix[0][0] + conf_matrix[0][1] + conf_matrix[1][0] + conf_matrix[1][1])

        # Calcola le metriche di valutazione
        tp = conf_matrix[1][1]
        tn = conf_matrix[0][0]
        fp = conf_matrix[0][1]
        fn = conf_matrix[1][0]

        tpr = tp / (tp + fn)  # True Positive Rate o Sensitivity
        tnr = tn / (tn + fp)  # True Negative Rate o Specificity
        ppv = tp / (tp + fp)  # Positive Predictive Value o Precision
        npv = tn / (tn + fn)  # Negative Predictive Value
        f1_score = 2 * (ppv * tpr) / (ppv + tpr)  # F1 Score

        #scrivo su file csv
        with open(path_output, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([threshold, far, frr, acc, tpr, tnr, ppv, npv, f1_score])
        


        #TPR (True Positive Rate) o Sensitivity: La proporzione di veri positivi rispetto al totale degli elementi positivi.

        #TNR (True Negative Rate) o Specificity: La proporzione di veri negativi rispetto al totale degli elementi negativi.

        #PPV (Positive Predictive Value) o Precision: La proporzione di veri positivi rispetto alla somma di veri positivi e falsi positivi.

        #NPV (Negative Predictive Value): La proporzione di veri negativi rispetto alla somma di veri negativi e falsi negativi.

        #F1 Score: Una media ponderata di precision e sensitivity, utile quando c'è uno sbilanciamento tra le classi.

        #FAR (False Acceptance Rate): La proporzione di falsi positivi

        #FRR (False Rejection Rate): La proporzione di falsi negativi

if __name__ == '__main__':
    get_accuracy("./csv/accessi_0.csv", "./csv/accuracy_0.csv")
    get_accuracy("./csv/accessi_1.csv", "./csv/accuracy_1.csv")
    get_accuracy("./csv/accessi_2.csv", "./csv/accuracy_2.csv")
    get_accuracy("./csv/accessi_3.csv", "./csv/accuracy_3.csv")
    get_accuracy("./csv/accessi_4.csv", "./csv/accuracy_4.csv")
    get_accuracy("./csv/accessi_combined.csv", "./csv/accuracy_combined.csv")

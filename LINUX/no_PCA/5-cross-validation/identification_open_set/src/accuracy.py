import pandas as pd
import csv


def get_accuracy(path_accessi,path_output):


    df = pd.read_csv(path_accessi)
    #lista da 0.01 a 0.80 con step 0.01
    threshold_values = [round(x * 0.01, 2) for x in range(1, 81)]
    with open(path_output, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["threshold", "CDIR", "FAR", "FRR"])

    for threshold in threshold_values:
    
        tentativi_impostori = 0
        tentativi_legittimi = 0
        far = 0
        cdir = 0
        # Itera sul DataFrame e aggiorna la matrice di confusione
        for index, row in df.iterrows():
            y_test = row['y_test']
            rf_predictions = eval(row['rf_predictions'])  # Converte la stringa in una lista
            massimo = max(rf_predictions)
            pos = rf_predictions.index(massimo)
            if y_test == -2: #non è nel db
                tentativi_impostori += 1
                if massimo >= threshold:
                    far += 1
            else:
                tentativi_legittimi += 1
                if massimo >= threshold  and pos == y_test:
                    cdir += 1
            
        #scrivo su file csv
        with open(path_output, 'a', newline='') as file:
            writer = csv.writer(file)
            frr = 1 - (cdir/tentativi_legittimi)
            writer.writerow([threshold, cdir/tentativi_legittimi, far/tentativi_impostori, frr])

            
if __name__ == '__main__':
    get_accuracy("./csv/accessi_combined.csv", "./csv/accuracy_combined.csv")
    get_accuracy("./csv/accessi_0.csv", "./csv/accuracy_0.csv")
    get_accuracy("./csv/accessi_1.csv", "./csv/accuracy_1.csv")
    get_accuracy("./csv/accessi_2.csv", "./csv/accuracy_2.csv")
    get_accuracy("./csv/accessi_3.csv", "./csv/accuracy_3.csv")
    get_accuracy("./csv/accessi_4.csv", "./csv/accuracy_4.csv")

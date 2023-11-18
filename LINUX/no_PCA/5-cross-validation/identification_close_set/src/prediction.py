import pandas as pd
import pickle
import os
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import precision_score, recall_score,accuracy_score
import csv

def predizione_modello(path,X_test,y_test):
    rf_model = pickle.load(open(path, 'rb'))
    rf_result = rf_model.predict(X_test)
    precision = precision_score(y_test, rf_result, average='weighted')
    recall = recall_score(y_test, rf_result, average='weighted')
    f1_score = 2 * (precision * recall) / (precision + recall)
    accuracy = accuracy_score(y_test, rf_result)
    return precision, recall, f1_score, accuracy

print("Accuracy calculation...")


test_data = pd.read_csv('./file_csv/features_test.csv')



X_test = test_data.drop('label', axis=1)
y_test = test_data['label']


#Controllo che il file pkl non esista già
if os.path.exists('./modelli/modello_combinato.pkl'):
    # Caricamento del modello da un file pickle
    with open('./modelli/modello_combinato.pkl', 'rb') as file:
        rf_model = pickle.load(file)
else:
    print("Error: modello_random_forest.pkl not found")
		
prec1, rec1, f1_1,acc1 = predizione_modello('./modelli/modello_0.pkl',X_test,y_test)
prec2, rec2, f1_2,acc2 = predizione_modello('./modelli/modello_1.pkl',X_test,y_test)
prec3, rec3, f1_3,acc3 = predizione_modello('./modelli/modello_2.pkl',X_test,y_test)
prec4, rec4, f1_4,acc4 = predizione_modello('./modelli/modello_3.pkl',X_test,y_test)
prec5, rec5, f1_5,acc5 = predizione_modello('./modelli/modello_4.pkl',X_test,y_test)
media_prec = (prec1 + prec2 + prec3 + prec4 + prec5) / 5
media_rec = (rec1 + rec2 + rec3 + rec4 + rec5) / 5
media_f1 = (f1_1 + f1_2 + f1_3 + f1_4 + f1_5) / 5
media_acc = (acc1 + acc2 + acc3 + acc4 + acc5) / 5


rf_probabilities = rf_model.predict_proba(X_test)
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
        index = rf_sorted.index(y_test[i]) + 1 
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
plt.annotate(f'Recognition Rate: {accuracy_at_rank1:.2%}',
             xy=(1, accuracy_at_rank1), xycoords='data',
             xytext=(20, 30), textcoords='offset points',
             arrowprops=dict(facecolor='black', arrowstyle='->', connectionstyle='arc3,rad=.2'))
plt.savefig('./output/cmc_curve.png')
plt.close()

rf_result = rf_model.predict(X_test)
precision = precision_score(y_test, rf_result, average='weighted')
recall = recall_score(y_test, rf_result, average='weighted')
f1_score = 2 * (precision * recall) / (precision + recall)
accuracy = accuracy_score(y_test, rf_result)
with open("./output/accuracy.csv",mode="w", newline='') as csv_file:
    header = ['Value', 'Average', 'Combined']
    writer = csv.writer(csv_file, delimiter=',')
    writer.writerow(header)
    writer.writerow(['Precision', str(media_prec), str(precision)])
    writer.writerow(['Recall', str(media_rec), str(recall)])
    writer.writerow(['F1 Score', str(media_f1), str(f1_score)])
    #writer.writerow(['Accuracy', str(media_acc), str(accuracy)])
print("Accuracy calculation completed, you can see the result in the output folder")
import pandas as pd
import os

# Lista dei file CSV
files = ['accuracy_0', 'accuracy_1', 'accuracy_2', 'accuracy_3', 'accuracy_4', 'accuracy_combined']

# Leggi i file CSV e crea un dizionario di DataFrame
dfs = {file: pd.read_csv(f'./csv/{file}.csv') for file in files}

# Crea un DataFrame risultante con le colonne desiderate
result_df = pd.DataFrame()

# Colonna 'th'
result_df['threshold'] = dfs['accuracy_0']['threshold']

# Colonne 'cdir medio', 'far medio', 'frr medio'
for metric in ['far', 'frr', 'acc', 'Recall', 'tnr', 'Precision', 'npv', 'f1_score']:
    result_df[f'{metric}_medio'] = sum(dfs[file][metric] for file in files[:-1]) / len(files[:-1])

# Colonne 'cdir combined', 'far combined', 'frr combined'
result_df['far_combined'] = dfs['accuracy_combined']['far']
result_df['frr_combined'] = dfs['accuracy_combined']['frr']
result_df['acc_combined'] = dfs['accuracy_combined']['acc']
result_df['Recall_combined'] = dfs['accuracy_combined']['Recall']
result_df['tnr_combined'] = dfs['accuracy_combined']['tnr']
result_df['Precision_combined'] = dfs['accuracy_combined']['Precision']
result_df['npv_combined'] = dfs['accuracy_combined']['npv']
result_df['f1_score_combined'] = dfs['accuracy_combined']['f1_score']



#elimino
os.remove("./csv/accuracy_0.csv")
os.remove("./csv/accuracy_1.csv")
os.remove("./csv/accuracy_2.csv")
os.remove("./csv/accuracy_3.csv")
os.remove("./csv/accuracy_4.csv")

# Salva il DataFrame risultante nel file CSV
output_file = './output/final_accuracy.csv'
result_df = result_df[['threshold', 'far_medio', 'far_combined', 'frr_medio', 'frr_combined', 'acc_medio', 'acc_combined', 'Recall_medio', 'Recall_combined', 'tnr_medio', 'tnr_combined', 'Precision_medio', 'Precision_combined', 'npv_medio', 'npv_combined', 'f1_score_medio', 'f1_score_combined']]
result_df.to_csv(output_file, index=False)




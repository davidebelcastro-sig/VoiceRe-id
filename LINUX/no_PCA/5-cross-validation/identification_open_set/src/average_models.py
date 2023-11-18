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
for metric in ['CDIR', 'FAR', 'FRR']:
    result_df[f'{metric}_medio'] = sum(dfs[file][metric] for file in files[:-1]) / len(files[:-1])

# Colonne 'cdir combined', 'far combined', 'frr combined'
result_df['cdir_combined'] = dfs['accuracy_combined']['CDIR']
result_df['far_combined'] = dfs['accuracy_combined']['FAR']
result_df['frr_combined'] = dfs['accuracy_combined']['FRR']


#elimino
os.remove("./csv/accuracy_0.csv")
os.remove("./csv/accuracy_1.csv")
os.remove("./csv/accuracy_2.csv")
os.remove("./csv/accuracy_3.csv")
os.remove("./csv/accuracy_4.csv")

# Salva il DataFrame risultante nel file CSV
output_file = './output/final_accuracy.csv'
#VOGLIO METTERE LE COLONNE IN QUESTO ORDINE: TH,CDIR COMBINED,CDIR MEDIO,FAR COMBINED,FAR MEDIO,FRR COMBINED,FRR MEDIO
result_df = result_df[['threshold', 'cdir_combined', 'CDIR_medio', 'far_combined', 'FAR_medio', 'frr_combined', 'FRR_medio']]
result_df.to_csv(output_file, index=False)




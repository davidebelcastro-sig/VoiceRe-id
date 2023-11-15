import pandas as pd



def detect(path):
    df = pd.read_csv(path)

    #prendono l'ultima riga colonna label
    last_label = df.iloc[-1]["label"]
    return last_label
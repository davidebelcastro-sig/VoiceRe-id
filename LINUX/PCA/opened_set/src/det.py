import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def det(path1,path2):
    # Carica il tuo file CSV
    df = pd.read_csv(path1)

    # Estrai le colonne di interesse
    thresholds = df['threshold']
    far_values = df['far']
    frr_values = df['frr']


    # Plotta la curva ROC
    plt.figure(figsize=(8, 8))
    plt.plot(far_values, frr_values, label='DET Curve')


    # Etichette e titoli
    plt.title('Detection Error TradeOff (DET) Curve')
    plt.xlabel('False Positive Rate (FAR)')
    plt.ylabel('False Reject Rate (FRR)')
    plt.legend()
    plt.savefig(path2)
    plt.close()

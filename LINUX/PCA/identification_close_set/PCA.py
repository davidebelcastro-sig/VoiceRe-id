from sklearn import decomposition
from sklearn.preprocessing import StandardScaler
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split

def PCA_analysis(data,i):
    df = pd.read_csv(data)
    X = df.iloc[:, 1:]
    y = df.iloc[:, 0]
    X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2, random_state=42)

    sc = StandardScaler()
    X_train_scaled = sc.fit_transform(X_train) # standardizza le caratteristiche del set di addestram X_train
    pca = decomposition.PCA().fit(X_train_scaled) # analisi delle componenti principali
    X_val_scaled = sc.transform(X_val)
    plt.figure(figsize=(11, 7))
    plt.plot(np.cumsum(pca.explained_variance_ratio_), color='k', lw=2)
    plt.xlabel('Number of components')
    plt.ylabel('Total explained variance')
    plt.xlim(0, 225)
    plt.yticks(np.arange(0, 1.1, 0.1))
    plt.axvline(26, c='b')
    plt.axhline(0.95, c='r')
    #plt.axhline(1.0, c='g')
    if i == "combinato":
        plt.savefig('./output/PCA_combinato.png')
    else:
        plt.savefig('./output/PCA_'+str(i)+".png")
    plt.close()
    pca_model = decomposition.PCA(n_components=26) # crea un modello PCA con 25 componenti principali
    X_train_pca = pca_model.fit_transform(X_train_scaled) #X_pca = X_train, calcola e applica la PCA al set di dati standardizzato X_scaled
    X_val_pca = pca_model.transform(X_val_scaled)
    return X_train_pca, pca_model, X_val_pca, y_train, y_val


if __name__ == '__main__':
    X_train_pca, pca_model, X_val_pca, y_train, y_val = PCA_analysis("dataset.csv")
    # puoi utilizzare X_pca nel tuo codice per ulteriori analisi o per l'addestramento di modelli utilizzando 
    # solo le prime 25 componenti principali. La variabile pca1 contiene le informazioni sulla PCA, ad esempio, 
    # i componenti principali e gli autovalori, che potrebbero essere utili in fasi successive dell'analisi.
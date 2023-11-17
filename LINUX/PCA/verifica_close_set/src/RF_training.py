import os
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import StratifiedKFold, RandomizedSearchCV, GridSearchCV
import pickle
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score, precision_score, recall_score, f1_score
from sklearn.model_selection import train_test_split
from pathlib import Path
from PCA import PCA_analysis

def prediction(data, file_name, i):
    #output_dir = r"C:\Users\susan\Documents\VSCode\BiometricSystems\output_file"
    output_dir = Path("output")
    if not output_dir.exists():
        output_dir.mkdir()
    output_path = os.path.join(output_dir, file_name + "_" + str(i)+".txt")
    output_file = open(output_path, "w")

    X_train_pca, pca_model, X_val_pca, y_train, y_val = PCA_analysis(data,i)

    skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

    rf_model = RandomForestClassifier()

    # Griglia di iperparametri da testare
    param_grid = {
        'max_depth': [None, 10, 20],
        'min_samples_split': [2, 5, 10],
        'min_samples_leaf': [1, 2, 3]
    }

    grid_search = GridSearchCV(estimator=rf_model, param_grid=param_grid, cv=skf, n_jobs=-1, verbose=3)
    grid_search.fit(X_train_pca, y_train)

    with open('./modelli/modello_random_forest_'+str(i)+".pkl", 'wb') as file:
        pickle.dump(grid_search, file)


    # Iperparametri ottimali
    best_params = grid_search.best_params_
    best_model = grid_search.best_estimator_
    accuracy = best_model.score(X_val_pca, y_val)

    print("\n Iperparametri ottimali: ", best_params)
    print("\n Accuracy: ", accuracy)
    print("\n Best score: ", grid_search.best_score_)
    print("\n Iperparametri ottimali: ", file=output_file)
    print(best_params, file=output_file)
    print("\n Accuracy: ", file=output_file)
    print(accuracy, file=output_file)
    print("\n Best score: ", file=output_file)
    print(grid_search.best_score_, file=output_file)


    y_pred = best_model.predict(X_val_pca)
    #rf_accuracy = accuracy_score(y_val, y_pred)
    #print("\nRandom Forest Accuracy: {:.2f}%".format(rf_accuracy * 100))

    classification_rep = classification_report(y_val, y_pred)
    conf_matrix = confusion_matrix(y_val, y_pred)

    # Stampa le altre metriche di valutazione
    print("\nClassification Report:")
    print(classification_rep)
    print("\nClassification Report:", file=output_file)
    print(classification_rep, file=output_file)

    # confusion matrix
    print("\nConfusion Matrix:")
    print(conf_matrix)
    print("\nConfusion Matrix:", file=output_file)
    print(conf_matrix, file=output_file)

    # precision, recall, f1
    precision = precision_score(y_val, y_pred, average='weighted')
    recall = recall_score(y_val, y_pred, average='weighted')
    f1 = f1_score(y_val, y_pred, average='weighted')
    print("\nPrecision:", precision)
    print("Recall:", recall)
    print("F1-Score:", f1)
    print("\nPrecision:", file=output_file)
    print(precision, file=output_file)
    print("Recall:", file=output_file)
    print(recall, file=output_file)
    print("F1-Score:", file=output_file)
    print(f1, file=output_file)

    output_file.close()  



def main(dataset,file_name,iterazioni):
    for i in range(iterazioni):
        prediction(dataset, file_name, i)



if __name__ == '__main__':
    dataset = "dataset.csv"
    file_name = "training_results"
    iterazioni = 10
    main(dataset,file_name,iterazioni)

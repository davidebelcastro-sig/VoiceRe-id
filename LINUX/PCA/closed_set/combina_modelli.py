import pickle
import copy


def combine_models(models):
    # Estrai i migliori estimatori dai modelli GridSearchCV
    best_estimators = [model.best_estimator_ for model in models]

    # Estrai tutti gli alberi da tutti i modelli
    all_estimators = [tree for model in best_estimators for tree in model.estimators_]

    # Crea una nuova foresta con tutti gli alberi combinati
    combined_model = copy.deepcopy(best_estimators[0])
    combined_model.estimators_ = all_estimators

    return combined_model




def start():
    with open("./modelli/modello_random_forest_0" + ".pkl", 'rb') as file:
        model0 = pickle.load(file)

    with open("./modelli/modello_random_forest_1" + ".pkl", 'rb') as file:
        model1 = pickle.load(file)

    with open("./modelli/modello_random_forest_2" + ".pkl", 'rb') as file:
        model2 = pickle.load(file)

    with open("./modelli/modello_random_forest_3" + ".pkl", 'rb') as file:
        model3 = pickle.load(file)

    with open("./modelli/modello_random_forest_4" + ".pkl", 'rb') as file:
        model4 = pickle.load(file)

    with open("./modelli/modello_random_forest_5" + ".pkl", 'rb') as file:
        model5 = pickle.load(file)

    with open("./modelli/modello_random_forest_6" + ".pkl", 'rb') as file:
        model6 = pickle.load(file)

    with open("./modelli/modello_random_forest_7" + ".pkl", 'rb') as file:
        model7 = pickle.load(file)

    with open("./modelli/modello_random_forest_8" + ".pkl", 'rb') as file:
        model8 = pickle.load(file)

    with open("./modelli/modello_random_forest_9" + ".pkl", 'rb') as file:
        model9 = pickle.load(file)

    modelli = [model0,model1,model2,model3,model4,model5,model6,model7,model8,model9]
    mod_comb = combine_models(modelli)


    # Salvataggio del modello in formato pickle
    with open("./modelli/modello_combinato.pkl", 'wb') as file:
         pickle.dump(mod_comb, file)   


if __name__ == '__main__':
    start()
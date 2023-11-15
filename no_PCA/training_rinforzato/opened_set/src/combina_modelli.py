import pickle
import prediction
import accuracy
import copy

def combine_models(models):
    # Estrai tutti gli alberi da tutti i modelli
    all_estimators = [tree for model in models for tree in model.estimators_]

    # Crea una nuova foresta con tutti gli alberi combinati
    combined_model = copy.deepcopy(models[0])
    combined_model.estimators_ = all_estimators
    
    return combined_model



with open("./modelli/modello_0" + ".pkl", 'rb') as file:
        model1 = pickle.load(file)

with open("./modelli/modello_1" + ".pkl", 'rb') as file:
        model2 = pickle.load(file)

with open("./modelli/modello_2" + ".pkl", 'rb') as file:
        model3 = pickle.load(file)

with open("./modelli/modello_3" + ".pkl", 'rb') as file:
        model4 = pickle.load(file)

with open("./modelli/modello_4" + ".pkl", 'rb') as file:
        model5 = pickle.load(file)



modelli = [model1, model2, model3, model4, model5]
mod_comb = combine_models(modelli)


# Salvataggio del modello in formato pickle
with open("./modelli/modello_combinato.pkl", 'wb') as file:
    pickle.dump(mod_comb, file)



import os

file_path = "./output"

#elimina tutte le immagini dentro file_path
for filename in os.listdir(file_path):
    if filename.endswith(".png"):
        os.remove(file_path+"/"+filename)




import os

file_path = "modello_random_forest.pkl"


if os.path.exists(file_path):
    os.remove(file_path)
    print("File Removed!")
else:
    print("File not exist!")



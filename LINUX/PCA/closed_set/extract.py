import zipfile
import os

def estrai(directory):
    ls = os.listdir(directory)
    for el in ls:
        with zipfile.ZipFile(directory + "/" + el, 'r') as zip_ref:
            zip_ref.extractall(directory)
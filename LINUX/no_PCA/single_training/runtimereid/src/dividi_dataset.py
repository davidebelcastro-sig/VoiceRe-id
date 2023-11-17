import os
from sklearn.model_selection import train_test_split
import shutil

def split_data(input_dir, train_dir, test_dir, split_ratio=0.8, random_seed=None):
    if random_seed is not None:
        random_state = random_seed
    else:
        random_state = None

    for label in os.listdir(input_dir):
        label_dir = os.path.join(input_dir, label)

        # Ignora eventuali file non desiderati nella directory
        if not os.path.isdir(label_dir):
            continue

        train_label_dir = os.path.join(train_dir, label)
        test_label_dir = os.path.join(test_dir, label)

        # Crea le directory di train e test per l'etichetta corrente
        os.makedirs(train_label_dir, exist_ok=True)
        os.makedirs(test_label_dir, exist_ok=True)

        # Lista di file nella directory corrente
        files = [f for f in os.listdir(label_dir) if f.endswith('.wav')]

        # Suddivide i file in addestramento e test
        train_files, test_files = train_test_split(files, test_size=(1 - split_ratio), random_state=random_state)

        # Copia i file di addestramento
        for file in train_files:
            src_path = os.path.join(label_dir, file)
            dest_path = os.path.join(train_label_dir, file)
            shutil.copy(src_path, dest_path)

        # Copia i file di test
        for file in test_files:
            src_path = os.path.join(label_dir, file)
            dest_path = os.path.join(test_label_dir, file)
            shutil.copy(src_path, dest_path)

if __name__ == "__main__":
    input_directory = "./data"  # Sostituisci con il percorso reale
    train_directory = "./data/train_data"  # Sostituisci con il percorso desiderato per i dati di addestramento
    test_directory = "./data/test_data"  # Sostituisci con il percorso desiderato per i dati di test

    split_data(input_directory, train_directory, test_directory, split_ratio=0.8, random_seed=42)

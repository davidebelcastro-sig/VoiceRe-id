echo "-Extraction models"
python3 src/extract.py
echo "-Combining models"
python3 src/combina_modelli.py
python3 src/re-train/reid.py
python3 src/remove_model.py

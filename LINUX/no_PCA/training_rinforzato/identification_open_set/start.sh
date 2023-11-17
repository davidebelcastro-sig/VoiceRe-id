#!/bin/bash

# Verifica se il file accessi.csv esiste
if [ -e "./csv/accessi.csv" ]; then

	echo "-Extraction models"
	python3 src/extract.py
	echo "-Combining models"
	python3 src/combina_modelli.py
	echo "-Remove previous files"
	python3 src/remove_img.py
	echo "-Performance Evaluation"
	python3 src/accuracy.py
	echo "-Curva ROC"
	python3 src/roc.py
	python3 src/remove_model.py

else

	echo "-Extraction models"
	#python3 src/crea_modelli.py
	python3 src/extract.py
	echo "-Combining models"
	python3 src/combina_modelli.py
	echo "-Training"
	python3 src/prediction.py
	echo "-Remove previous files"
	python3 src/remove_img.py
	echo "-Performance Evaluation"
	python3 src/accuracy.py
	echo "-Curva ROC"
	python3 src/roc.py
	python3 src/remove_model.py
	

fi

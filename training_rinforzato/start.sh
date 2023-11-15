#!/bin/bash

# Verifica se il file accessi.csv esiste
if [ -e "./csv/accessi.csv" ]; then

	echo "-Estrai modelli"
	python3 src/extract.py
	echo "-Combina modelli"
	python3 src/combina_modelli.py
	echo "Remove previous files"
	python3 src/remove_img.py
	echo "-Performance Evaluation"
	python3 src/accuracy.py
	echo "-Curva ROC"
	python3 src/roc.py
	echo "-Curva DET"
	python3 src/det.py
	echo "-Detect Thresold"
	python3 src/detect_thresold.py
	python3 src/remove_model.py

else

	echo "-Crea modelli"
	python3 src/crea_modelli.py
	echo "-Combina modelli"
	python3 src/combina_modelli.py
	echo "-Training"
	python3 src/prediction.py
	echo "Remove previous files"
	python3 src/remove_img.py
	echo "-Performance Evaluation"
	python3 src/accuracy.py
	echo "-Curva ROC"
	python3 src/roc.py
	echo "-Curva DET"
	python3 src/det.py
	echo "-Detect Thresold"
	python3 src/detect_thresold.py
	python3 src/remove_model.py
	

fi

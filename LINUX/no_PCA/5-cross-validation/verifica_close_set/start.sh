#!/bin/bash

# Verifica se il file accessi.csv esiste
if [ -e "./csv/accessi_combined.csv" ]; then

	echo "-Extraction models"
	python3 src/extract.py
	echo "-Combining models"
	python3 src/combina_modelli.py
	echo "-Remove previous files"
	python3 src/remove_img.py
	echo "-Performance Evaluation"
	python3 src/accuracy.py
	python3 src/average_models.py
	echo "-Curva ROC"
	python3 src/roc.py
	echo "-Curva DET"
	python3 src/det.py
	echo "-Detect Thresold"
	python3 src/detect_thresold.py
	python3 src/remove_model.py

else

	echo "-Extraction models"
	python3 src/extract.py
	echo "-Combining models"
	python3 src/combina_modelli.py
	echo "-Training"
	python3 src/prediction.py
	echo "-Remove previous files"
	python3 src/remove_img.py
	echo "-Performance Evaluation"
	python3 src/accuracy.py
	python3 src/average_models.py
	echo "-Curva ROC"
	python3 src/roc.py
	echo "-Curva DET"
	python3 src/det.py
	echo "-Detect Thresold"
	python3 src/detect_thresold.py
	python3 src/remove_model.py
	

fi

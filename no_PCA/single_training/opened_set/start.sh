#!/bin/bash

# Verifica se il file accessi.csv esiste
if [ -e "./file_csv/accessi.csv" ]; then

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

	echo "-Divido dataset"
	python3 src/dividi_dataset.py
	echo "-Feature Extraction"
	python3 src/create_file_csv_train.py
	python3 src/create_file_csv_test.py
	echo "-Training"
	python3 src/prediction.py
	python3 src/extract.py
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

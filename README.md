# Voice Re-Identification System

Voice re-identification (voice re-id) is a specialized application designed for recognizing individuals based on their voice patterns.

## System Structure

The project is organized into two main directories: **LINUX** and **NO_PCA**.

### LINUX Directory

The LINUX directory contains two subdirectories: **PCA** and **NO_PCA**.

#### PCA Subdirectory
- **Identification (Closed Set):** Run identification on the closed set by executing the command:


The results will be available in the PCA/Identification/Closed_Set/output directory.

#### NO_PCA Subdirectory
Inside the NO_PCA directory, there are two subdirectories:
- **5-Cross Validation:**
- **Identification (Closed Set):** Execute the following command:
  ```
  bash start.sh
  ```
- **Identification (Open Set):**
  ```
  python3 run.py
  ```
- **Verification:**
  ```
  python3 run.py
  ```

- **Single Training:**
- **Identification (Closed Set):**
  ```
  bash start.sh
  ```
- **Identification (Open Set):**
  ```
  python3 run.py
  ```
- **Verification:**
  ```
  python3 run.py
  ```
- **Run-Time Re-identification:**
  Allows user registration in the system and subsequent re-identification. Execute the appropriate commands as mentioned in the directory.

### Running Instructions

Follow the provided instructions in each directory to execute the specific components of the voice re-identification

## Installation

You can use the requirements.txt file to install packages with pip (created with the command pip freeze > requirements.txt):



## Dataset

The dataset is downloaded from the [link](https://github.com/soerenab/AudioMNIST/tree/master).


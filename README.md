# Voice Re-Identification System

Voice re-identification (voice re-id) is a specialized application designed for recognizing individuals based on their voice patterns.

## REPORT

For a complete explanation of the project and to view the obtained results, please refer to the project report.

## System Structure

The project is organized into two main directories: **LINUX** and **WINDOWS**.

**Note:** All commands must be executed within the appropriate directory.

Follow the provided instructions in each directory to execute the specific components of the voice re-identification.

### LINUX Directory

  The LINUX directory contains two subdirectories: **PCA** and **NO_PCA**.
  
  #### PCA Subdirectory
  - **Identification (Closed Set):** Run identification on the closed set by executing the command:
    ```
    bash start.sh
    ```
    The results will be available in the PCA/identification_close_set/output directory.
  
  - **Verification:** Run Verification by executing the command:
    ```
    bash start.sh
    ```
    The results will be available in the PCA/verifica_close_set/output directory.


  #### NO_PCA Subdirectory
  Inside the NO_PCA directory, there are two subdirectories:
  - **5-Cross Validation:**
  - **Single Training:**

  **Note** Both have the following commands
    
  - **Identification (Closed Set):** 
    ```
    bash start.sh
    ```
  - **Identification (Open Set):**
    ```
    bash start.sh
    ```
  - **Verification:**
    ```
      bash start.sh
    ```

- **Plus for Single Training:**

  - **Run-Time Re-identification:**
  Allows user registration in the system and subsequent re-identification. Execute the appropriate commands as mentioned in the directory.
  ```
  bash reid_runtime.sh
  ```

## Installation

You can use the requirements.txt file to install packages with pip (created with the command pip freeze > requirements.txt):
``` 
pip3 install -r requirements.txt
```

## Dataset

The dataset is downloaded from the [link](https://github.com/soerenab/AudioMNIST/tree/master).

## Output Example

This is the Confusion Matrix with 5 cross validation in Verification, without PCA

![Main screen](https://github.com/davidebelcastro-sig/PersonalTrainer/assets/73530772/2d116228-e29d-43ae-8c2b-827fbf883979)

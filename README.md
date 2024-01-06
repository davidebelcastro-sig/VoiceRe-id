# Voice Re-identification

Voice re-id is an application that allows a person to be recognized by their voice.


## How It Works

There are two directories
PCA and no_PCA
Both PCA and no_PCA perform reidentification from the speech signal via opened_set and closed_set and verification.
In the opened_set system it is possible also to run "run-time-reid" and be re-identified after registering in the system.
Accuracy values ​​are reported in the output directory inside the current directory.
Inside no_PCA there are two directories
single_training and training_rinforzato, they are two different ways to do training.


## Running Instructions

### Windows


### Linux

For PCA/verifica, inside this directory run:
```
bash start.sh
```
and the output are presents in the directory PCA/verifica/output


For PCA/identification_close_set, inside this directory run:
```
bash start.sh
```
and the output are presents in the directory PCA/identification_close_set/output


For no_PCA/single_training/identification_closed_set, inside this directory run:
```
bash start.sh
```
and the output are presents in the directory no_PCA/single_training/identification_closed_set/output


For no_PCA/single_training/identification_open_set, inside this directory run:
```
bash start.sh
```
and the output are presents in the directory no_PCA/single_training/identification_open_set/output


For no_PCA/single_training/verifica, inside this directory run:
```
bash start.sh
```
and the output are presents in the directory no_PCA/single_training/verifica/output


For no_PCA/single_training/runtimereid, inside this directory run:
```
bash reid_runtime.sh
```

For no_PCA/5-cross-validation is the same!!



## Installation  

You can use the requirements.txt file to install packages with pip (created with the command pip freeze > requirements.txt):
``` 
pip3 install -r requirements.txt
```

## Dataset

The dataset is downloaded from the [link](https://github.com/soerenab/AudioMNIST/tree/master).


## Output Example

This is the Confusion Matrix with 5 cross validation in Verification, without PCA

![Main screen](https://github.com/davidebelcastro-sig/VoiceRe-id/blob/main/cm.png)

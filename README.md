# Voice Re-identification

Voice re-id is an application that allows a person to be recognized by their voice.


## How It Works

There are two directories
PCA and no_PCA
Both PCA and no_PCA perform reidentification from the speech signal via opened_set and closed_set.
In the opened_set system it is possible to run "run-time-reid" and be re-identified after registering in the system.
Accuracy values ​​are reported in both the closed and opened sets.
Inside no_PCA there are two directories
single_training and training_rinforzato, they are two different ways to do training.


## Running Instructions

### Windows


### Linux

For PCA/closed_set
```
bash start.sh
```
and the output are presents in the directory PCA/closed_set/output


For PCA/opened_set
```
python3 run.py
```
and the output are presents in the directory PCA/opened_set/output


For no_PCA/single_training/closed_set
```
bash start.sh
```

For no_PCA/single_training/opened_set
```
python3 run.py
```

For no_PCA/training_rinforzato/closed_set
```
bash start.sh
```

For no_PCA/training_rinforzato/opened_set
```
python3 run.py
```

## Installation  

You can use the requirements.txt file to install packages with pip (created with the command pip freeze > requirements.txt):
``` 
pip3 install -r requirements.txt
```





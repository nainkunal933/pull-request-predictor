"""
Author : Pedram Mirshahreza
Created on Tue Dec 12 2019
"""

# Artificial Neural Network Model

# Importing the libraries
import keras
import numpy  as np
import pandas as pd

from   keras.models import Sequential
from   keras.layers import Dense

from   sklearn.model_selection import train_test_split
from   sklearn.utils           import class_weight
from   sklearn.metrics         import confusion_matrix
from   sklearn.metrics         import accuracy_score
from   sklearn.metrics         import f1_score
from   sklearn.metrics         import recall_score
from   sklearn.metrics         import precision_score



# ----------- Part 0 - Parameters -----------#
#The hyper parameters set for the ANN
test_set_ratio = 0.2
epochs         = 10
batch_size = 10


# ----------- Part 1 - Handling dataset -----------#

# Importing the dataset
file_name = 'convertcsv.csv'
dataset = pd.read_csv(file_name)

# remove unnecessary columns
del dataset["pr_number"]  # this is just ID .. not needed

# Assign X and y
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values

# Splitting the dataset into the Training set and Test set
X_train, X_test, y_train, y_test = train_test_split(X, y,
                                                    test_size=test_set_ratio,
                                                    random_state = 0)


# ----------- Part 2 - ANN model -----------#

# Initialising the ANN
classifier = Sequential()

# Adding the input layer and the first hidden layer
classifier.add(Dense(units = 3,
                     kernel_initializer = 'uniform',
                     activation         = 'relu'   ,
                     input_dim          = X_train.shape[1]))

# Adding the second hidden layer
classifier.add(Dense(units = 3,
                     kernel_initializer = 'uniform',
                     activation = 'relu'))

# Adding the output layer
classifier.add(Dense(units = 1,
                     kernel_initializer = 'uniform',
                     activation         = 'sigmoid'))

# Compiling the ANN
classifier.compile(optimizer = 'adam',
                        loss = 'binary_crossentropy',
                     metrics = ['accuracy'])

# create class weights to try to balance data
class_weights = class_weight.compute_class_weight('balanced',
                                                  np.unique(y_train),
                                                            y_train  )


# Fitting the ANN to the Training set

classifier.fit(X_train, y_train         ,
               batch_size   = batch_size,
               epochs       = epochs    ,
               class_weight = class_weights)

#----------- Part 3 - Making predictions and evaluating the model -----------#

# Predicting the Test set results
y_pred = classifier.predict(X_test)
y_pred = (y_pred > 0.5)


# Reporting Metrics:
# Confusion Matrix :
cm = confusion_matrix(y_test, y_pred)
print("\nConfusion matrix:\n-----------------")
print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in cm]))

print("\n====================\n")
print("Metrics:\n--------")
accuracy        =  accuracy_score(y_test, y_pred)
recall_score    =    recall_score(y_test, y_pred)
precision_score = precision_score(y_test, y_pred)
f1_score        =        f1_score(y_test, y_pred)

print("The model's accuracy is  {}%".format(round(accuracy       *100,3)))
print("The model's recall is    {}%".format(round(recall_score   *100,3)))
print("The model's precision is {}%".format(round(precision_score*100,3)))
print("The model's f1-score is  {}%".format(round(f1_score       *100,3)))

# Author: Kunal Nain

from keras.models import Sequential
from keras.layers import Dense
import json
import os
from sklearn.model_selection import train_test_split
import numpy as np

# Opening the output.json file which contains the data
os.chdir('..')
filepath = os.getcwd()
filepath = filepath + "/data/output.json"
f = open(filepath, "r")

# Loading the data
json_data = json.loads(f.read())

# Creating the lists to hold the training and testing data
X = []
y = []

# Populating the lists
for data_object in json_data:
    X.append([data_object['pr_status_check'], data_object['pr_user_type'], data_object['pr_user_contr'], data_object['pr_comment_count'], data_object['pr_time_duration']])
    y.append(data_object['pr_is_merged'])

# Converting the python lists to Numpy array
X = np.asarray(X)
y = np.asarray(y)

# Using Scikit Learn, splitting the training and testing data
X_train, X_test, y_train, y_test = train_test_split(X, y)

# Neural network with two layer
model = Sequential()
# This is the first input layer
model.add(Dense(5, input_shape=(5,)))
# This is the second layer which is uses a sigmoid activation function
model.add(Dense(1, activation='sigmoid'))
# Training the neural network
model.compile(optimizer='rmsprop', loss='binary_crossentropy', metrics=['accuracy'])
model.fit(X_train, y_train)
score = model.evaluate(X_test, y_test)
print("Score = ", score[0])
print("Accuracy = ", score[1])

from keras.models import Sequential
from keras.layers import Dense
import json
import os
from sklearn.model_selection import train_test_split
import numpy as np

os.chdir('..')
filepath = os.getcwd()
filepath = filepath + "/data/output.json"
f = open(filepath, "r")

json_data = json.loads(f.read())

X = []
y = []

for data_object in json_data:
    X.append([data_object['pr_status_check'], data_object['pr_user_type'], data_object['pr_user_contr'], data_object['pr_comment_count'], data_object['pr_time_duration']])
    y.append(data_object['pr_is_merged'])

X = np.asarray(X)
y = np.asarray(y)

X_train, X_test, y_train, y_test = train_test_split(X, y)

model = Sequential()
model.add(Dense(5, input_shape=(5,)))
model.add(Dense(1, activation='sigmoid'))
model.compile(optimizer='rmsprop', loss='binary_crossentropy', metrics=['accuracy'])
model.fit(X_train, y_train)
score = model.evaluate(X_test, y_test)
print("Score = ", score[0])
print("Accuracy = ", score[1])

import numpy as np
import json
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import os

# filepath = os.path.dirname(__file__)
os.chdir('..')
filepath = os.getcwd()
filepath = filepath + "/data/output.json"
f = open(filepath, "r")

json_data = json.loads(f.read())

x = []
y = []

for data_object in json_data:
    x.append(data_object['pr_status_check'])
    y.append(data_object['pr_is_merged'])

x_array = np.array(x)
y_array = np.array(y)

x_array = x_array.reshape(-1, 1)
y_array = y_array.reshape(-1, 1)

reg = LinearRegression().fit(x_array, y_array)
print("Score = ", reg.score(x_array, y_array))

plt.scatter(x_array, y_array)
plt.xlabel('PR Status Check')
plt.ylabel('PR Is Merged')
plt.title('Correlation')
plt.show()

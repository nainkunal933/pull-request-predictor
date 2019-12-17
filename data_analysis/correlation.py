import numpy as np
import json
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import os

os.chdir('..')
filepath = os.getcwd()
filepath = filepath + "/data/output.json"
f = open(filepath, "r")

json_data = json.loads(f.read())

x_status_check = []
x_user_type = []
x_user_contr = []
x_comment_count = []
x_time_duration = []
y = []

for data_object in json_data:
    x_status_check.append(data_object['pr_status_check'])
    x_user_type.append(data_object['pr_user_type'])
    x_user_contr.append(data_object['pr_user_contr'])
    x_comment_count.append(data_object['pr_comment_count'])
    x_time_duration.append(data_object['pr_time_duration'])
    y.append(data_object['pr_is_merged'])

x_array_status_check = np.array(x_status_check)
x_array_user_type = np.array(x_user_type)
x_array_user_contr = np.array(x_user_contr)
x_array_comment_count = np.array(x_comment_count)
x_array_time_duration = np.array(x_time_duration)

y_array = np.array(y)

x_array_status_check = x_array_status_check.reshape(-1, 1)
x_array_user_type = x_array_user_type.reshape(-1, 1)
x_array_user_contr = x_array_user_contr.reshape(-1, 1)
x_array_comment_count = x_array_comment_count.reshape(-1, 1)
x_array_time_duration = x_array_time_duration.reshape(-1, 1)

y_array = y_array.reshape(-1, 1)

reg_status_check = LinearRegression().fit(x_array_status_check, y_array)
reg_user_type = LinearRegression().fit(x_array_user_type, y_array)
reg_user_contr = LinearRegression().fit(x_array_user_contr, y_array)
reg_comment_count = LinearRegression().fit(x_array_comment_count, y_array)
reg_time_duration = LinearRegression().fit(x_array_time_duration, y_array)

print("PR Status Check Score = ", reg_status_check.score(x_array_status_check, y_array))
print("PR User Type Score = ", reg_user_type.score(x_array_user_type, y_array))
print("PR User Contribution Score = ", reg_user_contr.score(x_array_user_contr, y_array))
print("PR Comment Count Score = ", reg_comment_count.score(x_array_comment_count, y_array))
print("PR Time Duration Score = ", reg_time_duration.score(x_array_time_duration, y_array))

plt.scatter(x_array_status_check, y_array)
plt.xlabel('PR Status Check')
plt.ylabel('PR Is Merged')
plt.title('Correlation')
plt.show()

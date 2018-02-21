import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# import Data set

dataset = pd.read_csv('Salary_Data.csv')


#Getting Years as x ( independent), Salary as Y (Dependent)
x = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 1].values

# splitting data set into training and test set with test set = 1/3
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size= 1/3,random_state=0)

# fit simple linear regression into training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(x_train,y_train)

# predict the result (salary) from training set
y_predict = regressor.predict(x_test)

# The predicted Salary by model
# print(y_predict)
# The real salary
# print(y)

#Only the points changes, not the regression line
# plotting the training set result
plt.scatter(x_train,y_train , color = 'red')
#plotting the prediction result based on training set
plt.plot(x_train,regressor.predict(x_train), color = 'blue')
plt.title("Salary based on Year of Experience(Training)")
plt.xlabel("Year of Experience")
plt.ylabel("Salary")
plt.show()


# plotting the test set result
plt.scatter(x_test,y_test , color = 'red')
#plotting the prediction result based on test set
plt.plot(x_train,regressor.predict(x_train), color = 'blue')
plt.title("Salary based on Year of Experience(Test)")
plt.xlabel("Year of Experience")
plt.ylabel("Salary")
plt.show()
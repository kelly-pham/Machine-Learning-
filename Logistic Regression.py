import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#import data set
dataset = pd.read_csv('Social_Network_Ads.csv')
print(dataset.head())

#Create matrix for independent variables (Age and Estimated Salary)
x = dataset.iloc[:,[2,3]].values

#Create matrix for dependent variables (Purchased)
y = dataset.iloc[:, 4].values

#splitting dataset into training and test set
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=1/4,random_state=0)

#Scailing ( Age and Salary)
from sklearn.preprocessing import StandardScaler
x_scale = StandardScaler()
x_train = x_scale.fit_transform(x_train)
x_test = x_scale.transform(x_test)

#Fitting Logistic Regression into Training set
from sklearn.linear_model import LogisticRegression
classifier  = LogisticRegression()
classifier.fit(x_train,y_train)

#Predict the new value in Test set
y_predict = classifier.predict(x_test)

# Making a confusion matrix
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test,y_predict)

#Plotting Logistic Regression in Training Set
from matplotlib.colors import ListedColormap

# Import necessary libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# import data set
dataset = pd.read_csv("Data.csv")


# Create matrix for independent variable including Country, Age, Salary
X = dataset.iloc[:,:-1].values

#Create for dependent variable: Purchase
Y = dataset.iloc[:,3].values

# Filling missing data

from sklearn.preprocessing import Imputer
imputer = Imputer(missing_values ='Nan',strategy ='mean',axis=0)
imputer = imputer.fit(X[:,1:3])
X[:, 1:3] = imputer.fit_transform(X[:,1:3])

#Categorical data
from sklearn.preprocessing import LabelEncoder,OneHotEncoder
label_encoderX = LabelEncoder()

# divide spain, Germany and Frace into number to fit it equation ( 0,1,2)
X[:,0] =label_encoderX.fit_transform(X[:,0])
# print(X[:,0])

# create dummy variable ( 3 columns )
onehotencoder = OneHotEncoder(categorical_features= [0])
X = onehotencoder.fit_transform(X).toarray()


#create dummy variable for Purchase
label_encoderY = LabelEncoder()
Y =label_encoderX.fit_transform(Y)

#Splitting dataset into Test and Training
from sklearn.model_selection import train_test_split
X_train, X_test,Y_train,Y_test = train_test_split(X,Y,test_size=0.25
                                                , random_state= 5)    #Test set will have 25 % of data set
#Feature Scailing

from sklearn.preprocessing import StandardScaler
scale_X = StandardScaler()
X_train = scale_X.fit_transform(X_train)
X_test = scale_X.transform(X_test)    # not fit on test set

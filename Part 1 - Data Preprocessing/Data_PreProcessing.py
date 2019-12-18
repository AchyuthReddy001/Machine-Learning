#importing lib
import pandas as pd
import numpy as ny
import matplotlib.pyplot as plt

#importing dataset
data=pd.read_csv("Data.csv")
X=data.iloc[:,:-1]
y=data.iloc[:,-1:]

#taking care of missing data
from sklearn.preprocessing import Imputer
imputer=Imputer(missing_values=ny.nan,strategy="mean",axis=0)
imputer=imputer.fit(X.iloc[:,1:3])
X.iloc[:,1:3]=imputer.transform(X.iloc[:,1:3])

#categorical data
from sklearn.preprocessing import LabelEncoder,OneHotEncoder
lab_X=LabelEncoder()
X.iloc[:,0]=lab_X.fit_transform(X.iloc[:,0])
onehot=OneHotEncoder(categorical_features=[0])
X=onehot.fit_transform(X).toarray()

#splitting data into train and test sets
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.25,random_state=0)

#feature scaling
from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
X_train=sc.fit_transform(X_train)
X_test=sc.transform(X_test)
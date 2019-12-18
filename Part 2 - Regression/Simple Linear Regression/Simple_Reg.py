#importing Lib
import pandas as pd
import numpy as ny
import matplotlib.pyplot as plt

#importing data 
data=pd.read_csv("Salary_Data.csv")
X=data.iloc[:,:-1]
y=data.iloc[:,1:]

#splitting train and testset
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.25,random_state=0)

#model building
from sklearn.linear_model import LinearRegression
reg=LinearRegression()
reg.fit(X_train,y_train)

#prediction on test set
y_pred=reg.predict(X_test)

#visualising the training data
plt.scatter(X_train,y_train,color='red')
plt.plot(X_train,reg.predict(X_train),color="blue")
plt.title("Sal vs Yrs Exp(trainset)")
plt.ylabel("Salary")
plt.xlabel("Years Of Exp")
plt.show()

#visualising the test data
plt.scatter(X_test,y_test,color='red')
plt.plot(X_test,reg.predict(X_test),color="blue")
plt.title("Sal vs Yrs Exp(testset)")
plt.ylabel("Salary")
plt.xlabel("Years Of Exp")
plt.show()
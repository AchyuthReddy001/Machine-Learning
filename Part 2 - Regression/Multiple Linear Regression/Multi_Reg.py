#import libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#importing data 
data=pd.read_csv("50_Startups.csv")
X=data.iloc[:,:-1]
y=data.iloc[:,-1]

#categorical data
from sklearn.preprocessing import LabelEncoder,OneHotEncoder
lab_enc=LabelEncoder()
X.iloc[:,3]=lab_enc.fit_transform(X.iloc[:,3])
one_hot=OneHotEncoder(categorical_features=[3])
X=one_hot.fit_transform(X).toarray()

#dummy variable trap
X=X[:,1:]

#feature scaling
from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
X=sc.fit_transform(X)

#splitting data into train and test set
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.25)

#model building
from sklearn.linear_model import LinearRegression
reg=LinearRegression()
reg.fit(X_train,y_train)

#prediction on test set
y_pred=reg.predict(X_test)


#back elimination
import statsmodels.formula.api as sf
X=np.append(arr=np.ones((50,1)).astype(int),values=X,axis=1)
X_opt=X[:,[0,1,2,3,4,5]]
reg_ols=sf.OLS(endog=y,exog=X_opt).fit()
reg_ols.summary()
X_opt=X[:,[0,1,2,3,5]]
reg_ols=sf.OLS(endog=y,exog=X_opt).fit()
reg_ols.summary()
X_opt=X[:,[0,1,2,5]]
reg_ols=sf.OLS(endog=y,exog=X_opt).fit()
reg_ols.summary()

#model build after elimination
X=X[:,[1,2,5]]

#feature scaling
from sklearn.preprocessing import StandardScaler
sc=StandardScaler()
X=sc.fit_transform(X)

#splitting data into train and test set
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.25)

#model building
from sklearn.linear_model import LinearRegression
reg=LinearRegression()
reg.fit(X_train,y_train)

#prediction on test set
y_pred_elim=reg.predict(X_test)
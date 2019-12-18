#importing libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#importing dataset
data=pd.read_csv("Position_Salaries.csv")
X=data.iloc[:,1:2].values
y=data.iloc[:,2].values


#LinerReg model building
from sklearn.linear_model import LinearRegression
lin_reg=LinearRegression()
lin_reg.fit(X,y)

#BUilding a polynomial Reg model
from sklearn.preprocessing import PolynomialFeatures
ploy_fea=PolynomialFeatures(degree=4)
X_ply=ploy_fea.fit_transform(X)
poly_reg=LinearRegression()
poly_reg.fit(X_ply,y)

#visualising the data in both liner and polynomial
X_grid=np.arange(min(X),max(X),0.1)
X_grid=X_grid.reshape(len(X_grid),1)

plt.scatter(X,y,color="red")
plt.plot(X,lin_reg.predict(X),color="blue")
plt.plot(X_grid,poly_reg.predict(ploy_fea.fit_transform(X_grid)),color="black")
plt.title("Salary Detect")
plt.xlabel("Years Of Exp")
plt.ylabel("Salary")


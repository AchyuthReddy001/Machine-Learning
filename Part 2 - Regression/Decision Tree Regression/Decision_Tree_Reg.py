#import packages
import pandas as pd
import numpy as ny
import matplotlib.pyplot as plt

#import data set
data=pd.read_csv("Position_Salaries.csv")
X=data.iloc[:, 1:2].values
y=data.iloc[:, 2].values

#model devlop
from sklearn.tree import DecisionTreeRegressor
reg=DecisionTreeRegressor(random_state=0)
reg.fit(X,y)

#model prediction
y_pred=reg.predict(6.5)

#visu
X_grid=ny.arange(min(X),max(X),0.1)
X_grid=X_grid.reshape((len(X_grid),1))
plt.scatter(X,y,color="red")
plt.plot(X_grid,reg.predict(X_grid),color='green')
plt.title("D.T.Regressor")
plt.xlabel("Position")
plt.ylabel("Salary")
plt.show()

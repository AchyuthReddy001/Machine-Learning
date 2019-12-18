#importing packages
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#importing data

data=pd.read_csv("Position_Salaries.csv")
X=data.iloc[:,1:2].values
y=data.iloc[:, 2].values

#building the model
from sklearn.ensemble import RandomForestRegressor
req=RandomForestRegressor(n_estimators=10,random_state=0)
req.fit(X,y)

#prediction
y_prid=req.predict(6.5)

#visu
X_grid=np.arange(min(X),max(X),0.01)
X_grid=X_grid.reshape((len(X_grid),1))
plt.scatter(X,y,color="red")
plt.plot(X_grid,req.predict(X_grid),color='green')
plt.title("D.T.Regressor")
plt.xlabel("Position")
plt.ylabel("Salary")
plt.show()

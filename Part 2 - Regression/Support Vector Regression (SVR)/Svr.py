#importing librar
import pandas as pd
import numpy as ny
import matplotlib.pyplot as plt

#importing dataset
data=pd.read_csv("Position_Salaries.csv")
X=data.iloc[:,1:2]
y=data.iloc[:,2:]

#feature scaling
from sklearn.preprocessing import StandardScaler
sc_X=StandardScaler()
sc_y=StandardScaler()
X=sc_X.fit_transform(X)
y=sc_y.fit_transform(y)

#build the model
from sklearn.svm import SVR
reg=SVR(kernel="rbf")
reg.fit(X,y)

#prediction on particular value
y_pred=sc_y.inverse_transform(reg.predict(sc_X.transform(ny.array([[6.5]]))))


#visualising the model
plt.scatter(X,y,color="black")
plt.plot(X,reg.predict(X),color="red")
plt.title("Salary Detect(SVR)")
plt.xlabel("Exper")
plt.ylabel("Salary")
plt.show()
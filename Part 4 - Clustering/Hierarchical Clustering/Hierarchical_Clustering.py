#importing packages
import pandas as pd
import matplotlib.pyplot as plt

#importing dataset
data=pd.read_csv("E:/MY_GOAL/Machine Learning/Part 4 - Clustering/Section 25 - Hierarchical Clustering/Mall_Customers.csv")
X=data.iloc[:,[3,4]].values


#using dendrograms to find number of clusters
import scipy.cluster.hierarchy as sch
dendro=sch.dendrogram(sch.linkage(X,method='ward'))
plt.title("DendroGrams")
plt.xlabel("Customers")
plt.ylabel("Euclidean Dist")
plt.show()

#BUild HC model
from sklearn.cluster import AgglomerativeClustering
A_hc=AgglomerativeClustering(n_clusters=5,affinity="euclidean",linkage="ward")
y_hc=A_hc.fit_predict(X)

#visualising the clusters
plt.scatter(X[y_hc ==0,0],X[y_hc==0,1],s=100,c='red',label='C1')
plt.scatter(X[y_hc ==1,0],X[y_hc==1,1],s=100,c='green',label='C2')
plt.scatter(X[y_hc ==2,0],X[y_hc==2,1],s=100,c='blue',label='C3')
plt.scatter(X[y_hc ==3,0],X[y_hc==3,1],s=100,c='orange',label='C4')
plt.scatter(X[y_hc ==4,0],X[y_hc==4,1],s=100,c='yellow',label='C5')
plt.xlabel("Annual Income")
plt.ylabel("Age")
plt.title("Cluster Of Customers")
plt.show()
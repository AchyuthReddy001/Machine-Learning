#import lib
import pandas as pd
import matplotlib.pyplot as plt
import numpy as ny

#import dataset
dataset =pd.read_csv("E:\\MY_GOAL\\Machine Learning\\Part 4 - Clustering\\Section 24 - K-Means Clustering\\Mall_Customers.csv")
X=dataset.iloc[:,[3,4]].values

#using elbow method
from sklearn.cluster import KMeans
wcss=[]
for i in range(1,11):
    kmeans=KMeans(n_clusters=i,init='k-means++',max_iter=300,n_init=10,random_state=0)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)
plt.plot(range(1,11),wcss)
plt.title("Elbow Method")
plt.xlabel("No Of Clusters")
plt.ylabel("WCSS")
plt.show()    


#Build the kmeans cluster
kmeans=KMeans(n_clusters=5,init='k-means++',max_iter=300,n_init=10,random_state=0)
y_kmeans=kmeans.fit_predict(X)

#visualising the clusters
plt.scatter(X[y_kmeans ==0,0],X[y_kmeans==0,1],s=100,c='red',label='C1')
plt.scatter(X[y_kmeans ==1,0],X[y_kmeans==1,1],s=100,c='green',label='C2')
plt.scatter(X[y_kmeans ==2,0],X[y_kmeans==2,1],s=100,c='blue',label='C3')
plt.scatter(X[y_kmeans ==3,0],X[y_kmeans==3,1],s=100,c='orange',label='C4')
plt.scatter(X[y_kmeans ==4,0],X[y_kmeans==4,1],s=100,c='yellow',label='C5')
plt.scatter(kmeans.cluster_centers_[:,0],kmeans.cluster_centers_[:,1],s=300,c='black',label='Centroid')
plt.xlabel("Annual Income")
plt.ylabel("Age")
plt.title("Cluster Of Customers")
plt.show()
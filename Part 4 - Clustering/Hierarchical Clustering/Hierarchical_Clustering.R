#import data
data=read.csv("Mall_Customers.csv")
X=data[,4:5]

#Finding no of clusters using dendrograms
dendro=hclust(dist(X,method="euclidean"),method = 'ward.D')
plot(dendro,
     main = paste("DendroGrams"),
     xlab = "Customers",
     ylab = "Euclidean Distance")

#Build the model
hc=hclust(dist(X,method="euclidean"),method = 'ward.D')
y_hc=cutree(hc,5)

#visualising the clusters
library(cluster)
clusplot(X,
         y_hc,
         lines=0,
         shade=TRUE,
         color=TRUE,
         labels=2,
         plotchar=FALSE,
         span=TRUE,
         main=paste("KMeans Cluster Alg"),
         xlab="Annaul Income",
         ylab="SpendingScore")
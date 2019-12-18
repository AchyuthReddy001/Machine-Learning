#import data
data=read.csv("Mall_Customers.csv")
X=data[,4:5]

#Using ElBow method
set.seed(6)
wcss=vector()
for (i in 1:10) wcss[i]=sum(kmeans(X,i)$withinss)
plot(1:10,wcss,type='b',main=paste("Elbow Method"),xlab = "No oF Clusters",
     ylab = "WCSS")

#model build
set.seed(22)
km=kmeans(X,5,iter.max = 300,nstart = 10)

#visualising the clusters
library(cluster)
clusplot(X,
         km$cluster,
         lines=0,
         shade=TRUE,
         color=TRUE,
         labels=2,
         plotchar=FALSE,
         span=TRUE,
         main=paste("KMeans Cluster Alg"),
         xlab="Annaul Income",
         ylab="SpendingScore")
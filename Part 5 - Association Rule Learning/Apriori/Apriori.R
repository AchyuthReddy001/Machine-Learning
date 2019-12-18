#Data Preprocessing
dataset=read.csv("Market_Basket_Optimisation.csv",header = FALSE)

#install.packages('arules')
library(arules)
dataset=read.transactions("Market_Basket_Optimisation.csv",sep = ",",
                          rm.duplicates = TRUE)
summary(dataset)
itemFrequencyPlot(dataset,topN=10)

#train the model
rules=apriori(data = dataset,parameter = list(support=0.005, confidence=0.2))

#visualize
inspect(sort(rules,by='lift')[0:10])
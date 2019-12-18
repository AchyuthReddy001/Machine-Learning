#installing packages
install.packages("caTools")
library(caTools)

#importing datasets
data=read.csv("Data.csv")

#Missing values
data$Age=ifelse(is.na(data$Age),
                ave(data$Age,FUN = function(x) mean(x,na.rm = TRUE)),
                data$Age)
data$Salary=ifelse(is.na(data$Salary),
                   ave(data$Salary,FUN = function(x) mean(x,na.rm = TRUE)),
                   data$Salary)

#Categorical Data
data$Country=factor(data$Country,
                    levels = c('France','Spain','Germany'),
                    labels = c(1,2,3))

data$Purchased=factor(data$Purchased,
                      levels = c('No','Yes'),
                      labels = c(0,1))

#splitting data in to train and test sets
set.seed(123)
Split=sample.split(data$Purchased,SplitRatio = 0.8)
train_set=subset(data,Split==TRUE)
test_set=subset(data,Split==FALSE)

#feature Scaling
train_set[2:3]=scale(train_set[2:3])
test_set[2:3]=scale(test_set[2:3])


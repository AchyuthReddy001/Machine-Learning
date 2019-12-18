#importing packages
install.packages("caTools")
library(caTools)

#importing Dataset
data=read.csv("50_Startups.csv")

#categorical data
data$State=factor(data$State,levels  = c("New York","California","Florida"),
            labels = c(1,2,3))

#splitting data into train and test sets
set.seed(123)
values=sample.split(data$Profit,SplitRatio = 0.8)
train_set=subset(data,values==TRUE)
test_set=subset(data,values==FALSE)

#build the model back propagation
reg=lm(formula = Profit ~ R.D.Spend + Administration + 
         Marketing.Spend + State,data = data)
summary(reg)

reg=lm(formula = Profit ~ R.D.Spend + Administration + 
         Marketing.Spend,data = data)
summary(reg)
            
reg=lm(formula = Profit ~ R.D.Spend  + 
         Marketing.Spend,data = data)
summary(reg)

reg=lm(formula = Profit ~ R.D.Spend  ,data = data)
summary(reg)

y_pred



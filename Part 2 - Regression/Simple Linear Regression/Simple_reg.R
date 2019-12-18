#importing data
data=read.csv("Salary_Data.csv")

#splitting train and test set
library(caTools)
Split=sample.split(data$Salary,SplitRatio = 0.75)
train_set=subset(data,Split==TRUE)
test_set=subset(data,Split==FALSE)

#model building
reg=lm(formula =Salary ~ YearsExperience,data = train_set)
summary(reg)

#prediction
y_pred=predict(reg,newdata = test_set)

#visualising data
install.packages("ggplot2")
library(ggplot2)

#on traing data
ggplot()+
  geom_point(aes(train_set$YearsExperience,train_set$Salary),colour="red")+
  geom_line(aes(train_set$YearsExperience,predict(reg,newdata=train_set)),
            colour="blue")+
  ggtitle("Sal vs Exp(traingSet")+
  xlab("Years of Expr")+
  ylab("Salary")

#on test set
ggplot()+
  geom_point(aes(test_set$YearsExperience,test_set$Salary),colour="blue")+
  geom_line(aes(train_set$YearsExperience,predict(reg,newdata=train_set)),
             colour="red")+
  ggtitle("Sal vs Exp(testSet")+
  xlab("Years of Expr")+
  ylab("Salary")
              





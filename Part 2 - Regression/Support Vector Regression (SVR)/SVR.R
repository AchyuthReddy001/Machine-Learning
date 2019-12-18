#importing dataset
data=read.csv("Position_Salaries.csv")
data=data[2:3]

#installing lib
install.packages("e1071")
library("e1071")

#building the model
reg=svm(formula=Salary ~ .,data = data,
        type="eps-regression")


#predicting
y_pred=predict(reg,newdata = data.frame(Level=6.5))

#visualising the data
library(ggplot2)
ggplot()+
  geom_point(aes(x=data$Level,y=data$Salary),color="blue")+
  geom_line(aes(x=data$Level,y=predict(reg,newdata = data)),color="black")+
  ggtitle("Sal vs Exp using SVR")+
  xlab("Exp")+
  ylab("Salary")




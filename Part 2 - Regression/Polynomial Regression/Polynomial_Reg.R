#importing dataset
data=read.csv("Position_Salaries.csv")
data=data[2:3]

#building linear model
lin_reg=lm(formula=Salary ~ .,data = data)

#building a polynomial reg
data$Level2=data$Level^2
data$Level3=data$Level^3
data$Level4=data$Level^4

ploy_reg=lm(formula = Salary ~ .,data=data)

#visualising the data
library(ggplot2)

ggplot()+
  geom_point(aes(x=data$Level,y=data$Salary),color="blue")+
  geom_line(aes(x=data$Level,y=predict(lin_reg,newdata = data)),color="red")+
  geom_line(aes(x=data$Level,y=predict(ploy_reg,newdata = data)),color="green")+
  ggtitle("Salary Detect")+
  xlab("Expericence")+
  ylab("Salary")
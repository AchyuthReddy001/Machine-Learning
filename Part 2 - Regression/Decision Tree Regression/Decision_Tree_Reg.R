#importing dataset
data=read.csv("Position_Salaries.csv")
data=data[2:3]



#importing req pack
install.packages("rpart")
library("rpart")

#dev model
req=rpart(formula = Salary ~ .,
          data=data,control = rpart.control(minsplit = 1))

#prediction
y_pred=predict(req,data.frame(Level=6.5))

#visualising model
library("ggplot2")
X_grid=seq(min(data$Level),max(data$Level),0.01)
ggplot()+
  geom_point(aes(x=data$Level,y=data$Salary),color="blue")+
  geom_line(aes(x=X_grid,y=predict(req,newdata = data.frame(Level=X_grid))),color="black")+
  ggtitle("Sal vs Exp using DecsionTreeRegression")+
  xlab("Exp")+
  ylab("Salary")



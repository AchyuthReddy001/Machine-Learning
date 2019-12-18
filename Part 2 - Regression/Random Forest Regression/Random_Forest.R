#importing data to r inv
data=read.csv("Position_Salaries.csv")
dataset=data[2:3]

#importing lib
install.packages("randomForest")
library("randomForest")
req=randomForest(x=dataset[1],
                 y=dataset$Salary,
                 ntree = 500)
#prediction
y_pred=predict(req,data.frame(Level=6.5))

#visualising
library("ggplot2")
X_grid=seq(min(dataset$Level),max(dataset$Level),0.1)
ggplot()+
  geom_point(aes(x=dataset$Level,y=dataset$Salary),
             color='red')+
  geom_line(aes(x=X_grid,y=predict(req,newdata = data.frame(Level=X_grid))),
            color="blue")+
  ggtitle("RandomForestReg")+
  xlab("Position")+
  ylab("Salary")
#importingdata
data=read.csv("Social_Network_Ads.csv")
dataset=data[,3:5]

#splitting data
set.seed(123)
library(caTools)
split=sample.split(dataset$Purchased,SplitRatio = 0.75)
train_set=subset(dataset,split==TRUE)
test_set=subset(dataset,split==FALSE)

#feature scale
train_set[,1:2]=scale(train_set[,1:2])
test_set[,1:2]=scale(test_set[,1:2])

#build the model and test the model
install.packages('e1071')
library(e1071)
classifier=svm(formula=Purchased ~ .,
               data=train_set,
               type='C-classification',
               kernel = 'linear')
#prediction
y_pred=predict(classifier,newdata =test_set[-3])

#confusion matrix
cm=table(test_set[,3],y_pred)


# Visualising the Training set results
#install.packages('ElemStatLearn')
library(ElemStatLearn)
set = train_set
X1 = seq(min(set[, 1]) - 1, max(set[, 1]) + 1, by = 0.01)
X2 = seq(min(set[, 2]) - 1, max(set[, 2]) + 1, by = 0.01)
grid_set = expand.grid(X1, X2)
colnames(grid_set) = c('Age', 'EstimatedSalary')

y_grid = predict(classifier,newdata = grid_set)
plot(set[, -3],
     main = 'SVM (Training set)',
     xlab = 'Age', ylab = 'Estimated Salary',
     xlim = range(X1), ylim = range(X2))
contour(X1, X2, matrix(as.numeric(y_grid), length(X1), length(X2)), add = TRUE)
points(grid_set, pch = '.', col = ifelse(y_grid == 1, 'springgreen3', 'tomato'))
points(set, pch = 21, bg = ifelse(set[, 3] == 1, 'green4', 'red3'))

# Visualising the Test set results
library(ElemStatLearn)
set = test_set
X1 = seq(min(set[, 1]) - 1, max(set[, 1]) + 1, by = 0.01)
X2 = seq(min(set[, 2]) - 1, max(set[, 2]) + 1, by = 0.01)
grid_set = expand.grid(X1, X2)
colnames(grid_set) = c('Age', 'EstimatedSalary')

y_grid =predict(classifier,newdata = grid_set)
plot(set[, -3],
     main = 'SVM (Test set)',
     xlab = 'Age', ylab = 'Estimated Salary',
     xlim = range(X1), ylim = range(X2))
contour(X1, X2, matrix(as.numeric(y_grid), length(X1), length(X2)), add = TRUE)
points(grid_set, pch = '.', col = ifelse(y_grid == 1, 'springgreen3', 'tomato'))
points(set, pch = 21, bg = ifelse(set[, 3] == 1, 'green4', 'red3'))



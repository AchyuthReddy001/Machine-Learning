#import data
dataset_ori=read.delim("Restaurant_Reviews.tsv",quote = "",stringsAsFactors = FALSE)

#datacleaning
# install.packages('NLP')
library(tm)
corpus=VCorpus(VectorSource(dataset_ori$Review))
corpus=tm_map(corpus,content_transformer(tolower))
corpus=tm_map(corpus,removeNumbers)
corpus=tm_map(corpus,removePunctuation)

#install.packages("SnowballC")
library(SnowballC)
corpus=tm_map(corpus,removeWords,stopwords())
corpus=tm_map(corpus,stemDocument)
corpus=tm_map(corpus,stripWhitespace)

#create a bag of words
dtm=DocumentTermMatrix(corpus)
dtm=removeSparseTerms(dtm,0.999)

#dataset
dataset=as.data.frame(as.matrix(dtm))
dataset$liked=dataset_ori$Liked

#encoding target var
dataset$liked=factor(dataset$liked,levels = c(0,1))

#splitting data
set.seed(123)
library(caTools)
split=sample.split(dataset$liked,SplitRatio = 0.80)
train_set=subset(dataset,split==TRUE)
test_set=subset(dataset,split==FALSE)



#build the model and test the model
#install.packages('randomForest')
library(randomForest)
classifier=randomForest(x=train_set[-692],
                        y=train_set$liked,
                        ntree = 10)
#prediction
y_pred=predict(classifier,newdata =test_set[-692])
y_pred = ifelse(prob_pred > 0.5, 1, 0)
#confusion matrix
cm=table(test_set[,692],y_pred)

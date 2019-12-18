#importing lib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re
import nltk
from sklearn.feature_extraction.text import  CountVectorizer
#nltk.download("stopwords")
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from sklearn.metrics import confusion_matrix
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split

#importing dataset
dataset=pd.read_csv('Restaurant_Reviews.tsv',delimiter="\t",quoting=3)

#cleaning
corpus=[]
ps=PorterStemmer()
for i in range (1000):
    review = re.sub("[^a-zA-Z]", " ", dataset["Review"][i])
    review=review.lower()
    review=review.split()
    review= [ps.stem(word) for word in review if not word in set(stopwords.words('english'))]
    review=" ".join(review)
    corpus.append(review)

#create bag of words
cv=CountVectorizer()
X=cv.fit_transform(corpus).toarray()
y = dataset.iloc[:, 1].values

# Splitting the dataset into the Training set and Test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20, random_state = 0)

# Fitting Naive Bayes to the Training set
classifier = GaussianNB()
classifier.fit(X_train, y_train)

# Predicting the Test set results
y_pred = classifier.predict(X_test)

# Making the Confusion Matrix
cm = confusion_matrix(y_test, y_pred)
print(cm)
#import lib

import pandas as pd
import numpy as ny
import matplotlib.pyplot as plt

#importing dataset
dataset=pd.read_csv("E:\\MY_GOAL\\Machine Learning\\Part 5 - Association Rule Learning\\Section 28 - Apriori\\Market_Basket_Optimisation.csv",header=None)
trans=[]
for i in range(0,7501):
       trans.append([str(dataset.values[i,j])for j in range(0,20)])
       
#train the model
from apyori import apriori 
rules=apriori(trans,min_support=0.005,min_confidence=0.2,min_lift=3,min_length=2)

#visualize
res=list(rules)
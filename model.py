import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle

df=pd.read_csv('diabetes.csv')

X=df.iloc[:,:-1] # independent variables
Y=df.iloc[:,-1] # target variable 

X_train,X_test,y_train,y_test=train_test_split(X,Y,test_size=0.3,random_state=0) 
# 70% train, 30% test. 

classifier=RandomForestClassifier()
classifier.fit(X_train,y_train)

y_pred=classifier.predict(X_test)

from sklearn.metrics import accuracy_score
score=accuracy_score(y_test,y_pred)

print('Score is',score)

pickle.dump(classifier, open('model.pkl','wb'))

print(classifier.predict([[2,3,4,1]]))
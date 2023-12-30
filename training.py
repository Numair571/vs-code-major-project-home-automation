import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
import pickle

data=pd.read_csv('guesture.csv')
x=data.iloc[:,:-1].values
y=data.iloc[:,-1].values

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2)
classifier=KNeighborsClassifier()
classifier.fit(x_train,y_train)

y_pred=classifier.predict(x_test)
print(accuracy_score(y_pred,y_test))
model=open('model.pkl','wb')
pickle.dump(classifier,model)
model.close()
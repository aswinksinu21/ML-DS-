from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score
from sklearn.datasets import load_breast_cancer
data=load_breast_cancer()
x=data.data
y=data.target
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2, random_state=42)
nb=GaussianNB()
nb.fit(x_train,y_train)
print(nb.predict(x_test))
v=nb.predict(x_test)
result=accuracy_score(y_test,v)
print("Accuracy::",result)
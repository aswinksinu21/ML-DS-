from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
from sklearn.metrics import accuracy_score
iris=load_iris()
x=iris.data # features
y=iris.target # target variable # for reproducability
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=42)
knn=KNeighborsClassifier(n_neighbors=7)
knn.fit(x_train,y_train) # trying to fit maximum data
print(knn.predict(x_test))
v=knn.predict(x_test) # result of model prediction
result=accuracy_score(y_test,v) # comparing both prediction
print("accuracy",result)

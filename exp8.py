import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
data= pd.read_csv('Salary_Data.csv')
x=data['YearsExperience'].values.reshape(-1,1)
y=data['Salary']
x_train,x_test,y_train,y_test= train_test_split(x, y, test_size=0.2, random_state=47)
sr=LinearRegression()
sr.fit(x_train,y_train)
y_pred=sr.predict(x_test)
r2=r2_score(y_test,y_pred)
print("R-squared",r2)
plt.scatter(x_test,y_test,color='black',label='Data Points')
plt.plot(x_test,y_pred, color='blue',linewidth=3, label='Regression line')
plt.xlabel('Year Of Experience')
plt.ylabel('Salary')
plt.show()

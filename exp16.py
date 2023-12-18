import tensorflow as tf
from tensorflow.keras.datasets import mnist
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense,Flatten
from tensorflow.keras.utils import to_categorical
(X_train,y_train),(X_test,y_test) = mnist.load_data()
X_train = X_train/255.0
X_test = X_test/255.0
X_train = X_train.reshape(-1,28*28)
print(X_train)
X_test=X_test.reshape(-1,28*28)
print(X_test)
y_train=to_categorical(y_train)
y_test=to_categorical(y_test)
print(y_test)
model=Sequential([
 Dense(128, activation='relu', input_shape=(28 * 28,)),
 Dense(64,activation='relu'),
 Dense(10,activation='softmax')
])
model.compile(optimizer='adam',loss='categorical_crossentropy',metrics=['accuracy'])
model.fit(X_train,y_train,epochs=5,batch_size=32,validation_split=0.2)
loss,accuracy=model.evaluate(X_test,y_test)

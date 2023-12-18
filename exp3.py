import matplotlib.pyplot as plt
categories = ["category 1","category 2","category 3",]
values = [1,2,3]
plt.bar(categories,values,color = "red")
plt.xlabel('categories')
plt.ylabel('values')
plt.title('Bar Chart')
plt.show()
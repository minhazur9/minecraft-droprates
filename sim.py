import matplotlib.pyplot as plt 
import random


x = range(1,201)
y = []
for i in x:
    y.append(random.randint(0,50))

plt.scatter(x,y)
plt.ylabel('some numbers') 
plt.show()
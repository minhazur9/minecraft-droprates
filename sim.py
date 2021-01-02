import matplotlib.pyplot as plt 
import random


def simulate(rate,iterations=100000):
    x = range(1,iterations+1)
    y = generateNumbers(rate,x)
    generatePlot(x,y)

def generateNumbers(rate,iterations):
    y = []
    for i in iterations:
        y.append(random.random())
    return y

def generatePlot(x,y):
    size = 50
    if(len(x) > 500):
        size *= 500 / len(x)
    plt.scatter(x,y,size)
    plt.ylabel('some numbers') 
    plt.show()

simulate(100)
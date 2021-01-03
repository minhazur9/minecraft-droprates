import matplotlib.pyplot as plt 
import numpy as np

def simulate(rateA,sampleA,rateB, sampleB, iterations=1000, y1label='SampleA',y2label='SampleB'):
    y1 = []
    y2 = []
    for i in range(0,iterations):  
        populationA = list(range(1,sampleA+1))
        populationB = list(range(1,sampleB+1))
        resultsA = generateNumbers(sampleA)  
        resultsB = generateNumbers(sampleB)  
        y1.append(getSuccesses(populationA,resultsA,rateA))
        y2.append(getSuccesses(populationB,resultsB,rateB))
    generatePlot(iterations,y1,y2,y1label,y2label)

def generateNumbers(sample):
    y = np.random.random(sample)
    return y

def getSuccesses(population,successes,rate):
    size = 50
    rate = rate / 100
    multiplier = int(len(population)/2)
    hits = 0
    for outcome in successes:
        if outcome <= rate:
            hits += 1
    return hits

def generatePlot(x,y1,y2,y1label,y2label):
    size = 50
    x = list(range(0,x))
    maxA = max(y1)
    maxB = max(y2)
    if(len(x) > 500):
        size *= 500 / len(x)
    plt.scatter(x,y1,s=size,label=y1label,alpha=0.65)
    plt.scatter(x,y2,s=size,label=y2label,c='red',alpha=0.65)
    plt.legend([f'Most {y1label} - {maxA}',f'Most {y2label} - {maxB}'])
    plt.show()

simulate(rateA=3.7,sampleA=262,rateB=50,sampleB=305,iterations=1000,y1label='Enderpearls',y2label="Blazerods")

import matplotlib.pyplot as plt 
import numpy as np
import pandas as pd

def simulate(rate,iterations=1000,y1label='Hits',y2label='Misses'):
    if(iterations % 2 != 0):
        iterations += 1
    x = list(range(1,iterations+1))
    y = generateNumbers(iterations)
    generatePlot(x,y,rate,y1label,y2label)

def generateNumbers(iterations):
    y = np.random.random(iterations)
    return y

def generatePlot(x,y,rate,y1label,y2label):
    size = 50
    rate = rate / 100
    multiplier = int(len(x)/2)
    outcomes = []
    hits = 0
    misses = 0
    for outcome in y:
        if outcome <= 0.047:
            outcomes.append('hit')
            hits += 1
        else:
            outcomes.append('miss')
            misses += 1
    df = pd.DataFrame(dict(x=x, y=y, label=outcomes))
    groups = df.groupby('label')
    colors = {'hit':'#2AD449', 'miss':'#FF4D4D'}
    fig, ax = plt.subplots()
    if(len(x) > 500):
        size *= 500 / len(x)
    for name, group in groups: 
        ax.scatter(group.x,group.y,s=size,label=name,c=colors[name],alpha=0.65)
    ax.legend([f'{y1label} - {hits}',f'{y2label} - {misses}'])
    plt.show()

simulate(4.7,262,'Enderpearls')
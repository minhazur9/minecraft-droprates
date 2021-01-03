import matplotlib.pyplot as plt 
import numpy as np
import pandas as pd

def simulate(rate,attempts,iterations=1000, y1label='Hits',y2label='Misses'):
    if(attempts % 2 != 0):
        attempts += 1
    for i in range(0,iterations):  
        population = list(range(1,attempts+1))
        successes = generateNumbers(attempts)  
        sampleResults(population,successes,rate)
    # generatePlot(x,y,rate,y1label,y2label)

def generateNumbers(attempts):
    y = np.random.random(attempts)
    return y

def sampleResults(population,successes,rate):
    size = 50
    rate = rate / 100
    multiplier = int(len(population)/2)
    hits = 0
    misses = 0
    for outcome in successes:
        if outcome <= rate:
            hits += 1
        else:
            misses += 1
    print(f'hits:{hits}')

def generatePlot(x,y,rate,y1label,y2label):
    # size = 50
    # rate = rate / 100
    # multiplier = int(len(x)/2)
    # outcomes = []
    # hits = 0
    # misses = 0
    # for outcome in y:
    #     if outcome <= rate:
    #         outcomes.append('hit')
    #         hits += 1
    #     else:
    #         outcomes.append('miss')
    #         misses += 1
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

simulate(4.7,262,y1label='Enderpearls')

# simulate(50,305,'Blazerods')
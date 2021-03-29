from geneticLibrary import *
from matplotlib import pyplot as plt

numItems = 3
'''
#Create items to bag
minValue = 50
maxValue = 120
minWeight = 10
maxWeight = 50
items = createItems(numItems, minValue, maxValue, minWeight, maxWeight)
'''
items = [
    [10, 20, 30],
    [60, 100, 120]
]

bagWeight = 50
numIndividual = 10
epochs = 100

population = createPopulation(numIndividual, numItems)

fitnessHistory = [ averageFitnessFunc(population,items,bagWeight), ]

for i in range(epochs):
    population = evolve(population, items, bagWeight)
    fitnessHistory.append(averageFitnessFunc(population,items,bagWeight))

for fitness in fitnessHistory:
    print(fitness)

plt.plot(range(len(fitnessHistory)), fitnessHistory)
plt.grid(True, zorder=0)
plt.title("Knapsack Problem")
plt.xlabel("Generation")
plt.ylabel("Average Fitness")
plt.show()

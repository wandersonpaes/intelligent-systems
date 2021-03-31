from geneticLibrary import *
from matplotlib import pyplot as plt

numItems = 3
'''
#Create items to knapsack automatically
minValue = 50
maxValue = 120
minWeight = 10
maxWeight = 50
items = createItems(numItems, minValue, maxValue, minWeight, maxWeight)
'''
#Create items to knapsack manually
items = [
    [10, 20, 30],
    [60, 100, 120]
]

KnapsackWeight = 50
numIndividual = 10
epochs = 100

#Create the population
population = createPopulation(numIndividual, numItems)

#Keeping the fitness average in a list for analysis
fitnessHistory = [ averageFitnessFunc(population,items,KnapsackWeight), ]

#Evolve the population by epochs
for i in range(epochs):
    population = evolve(population, items, KnapsackWeight)
    fitnessHistory.append(averageFitnessFunc(population,items,KnapsackWeight))

#Showing fitness averages over the course of evolution
for fitness in fitnessHistory:
    print(fitness)

#Showing the average fitness graph over the generations
plt.plot(range(len(fitnessHistory)), fitnessHistory)
plt.grid(True, zorder=0)
plt.title("Knapsack Problem")
plt.xlabel("Generation")
plt.ylabel("Average Fitness")
plt.show()

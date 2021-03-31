from random import randint, choices, random

#Function that creates available items with weight and value
def createItems(numItems, minValue, maxValue, minWeight, maxWeight):
    return [
        [ randint(minWeight, maxWeight) for x in range(numItems)],
        [ randint(minValue, maxValue) for y in range(numItems) ]
    ]

#Function that create a member of population
def createIndividual(length):
    return [ randint(0,1) for x in range(length) ]

#Function that create the population
def createPopulation(numIndividual, length):
    return [ createIndividual(length) for x in range(numIndividual) ]

#Function that determine the fitness of an individual. Higher is batter.
def fitnessFunc(individual, itemsToKnapsack, KnapsackWeight):
    sumWeight = 0
    sumValues = 0
    weights = itemsToKnapsack[0]
    values = itemsToKnapsack[1]
    length = len(individual)
    #For invalid individual is given a low probability to your value
    lowProbability = (sum(x for x in weights))*0.01

    for i in range(length):
        if individual[i]==1:
            sumWeight+=weights[i]
            sumValues+=values[i]

    if sumWeight <= KnapsackWeight:
        if sumWeight==0:
            return lowProbability
        else:
            return sumValues
    else:
        return lowProbability

#Function that determine average fitness for a populatiton
def averageFitnessFunc(population, itemsToKnapsack, KnapsackWeight):
    somaFitness = 0

    for elem in population:
        somaFitness+=fitnessFunc(elem, itemsToKnapsack, KnapsackWeight)

    return somaFitness/(len(population)*1.0)

#Function that evolve the population
def evolve(population, itemsToKnapsack, KnapsackWeight, mutateRate=0.01):
    #Putting individual and your fitness in a matrix,
    #column 0 is the fitness number and column 1 is the individual
    graded = [ (fitnessFunc(x,itemsToKnapsack,KnapsackWeight), x) for x in population ]
    #Fitness sum of all individual
    fitnessSum = sum(x[0] for x in graded)
    #Probability of each individual
    probabilities = [ ((100*x[0])/fitnessSum) for x in graded ]

    length=len(population)
    #Roulette selection
    #Each individual of population has a probability to be choosen
    #k individual are choosen to be parent
    parents = choices(population,probabilities,k=length)

    #Mutate some parents
    for individual in parents:
        if mutateRate > random():
            indexToMutate = randint(0, len(individual)-1)
            individual[indexToMutate] = randint(0,1)

    childrens = []
    #Crossover parents to create a children
    while len(childrens) < length:
        male = randint(0,length-1)
        female = randint(0,length-1)
        if male != female:
            male = parents[male]
            female = parents[female]
            half = len(male) // 2
            
            child = male[:half] + female[half:]
            
            childrens.append(child)

    return childrens

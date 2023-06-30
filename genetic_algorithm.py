# Import libraries
import random
import string

import numpy as np
from numpy import random as rd


# Function to generate random character sets
def random_chromosome(size):
    return "".join(
        random.choice(string.ascii_letters) for letters in range(size)
    )


# Target object
target = "banana"
# Set the population and chromosomes size, also the number of generations
population_size = 10
chromosome_size = len(target)
number_of_generations = 500
# Population list that will be fulfilled by the individuals
population_list = []
# Variable to calculate fitness of each individual
cont = 0

# Loop that calls the function random_chromosome to initialize the first population
for i in range(population_size):
    population_list.append(random_chromosome(chromosome_size))

# Print first generation
print("First generation:\n", population_list)

# Iterate until reach the number of generations set
for i in range(number_of_generations):
    # Result list that will be filled by the fitness score
    result_fitness = []

    # Calculate fitness score of each individual
    for chro in range(population_size):
        for i in range(chromosome_size):
            if population_list[chro][i] == target[i]:
                cont += 1
        result_fitness.append(cont)
        cont = 0

    # Detect where the highest fittest scores are
    not_zero = np.count_nonzero(result_fitness)
    parents_index = np.zeros(2)
    if not_zero == 0:  # if all the indiduals have zero score
        parents_index = np.array([0, 1])
    elif not_zero == 1:  # if only one individual has non zero score
        max_value = max(result_fitness)
        parents_index[0] = result_fitness.index(max_value)
        if parents_index[0] != 0:
            parents_index[1] = 0
        else:
            parents_index[1] = 1
    else:
        parents_index = np.argsort(result_fitness)[population_size - 2 :]

    parents_index = parents_index.astype("int")

    # Two parents with the highest scores
    parent_1 = population_list[parents_index[0]]
    parent_2 = population_list[parents_index[1]]

    # Crossover the parents to generate two children
    point = rd.randint(1, chromosome_size)
    children_1 = parent_1[:point] + parent_2[point:]
    children_2 = parent_2[:point] + parent_1[point:]

    # Mutation: insertion of random genes in each children
    children_1 = list(children_1)
    children_1[rd.randint(0, chromosome_size)] = random.choice(
        string.ascii_letters
    )
    children_1 = "".join(i for i in children_1)

    children_2 = list(children_2)
    children_2[rd.randint(0, chromosome_size)] = random.choice(
        string.ascii_letters
    )
    children_2 = "".join(i for i in children_2)

    # Replace individuals with the lowest scores by the new children
    population_list[np.argsort(result_fitness)[0]] = children_1
    population_list[np.argsort(result_fitness)[1]] = children_2

# Print last generation
print("\nLast generation:\n", population_list)

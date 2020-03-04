from classes import Single, Population
from evolution import Child

goal = [2,4,6,8,10]     # This value will be changed once genetic algorithm is properly implemented.

# Define the basic parameters
pop_size = 20
current_gen = 1
mut_chance = 0.05

# Generate the initial population
generation = Population(pop_size)
generation.create_pop()

# Compute fitness of initial population
generation.pop_fitness(goal)

# Begin the 'evolution' process, whereby children are made, the weak are culled, and only the strong survive
while (generation.get_fittest().fitness > 0):     

    # Sort generation in order of fittest to least fittest
    generation.sort_fittest()

    # Print out best of current generation
    print("Best Chromosome: %s \nFitness: %d \nCurrent Generation: %d" % (generation.get_fittest().combination, generation.get_fittest().fitness, current_gen))
    
    # Create new generation for population
    generation.new_generation(mut_chance)

    # Compute fitness of children
    generation.pop_fitness(goal)

    # Increment the generation counter
    current_gen += 1


print("Goal of %s reached" %goal)

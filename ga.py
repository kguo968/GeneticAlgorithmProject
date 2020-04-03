from classes import Population

def genetic_algorithm(goal=[3,3,7,9,2], pop_size=20, mut_chance=0.05):
    
    # Get user input for the goal of the Genetic Algorithm
    '''
    goal = input("Enter 5 integers (0-10 inclusive) that you wish to converge to, separated by a space: ")
    goal = goal.split()
    goal = list(map(int, goal))
    '''

    # Define the basic parameters
    '''
    pop_size = 20
    mut_chance = 0.05
    '''
    current_gen = 1

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
        if __name__ == "__main__":
            print("Best Chromosome: %s \nFitness: %d \nCurrent Generation: %d" % (generation.get_fittest().combination, generation.get_fittest().fitness, current_gen))
        

        # Create new generation for population
        generation.new_generation(mut_chance)

        # Compute fitness of children
        generation.pop_fitness(goal)

        # Increment the generation counter
        current_gen += 1

    if __name__ == "__main__":
        print("Goal of %s reached" %goal)
    

    return current_gen

if __name__ == "__main__":
    a = genetic_algorithm()
    
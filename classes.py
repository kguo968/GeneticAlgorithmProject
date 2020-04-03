from random import randrange, uniform
import evolution as evo

class Single:

    def __init__(self, size):
        # Basic parameters for each 'chromosome', where each value in the index of the array is a 'gene'
        self.combination = [randrange(11) for i in range(size)]
        self.length = size
        self.fitness = 0
    
    def calcFitness(self, goal):
        # Calculate fitness of chromosome

        for i in range(len(goal)):
            self.fitness += abs(self.combination[i]-goal[i])         # Closer fitness is to 0, the better

class Population:
    # Class which defines the generation, stores each 'Single'/'Child' in a list
    def __init__(self, pop_size):
        self.population = []
        self.size = pop_size

    def create_pop(self, goal_size):
    # Instantiate objects from the Single class to populate the generation    
        for i in range(self.size):
            self.population.append(Single(goal_size))

    def pop_fitness(self, goal):
    # Call calcFitness from 'Single' class to calculate fitness of every object in the generation
        for i in range(self.size):
            self.population[i].calcFitness(goal)

    def sort_fittest(self):
    # Sort generation from best to worst
        self.population.sort(key = lambda x: x.fitness)

    def get_fittest(self):
    # Get the fittest of the generation
        self.sort_fittest()
        return self.population[0]
    
    def new_generation(self, mut_chance):
    # Make the children for the next generation
        children = []

        # Randomly produce children
        evo.create_child(self.population, self.size, children, mut_chance)

        # Update the population with the newly generated children
        self.population = children



        



            

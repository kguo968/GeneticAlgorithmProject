from random import randrange, uniform

class Child:
    # Child class added in evolution.py file in order to avoid ImportError

    def __init__(self, parent_a, parent_b, cross_point, mut_chance):
        # One Point Crossover
        self.combination = parent_a.combination[:cross_point+1]
        self.combination.extend(parent_b.combination[cross_point+1:])
        
        # Mutate the child based on random chance
        if (uniform(0,1) <= mut_chance):
            self.mutate_pop(self.combination)
   
        self.length = 5
        self.fitness = 0
    
    def calcFitness(self, goal):
    # Calculate the fitness of the children
        for i in range(len(goal)):
            self.fitness += abs(self.combination[i]-goal[i])

    def mutate_pop(self, child):        
        '''
        MAYBE CHANGE THIS FOR FUTURE ITERATIONS
        '''
    # Change a randomly chosen gene for mutation
        mutate_gene = randrange(len(child))
        child[mutate_gene] = randrange(0,11)

def create_child(population, size, children, mut_chance):

    elite_size = size//2

    for i in range(size):
        if i < elite_size:
            # Select both parents randomly from 'elite' population 
            parent_a = population[randrange(elite_size)]
            parent_b = population[randrange(elite_size)]
        else:
            # Randomly select parents from entire population
            parent_a = population[randrange(size)]
            parent_b = population[randrange(size)]
        
        # The cross_point value determines all the inhereted values from parent_a (up to the cross_point value)
            # i.e. parent_a = [1,2,3,4,5], parent_b = [6,7,8,9,10], cross_point = 2
            # child = [1,2,3,9,10]
        cross_point = randrange(len(parent_a.combination)-1)

        # Instantiate objects from Child class to generate the children
        '''
        PERHAPS CHANGE CROSSOVER PROCESS
        '''
        children.append(Child(parent_a, parent_b, cross_point, mut_chance))


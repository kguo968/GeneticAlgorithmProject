from ga import genetic_algorithm

#gen_number = []
sample_size = 1000
compute_base = False

# Create new textfile to store the results
if compute_base:   # Only generate new baseline_results is requested to do so 
    f = open("baseline_results.txt", "w+")

g = open("compare_results.txt", "w+")


for i in range(sample_size):

    # Run the GA + add it to the list (can remove when confirm writing to textfile works as intended)
    if compute_base:
        # Only run baseline GA if specified
        results = genetic_algorithm(pop_size=20)
        
        if (i+1 == sample_size):
            f.write("%d" %results)
        else:
            f.write("%d\n" %results)
        
    
    results2 = genetic_algorithm(pop_size=100)
    #gen_number.append(results)
    
    # Write the results of each generation to the textfile
    if (i+1 == sample_size):
        g.write("%d" %results2)
    else:
        g.write("%d\n" %results2)
    print("Sample: %d" %(i))

if compute_base:
    f.close()

g.close()

print("Completed sampling")
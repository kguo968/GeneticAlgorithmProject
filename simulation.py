from ga import genetic_algorithm

gen_number = []
sample_size = 10

# Create new textfile to store the results
f = open("results.txt", "w+")

for i in range(sample_size):

    # Run the GA + add it to the list (can remove when confirm writing to textfile works as intended)
    results = genetic_algorithm(pop_size=20)
    gen_number.append(results)
    
    # Write the results of each generation to the textfile
    if (i+1 == sample_size):
        f.write("%d" %results)
    else:
        f.write("%d\n" %results)
f.close()
 
print(gen_number)
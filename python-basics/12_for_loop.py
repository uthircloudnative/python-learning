# Simple for loop
for i in range(5):
    print("Executing for loop: ", i)


# For loop with break
for i in range(10):
    if i == 5:
        print(("Condition met, breaking the loop at: ", i))
        break
else:
    print("Condition not met, loop completed without break.")


iteration = 0
total_iteration = 10
for i in range(total_iteration):
    print("Current Iteration: ", i)
    iteration += 1
    if iteration == 5:
        print(" Condition met, breaking the loop at iteration: ", iteration)
        break
else:
    print("Condition not met, loop completed without break.", iteration)

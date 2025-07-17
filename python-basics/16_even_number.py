even_number_count = 0

for i in range(1, 11):
    print("Actual number is :", i)
    if i % 2 == 0:
        print("Even number found :", i)
        even_number_count += 1
print("Total even numbers found in range 1 to 10:", even_number_count)

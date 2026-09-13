temperatures = [12, 14, 15, 10, 11, 14, 16]

total = 0
for temp in temperatures:
    total += temp

average = total / len(temperatures)
print("Average temperature:", average)

import os

here = os.path.dirname(os.path.abspath(__file__))
input_file = os.path.join(here, "input.txt")

f = open(input_file, "r")

reached_ings = False
fresh_ranges = []
ingredients = []

for line in f:
    if line.strip() == "":
        reached_ings = True
        continue
    if reached_ings == False:
        temp = line.strip().split("-")
        fresh_ranges.append([int(temp[0]),int(temp[1])])
    else:
        ingredients.append(int(line.strip()))

fresh_number = 0 

for this_ing in ingredients:
    for this_range in fresh_ranges:
        if this_ing >= this_range[0] and this_ing <= this_range[1]:
            # then it is in a fresh range and we need to consider no further ranges for this ingredient
            fresh_number += 1
            break 

print(fresh_number)
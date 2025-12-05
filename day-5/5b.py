import os

here = os.path.dirname(os.path.abspath(__file__))
input_file = os.path.join(here, "input.txt")

f = open(input_file, "r")

reached_ings = False
fresh_ranges = []

for line in f:
    if line.strip() == "":
        reached_ings = True
        break
    temp = line.strip().split("-")
    fresh_ranges.append([int(temp[0]),int(temp[1])])

reset = True

while True:  
    fresh_ranges.sort(key= lambda range:range[0])
    if not reset: break
    reset = False
    for idx1, this_range1 in enumerate(fresh_ranges):
        temp_list = fresh_ranges.copy()
        temp_list.pop(idx1)
        for idx2, this_range2 in enumerate(temp_list):
            # Does this range overlap?
            if this_range1[0] <= this_range2[1] and this_range1[1] >= this_range2[0]:
                # Overlap found
                new_range = [min(this_range1[0],this_range2[0]),max(this_range1[1],this_range2[1])]
                fresh_ranges.pop(idx1)
                fresh_ranges.pop(idx2)
                fresh_ranges.append(new_range)
                reset = True
                break

        if reset: break

total = 0
for this_range in fresh_ranges:
    total += 1 + this_range[1] - this_range[0]

print(total)
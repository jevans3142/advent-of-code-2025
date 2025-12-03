import os

here = os.path.dirname(os.path.abspath(__file__))
input_file = os.path.join(here, "input.txt")

f = open(input_file, "r")

input = f.read()

ranges_temp = input.split(",")

invalid_total = 0

for this_range in ranges_temp: 
    idxs = this_range.split("-")
    first_id = int(idxs[0])
    last_id = int(idxs[1])

    for id in range(first_id,last_id+1):
        # First check if odd number of digits, because these have to be vaid
        if len(str(id)) % 2 != 0:
            continue
        # So has to be even digits - let's split into two
        first_half = str(id)[:(len(str(id))//2)]         
        second_half = str(id)[(len(str(id))//2):] 
        if first_half == second_half:
            invalid_total += id

print(invalid_total)
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
        for this_length in range(1,1+(len(str(id)) // 2)): 
            if (len(str(id)) % this_length) == 0:
                # ie. we have a length that divides neatly into this length id
                # Invalid if all the divided substrings are equal
                substrings = [ str(id)[i:i+this_length] for i in range(0, len(str(id)), this_length) ]            
                if substrings.count(substrings[0]) == len(substrings):
                    invalid_total += id
                    break

print(invalid_total)
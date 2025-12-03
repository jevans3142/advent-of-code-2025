import os
import math 

here = os.path.dirname(os.path.abspath(__file__))
input_file = os.path.join(here, "input.txt")

f = open(input_file, "r")

total_joltage = 0

for line in f:
    this_joltage = 0 
    remaining_line = line.strip()
    for this_digit_position in range(12,0,-1):
        line_sorted = sorted(remaining_line[:-(this_digit_position-1) or None ],reverse=True)
        this_digit = line_sorted[0]
        digit_idx = remaining_line.index(this_digit)
        remaining_line = remaining_line[digit_idx+1:]
        this_joltage += int(int(this_digit) * math.pow(10,this_digit_position-1))

    total_joltage += this_joltage

print(total_joltage)
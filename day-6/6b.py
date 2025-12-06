import os
import math

here = os.path.dirname(os.path.abspath(__file__))
input_file = os.path.join(here, "input.txt")

f = open(input_file, "r")

raw_lines = []

for line in f:
    raw_lines.append(line.replace("\n", "")+ " ")

grand_total = 0

mode = ""

current_number_set = []

# Go col by col
for col_idx in range(len(raw_lines[0])):
    if raw_lines[-1][col_idx] != " ":
        mode = raw_lines[-1][col_idx]

    if [x[col_idx] for x in raw_lines].count(" ") == len(raw_lines):
        if mode == "+":
            grand_total += int(math.fsum(current_number_set))
        if mode == "*":
            grand_total += int(math.prod(current_number_set))
        current_number_set = []
        continue

    this_number_str = ""
    for row_idx in range(len(raw_lines) - 1):
        this_number_str += raw_lines[row_idx][col_idx]
    current_number_set.append(int(this_number_str))

print(grand_total)

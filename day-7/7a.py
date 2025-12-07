import os
import math

here = os.path.dirname(os.path.abspath(__file__))
input_file = os.path.join(here, "input.txt")

f = open(input_file, "r")

raw_lines = []

for line in f:
    raw_lines.append(list(line.strip()))

beamsplits = 0

for row_idx, this_line in enumerate(raw_lines):
    if row_idx == 0: continue # Skip first line 
    for col_idx, this_char in enumerate(this_line):
        if this_char == ".":
            if raw_lines[row_idx-1][col_idx] == "S" or raw_lines[row_idx-1][col_idx] == "|":
                raw_lines[row_idx][col_idx] = "|"
        if this_char == "^" and raw_lines[row_idx-1][col_idx] == "|" :
            raw_lines[row_idx][col_idx-1] = "|"
            raw_lines[row_idx][col_idx+1] ="|"
            beamsplits += 1

print(beamsplits)

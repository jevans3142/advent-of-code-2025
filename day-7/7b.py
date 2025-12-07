import os
import math

here = os.path.dirname(os.path.abspath(__file__))
input_file = os.path.join(here, "input.txt")

f = open(input_file, "r")

raw_lines = []

for line in f:
    raw_lines.append(list(line.strip()))

for row_idx, this_line in enumerate(raw_lines):
    if row_idx == 0: continue # Skip first line 
    for col_idx, this_char in enumerate(this_line):
        # First continue any beams that already exist down into empty space
         if this_char == ".":
            if raw_lines[row_idx-1][col_idx] == "S":
                raw_lines[row_idx][col_idx] = 1
            if str(raw_lines[row_idx-1][col_idx]).isdigit(): 
                raw_lines[row_idx][col_idx] = int(raw_lines[row_idx-1][col_idx])
    for col_idx, this_char in enumerate(this_line):
        # Now do any beamsplitting
        if this_char == "^" and str(raw_lines[row_idx-1][col_idx]).isdigit():
            if raw_lines[row_idx][col_idx-1] == ".":
                raw_lines[row_idx][col_idx-1] = int(raw_lines[row_idx-1][col_idx])
            else:
                raw_lines[row_idx][col_idx-1] += int(raw_lines[row_idx-1][col_idx])

            if raw_lines[row_idx][col_idx+1] == ".":
                raw_lines[row_idx][col_idx+1] = int(raw_lines[row_idx-1][col_idx])
            else:
                raw_lines[row_idx][col_idx+1] += int(raw_lines[row_idx-1][col_idx])



timelines = 0

for this_char in raw_lines[-1]:
    if str(this_char).isdigit():
        timelines += int(this_char)

print(timelines)
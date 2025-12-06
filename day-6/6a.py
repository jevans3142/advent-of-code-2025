import os
import math

here = os.path.dirname(os.path.abspath(__file__))
input_file = os.path.join(here, "input.txt")

f = open(input_file, "r")

raw_lines = []

for line in f:
    raw_lines.append(line.strip().split())

operator_line = raw_lines.pop(-1)

grand_total = 0

for col_idx in range(len(raw_lines[0])):
    if operator_line[col_idx] == "+":
        result = int(math.fsum([int(x[col_idx]) for x in raw_lines]))
    if operator_line[col_idx] == "*":
        result = int(math.prod([int(x[col_idx]) for x in raw_lines]))
    grand_total += result

print(grand_total)

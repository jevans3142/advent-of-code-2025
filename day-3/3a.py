import os

here = os.path.dirname(os.path.abspath(__file__))
input_file = os.path.join(here, "input.txt")

f = open(input_file, "r")

total_joltage = 0

for line in f:
    line_sorted = sorted(line.strip()[:-1],reverse=True)
    first_digit = line_sorted[0]
    part_line = line[line.index(first_digit)+1:]
    part_line_sorted = sorted(part_line,reverse=True)
    second_digit = part_line_sorted[0]
    total_joltage += (int(first_digit) * 10 + int(second_digit))

print(total_joltage)
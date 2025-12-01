import os

here = os.path.dirname(os.path.abspath(__file__))
input_file = os.path.join(here, "input.txt")

f = open(input_file, "r")

current_pos = 50
password = 0

for line in f:
    direction = line[0]
    number = int(line[1:])
    if direction == "L":
        current_pos = (current_pos - number) % 100 
    if direction == "R":
        current_pos = (current_pos + number) % 100 
    if current_pos == 0:
        password = password + 1

print("Password is:" + str(password))

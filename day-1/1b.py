import os

here = os.path.dirname(os.path.abspath(__file__))
input_file = os.path.join(here, "input.txt")

f = open(input_file, "r")

current_pos = 50
password = 0

for line in f:
    direction = line[0]
    number = int(line[1:])

    if number == 0: 
        continue

    if direction == "L":
        if current_pos == 0:
            fake_cur_pos = 0
        else:
            fake_cur_pos = 100-current_pos
  
        next_pos_raw = fake_cur_pos + number
        password_num = int(next_pos_raw // 100)
        password = password + password_num     
        current_pos = (current_pos - number) % 100 

    if direction == "R":
        next_pos_raw = current_pos + number
        password_num = int(next_pos_raw // 100)
        password = password + password_num
        current_pos = next_pos_raw % 100 

print("Password is:" + str(password))

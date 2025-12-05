import os

here = os.path.dirname(os.path.abspath(__file__))
input_file = os.path.join(here, "input.txt")

f = open(input_file, "r")

layout = []

def check_cell(row,col,row_length,col_length):
    if row < 0:
        return 0
    if row >= row_length:
        return 0
    if col < 0: 
        return 0
    if col >= col_length:
        return 0
    if layout[row][col] == "@":
        return 1
    return 0

for line in f:
    layout.append(line.strip())

row_len = len(layout)
col_len = len(layout[0])

reachable_rolls = 0

for row_idx in range(row_len):
    for col_idx in range(col_len):

        if layout[row_idx][col_idx] != "@":
            continue

        # Check all 8 around this
        count = 0 
        count += check_cell(row_idx-1,col_idx-1,row_len,col_len)
        count += check_cell(row_idx,col_idx-1,row_len,col_len)
        count += check_cell(row_idx+1,col_idx-1,row_len,col_len)
        count += check_cell(row_idx-1,col_idx,row_len,col_len)
        count += check_cell(row_idx+1,col_idx,row_len,col_len)
        count += check_cell(row_idx-1,col_idx+1,row_len,col_len)
        count += check_cell(row_idx,col_idx+1,row_len,col_len)
        count += check_cell(row_idx+1,col_idx+1,row_len,col_len)
        if count <4:
            reachable_rolls += 1 


print(reachable_rolls)
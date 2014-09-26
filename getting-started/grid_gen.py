import random


def read_int(message):
    result = input(message)
    try:
        if result:
            result = int(result)
        else:
            return result
    except ValueError as err:
        print(err)
    return result

def make_default(now, default):
    if now:
        return now
    else:
        return default

cnt_rows = read_int('rows: ')
cnt_columns = read_int('columns: ')
minimum = read_int('minimum number (or Enter for 0)')
minimum = make_default(minimum, 0)
maximum = read_int('maximum number (or Enter for 1000)')
maximum = make_default(maximum, 1000)

if maximum < minimum:
    print("maximum number cannot be less than minimum number")
    maximum = minimum * 2

cur_row = 0
while cur_row < cnt_rows:
    current_line = ''
    cur_column = 0
    while cur_column < cnt_columns:
        current_output = random.randint(minimum, maximum)
        current_output = str(current_output)
        while len(current_output) < 12:
            current_output = ' ' + current_output
        current_line += current_output
        cur_column += 1
    print(current_line)
    cur_row += 1


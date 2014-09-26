print('Enter one integer each line, or just Enter to end input\n')

total = 0
count = 0
line = None

while True:
    line = input()
    if not line:
        break
    try:
        number = int(line)
    except ValueError as err:
        print(err)
        continue

    total += number
    count += 1

print("total: ", total, "count: ", count, "mean: ", total / count)

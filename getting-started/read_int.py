def read_int(msg):
    line = input(msg)
    try:
        result = int(line)
        return result
    except ValueError as err:
        print(err)
        return read_int(msg)

print(read_int('Enter an integer'))

data = input("Enter a number: ")

try:
    i = int(data)
    print("valid number input: ", i)
except ValueError as err:
    print(err)

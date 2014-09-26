a = 1
b = "2"
c = 0

try:
    c = a + b
except TypeError as e:
    c = a + int(b)

print(c)

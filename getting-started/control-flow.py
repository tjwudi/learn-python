a = 9

if a < 9:
    print("a is less than 9")
elif 9 < a:
    print("a is bigger than 9")
else:
    print("a is equal to 9")



while a < 19:
    a = a + 1

print(a)


for name in ['Peking', 'WuHan', 'ShangHai']:
    print(name)


for letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
    if letter in 'AEIOU':
        print(letter, "is vowel")
    else:
        print(letter, "is consonant")

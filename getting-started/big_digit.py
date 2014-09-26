import sys

digits = sys.argv[1]

zero = ['  ***  ',
        ' *   * ',
        '*     *',
        '*     *',
        '*     *',
        ' *   * ',
        '  ***  ']

one = ['  ***  ',
       '    *  ',
       '    *  ',
       '    *  ',
       '    *  ',
       '    *  ',
       ' ***** ']

digit_graph = [zero, one]

length = len(digits)
i = 0

while i < length:
  try: 
    digit = int(digits[i])
  except ValueError as err:
    print(err, 'in', digits)
  print(digit_graph[digit])
  i += 1


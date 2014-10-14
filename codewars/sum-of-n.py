def sum_of_n(n):
  # your code goes here
  sign = 1 if n > 0 else -1;
  list = []
  for i in range(abs(n) + 1):
    list.append(i * sign + list[-1] if i > 0 else 0)
  return list

print(sum_of_n(-9))
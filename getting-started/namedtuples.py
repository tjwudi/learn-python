import collections

Sale = collections.namedtuple('Sale', 'productname quantity price');

sales = []
sales.append(Sale('Wars Suit', 5, 10))
sales.append(Sale('Big Data Book', 10.2, 22))

total = 0
for sale in sales:
  total += sale.quantity * sale.price

print('${0:.2f}'.format(total))
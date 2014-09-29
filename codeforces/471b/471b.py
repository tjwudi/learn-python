import sys

def swap_arr_el(arr, i, j):
  c = arr[i]
  arr[i] = arr[j]
  arr[j] = c

n = int(input())
arr = input()
arr = arr.split(' ')
for i in range(0, len(arr)):
  arr[i] = int(arr[i])

arr_t = []
for i in range(0, len(arr)):
  arr_t.append((i, arr[i]))

swap_idxes = []
for i in range(0, len(arr_t) - 1):
  curmin = 100000000000000000
  curmin_idx = None
  for j in range(i,len(arr_t)):
    if arr_t[j][1] < curmin:
      curmin = arr_t[j][1]
      curmin_idx = j
  swap_arr_el(arr_t, i, curmin_idx)
  if i>=1 and arr_t[i][1] == arr_t[i-1][1]:
    swap_idxes.append(i-1)
if len(arr_t) >= 2 and (arr_t[-1][1] == arr_t[-2][1]):
  swap_idxes.append(-2)

if len(swap_idxes) < 2:
  print('NO')
else:
  print('YES')
    ans = []
    for i in range(0, len(arr_t)):
      ans.append(str(arr_t[i][0]+1))
  print(' '.join(ans))
  swap_arr_el(ans, swap_idxes[0], swap_idxes[0] + 1)
  print(' '.join(ans))
  swap_arr_el(ans, swap_idxes[1], swap_idxes[1] + 1)
  print(' '.join(ans))

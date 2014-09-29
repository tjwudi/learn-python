import math

class SuffixArray:
  def __init__(self, string):
    self.__chrs = list(string)
    self.__itertime = math.ceil(math.log(len(string), 2))
    self.__matrix = [[0] * len(string)
      for _ in range(0, self.__itertime + 1)]
    self.__build()

  def getresult(self):
    return self.__matrix[-1]

  def __build(self):
    for idx, c in enumerate(self.__chrs):
      self.__matrix[0][idx] = ord(c) - ord('a')
    for k in range(1, self.__itertime + 1):
      prevrow, currow = (self.__matrix[k - 1], self.__matrix[k])
      tmp = list(map(lambda x: (x[1], -1 if ((x[0] + (1 << (k - 1))) >= len(prevrow)) else prevrow[x[0] + (1 << (k - 1))], x[0]), enumerate(prevrow)))
      tups = sorted([(first, second, idx) for first, second, idx in tmp], key = lambda x: (x[0], x[1]))
      for idx, tup in enumerate(tups):
        if idx == 0:
          currow[tup[2]] = 0
        else:
          currow[tup[2]] = currow[tups[idx - 1][2]] if (idx > 0 and tups[idx][0] == tups[idx - 1][0] and tups[idx][1] == tups[idx - 1][1]) else idx

sa = SuffixArray('aabaaa').getresult()
print(sa)
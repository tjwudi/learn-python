# return a list of tuples sorted by frequency with
# the most frequent letter first. Any letters with the
# same frequency are ordered alphabetically

dic = {}

def inc(c):
    if 'a' <= c <= 'z':
      if dic.get(c, 0) == 0:
          dic[c] = 1
      else:
          dic[c] += 1

def letter_frequency(text):
  text = text.lower()
  for c in text:
      inc(c)
  result = []
  for key in dic:
      value = dic[key]
      result.append((key, value))
  return sorted(result, key = lambda x: (-x[1], x[0]))

print(letter_frequency("""wklv lv d vhfuhw phvvdjh"""))
from collections import Counter, defaultdict
import sys
import re

with open(sys.argv[1]) as f:
  data = f.read()

def remove_pairs(start):
  last = ''
  final = []
  for c in start:
    if c != last and c.lower() == last.lower():
      final.pop()
      last = final[-1] if final else ''
    else:
      final.append(c)
      last = c
  return ''.join(final)

data = remove_pairs(data)

print(len(data))
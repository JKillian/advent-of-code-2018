from collections import Counter, defaultdict
import sys
import re
import operator as op
from string import ascii_lowercase

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

results = {
  l: len(remove_pairs(data.replace(l, '').replace(l.upper(), '')))
  for l in ascii_lowercase
}

print(min(results.items(), key=op.itemgetter(1)))
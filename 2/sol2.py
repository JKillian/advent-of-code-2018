from collections import Counter
import sys

with open(sys.argv[1]) as f:
  lines = [l.strip() for l in f]

for i, l in enumerate(lines):
  for m in lines[i+1:]:
    diff = 0
    lets = ''
    for c0, c1 in zip(l,m):
      if c0 != c1:
        diff += 1
      else:
        lets += c0
    if diff == 1:
      print(lets)
      print(l, m)
from collections import Counter
import sys

with open(sys.argv[1]) as f:
  lines = [l.strip() for l in f]

twos = 0
threes = 0
for l in lines:
  c = Counter(l)
  if 2 in c.values():
    twos += 1
  if 3 in c.values():
    threes += 1
print(twos * threes)

from collections import Counter
import sys
import re

r = re.compile(r'#(\d+) @ (\d+),(\d+): (\d+)x(\d+)')

with open(sys.argv[1]) as f:
  lines = [[int(x) for x in r.match(l.strip()).groups()] for l in f]

fabric = []
for _ in range(1200):
  fabric.append([0 for _ in range(1200)])

for _,x,y,w,h in lines:
  for a in range(x,x+w):
    for b in range (y,y+h):
      fabric[a][b] += 1

cnt = 0
for lst in fabric:
  for b in lst:
    if b > 1:
      cnt += 1 
# print(fabric)
print(cnt)

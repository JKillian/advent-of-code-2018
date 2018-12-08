from collections import Counter
import sys
import re

r = re.compile(r'#(\d+) @ (\d+),(\d+): (\d+)x(\d+)')

with open(sys.argv[1]) as f:
  lines = [[int(x) for x in r.match(l.strip()).groups()] for l in f]

fabric = []
for _ in range(1200):
  fabric.append([0 for _ in range(1200)])

dead_claims = set()
for claim,x,y,w,h in lines:
  for a in range(x,x+w):
    for b in range (y,y+h):
      if fabric[a][b] > 0:
        dead_claims.add(fabric[a][b])
        dead_claims.add(claim)
      fabric[a][b] = claim

claims = [l[0] for l in lines]
for c in dead_claims:
  claims.remove(c)
print(claims)



from collections import defaultdict

with open('data1') as f:
  nums = [int(l.strip()) for l in f]

tot = 0
seen = defaultdict(lambda: False)
for i in range(1000000):
  if seen[tot]:
    print(tot)
    break
  seen[tot] = True
  tot += nums[i % len(nums)]


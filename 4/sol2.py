from collections import Counter, defaultdict
import sys
import re

r = re.compile(r'\[1518-(\d+)-(\d+) (\d+):(\d+)\] (.+)')

with open(sys.argv[1]) as f:
  lines = [[x for x in r.match(l.strip()).groups()] for l in f]

for l in lines:
  l[0:4] = [int(x) for x in l[0:4]]

order = sorted(lines)


guards = defaultdict(list)
counts = defaultdict(lambda: 0)
curr_guard = 0
start_sleep = 0
for _,__,h,m,t in order:
  if t.startswith("Guard "):
    curr_guard = int(t.split(' ')[1][1:])
    guards[curr_guard].append([False for _ in range(60)])
  elif t == 'falls asleep':
    start_sleep = m
  elif t == 'wakes up':
    guards[curr_guard][-1][start_sleep:m] = [True for _ in range(m-start_sleep)]
  else:
    print('invalid command', t)

counts = {
  g: sum(len([x for x in d if x]) for d in days)
  for g, days in guards.items()
  if days
}

c = Counter(counts)
most_guard = c.most_common(1)[0][0]
all_guards = {}
for g in guards:
  mins = Counter()
  for d in guards[g]:
    for i, b in enumerate(d):
      if b:
        mins[i] += 1
  all_guards[g] = mins.most_common(1)

all_guards = [[a,*b] for a,b in all_guards.items() if b]
print(all_guards)
best = max(all_guards, key=lambda l: l[1][1])

print(best, "ans:", best[0] * best[1][0])

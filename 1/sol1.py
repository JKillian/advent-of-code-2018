with open('data1') as f:
  lines = [int(l.strip()) for l in f]
print(sum(lines))

import sys
lines = sys.stdin.readlines()

l = int(lines[0])
r = int(lines[1])
maxxor = 0

for a in xrange(l,r+1):
  for b in xrange(a+1,r+1):
    maxxor = max(maxxor, a ^ b)

print maxxor
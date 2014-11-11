import sys

lines = sys.stdin.readlines()

test_cases = int(lines[0])

for case in xrange(1, test_cases+1):
  cuts = int(lines[case])
  if cuts % 2 == 0:
    print cuts**2/4
  else:
    print (cuts**2-1)/4

#O(1) efficiency
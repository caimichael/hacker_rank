import sys

lines = sys.stdin.readlines()

number_test_cases = int(lines[0].rstrip())

for i in range(number_test_cases):
  counter = 0
  palin = lines[i+1].rstrip()
  palin = [ord(a) for a in palin]
  
  for j in xrange(len(palin)/2):
    counter += abs(palin[j] - palin[len(palin) - 1 - j])

  print counter

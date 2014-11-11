import sys

lines = sys.stdin.readlines()

number_test_cases = int(lines[0].rstrip())

for i in range(number_test_cases): #O(t)
  counter = 0
  palin = lines[i+1].rstrip()
  palin = [ord(a) for a in palin]
  
  for j in xrange(len(palin)/2): #O(n)
    while palin[j] < palin[len(palin) - 1 - j]: #O(d)
      palin[len(palin) - 1 - j] -= 1
      counter += 1

    while palin[j] > palin[len(palin) - 1 - j]:
      palin[j] += 1
      counter += 1
  
  print counter

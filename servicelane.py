import sys

lines = sys.stdin.readlines()

n_and_t = lines[0].rstrip().split(" ")
n = int(n_and_t[0])
t = int(n_and_t[1])

width_as_str = lines[1].rstrip().split(" ")
width = [int(a) for a in width_as_str]

for i in range(2, len(lines)):
  start_stop_as_str = lines[i].rstrip().split(" ")
  start = int(start_stop_as_str[0])
  stop = int(start_stop_as_str[1])

  m = width[start]

  for j in range(start + 1, stop + 1):
    m = min(m, width[j])

  print m
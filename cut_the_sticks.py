import sys

lines = sys.stdin.readlines()

number_test_cases = int(lines[0].rstrip())

stick_list = lines[1].split(" ")
stick_list = map(int, stick_list)

stick_list.sort()

for x in stick_list:
  min_val = stick_list[0]
  x -= min_val #Can't modify items in a list while iterating over that list
  #Only other way I can think of it is usind a numpy ndarray and broadcasting the -min_val

print stick_list

# stick_list = [x for x in stick_list if x > 0] #creating a new list removing the 0s
#   #or maybe try using the reversed generator to generate a new list, and then .pop off the 0s from the end?
#   The .pop() function can pop off elements at any index. Still may have the issue of 
#   not being able to modify lists during the iteration, but give it a try
#   print len(stick_list)
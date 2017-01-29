import re

pattern = '^M{0,3}$'

a = re.search(pattern, 'M')
print a

a = re.search(pattern, 'MM')
print a

a = re.search(pattern, 'MMM')
print a

a = re.search(pattern, 'MMMM')
print a
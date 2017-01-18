import re

pattern = '^M?M?M?$'
a = re.search(pattern, 'M')
print a

pattern = '^M?M?M?$'
a = re.search(pattern, 'MM')
print a

pattern = '^M?M?M?$'
a = re.search(pattern, 'MMM')
print a

a = re.search(pattern, 'MMMM')
print a

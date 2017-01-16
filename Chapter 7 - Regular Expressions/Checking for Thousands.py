import re

pattern = '^M?M?M?$'

x = re.search(pattern, 'M')
print x

y = re.search(pattern, 'MM')
print y

z = re.search(pattern, 'MMM')
print z

a = re.search(pattern, 'MMMM')
print a

b = re.search(pattern, '')
print b
import re

pattern = '^M?M?M?M?(CM|CD|D?C?C?C?)(XC|XL|L?X?X?X?)$'

a = re.search(pattern, 'MCMXL')
print a

a = re.search(pattern, 'MCML')
print a

a = re.search(pattern, 'MCMLX')
print a

a = re.search(pattern, 'MCMLXXX')
print a

a = re.search(pattern, 'MCMLXXXX')
print a
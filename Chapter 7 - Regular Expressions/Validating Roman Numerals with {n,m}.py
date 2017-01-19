import re

# pattern = '^M?M?M?M?(CM|CD|D?C?C?C?)(XC|XL|L?X?X?X?)(XC|XL|L?X?X?X?)(IX|IV|V?I?I?I?)$'
pattern = '^M{0,4}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$'

a = re.search(pattern, 'MDLV')
print a

a = re.search(pattern, 'MMDCLXVI')
print a

a = re.search(pattern, 'MMMMDCCCLXXXVIII')
print a

a = re.search(pattern, 'I')
print a

import re

s = '100 BROAD'
print s

s1 = re.sub('ROAD$', 'RD.', s)
print s1

s2 = re.sub('\\bROAD$', 'RD.', s)
print s2

s3 = re.sub(r'\bROAD$', 'RD.', s)
print s3

s = '100 BROAD ROAD APT. 3'
s4 = re.sub(r'\bROAD$', 'RD.', s)
print s4

s5 = re.sub(r'\bROAD\b', 'RD.', s)
print s5

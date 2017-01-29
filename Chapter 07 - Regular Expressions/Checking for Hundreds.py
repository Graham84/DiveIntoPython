import re

pattern = '^M?M?M?(CM|CD|D?C?C?C?)$'

a = re.search(pattern, 'MCM')
print a

b = re.search(pattern, 'MD')
print b

c = re.search(pattern, 'MMMCCC')
print c

d = re.search(pattern, 'MCMC')
print d

e = re.search(pattern, '')
print e

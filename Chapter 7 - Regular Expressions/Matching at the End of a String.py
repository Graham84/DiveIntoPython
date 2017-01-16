s = '100 NORTH MAIN ROAD'
print s
s1 = s.replace('ROAD', 'RD.')
print s1

s = '100 NORTH BROAD ROAD'
print s
s2 = s.replace('ROAD', 'RD.')
print s2

s3 = s[:-4] + s[-4:].replace('ROAD', 'RD.')
print s3

import re
s4 = re.sub('ROAD$', 'RD.', s)
print s4

import re

# Finding the numbers
phonePattern = re.compile(r'^(\d{3})-(\d{3})-(\d{4})$')
print phonePattern.search('800-555-1212').groups()
print phonePattern.search('800-555-1212')
print phonePattern.search('800-555-1212-1234')

# Finding the Extension
phonePattern = re.compile(r'^(\d{3})-(\d{3})-(\d{4})-(\d+)$')
print phonePattern.search('800-555-1212-1234').groups()
print phonePattern.search('800 555 1212 1234')
print phonePattern.search('800-555-1212')

# Handling different Seperators
phonePattern = re.compile(r'^(\d{3})\D+(\d{3})\D+(\d{4})\D+(\d+)$')
print phonePattern.search('800 555 1212 1234').groups()
print phonePattern.search('800-555-1212-1234').groups()
print phonePattern.search('80055512121234')
print phonePattern.search('800-555-1212')

# Handling Nnumbers without Seperators
phonePattern = re.compile(r'^(\d{3})\D*(\d{3})\D*(\d{4})\D*(\d*)$')
print phonePattern.search('80055512121234').groups()
print phonePattern.search('800.555.1212 x1234').groups()
print phonePattern.search('800-555-1212').groups()
print phonePattern.search('(800)5551212 x1234')

# Handling Leading Characters
phonePattern = re.compile(r'^\D*(\d{3})\D*(\d{3})\D*(\d{4})\D*(\d*)$')
print phonePattern.search('(800)5551212 ext. 1234').groups()
print phonePattern.search('800-555-1212').groups()
print phonePattern.search('work 1-(800) 555.1212 #1234')

# Phone Number, Wherever I May Find Ye
phonePattern = re.compile(r'(\d{3})\D*(\d{3})\D*(\d{4})\D*(\d*)$')
print phonePattern.search('work 1-(800) 555.1212 #1234').groups()
print phonePattern.search('800-555-1212').groups()
print phonePattern.search('80055512121234').groups()

# Parsing Phone Numbers - Final Version
phonePattern = re.compile(r'''
            # don't match beginning of String, number can start anywhere
(\d{3})     # area code is 3 digits(e.g. '800')
\D*         # optional seperator is any number of non digits
(\d{3})     # trunk is 3 digits(e.g. '500')
\D*         # optional seperator
(\d{4})     # rest of number is 4 digits(e.g. '1212')
\D*         # optional seperator
(\d*)       # extension is optional and can be any number of digits
$           # end of string

''', re.VERBOSE)
print phonePattern.search('work 1-(800) 555.1212 #1234').groups()
print phonePattern.search('800-555-1212').groups()

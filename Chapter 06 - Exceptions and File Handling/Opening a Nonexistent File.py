# >>> fscok = open("/notthere","r")
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# IOError: [Errno 2] No such file or directory: '/notthere'

# >>> try:
# ...     fscok = open("/notthere")
# ... except IOError:
# ...     print "This file does not exist, exiting gracefully"
# ... print "This line will always print"

# This file does not exist, exiting gracefully
# This line will always print

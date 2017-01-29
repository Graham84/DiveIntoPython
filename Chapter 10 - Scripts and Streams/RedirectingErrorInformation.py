import sys
fsock = open('error.log', 'w')
raise Exception, 'this error will be logged'

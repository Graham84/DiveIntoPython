"""
#>>> def f(x):
	return x*2

#>>> f(3)
6
#>>> g = lambda x: x*2
#>>> g(3)
6
#>>> (lambda x: x*2)(3)
6
#>>> s = "this 	is\n\ttest"
#>>> print s
this 	is
	test
#>>> s = "this 	is\n\ttest"
#>>>
#>>> s = "this 	is\na\ttest"
#>>> print s
this 	is
a	test
#>>> print s.split()
['this', 'is', 'a', 'test']
#>>> print " ".join(s.split())
this is a test
#>>>


#>>> import odbchelper
#>>> object = odbchelper
#>>> method = 'buildConnectionString'
#>>> getattr(object, method)
<function buildConnectionString at 0x02A9C970>
#>>> print getattr(object, method).__doc__
Build a connection string from a dictionary of parameters.

    Returns String.
#>>> print str(getattr(object, method).__doc__)
Build a connection string from a dictionary of parameters.

    Returns String.

Why use str on a doc string
#>>> def foo(): print 2

#>>> foo()
2
#>>> foo.__doc__
#>>> foo.__doc__ == None
True
#>>> str(foo.__doc__)
'None'
#>>>
#faster
#>>> foo.__doc__ is None
True


#>>> s = 'buildConnectionString'
#>>> s.ljust(30)
'buildConnectionString         '
#>>> s.ljust(20)
'buildConnectionString'
#>>> li = ['a','b','c']
#>>> print "\n".join(li)
a
b
c

"""
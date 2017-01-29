"""
Introducing and
#>>> 'a' and 'b'
'b'
#>>> '' and 'b'
''
#>>> '  ' and 'b'
'b'
#>>> 'a' and 'b' and 'c'
'c'
#>>>


Introducing or
#>>> 'a' or 'b'
'a'
#>>> ' ' or 'b'
' '
#>>> '' or 'b'
'b'
#>>> '' or [] or {}
{}
#>>> ' ' or [] or {}
' '
#>>> def sidefx():
	print "in sidefx()"
	return 1

#>>> 'a' or sidefx()
'a'
#>>> sidefx() or 'a'
in sidefx()
1
#>>>


Using the and-or Trick
#>>> a = 'first'
#>>> b = 'second'
#>>> 1 and a or b
'first'
#>>> 0 and a or b
'second'
works incirrectly if first value is false ''
#>>> a = ''
#>>> b = 'second'
#>>> 1 and a or b
'second'

ensure a has a value. the list [a] is true because it has one element
checks the first element of the list [0]
#>>> (1 and [a] or [b])[0]
''



"""
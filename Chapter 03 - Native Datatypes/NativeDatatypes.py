#dictionary
d = {"server":"mpilgrim", "database":"master"}
print d
print d["server"]
print d['database']
d['database'] = "pubs"
print d
d['uid'] = "sa"
print d

#dictionary keys are case sensitive
k = {}
print k
#key
k["key"] = "value"
print k
#key
k["key"] = "other value"
print k
#Key
k["Key"] = "third value"
print k

#mixing datatypes in dictionaries
print d
d["retrycount"] = 3
d[42] = "douglas"
print d
#delete
del d[42]
print d
#empty
d.clear()
print d


#Lists
li = ["a", "b" ,"mpilgrim" , "z", "example"]
print li
print li[0]
print li[4]
print li[-1]
print li[-3]

#getting a list subset: Slicing
print li[1:3]
print li[1:-1]
print li[0:3]

#slicing shorthand
#same as li[0:3]
print li[:3]
print li[3:]
#shorthand for entire list
print li[:]

li.append('new')
li.insert(2,'new')
li.extend(['two','elements'])
print li

#the difference between extend and append
li = ['a','b','c']
li.extend(['d','e','f'])
print li
print len(li)
print li[-1]

li = ['a','b','c']
li.append(['d','e','f'])
print li
print len(li)
print li[-1]

li = ["a","b",'new',"mpilgrim","z","example",'two','elements']
print li.index('example')
print li.index('new')
#print li.index('c')
print 'c' in li
print 'b' in li

li.remove("z")
print li
li.remove('new')
print li
#li.remove('c')
#print li
li.pop()
print li

#using list operators
li = ['a', 'b', 'mpilgrim']
li = li + ['example', 'new']
print li
li += ['two']
print li
li = [1, 2] * 3
print li

# tuples - immutable list
# cannot be changed in any way once it is created
t = ("a","b","graham","z","example")
print t
print t[0]
print t[-1]
print t[1:3]

# t.append("new")
# t.remove("z")
# t.index("example")
print "z" in t

# assigning multiple values at once
v = ('a','b','c')
(x,y,z) = v
print x
print y
print z


g = range(7)
print g
(Monday,Tuesday,Wednesday,Thursday,Friday,Saturday,Sunday) = range(7)
print Monday,\
    Tuesday,\
    Wednesday,\
    Thursday,\
    Friday,\
    Saturday,\
    Sunday


print range.__doc__
#print range.__globals__
print range.__init__()
print range.__doc__
print range.__module__
print range.__str__()


# formatting strings
k = 'uid'
v = 'sa'
print "%s:%s" % (k, v)

uid = 'sa'
pwd = 'secret'
print pwd + " is not a good password for " + uid
print "%s is not a good password for %s" % (pwd, uid)
userCount = 6
print "users connected: %d" % (userCount)
# print "Users connected: " + userCount

# formatting numbers
# treats the value as a decimal and prints to 6 decimal places
print "Today's stock price: %f" % 50.4625
# truncates the value to 2 decimal places
print "Today's stock price: %.2f" % 50.4625
# combine modifiers
# adding the + modifier displays a plus or minus sign before the value
# note that the .2 modifier is still in place and is padding the value to 2 decimal places
print "Change since yesterday: %+.2f" % 1.5


# Mapping Lists
li = [1,9,8,4]
print li
li = [elem*2 for elem in li]
print li

params = {"server":"mpilgrim", "database":"master",  "uid":"sa", "pwd":"secret" }
print params.keys()
print params.values()
print params.items()

# joining lists and splitting strings
print [k for k, v in params.items()]
print [v for k, v in params.items()]
print ["%s=%s" % (k, v) for k, v in params.items()]
print ";".join(["%s=%s" % (k, v) for k, v in params.items()])

# splitting a string
li = ['server=mpilgrim', 'uid=sa', 'database=master', 'pwd=secret']
s = ";".join(li)
print li
print s
print s.split(";")
print s.split(";", 1)

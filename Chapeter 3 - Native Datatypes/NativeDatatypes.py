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

#tuples


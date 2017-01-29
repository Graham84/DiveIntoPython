"""
#>>> from apihelper import info
#>>> li = []
#>>> info(li)
__add__    x.__add__(y) <==> x+y
__class__  list() -> new empty list list(iterable) -> new list initialized from iterable's items
__contains__ x.__contains__(y) <==> y in x
__delattr__ x.__delattr__('name') <==> del x.name
__delitem__ x.__delitem__(y) <==> del x[y]
__delslice__ x.__delslice__(i, j) <==> del x[i:j] Use of negative indices is not supported.
__eq__     x.__eq__(y) <==> x==y
__format__ default object formatter
__ge__     x.__ge__(y) <==> x>=y
__getattribute__ x.__getattribute__('name') <==> x.name
__getitem__ x.__getitem__(y) <==> x[y]
__getslice__ x.__getslice__(i, j) <==> x[i:j] Use of negative indices is not supported.
__gt__     x.__gt__(y) <==> x>y
__iadd__   x.__iadd__(y) <==> x+=y
__imul__   x.__imul__(y) <==> x*=y
__init__   x.__init__(...) initializes x; see help(type(x)) for signature
__iter__   x.__iter__() <==> iter(x)
__le__     x.__le__(y) <==> x<=y
__len__    x.__len__() <==> len(x)
__lt__     x.__lt__(y) <==> x<y
__mul__    x.__mul__(n) <==> x*n
__ne__     x.__ne__(y) <==> x!=y
__new__    T.__new__(S, ...) -> a new object with type S, a subtype of T
__reduce__ helper for pickle
__reduce_ex__ helper for pickle
__repr__   x.__repr__() <==> repr(x)
__reversed__ L.__reversed__() -- return a reverse iterator over the list
__rmul__   x.__rmul__(n) <==> n*x
__setattr__ x.__setattr__('name', value) <==> x.name = value
__setitem__ x.__setitem__(i, y) <==> x[i]=y
__setslice__ x.__setslice__(i, j, y) <==> x[i:j]=y Use of negative indices is not supported.
__sizeof__ L.__sizeof__() -- size of L in memory, in bytes
__str__    x.__str__() <==> str(x)
__subclasshook__ Abstract classes can override this to customize issubclass(). This is invoked early on by abc.ABCMeta.__subclasscheck__(). It should return True, False or NotImplemented. If it returns NotImplemented, the normal algorithm is used. Otherwise, it overrides the normal algorithm (and the outcome is cached).
append     L.append(object) -- append object to end
count      L.count(value) -> integer -- return number of occurrences of value
extend     L.extend(iterable) -- extend list by appending elements from the iterable
index      L.index(value, [start, [stop]]) -> integer -- return first index of value. Raises ValueError if the value is not present.
insert     L.insert(index, object) -- insert object before index
pop        L.pop([index]) -> item -- remove and return item at index (default last). Raises IndexError if list is empty or index is out of range.
remove     L.remove(value) -- remove first occurrence of value. Raises ValueError if the value is not present.
reverse    L.reverse() -- reverse *IN PLACE*
sort       L.sort(cmp=None, key=None, reverse=False) -- stable sort *IN PLACE*; cmp(x, y) -> -1, 0, 1
#>>>


"""
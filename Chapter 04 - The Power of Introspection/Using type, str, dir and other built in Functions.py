"""
Console output

The type Function
#>>> type(1)
<type 'int'>
#>>> li = []
#>>> type(li)
<type 'list'>
#>>> import odbchelper
#>>> type(odbchelper)
<type 'module'>
#>>> import types
#>>> type(odbchelper) == types.ModuleType
True
#>>>


The str Function
#>>> str(1)
'1'
#>>> horsemen = ['war','pestience','famine']
#>>> horsemen
['war', 'pestience', 'famine']
#>>> horsemen.append('Powerbuilder')
#>>> horsemen
['war', 'pestience', 'famine', 'Powerbuilder']
#>>> str(horsemen)
"['war', 'pestience', 'famine', 'Powerbuilder']"
#>>> str(odbchelper)
"<module 'odbchelper' from 'odbchelper.pyc'>"
#>>> str(None)
'None'
#>>> str(none)

Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    str(none)
NameError: name 'none' is not defined
#>>>


The dir Function
#>>> li = []
#>>> dir(li)
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__delslice__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getslice__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__setslice__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
#>>> d = {}
#>>> dir(d)
['__class__', '__cmp__', '__contains__', '__delattr__', '__delitem__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__init__', '__iter__', '__le__', '__len__', '__lt__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'clear', 'copy', 'fromkeys', 'get', 'has_key', 'items', 'iteritems', 'iterkeys', 'itervalues', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values', 'viewitems', 'viewkeys', 'viewvalues']
#>>> dir(odbchelper)
['__builtins__', '__doc__', '__file__', '__name__', '__package__', 'buildConnectionString']
#>>>


The callable Function
#>>> import string
#>>> string.punctuation
'!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'
#>>> string.join
<function join at 0x022F1BB0>
#>>> callable(string.punctuation)
False
#>>> callable(string.join)
True
#>>> print string.join.__doc__
join(list [,sep]) -> string

    Return a string composed of the words in list, with
    intervening occurrences of sep.  The default separator is a
    single space.

    (joinfields and join are synonymous)


The __builtin__ Module
#>>> from apihelper import info
#>>> import __builtin__
#>>> info(__builtin__, 20)
ArithmeticError      Base class for arithmetic errors.
AssertionError       Assertion failed.
AttributeError       Attribute not found.
BaseException        Common base class for all exceptions
BufferError          Buffer error.
BytesWarning         Base class for warnings about bytes and buffer related problems, mostly related to conversion from str or comparing to str.
DeprecationWarning   Base class for warnings about deprecated features.
EOFError             Read beyond end of file.
EnvironmentError     Base class for I/O related errors.
Exception            Common base class for all non-exit exceptions.
FloatingPointError   Floating point operation failed.
FutureWarning        Base class for warnings about constructs that will change semantically in the future.
GeneratorExit        Request that a generator exit.
IOError              I/O operation failed.
ImportError          Import can't find module, or can't find name in module.
ImportWarning        Base class for warnings about probable mistakes in module imports
IndentationError     Improper indentation.
IndexError           Sequence index out of range.
KeyError             Mapping key not found.
KeyboardInterrupt    Program interrupted by user.
LookupError          Base class for lookup errors.
MemoryError          Out of memory.
NameError            Name not found globally.
NotImplementedError  Method or function hasn't been implemented yet.
OSError              OS system call failed.
OverflowError        Result too large to be represented.
PendingDeprecationWarning Base class for warnings about features which will be deprecated in the future.
ReferenceError       Weak ref proxy used after referent went away.
RuntimeError         Unspecified run-time error.
RuntimeWarning       Base class for warnings about dubious runtime behavior.
StandardError        Base class for all standard Python exceptions that do not represent interpreter exiting.
StopIteration        Signal the end from iterator.next().
SyntaxError          Invalid syntax.
SyntaxWarning        Base class for warnings about dubious syntax.
SystemError          Internal error in the Python interpreter. Please report this to the Python maintainer, along with the traceback, the Python version, and the hardware/OS platform and version.
SystemExit           Request to exit from the interpreter.
TabError             Improper mixture of spaces and tabs.
TypeError            Inappropriate argument type.
UnboundLocalError    Local name referenced but not bound to a value.
UnicodeDecodeError   Unicode decoding error.
UnicodeEncodeError   Unicode encoding error.
UnicodeError         Unicode related error.
UnicodeTranslateError Unicode translation error.
UnicodeWarning       Base class for warnings about Unicode related problems, mostly related to conversion problems.
UserWarning          Base class for warnings generated by user code.
ValueError           Inappropriate argument value (of correct type).
Warning              Base class for warning categories.
WindowsError         MS-Windows OS system call failed.
ZeroDivisionError    Second argument to a division or modulo operation was zero.
__import__           __import__(name, globals={}, locals={}, fromlist=[], level=-1) -> module Import a module. Because this function is meant for use by the Python interpreter and not for general use it is better to use importlib.import_module() to programmatically import a module. The globals argument is only used to determine the context; they are not modified. The locals argument is unused. The fromlist should be a list of names to emulate ``from name import ...'', or an empty list to emulate ``import name''. When importing a module from a package, note that __import__('A.B', ...) returns package A when fromlist is empty, but its submodule B when fromlist is not empty. Level is used to determine whether to perform absolute or relative imports. -1 is the original strategy of attempting both absolute and relative imports, 0 is absolute, a positive number is the number of parent directories to search relative to the current module.
abs                  abs(number) -> number Return the absolute value of the argument.
all                  all(iterable) -> bool Return True if bool(x) is True for all values x in the iterable. If the iterable is empty, return True.
any                  any(iterable) -> bool Return True if bool(x) is True for any x in the iterable. If the iterable is empty, return False.
apply                apply(object[, args[, kwargs]]) -> value Call a callable object with positional arguments taken from the tuple args, and keyword arguments taken from the optional dictionary kwargs. Note that classes are callable, as are instances with a __call__() method. Deprecated since release 2.3. Instead, use the extended call syntax: function(*args, **keywords).
basestring           Type basestring cannot be instantiated; it is the base for str and unicode.
bin                  bin(number) -> string Return the binary representation of an integer or long integer.
bool                 bool(x) -> bool Returns True when the argument x is true, False otherwise. The builtins True and False are the only two instances of the class bool. The class bool is a subclass of the class int, and cannot be subclassed.
buffer               buffer(object [, offset[, size]]) Create a new buffer object which references the given object. The buffer will reference a slice of the target object from the start of the object (or at the specified offset). The slice will extend to the end of the target object (or with the specified size).
bytearray            bytearray(iterable_of_ints) -> bytearray. bytearray(string, encoding[, errors]) -> bytearray. bytearray(bytes_or_bytearray) -> mutable copy of bytes_or_bytearray. bytearray(memory_view) -> bytearray. Construct an mutable bytearray object from: - an iterable yielding integers in range(256) - a text string encoded using the specified encoding - a bytes or a bytearray object - any object implementing the buffer API. bytearray(int) -> bytearray. Construct a zero-initialized bytearray of the given length.
bytes                str(object='') -> string Return a nice string representation of the object. If the argument is a string, the return value is the same object.
callable             callable(object) -> bool Return whether the object is callable (i.e., some kind of function). Note that classes are callable, as are instances with a __call__() method.
chr                  chr(i) -> character Return a string of one character with ordinal i; 0 <= i < 256.
classmethod          classmethod(function) -> method Convert a function to be a class method. A class method receives the class as implicit first argument, just like an instance method receives the instance. To declare a class method, use this idiom: class C: def f(cls, arg1, arg2, ...): ... f = classmethod(f) It can be called either on the class (e.g. C.f()) or on an instance (e.g. C().f()). The instance is ignored except for its class. If a class method is called for a derived class, the derived class object is passed as the implied first argument. Class methods are different than C++ or Java static methods. If you want those, see the staticmethod builtin.
cmp                  cmp(x, y) -> integer Return negative if x<y, zero if x==y, positive if x>y.
coerce               coerce(x, y) -> (x1, y1) Return a tuple consisting of the two numeric arguments converted to a common type, using the same rules as used by arithmetic operations. If coercion is not possible, raise TypeError.
compile              compile(source, filename, mode[, flags[, dont_inherit]]) -> code object Compile the source string (a Python module, statement or expression) into a code object that can be executed by the exec statement or eval(). The filename will be used for run-time error messages. The mode must be 'exec' to compile a module, 'single' to compile a single (interactive) statement, or 'eval' to compile an expression. The flags argument, if present, controls which future statements influence the compilation of the code. The dont_inherit argument, if non-zero, stops the compilation inheriting the effects of any future statements in effect in the code calling compile; if absent or zero these statements do influence the compilation, in addition to any features explicitly specified.
complex              complex(real[, imag]) -> complex number Create a complex number from a real part and an optional imaginary part. This is equivalent to (real + imag*1j) where imag defaults to 0.
copyright            interactive prompt objects for printing the license text, a list of contributors and the copyright notice.
credits              interactive prompt objects for printing the license text, a list of contributors and the copyright notice.
delattr              delattr(object, name) Delete a named attribute on an object; delattr(x, 'y') is equivalent to ``del x.y''.
dict                 dict() -> new empty dictionary dict(mapping) -> new dictionary initialized from a mapping object's (key, value) pairs dict(iterable) -> new dictionary initialized as if via: d = {} for k, v in iterable: d[k] = v dict(**kwargs) -> new dictionary initialized with the name=value pairs in the keyword argument list. For example: dict(one=1, two=2)
dir                  dir([object]) -> list of strings If called without an argument, return the names in the current scope. Else, return an alphabetized list of names comprising (some of) the attributes of the given object, and of attributes reachable from it. If the object supplies a method named __dir__, it will be used; otherwise the default dir() logic is used and returns: for a module object: the module's attributes. for a class object: its attributes, and recursively the attributes of its bases. for any other object: its attributes, its class's attributes, and recursively the attributes of its class's base classes.
divmod               divmod(x, y) -> (quotient, remainder) Return the tuple ((x-x%y)/y, x%y). Invariant: div*y + mod == x.
enumerate            enumerate(iterable[, start]) -> iterator for index, value of iterable Return an enumerate object. iterable must be another object that supports iteration. The enumerate object yields pairs containing a count (from start, which defaults to zero) and a value yielded by the iterable argument. enumerate is useful for obtaining an indexed list: (0, seq[0]), (1, seq[1]), (2, seq[2]), ...
eval                 eval(source[, globals[, locals]]) -> value Evaluate the source in the context of globals and locals. The source may be a string representing a Python expression or a code object as returned by compile(). The globals must be a dictionary and locals can be any mapping, defaulting to the current globals and locals. If only globals is given, locals defaults to it.
execfile             execfile(filename[, globals[, locals]]) Read and execute a Python script from a file. The globals and locals are dictionaries, defaulting to the current globals and locals. If only globals is given, locals defaults to it.
exit                 None
file                 file(name[, mode[, buffering]]) -> file object Open a file. The mode can be 'r', 'w' or 'a' for reading (default), writing or appending. The file will be created if it doesn't exist when opened for writing or appending; it will be truncated when opened for writing. Add a 'b' to the mode for binary files. Add a '+' to the mode to allow simultaneous reading and writing. If the buffering argument is given, 0 means unbuffered, 1 means line buffered, and larger numbers specify the buffer size. The preferred way to open a file is with the builtin open() function. Add a 'U' to mode to open the file for input with universal newline support. Any line ending in the input file will be seen as a '\n' in Python. Also, a file so opened gains the attribute 'newlines'; the value for this attribute is one of None (no newline read yet), '\r', '\n', '\r\n' or a tuple containing all the newline types seen. 'U' cannot be combined with 'w' or '+' mode.
filter               filter(function or None, sequence) -> list, tuple, or string Return those items of sequence for which function(item) is true. If function is None, return the items that are true. If sequence is a tuple or string, return the same type, else return a list.
float                float(x) -> floating point number Convert a string or number to a floating point number, if possible.
format               format(value[, format_spec]) -> string Returns value.__format__(format_spec) format_spec defaults to ""
frozenset            frozenset() -> empty frozenset object frozenset(iterable) -> frozenset object Build an immutable unordered collection of unique elements.
getattr              getattr(object, name[, default]) -> value Get a named attribute from an object; getattr(x, 'y') is equivalent to x.y. When a default argument is given, it is returned when the attribute doesn't exist; without it, an exception is raised in that case.
globals              globals() -> dictionary Return the dictionary containing the current scope's global variables.
hasattr              hasattr(object, name) -> bool Return whether the object has an attribute with the given name. (This is done by calling getattr(object, name) and catching exceptions.)
hash                 hash(object) -> integer Return a hash value for the object. Two objects with the same value have the same hash value. The reverse is not necessarily true, but likely.
help                 Define the builtin 'help'. This is a wrapper around pydoc.help (with a twist).
hex                  hex(number) -> string Return the hexadecimal representation of an integer or long integer.
id                   id(object) -> integer Return the identity of an object. This is guaranteed to be unique among simultaneously existing objects. (Hint: it's the object's memory address.)
input                input([prompt]) -> value Equivalent to eval(raw_input(prompt)).
int                  int(x=0) -> int or long int(x, base=10) -> int or long Convert a number or string to an integer, or return 0 if no arguments are given. If x is floating point, the conversion truncates towards zero. If x is outside the integer range, the function returns a long instead. If x is not a number or if base is given, then x must be a string or Unicode object representing an integer literal in the given base. The literal can be preceded by '+' or '-' and be surrounded by whitespace. The base defaults to 10. Valid bases are 0 and 2-36. Base 0 means to interpret the base from the string as an integer literal. >>> int('0b100', base=0) 4
intern               intern(string) -> string ``Intern'' the given string. This enters the string in the (global) table of interned strings whose purpose is to speed up dictionary lookups. Return the string itself or the previously interned string object with the same value.
isinstance           isinstance(object, class-or-type-or-tuple) -> bool Return whether an object is an instance of a class or of a subclass thereof. With a type as second argument, return whether that is the object's type. The form using a tuple, isinstance(x, (A, B, ...)), is a shortcut for isinstance(x, A) or isinstance(x, B) or ... (etc.).
issubclass           issubclass(C, B) -> bool Return whether class C is a subclass (i.e., a derived class) of class B. When using a tuple as the second argument issubclass(X, (A, B, ...)), is a shortcut for issubclass(X, A) or issubclass(X, B) or ... (etc.).
iter                 iter(collection) -> iterator iter(callable, sentinel) -> iterator Get an iterator from an object. In the first form, the argument must supply its own iterator, or be a sequence. In the second form, the callable is called until it returns the sentinel.
len                  len(object) -> integer Return the number of items of a sequence or collection.
license              interactive prompt objects for printing the license text, a list of contributors and the copyright notice.
list                 list() -> new empty list list(iterable) -> new list initialized from iterable's items
locals               locals() -> dictionary Update and return a dictionary containing the current scope's local variables.
long                 long(x=0) -> long long(x, base=10) -> long Convert a number or string to a long integer, or return 0L if no arguments are given. If x is floating point, the conversion truncates towards zero. If x is not a number or if base is given, then x must be a string or Unicode object representing an integer literal in the given base. The literal can be preceded by '+' or '-' and be surrounded by whitespace. The base defaults to 10. Valid bases are 0 and 2-36. Base 0 means to interpret the base from the string as an integer literal. >>> int('0b100', base=0) 4L
map                  map(function, sequence[, sequence, ...]) -> list Return a list of the results of applying the function to the items of the argument sequence(s). If more than one sequence is given, the function is called with an argument list consisting of the corresponding item of each sequence, substituting None for missing values when not all sequences have the same length. If the function is None, return a list of the items of the sequence (or a list of tuples if more than one sequence).
max                  max(iterable[, key=func]) -> value max(a, b, c, ...[, key=func]) -> value With a single iterable argument, return its largest item. With two or more arguments, return the largest argument.
memoryview           memoryview(object) Create a new memoryview object which references the given object.
min                  min(iterable[, key=func]) -> value min(a, b, c, ...[, key=func]) -> value With a single iterable argument, return its smallest item. With two or more arguments, return the smallest argument.
next                 next(iterator[, default]) Return the next item from the iterator. If default is given and the iterator is exhausted, it is returned instead of raising StopIteration.
object               The most base type
oct                  oct(number) -> string Return the octal representation of an integer or long integer.
open                 open(name[, mode[, buffering]]) -> file object Open a file using the file() type, returns a file object. This is the preferred way to open a file. See file.__doc__ for further information.
ord                  ord(c) -> integer Return the integer ordinal of a one-character string.
pow                  pow(x, y[, z]) -> number With two arguments, equivalent to x**y. With three arguments, equivalent to (x**y) % z, but may be more efficient (e.g. for longs).
print                print(value, ..., sep=' ', end='\n', file=sys.stdout) Prints the values to a stream, or to sys.stdout by default. Optional keyword arguments: file: a file-like object (stream); defaults to the current sys.stdout. sep: string inserted between values, default a space. end: string appended after the last value, default a newline.
property             property(fget=None, fset=None, fdel=None, doc=None) -> property attribute fget is a function to be used for getting an attribute value, and likewise fset is a function for setting, and fdel a function for del'ing, an attribute. Typical use is to define a managed attribute x: class C(object): def getx(self): return self._x def setx(self, value): self._x = value def delx(self): del self._x x = property(getx, setx, delx, "I'm the 'x' property.") Decorators make defining new properties or modifying existing ones easy: class C(object): @property def x(self): "I am the 'x' property." return self._x @x.setter def x(self, value): self._x = value @x.deleter def x(self): del self._x
quit                 None
range                range(stop) -> list of integers range(start, stop[, step]) -> list of integers Return a list containing an arithmetic progression of integers. range(i, j) returns [i, i+1, i+2, ..., j-1]; start (!) defaults to 0. When step is given, it specifies the increment (or decrement). For example, range(4) returns [0, 1, 2, 3]. The end point is omitted! These are exactly the valid indices for a list of 4 elements.
raw_input            raw_input([prompt]) -> string Read a string from standard input. The trailing newline is stripped. If the user hits EOF (Unix: Ctl-D, Windows: Ctl-Z+Return), raise EOFError. On Unix, GNU readline is used if enabled. The prompt string, if given, is printed without a trailing newline before reading.
reduce               reduce(function, sequence[, initial]) -> value Apply a function of two arguments cumulatively to the items of a sequence, from left to right, so as to reduce the sequence to a single value. For example, reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]) calculates ((((1+2)+3)+4)+5). If initial is present, it is placed before the items of the sequence in the calculation, and serves as a default when the sequence is empty.
reload               reload(module) -> module Reload the module. The module must have been successfully imported before.
repr                 repr(object) -> string Return the canonical string representation of the object. For most object types, eval(repr(object)) == object.
reversed             reversed(sequence) -> reverse iterator over values of the sequence Return a reverse iterator
round                round(number[, ndigits]) -> floating point number Round a number to a given precision in decimal digits (default 0 digits). This always returns a floating point number. Precision may be negative.
set                  set() -> new empty set object set(iterable) -> new set object Build an unordered collection of unique elements.
setattr              setattr(object, name, value) Set a named attribute on an object; setattr(x, 'y', v) is equivalent to ``x.y = v''.
slice                slice(stop) slice(start, stop[, step]) Create a slice object. This is used for extended slicing (e.g. a[0:10:2]).
sorted               sorted(iterable, cmp=None, key=None, reverse=False) --> new sorted list
staticmethod         staticmethod(function) -> method Convert a function to be a static method. A static method does not receive an implicit first argument. To declare a static method, use this idiom: class C: def f(arg1, arg2, ...): ... f = staticmethod(f) It can be called either on the class (e.g. C.f()) or on an instance (e.g. C().f()). The instance is ignored except for its class. Static methods in Python are similar to those found in Java or C++. For a more advanced concept, see the classmethod builtin.
str                  str(object='') -> string Return a nice string representation of the object. If the argument is a string, the return value is the same object.
sum                  sum(sequence[, start]) -> value Return the sum of a sequence of numbers (NOT strings) plus the value of parameter 'start' (which defaults to 0). When the sequence is empty, return start.
super                super(type, obj) -> bound super object; requires isinstance(obj, type) super(type) -> unbound super object super(type, type2) -> bound super object; requires issubclass(type2, type) Typical use to call a cooperative superclass method: class C(B): def meth(self, arg): super(C, self).meth(arg)
tuple                tuple() -> empty tuple tuple(iterable) -> tuple initialized from iterable's items If the argument is a tuple, the return value is the same object.
type                 type(object) -> the object's type type(name, bases, dict) -> a new type
unichr               unichr(i) -> Unicode character Return a Unicode string of one character with ordinal i; 0 <= i <= 0x10ffff.
unicode              unicode(object='') -> unicode object unicode(string[, encoding[, errors]]) -> unicode object Create a new Unicode object from the given encoded string. encoding defaults to the current default string encoding. errors can be 'strict', 'replace' or 'ignore' and defaults to 'strict'.
vars                 vars([object]) -> dictionary Without arguments, equivalent to locals(). With an argument, equivalent to object.__dict__.
xrange               xrange(stop) -> xrange object xrange(start, stop[, step]) -> xrange object Like range(), but instead of returning a list, returns an object that generates the numbers in the range on demand. For looping, this is slightly faster than range() and more memory efficient.
zip                  zip(seq1 [, seq2 [...]]) -> [(seq1[0], seq2[0] ...), (...)] Return a list of tuples, where each tuple contains the i-th element from each of the argument sequences. The returned list is truncated in length to the length of the shortest argument sequence.
#>>>


Getting Objet References with getattr
#>>> li = ['Larry', 'Curly']
#>>> li.pop
<built-in method pop of list object at 0x02A58FA8>
#>>> getattr(li, "pop")
<built-in method pop of list object at 0x02A58FA8>
#>>> getattr(li, "append")("Moe")
#>>> li
['Larry', 'Curly', 'Moe']
#>>> getattr({},"clear")
<built-in method clear of dict object at 0x02A324B0>
#>>> getattr((),"pop")

Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    getattr((),"pop")
AttributeError: 'tuple' object has no attribute 'pop'
#>>>
#>>>
#>>> import odbchelper
#>>> odbchelper.buildConnectionString
<function buildConnectionString at 0x02A9C970>
#>>> getattr(odbchelper, "buildConnectionString")
<function buildConnectionString at 0x02A9C970>
#>>> object = odbchelper
#>>> method  = "buildConnectionString"
#>>> getattr(object, method)
<function buildConnectionString at 0x02A9C970>
#>>> type(getattr(object, method))
<type 'function'>
#>>> import types
#>>> type(getattr(object, method)) == types.FunctionType
True
#>>> callable(getattr(object, method))
True


getattr As a Dispatcher
import statsout
def output(data, format = "text"):
    output_function = getattr(statsout, "output_%s" % format)
    return output_function(data)

Third argument default value returned. Prevents nulls and exceptions
def output(data, format = "text"):
    output_function = getattr(statsout, "output_%s" % format, statsout.output_text)
    return output_function(data)


Filtering Lists
#>>> li = ['a','mpilgrim','foo','b','c','b','d','d']
#>>> li
['a', 'mpilgrim', 'foo', 'b', 'c', 'b', 'd', 'd']
#>>> [elem for elem in li if len(elem) > 1]
['mpilgrim', 'foo']
#>>> [elem for elem in li if elem != "b"]
['a', 'mpilgrim', 'foo', 'c', 'd', 'd']
#>>> [elem for elem in li if li.count(elem) == 1]
['a', 'mpilgrim', 'foo', 'c']

"""
# >>> f = open("/music/singles/kairo.mp3", "rb")
# >>> f
# <open file '/music/singles/kairo.mp3' , mode 'rb' at 010E3988>
# >>> f.mode
# 'rb'
# >>> f.name
# '/music/singles/kairo.mp3'
# >>> f.tell()
# 0
# >>> f.seek(-128, 2)
# >>> f.tell()
# 7542909
# >>> tagData = f.read(128)
# >>> tagData

# >>> f.tell()
# 7543037

# Closing Files
# >>> f
# <open file '/music/singles/kairo.mp3' , mode 'rb' at 010E3988>
# >>> f.closed()
# False
# >>> f.close()
# >>> f
# <closed file '/music/singles/kairo.mp3' , mode 'rb' at 010E3988>
# >>> f.closed()
# True
# >>> f.seek(0)
# Traceback (innermost last):
#     File "<interactive input>", line 1 in ?
# ValueError: I/O operation operation on closed file
# >>> f.tell()
# Traceback (innermost last):
#     File "<interactive input>", line 1 in ?
# ValueError: I/O operation operation on closed file
# >>> f.read()
# Traceback (innermost last):
#     File "<interactive input>", line 1 in ?
# ValueError: I/O operation operation on closed file
# >>> f.close()




# >>> print open.__doc__
# open(name[, mode[, buffering]]) -> file object

# Open a file using the file() type, returns a file object.  This is the
# preferred way to open a file.  See file.__doc__ for further information.
# >>> print file.__doc__
# file(name[, mode[, buffering]]) -> file object

# Open a file.  The mode can be 'r', 'w' or 'a' for reading (default),
# writing or appending.  The file will be created if it doesn't exist
# when opened for writing or appending; it will be truncated when
# opened for writing.  Add a 'b' to the mode for binary files.
# Add a '+' to the mode to allow simultaneous reading and writing.
# If the buffering argument is given, 0 means unbuffered, 1 means line
# buffered, and larger numbers specify the buffer size.  The preferred way
# to open a file is with the builtin open() function.
# Add a 'U' to mode to open the file for input with universal newline
# support.  Any line ending in the input file will be seen as a '\n'
# in Python.  Also, a file so opened gains the attribute 'newlines';
# the value for this attribute is one of None (no newline read yet),
# '\r', '\n', '\r\n' or a tuple containing all the newline types seen.

# 'U' cannot be combined with 'w' or '+' mode.

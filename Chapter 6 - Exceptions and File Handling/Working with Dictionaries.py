import os

# Constructing Pathnames
print os.path.join("c:\\music\\ap\\", "mahadeva.mp3")
print os.path.join("c:\\music\\ap", "mahadeva.mp3")
print os.path.expanduser("~")
print os.path.join(os.path.expanduser("~"), "Python")

# Splitting Pathnames
print os.path.split("c:\\music\\ap\\mahadeva.mp3")
(filepath, filename) = os.path.split("c:\\music\\ap\\mahadeva.mp3")
print filepath
print filename

(shortname, extension) = os.path.splitext(filename)
print shortname
print extension

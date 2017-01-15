import os

for k, v in os.environ.items():
    print "%s = %s" % (k, v)

print "\n".join(["%s = %s" % (k, v) for k, v in os.environ.items()])


import sys

print '\n'.join(sys.modules.keys())


import fileinfo

print '\n'.join(sys.modules.keys())
print fileinfo
print sys.modules['fileinfo']

from fileinfo import MP3FileInfo
print MP3FileInfo.__module__
print sys.modules[MP3FileInfo.__module__]

# sitecustomise.py
# this file can be anywhere in your python path,
# but it usually goes in ${pythondir}/lib/site-packages/

import sys
# sys.setdefaultencoding('iso-8859-1')
print sys.getdefaultencoding()
s = u'La Pe\xf1a'
print s

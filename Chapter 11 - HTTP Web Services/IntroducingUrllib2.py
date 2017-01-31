import httplib
httplib.HTTPConnection.debuglevel = 1
import urllib2
request = urllib2.Request('http://diveintomark.org/xml/atom.xml')
opener = urllib2.build_opener()
feeddata = opener.open(request).read()
print feeddata

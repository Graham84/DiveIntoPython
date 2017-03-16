import httplib
httplib.HTTPConnection.debuglevel = 1
import urllib2
request = urllib2.Request('http://diveintomark.org/xml/atom.xml')
opener = urllib2.build_opener()
feeddata = opener.open(request).read()
print feeddata

# adding Headers with the Request Object
print request
print request.get_full_url()
print request.add_header('User-Agent', 'OpenAnything/1.0 +http://diveintopython.org/')
feeddata = opener.open(request).read()
print feeddataimport httplib
httplib.HTTPConnection.debuglevel = 1
import urllib2
request = urllib2.Request('http://diveintomark.org/xml/atom.xml')
opener = urllib2.build_opener()
feeddata = opener.open(request).read()
print feeddata

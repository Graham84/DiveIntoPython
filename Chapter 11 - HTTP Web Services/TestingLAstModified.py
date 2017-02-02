import urllib2
request = urllib2.Request('http://diveintomark.org/xml/atom.xml')
opener = urllib2.build_opener()
firstdatastream = opener.open(request)
print firstdatastream.headers.dict

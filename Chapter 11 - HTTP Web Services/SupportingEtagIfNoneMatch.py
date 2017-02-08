import urllib2, openanything
request = urllib.Request('http://diveintomark.org/xml/atom.xml')
opener = urllib2.build_opener(
    openanything.DefaultErrorhandler())
firstdatastream = opener.open(request)
firstdatastream.headers.get('ETag')
firstdata = firstdatastream.read()
print firstdata
request.add_header()


import urllib2, openanything
request = urllib.Request('http://diveintomark.org/xml/atom.xml')
opener = urllib2.build_opener(
    openanything.DefaultErrorhandler())
firstdatastream = opener.open(request)
firstdatastream.headers.get('ETag')
firstdata = firstdatastream.read()
print firstdata
request.add_header()
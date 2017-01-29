from xml.dom import minidom
import urllib
usock = urllib.urlopen('http://slashdot.org/slashdot.rdf')
xmldoc = minidom.parse(usock)
usock.close()
print xmldoc.toxml()


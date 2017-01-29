from xml.dom import minidom
contents = "<grammar><ref id = 'bit'><p>0</p><p>1</p></ref></grammar>"
import StringIO
ssock = StringIO.StringIO(contents)
print ssock.read()
print ssock.read()
print ssock.seek(0)
print ssock.seek(15)
print ssock.seek(15)
print ssock.read()
ssock.close()

# Parsing XML from a String (File-like Object Way)
contents = "<grammar><ref id = 'bit'><p>0</p><p>1</p></ref></grammar>"
ssock = StringIO.StringIO(contents)
xmldoc = minidom.parse(ssock)
ssock.close()
print xmldoc.toxml()

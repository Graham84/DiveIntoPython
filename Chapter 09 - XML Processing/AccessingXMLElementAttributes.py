from xml.dom import minidom
xmldoc = minidom.parse('binary.xml')
print xmldoc
print xmldoc.toxml()

reflist = xmldoc.getElementsByTagName('ref')
print reflist
for r in reflist:
    print r.toxml()

bitref = reflist[0]
print bitref.toxml()
print bitref.attributes
print bitref.attributes.keys()
print bitref.attributes.values()
print bitref.attributes["id"]


# Accessing Individual XML Attributes
a = bitref.attributes["id"]
print a
print a.name
print a.value

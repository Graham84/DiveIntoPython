from xml.dom import minidom
xmldoc = minidom.parse('binary.xml')
print xmldoc

reflist = xmldoc.getElementsByTagName('ref')
print reflist

print reflist[0].toxml
print reflist[0].toxml()
print reflist[1].toxml()

firstref = reflist[0]
print firstref.toxml()

plist = firstref.getElementsByTagName("p")
print plist

print plist[0].toxml()
print plist[1].toxml()


# playing around
secondref = reflist[1]
print secondref.toxml()

qlist = secondref.getElementsByTagName("xref")
print qlist

print qlist[0].toxml()
print qlist[1].toxml()

for q in qlist:
    print q

for q in qlist:
    print q.toxml()

# searching is actually recursive
plist = xmldoc.getElementsByTagName("p")
print plist

for p in plist:
    print p.toxml()

print plist[0].toxml()
print plist[1].toxml()
print plist[2].toxml()

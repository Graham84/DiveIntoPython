from xml.dom import minidom
xmldoc = minidom.parse('C:\\Users\\Graham\\Desktop\\Graham\\CIT\\git\\DiveIntoPython\\Chapter 9 - XML Processing\\binary.xml')
print xmldoc
print xmldoc.toxml()

print xmldoc.childNodes
print xmldoc.childNodes[0]
print xmldoc.firstChild
print xmldoc.childNodes[1]

grammarNode = xmldoc.childNodes[1]
print grammarNode
print grammarNode.toxml()

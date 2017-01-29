from xml.dom import minidom
fsock = open('C:\Users\Graham\Desktop\Graham\CIT\git\DiveIntoPython\Chapter 9 - XML Processing\\binary.xml')
xmldoc = minidom.parse(fsock)
fsock.close()
print xmldoc.toxml()

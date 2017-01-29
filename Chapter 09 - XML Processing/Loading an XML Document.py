from xml.dom import minidom
xmldoc = minidom.parse('C:\\Users\\Graham\\Desktop\\Graham\\CIT\\git\\DiveIntoPython\\Chapter 09 - XML Processing\\binary.xml')
print xmldoc
print xmldoc.toxml()

print xmldoc.childNodes
print xmldoc.childNodes[0]
print xmldoc.firstChild
print xmldoc.childNodes[1]

grammarNode = xmldoc.childNodes[1]
print grammarNode
print grammarNode.toxml()


# child nodes can be text
print grammarNode.childNodes
print grammarNode.childNodes[1]
print grammarNode.childNodes[1].toxml()
print grammarNode.childNodes[3]
print grammarNode.childNodes[3].toxml()
print grammarNode.lastChild.toxml()

# drilling Down all the Way to Text
print grammarNode
refNode = grammarNode.childNodes[1]
print refNode
print refNode.childNodes
pNode = refNode.childNodes[2]
print pNode
print pNode.toxml()
print pNode.firstChild
# print pNode.firstChild.data

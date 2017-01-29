def parse_Document(self, node):
    """parse the document node
    The document node by itself isn't interesting (to us), but
    its only child, node.documentElement, is: it's the root node
    of the grammar.
    """
    self.parse(node.documentElement)


def parse_Text(self, node):
    """parse a text node
    The text of a text node is usually added to the output buffer
    verbatim.  The one exception is that <p class='sentence'> sets
    a flag to capitalize the first letter of the next word.  If
    that flag is set, we capitalize the text and reset the flag.
    """
    text = node.data
    if self.capitalizeNextWord:
        self.pieces.append(text[0].upper())
        self.pieces.append(text[1:])
        self.capitalizeNextWord = 0
    else:
        self.pieces.append(text)


def parse_Element(self, node):
    """parse an element
    An XML element corresponds to an actual tag in the source:
    <xref id='...'>, <p chance='...'>, <choice>, etc.
    Each element type is handled in its own method.  Like we did in
    parse(), we construct a method name based on the name of the
    element ("do_xref" for an <xref> tag, etc.) and
    call the method.
    """
    handlerMethod = getattr(self, "do_%s" % node.tagName)
    handlerMethod(node)


def parse_Comment(self, node):
    """parse a comment
    The grammar can contain XML comments, but we ignore them
    """
    pass

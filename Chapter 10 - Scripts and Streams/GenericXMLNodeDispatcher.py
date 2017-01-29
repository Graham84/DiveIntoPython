def parse(self, node):
    parseMethod = getattr(self, "parse_%s" % node.__class__.__name__)
    parseMethod(node)

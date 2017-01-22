htmlSource = """
<html>
<head>
<title>Test Page</title>
</head>
<body>
<ul>
<li><a href=index.html>Home</a></li>
<li><a href=toc.html>Table of Contents</a></li>
<li><a href=history.html>History</a></li>
</body>"""

from BaseHTMLProcessor import BaseHTMLProcessor
parser = BaseHTMLProcessor()
parser.feed(htmlSource)
print parser.pieces
print parser.output()

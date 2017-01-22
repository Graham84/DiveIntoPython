import urllib
# sock = urllib.urlopen("http://www.amazon.co.uk/")
sock = urllib.urlopen("http://www.bbc.co.uk/programmes/b088dp43")
htmlsource = sock.read()
sock.close()

print htmlsource

import urllib, IntroducingUrllister

usock = urllib.urlopen("http://www.bbc.co.uk/programmes/b088dp43")
parser = IntroducingUrllister.URLLister()
parser.feed(usock.read())
usock.close()
parser.close()
for url in parser.urls:
    print url


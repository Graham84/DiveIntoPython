request.eaders
import openanything
opener = urllib2.build_opener(
    openanything.DefaultErrorHandler())
seconddatastream = oener.open(request)
print seconddatastream.status
print seconddatastream.read()


import httplib
import urllib
import urllib2
import json

#curl -XGET -d 'cards=[
#    {"rank":"5","suit":"diamonds"},
#    {"rank":"6","suit":"diamonds"},
#    {"rank":"7","suit":"diamonds"},
#    {"rank":"7","suit":"spades"},s
#    {"rank":"8","suit":"diamonds"},
#    {"rank":"9","suit":"diamonds"}
#]' http://rainman.leanpoker.org/rank

def query(card_list):
    params = json.dumps(card_list)
    req = urllib2.urlopen('http://rainman.leanpoker.org/rank', 'cards=' + params)
    print(req.read())



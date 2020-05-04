import urllib
import urllib2

url = 'http://127.0.0.1:5000/game/start'
values =  {'rows' : 5,
        'columns' : 5}

data = urllib.urlencode(values)
req = urllib2.Request(url,data)
response = urllib2.urlopen(req)
the_page = response.read
print(the_page)

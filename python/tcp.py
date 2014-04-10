
# Read from log file and send to logstash tcp port

import socket
import time
import sys


if len(sys.argv) != 2:
	print 'argument error!'
	exit(1)

filename = sys.argv[1]
f = open(filename, 'r')

# Socket connection
s = socket.socket()
host = socket.gethostname()
port = 9999
s.connect((host, port))
print 'send start'

while 1:
	where = f.tell()
	line = f.readline()
	if not line:
		time.sleep(1)
		f.seek(where)
	else:
		s.send(line),
	





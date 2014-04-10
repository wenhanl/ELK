
# Read from log file and send to logstash tcp port

import socket
import time
import sys

print len(sys.argv)

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

while True:
	for line in f:
		s.send(line)
	time.sleep(5)

print 'success!'
	





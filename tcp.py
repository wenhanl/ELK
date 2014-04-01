
# Read from log file and send to logstash tcp port

import socket

f = open('/tmp/access_log1', 'r')

# Socket connection
s = socket.socket()
host = socket.gethostname()
port = 9999
s.connect((host, port))

for line in f:
	s.send(line)

print 'success!'
	





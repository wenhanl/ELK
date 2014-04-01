import socket

s = socket.socket()
host = socket.gethostname()
port = 9999
s.bind((host, port))

s.listen(5)
while True:
	c, addr = s.accept()
	print 'Got conn', addr
	print c.recv(1024),
	c.close()

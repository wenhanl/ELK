
# Read from log file and send to logstash tcp port

import socket
import time
import sys
import os
'''
def follow(thefile):
    thefile.seek(0,2)
    while True:
        line = thefile.readline()
        if not line:
            time.sleep(0.1)
            continue
        yield line


if __name__ == '__main__':
	if len(sys.argv) != 2:
		print 'argument error!'
		exit(1)

	filename = sys.argv[1]
#	f = open(filename, 'r')

#	for line in f:
#		print line,
#	f.close()
	logfile = open(filename,"r")
	loglines = follow(logfile)
	for line in loglines:
		print line,
'''
filename = sys.argv[1]
f = open(filename, 'r')
while 1:
    where = f.tell()
    line = f.readline()
    if not line:
        time.sleep(1)
        f.seek(where)
    else:
        print line,
	





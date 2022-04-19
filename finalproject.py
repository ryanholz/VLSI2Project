#!/usr/bin/python
import sys
import threading

# Function that outputs a string
def print_str(fileName, threadNum):
	print threadNum, ':', fileName, '\n'
	print 'End of thread\n'

# Read command line inputs
t = []

for i in range(1, len(sys.argv)):
	t.append(threading.Thread(target=print_str, args=(str(sys.argv[i]), i)))

for i in range(0, len(sys.argv)):
	t[i].start();

for i in range(1, len(sys.argv)):
	t[i].join();

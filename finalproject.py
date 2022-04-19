#!/usr/bin/python
import sys
import threading

# Function that outputs a string
def print_str(fileName, threadNum):
	# Open a file and write to it
	wrapper = open(fileName, "wb")

	# Print to file then output closed thread notification
	wrapper.write('{0}: {1}\n'.format(threadNum, fileName))
	print 'End of thread ', threadNum, '\n'
	
	# Close file after finished
	wrapper.close()

# Read command line inputs
t = []

for i in range(1, len(sys.argv)):
	t.append(threading.Thread(target=print_str, args=(str(sys.argv[i]), i)))

for i in range(0, len(sys.argv)):
	t[i].start();

for i in range(1, len(sys.argv)):
	t[i].join();

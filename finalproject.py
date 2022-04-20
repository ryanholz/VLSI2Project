# VLSI 2 Final Project
# Project: 6 - Design Automation 1
#-------------------------------------------
# Group 2 Members:
# - Daniyal Tahsildar
# - Rutvik Desai
# - Ryan Holzhousen
# - Kevin Ferreira
#-------------------------------------------

#!/usr/bin/python
import sys
import threading
# TODO: Uncomment once file is working
#import InputOutputFinger

# Function that outputs a string
def print_str(fileName, threadNum):
	# Open verilog file to read and create a new file and write to it
	wrapper = open('wrapper_{0}'.format(fileName), "wb")
	#socFile = open(fileName, "rb")

	# TODO:
	# Continue to implement once parser is completed

	# Print to file then print end of thread notification
	wrapper.write('/*\n* Wrapper code generated using finalproject.py\n*/\n')
	wrapper.write('{0}: {1}\n'.format(threadNum, fileName))
	print 'End of thread ', threadNum, '\n'
	
	# Close files after finished
	wrapper.close()
	#socFile.close()

# Creating array to hold all the thread data
t = []

# Creating threads 
for i in range(1, len(sys.argv)):
	t.append(threading.Thread(target=print_str, args=(str(sys.argv[i]), i)))

# Start thread execution after thread creation
for i in range(0, len(sys.argv)):
	t[i].start();

# Wait for each thread to finish executing
for i in range(1, len(sys.argv)):
	t[i].join();

print 'Wrapper Generation complete!\n'

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
import os
import threading
import iverilogReader as ivr

# Function that outputs a string
def print_str(fileName, threadNum):
    # Open verilog file to read and create a new file and write to it
    wrapper = open('wrapper_{0}'.format(fileName), "w")

    # Read Module name and store in variable
    ivOutFile = open(fileName, "r")
    moduleName = ivr.findModule(ivOutFile)

    # Read input ports and store in variable
    ivOutFile = open(fileName, "r")
    inputList = ivr. findInputs(ivOutFile)

    # Read output ports and store in variable
    ivOutFile = open(fileName, "r")
    outputList = ivr.findOutputs(ivOutFile)

    # Generate comments at the beginning of file
    wrapper.write('/*\n* Wrapper code generated using finalproject.py\n*\n')
    wrapper.write('* Module name: {0}\n'.format(moduleName))
    wrapper.write('* Inputs: {0}\n'.format(inputList))
    wrapper.write('* Outputs: {0}\n*\n'.format(outputList))
    wrapper.write('* Generate by thread {0}. From file {1}\n'.format(threadNum, fileName))
    wrapper.write('*/\n')

    # Generate module definition
    wrapper.write('module {0} ('.format(moduleName))
    for i in range(0, len(inputList)):
        if '[' in inputList[i]:
            # Skip if data range is present
            pass
        else:
            wrapper.write('{0}, '.format(inputList[i]))
    for i in range(0, len(outputList)):
        if '[' in outputList[i]:
            # Skip input range in module declaration
            pass
        else:
            wrapper.write('{0}'.format(outputList[i]))
            if i < len(outputList) - 1:
                wrapper.write(', ')
    wrapper.write(')\n\n')

    # Declare input signals
    wrapper.write('/*\n* Input Signals\n*/\n')
    i = 0
    while(i < len(inputList)):
        if '[' in inputList[i]:
            wrapper.write('input {0}{1};\n'.format(inputList[i], inputList [i+1]))
            i += 1
        else:
            wrapper.write('input {0};\n'.format(inputList[i]))
        i += 1

    # Declare output signals
    wrapper.write('\n/*\n*Output Signals\n*/\n')
    i = 0
    while(i < len(outputList)):
        if '[' in outputList[i]:
            wrapper.write('output {0}{1};\n'.format(outputList[i], outputList[i+1]))
            i += 1
        else:
            wrapper.write('output {0};\n'.format(outputList[i]))
        i += 1

    # TODO
    # Module instantiation

    # Close files after finished
    wrapper.close()
    ivOutFile.close()

# If no files are given then output an error message
if len(sys.argv) < 2:
    print ('ERROR: No files provided.\nPlease try again.\n')
    sys.exit()

# Creating array to hold all the thread data
t = []

# Creating threads 
for i in range(1, len(sys.argv)):
    t.append(threading.Thread(target=print_str, args=(str(sys.argv[i]), i)))

# Start thread execution after thread creation
for i in range(0, len(sys.argv) - 1):
    t[i].start();

# Wait for each thread to finish executing
for i in range(1, len(sys.argv) - 1):
    t[i].join();

# TODO
# iverilog command using the syntax below
os.system("echo Hello")

# Final Confirmation message
print ('Wrapper Generation complete!\n')
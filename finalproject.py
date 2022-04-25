# VLSI 2 Final Project
# Project: 6 - Design Automation 1
#-------------------------------------------
# Group 2 Members:
# - Daniyal Tahsildar
# - Rutvik Desai
# - Ryan Holzhausen
# - Kevin Ferreira
#-------------------------------------------

#!/usr/bin/python
import sys
import os
import threading
import pyverilogReader as pvr

# Function that outputs a string
def print_str(fileName, threadNum):
    # Open verilog file to read and create a new file and write to it
    wrapper = open('wrapper_{0}'.format(fileName), "w")

    # Read Module name and store in variable
    pvOut = pvr.runPyVerilog(fileName)
    moduleName = pvr.findModule(pvOut)
    
    # Read parameters and store in variable
    parameterList = pvr.findParameters(pvOut)

    # Read input ports and store in variable
    # ivOutFile = open(fileName, "r")
    inputList = pvr.findInputs(pvOut)

    # Read output ports and store in variable
    # ivOutFile = open(fileName, "r")
    outputList = pvr.findOutputs(pvOut)
    
    # print(pvOut)
    # print("Module: {}".format(moduleName))
    # print("Inputs: {}".format(inputList))
    # print("Outputs: {}".format(outputList))

    # Generate comments at the beginning of file
    wrapper.write('/*\n* Wrapper code generated using finalproject.py\n*\n')
    wrapper.write('* Module name: {0}\n'.format(moduleName))
    wrapper.write('* Parameters: {0}\n'.format(parameterList))
    wrapper.write('* Inputs: {0}\n'.format(inputList))
    wrapper.write('* Outputs: {0}\n*\n'.format(outputList))
    wrapper.write('* Generate by thread {0}. From file {1}\n'.format(threadNum, fileName))
    wrapper.write('*/\n')

    # Generate module definition
    wrapper.write('module wrapper_{0} ('.format(moduleName))
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
    
    # Declare parameters
    wrapper.write('/*\n* Parameters\n*/\n')
    i = 0
    while(i < len(parameterList)):
        wrapper.write('localparam {0};\n'.format(parameterList[i]))
        i += 1

    # Declare input signals
    wrapper.write('\n/*\n* Input Signals\n*/\n')
    wrapper.write('input TCK, TDI, TMS, TRST;\n')

    # Declare output signals
    wrapper.write('\n/*\n* Output Signals\n*/\n')
    wrapper.write('output TDO;\n')

    # Declare other signals needed
    wrapper.write('\n/* Additional Signals */\n')
    wrapper.write('reg [31:0] socOutput;\nreg socCLK;\nreg socRST;\nreg socTestSel;\n\n')

    # Instantiate modules
    wrapper.write('jtag_tap #(.WIDTH(32)) JTAG_TAP (.TCK(TCK), .TMS(TMS), .TDI(TDI), .TRST(TRST), .socOutput(socOutput), .TDO(TDO), .socCLK(socCLK), .socRST(socRST)m .socTestSel(socTestSel));\n')

    wrapper.write('{0} #(.WIDTH(32)) ('.format(moduleName))
    i = 0
    while(i < len(inputList)):
        if i != 0:
            wrapper.write(', ')
        if 'clk' in inputList[i]:
            wrapper.write('.{0}(TCK)'.format(inputList[i]))
        if 'dat_o' in inputList[i]:
            wrapper.write('.{0}(socOutput)')
        if 'rst' in inputList[i]:
            wrapper.write('.{0}(TRST)')
        if '[' in inputList[i]:
            pass
        else:
            wrapper.write('.{0}(0)'.format(inputList[i]))
        i += 1

    wrapper.write(')')

    # Close files after finished
    wrapper.close()

# If no files are given then output an error message
if len(sys.argv) < 2:
    print ('ERROR: No files provided.\nPlease try again.\n')
    sys.exit()

# Command to source the necessary files to use pyverilog on the ECE servers
# Note: Comment out the line below if not on ECE servers
os.system("source /usr/local/anaconda3/settings")

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

# Final Confirmation message
print ('Wrapper Generation complete!\n')

# VLSI2Project

Repository for WBSoc can be [found here](https://github.com/apdn/WBSoC)

Repository for Pyverilog library [found here](https://github.com/PyHDI/Pyverilog)

In order to run the necessary code, the Pyverilog library must be installed. This is done by running the terminal command:
pip install pyverilog==1.3.0

To generate the wrapper files, input the following command into the terminal:
python finalproject.py <verilog file 1> <verilog file 2> <verilog file n>

finalproject.py - The logic implemented in this file wraps the modules by integrating all the input and outputs fetched from the pyverilogReader file using Multithreading and command line Argument technique. The inputs passed into the final project script are simply the Verilog files that the user wants wrappers for.

jtag_tap.v - This is the jtag interface that is used to communicate with the module that a wrapper is being created for.

pyverilogReader.v - This file imports the pyverilog library, which contains a variety of functionalities that are useful for handling the reading and writing of Verilog code. The function runPyVerilog takes a Verilog code as input, and runs the pyverilog perser and AST code generator to create a comprehensive analysis of the input file. runPyVerilog also reformats the pyverilog output so that it can be read and interpreted by other functions.

shift_register.v - A 32-bit shift register used to interpret the data from the IP’s single output port

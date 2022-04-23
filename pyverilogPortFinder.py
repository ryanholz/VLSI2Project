import pyverilog

from pyverilog.vparser.parser import VerilogParser
from pyverilog.ast_code_generator.codegen import ASTCodeGenerator

def runPyVerilog(fileName):
    parser = VerilogParser()
    expected_ast = parser.parse(open(fileName).read())
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)
    return expected_code

def reformat(code):
    new = code.replace(';', '; \n')
    new = new.replace('  ', '')
    new = new.replace('\n\n\n', '\n')
    new = new.replace('\n\n', '\n')
    result = []
    word = ''
    for c in new:
        if c != ' ':
            word = word + c
        else:
            result.append(word)
            word = ''
    return result

def moduleFinder(code) :
    index = 0
    for word in code: # For every line in the file
        if word == '\nmodule': # If the word 'module' appears in the line
            moduleName = code[index + 1] # Find module name
            break
        index += 1
    index = 0
    for c in moduleName:
        if c == '\n' or c == '(':
            moduleName = moduleName[:index]
            break
        index += 1            
    return moduleName

def inputFinder(code):
    inputList = [] # Initialize array of inputs
    index = 0
    for word in code: # For every line in the file
        if word == '\ninput': # If the word 'input' appears in the line
            if code[index + 1][0] == '[':
                inputList.append(code[index + 1])
                inputList.append(code[index + 2][:-1])
            else:
                inputList.append(code[index + 1][:-1])
        index += 1
    return inputList

def outputFinder(code):
    outputList = [] # Initialize array of inputs
    index = 0
    for word in code: # For every line in the file
        if word == '\noutput': # If the word 'input' appears in the line
            if code[index + 1][0] == '[':
                outputList.append(code[index + 1])
                outputList.append(code[index + 2][:-1])
            else:
                outputList.append(code[index + 1][:-1])
        index += 1
    return outputList

pvOutput = runPyVerilog("uart_top.v")
pvOutput = reformat(pvOutput)
# print(pvOutput)
print("Module: {}".format(moduleFinder(pvOutput)))
print("Inputs: {}".format(inputFinder(pvOutput)))
print("Outputs: {}".format(outputFinder(pvOutput)))
print("Done")
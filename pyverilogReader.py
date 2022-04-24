import pyverilog

from pyverilog.vparser.parser import VerilogParser
from pyverilog.ast_code_generator.codegen import ASTCodeGenerator

def runPyVerilog(fileName):
    parser = VerilogParser()
    expected_ast = parser.parse(open(fileName).read())
    codegen = ASTCodeGenerator()
    expected_code = codegen.visit(expected_ast)
    new = expected_code.replace(';', '; \n')
    new = new.replace(',', ', \n')
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

def findParameters(code):
    parameterList = [] # Initialize array of inputs
    index = 0
    for word in code: # For every line in the file
        if word == '\nparameter': # If the word 'input' appears in the line
            parameterList.append(code[index + 1] + " = " + code[index + 3][:-1])
        index += 1
    return parameterList

def findModule(code) :
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

def findInputs(code):
    inputList = [] # Initialize array of inputs
    index = 0
    for word in code: # For every line in the file
        if word == '\ninput': # If the word 'input' appears in the line
            if code[index + 1][0] == '[':
                inputList.append(code[index + 1] + ' ')
                inputList.append(code[index + 2][:-1])
            else:
                inputList.append(code[index + 1][:-1])
        index += 1
    return inputList

def findOutputs(code):
    outputList = [] # Initialize array of inputs
    index = 0
    for word in code: # For every line in the file
        if word == '\noutput': # If the word 'input' appears in the line
            if code[index + 1] == 'reg':
                if code[index + 2][0] == '[':
                    outputList.append(code[index + 2] + ' ')
                    outputList.append(code[index + 3][:-1])
                else:
                    outputList.append(code[index + 2][:-1])
            elif code[index + 1][0] == '[':
                outputList.append(code[index + 1] + ' ')
                outputList.append(code[index + 2][:-1])
            else:
                outputList.append(code[index + 1][:-1])
        index += 1
    return outputList

# pvOutput = runPyVerilog("uart_top.v")
# pvOutput = reformat(pvOutput)
# print(pvOutput)
# print("Module: {}".format(findModule(pvOutput)))
# print("Inputs: {}".format(findInputs(pvOutput)))
# print("Outputs: {}".format(findOutputs(pvOutput)))
# print("Done")

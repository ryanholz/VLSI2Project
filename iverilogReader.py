def nextWord(target, source):
    for i, w in enumerate(source):
        if w == target:
            return str(source[i + 1])


def findModule(fileName) :
    for line in fileName: # For every line in the file
        if 'ModuleDef:' in line: # If the word 'module' appears in the line
            theLine = line.split() # Split the line into an array of words
            moduleName = nextWord('ModuleDef:', theLine)
    return moduleName

def findInputs(fileName):
    inputList = [] # Initialize array of inputs
    index = 0
    contents = fileName.readlines()
    for line in contents: # For every line in the file
        if 'Input:' in line: # If the word 'input' appears in the line
            theLine = contents[index].split() # Split the line into an array of words
            inputName = nextWord('Input:', theLine)
            if 'Width:' in contents[index + 1]:
                upperBit = nextWord('IntConst:', contents[index+2].split())
                lowerBit = nextWord('IntConst:', contents[index+3].split())
                inputList.append('[' + upperBit + ':' + lowerBit + '] ' + inputName[:-1])
            else:
                inputList.append(inputName[:-1])
        index += 1
    return inputList

def findOutputs(fileName):
    outputList = [] # Initialize array of inputs
    index = 0
    contents = fileName.readlines()
    for line in contents: # For every line in the file
        if 'Output:' in line: # If the word 'input' appears in the line
            theLine = contents[index].split() # Split the line into an array of words
            outputName = nextWord('Output:', theLine)
            if 'Width:' in contents[index + 1]:
                upperBit = nextWord('IntConst:', contents[index+2].split())
                lowerBit = nextWord('IntConst:', contents[index+3].split())
                outputList.append('[' + upperBit + ':' + lowerBit + '] ' + outputName[:-1])
            else:
                outputList.append(outputName[:-1])
        index += 1
    return outputList

#Find module name and inputs and outputs of given file
file1Name = "testText.txt"
file1 = open(file1Name, "r")
inputList = findInputs(file1)
file1 = open(file1Name, "r")
outputList = findOutputs(file1)
file1 = open(file1Name, "r")
moduleName = findModule(file1)

# Print results
print('Module:', moduleName)
print('Inputs:', inputList)
print('Outputs:', outputList)

# Closing text file
file1.close()
print('Done')
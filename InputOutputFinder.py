def nextWord(target, source):
    for i, w in enumerate(source):
        if w == target:
            return str(source[i+1])

def findModule(fileName)
moduleName = []
    for line in fileName:
        if 'module' in line:
            theLine = line.split()
            indexComment = 999999;
            index = 0
            for w in theLine:
                index += 1
                if w == 'module':
                    indexTarget = index
                if w == '//':
                    indexComment = index
            if indexTarget < indexComment:
                string2 = nextWord('module', theLine)
                if string2 != None:
                    try:
                        string3 = nextWord(string2, theLine)
                        if string3[-1] == ',':
                            string3 = string3[:-1]
                        moduleName.append(string2 + ' ' + string3)
                    except:
                        if string2[-1] == ',':
                            string2 = string2[:-1]
                        moduleName.append(string2)
    return moduleName

def findInputs(fileName):
    inputList = []
    for line in fileName:
        if 'input' in line:
            theLine = line.split()
            indexComment = 999999;
            index = 0
            for w in theLine:
                index += 1
                if w == 'input':
                    indexTarget = index
                if w == '//':
                    indexComment = index
            if indexTarget < indexComment:
                string2 = nextWord('input', theLine)
                if string2 != None:
                    try:
                        string3 = nextWord(string2, theLine)
                        if string3[-1] == ',':
                            string3 = string3[:-1]
                        inputList.append(string2 + ' ' + string3)
                    except:
                        if string2[-1] == ',':
                            string2 = string2[:-1]
                        inputList.append(string2)
    return inputList
                
def findOutputs(fileName):
    outputList = []
    for line in fileName:
        if 'output' in line:
            theLine = line.split()
            indexComment = 999999;
            index = 0
            for w in theLine:
                index += 1
                if w == 'output':
                    indexTarget = index
                if w == '//':
                    indexComment = index
            if indexTarget < indexComment:
                string2 = nextWord('output', theLine)
                if string2 != None:
                    if string2 == 'reg':
                        string3 = nextWord(string2, theLine)
                        try:
                            string4 = nextWord(string3, theLine)
                            if string4[-1] == ',':
                                string4 = string4[:-1]
                            outputList.append(string2 + ' ' + string3 + ' ' + string4)
                        except:
                            if string3[-1] == ',':
                                string3 = string3[:-1]
                            outputList.append(string2 + ' ' + string3)
                    else:
                        try:
                            string3 = nextWord(string2, theLine)
                            if string3[-1] == ',':
                                string3 = string3[:-1]
                            outputList.append(string2 + ' ' + string3)
                        except:
                            if string2[-1] == ',':
                                string2 = string2[:-1]
                            outputList.append(string2)
    return outputList

# find inputs and outputs of given file
file1Name = "wbram.v"
file1 = open(file1Name, "r")
inputList = findInputs(file1)
file1 = open(file1Name, "r")
outputList = findOutputs(file1)

# print results
print('Inputs:', inputList)
print('Outputs:', outputList)

# closing text file
file1.close()
print('Done')

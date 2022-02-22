def openFile(filename) :
    f = open(filename, "r")
    return f.read()

def writeFile(filename, text) :
    f = open(filename, "w")
    f.write(text)



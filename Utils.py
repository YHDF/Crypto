import StringUtils as SU
import FileUtils as FU
# CESAR
def fileToCesar(filename, key, alphalist) :
    text = FU.openFile(filename)
    FU.writeFile('_code.txt', SU.textToCesar(text, key, alphalist))

def cesarTofile(filename,key,alphalist) :
    text = FU.openFile(filename)
    FU.writeFile('_decode.txt', SU.cesarToText(text, key, alphalist))

# VIGENAIRE
def fileToVig(filename, key, alphalist) :
    text = FU.openFile(filename)
    filenameNoExt = filename.split('.')[0]
    FU.writeFile(filenameNoExt+'_code.txt', SU.textToVig(text, key, alphalist))

def vigTofile(filename, key, alphalist) :
    text = FU.openFile(filename)
    filenameNoExt = filename.split('.')[0]
    FU.writeFile(filenameNoExt+'_decode.txt', SU.vigToText(text, key, alphalist))


import StringUtils as SU
import FileUtils as FU
import math

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

## KEY_LENGTH
def get2chars(text, alphalist, index):
    return text[index:index+2];

def removeoccurence(text, alphalist, index) :
    return text[index: index+1 : ]

def find_nth(haystack, needle, n):
    start = haystack.find(needle)
    while start >= 0 and n > 1:
        start = haystack.find(needle, start+len(needle))
        n -= 1
    return start
def getoccurencesindex(text, alphalist):
    pairoccurencetable = []
    tmptext = text
    pairenormalindex = []

    for i in range(len(text)) :
        temparray = []
        firstchars = get2chars(text, alphalist, i)
        if(len(firstchars) < 2):
            break
        tempnormalarray = [0 for x in range(2)]
        tempnormalarray[0] = i
        tempnormalarray[1] = i + 1
        pairenormalindex.append(tempnormalarray)
        tmptext = tmptext.replace(firstchars, '  ', 1)
        indexfistoccurence = tmptext.find(firstchars)
        #print(tmptext)
        #indexfistoccurence = find_nth(tmptext, firstchars, 2)
        temparray = [0 for x in range(2)]
        temparray[0] = indexfistoccurence
        temparray[1] = indexfistoccurence + 1
        pairoccurencetable.append(temparray)
    occurenceresult = []
    normalresult = []
    for i in range(len(pairoccurencetable)):
        if(pairoccurencetable[i][0] != -1) :
            occurenceresult.append(pairoccurencetable[i])
            normalresult.append(pairenormalindex[i])
    distance = []
    for i in range(len(occurenceresult)) :
        distance.append(occurenceresult[i][0] - normalresult[i][0])
    lengthgcd = []
    for i in range(2, 9) :
        dividable = 0
        for item in distance :
            if item % i == 0:
                dividable += 1
        lengthgcd.append(dividable)
    
    gcd = lengthgcd.index(max(lengthgcd)) + 2 
    
    return gcd
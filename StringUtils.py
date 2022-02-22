import unidecode

occurences = []
rateOccurences = []

def toLowerCase(text):
    return text.lower() 

def replaceAccents(text):
    return text.replace(text, unidecode.unidecode(text))

def occurenceOfLetter(text, alphalist) :
    for letter in alphalist :
        occurences.append(text.count(letter))

    return occurences

def rateOfLetter(text, alphalist) :
    for idx in range(len(alphalist)) :
        rateOccurences.append('%.3f'%(occurences[idx]/len(text)))
    
    return rateOccurences

# Chiffrage CESAR
def charToCesar(char, key, alphalist) :
    if char not in alphalist :
        return char

    keyIdx = (alphalist.index(char) + key)

    if keyIdx > 26 :
        listIdx = keyIdx - 26
        return alphalist[listIdx]

    return alphalist[keyIdx]

def cesarToChar(char, key, alphalist) :
    if char not in alphalist :
        return char

    keyIdx = (alphalist.index(char) - key)

    return alphalist[keyIdx]

def textToCesar(text, key, alphalist) :
    result = ""
    for char in text :
        result += charToCesar(char, key, alphalist)

    return result

def cesarToText(text, key, alphalist) :
    result = ""
    for char in text :
        result += cesarToChar(char, key, alphalist)

    return result

# Chiffrage VIGENAIRE
def textToVig(text, key, alphalist) :
    keyIdx = 0
    result = ""

    for char in text :
        result += charToCesar(char, key[keyIdx], alphalist)
        keyIdx += 1
        
        if (keyIdx >= len(key)) :
            keyIdx = 0
            
    return result

def vigToText(text, key, alphalist) :
    keyIdx = 0
    result = ""

    for char in text :
        result += cesarToChar(char, key[keyIdx], alphalist)
        keyIdx += 1
        
        if (keyIdx >= len(key)) :
            keyIdx = 0
            
    return result
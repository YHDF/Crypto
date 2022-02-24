import unidecode
import numpy as np
import math

# Variables globales
ICLangue = 0.0778
prob_lettre_alphabet = 0.0385

# alphabet d'occurrences dans la langue française
frenchOccurences = ['e', 'a', 'i', 's', 'n', 'r', 't', 'o', 'l', 'u', 'd', 'c', 'm', 'p', 'g', 'b', 'v', 'h', 'f', 'q', 'y', 'x', 'j', 'k', 'w', 'z']

# TODO Ajouter toLowerCase et replaceAccents pour toutes les fonctions
def toLowerCase(text):
    return text.lower() 

def replaceAccents(text):
    return text.replace(text, unidecode.unidecode(text))

def clean(text) :
    return replaceAccents(toLowerCase(text))

def occurenceOfLetter(text, alphalist) :
    text = clean(text)
    occurences = []
    for letter in alphalist :
        occurences.append(text.count(letter))

    return occurences

def rateOfLetter(text, alphalist) :
    text = clean(text)
    rateOccurences = []
    occurences = occurenceOfLetter(text, alphalist)

    for idx in range(len(alphalist)) :
        rateOccurences.append('%.3f'%(occurences[idx]/len(text)))
    
    return rateOccurences

# Chiffrage CESAR
def charToCesar(char, key, alphalist) :
    if char not in alphalist :
        return char

    keyIdx = (alphalist.index(char) + key)

    if keyIdx > len(alphalist) :
        listIdx = keyIdx - len(alphalist)
        return alphalist[listIdx]

    return alphalist[keyIdx]

def cesarToChar(char, key, alphalist) :
    if char not in alphalist :
        return char

    keyIdx = (alphalist.index(char) - key)

    return alphalist[keyIdx]

def textToCesar(text, key, alphalist) :
    text = clean(text)
    result = ""
    for char in text :
        result += charToCesar(char, key, alphalist)

    return result

def cesarToText(text, key, alphalist) :
    text = clean(text)
    result = ""
    for char in text :
        result += cesarToChar(char, key, alphalist)

    return result

# Chiffrage VIGENERE
def textToVig(text, key, alphalist) :
    text = clean(text)
    keyIdx = 0
    result = ""

    for char in text :
        result += charToCesar(char, key[keyIdx], alphalist)
        keyIdx += 1
        
        if (keyIdx >= len(key)) :
            keyIdx = 0
            
    return result

def vigToText(text, key, alphalist) :
    text = clean(text)
    keyIdx = 0
    result = ""

    for char in text :
        result += cesarToChar(char, key[keyIdx], alphalist)
        keyIdx += 1
        
        if (keyIdx >= len(key)) :
            keyIdx = 0
            
    return result

# CryptAnalyse
## Attaque bruteforce semi-auto
def attaque_brute_force_sa(text, alphalist): 
    text = clean(text)
    for key in range(len(alphalist)):
        resultText = vigToText(text, [key], alphalist)
        print("\nClé " + str(key) +  " - Texte : " + resultText)
        decision = input("Pour tester la clé suivante, appuyer sur la touche N, sinon S pour stopper. ")

        if(decision == 'S' or decision == 's') :
            return "Exiting..." # TODO choose better string to print
        
## Attaque statistique sru le "e"
def e_attack(text, alphalist) :
    text = clean(text)
    for char in frenchOccurences :
        key = alphalist.index(char) # clé de déchiffrage
        resultText = vigToText(text, [key], alphalist)
        print("\nClé " + str(key) +  " - Texte : " + resultText)
        decision = input("Pour tester la clé suivante, appuyer sur la touche N, sinon S pour stopper. ")

        if(decision == 'S' or decision == 's') :
            return "Exiting..." # TODO choose better string to print


## Attaque par coincidence
# On applique la formule pour le calcul de l'IC
# IC = sigma[q=a -> q=z](nq(nq - 1)/n(n-1))
# avec n le nombre de lettres total du msg
# na le nombre de A, nb le nombre de B, nc le nombre de C etc...
def indexC(text, alphalist) :
    text = clean(text)
    arrayOccurences = occurenceOfLetter(text, alphalist)
    ic = 0.0
    n = len(text)

    for nq in arrayOccurences :
        ic += float((nq * (nq - 1))) / float((n * (n - 1)))

    return float('%.4f'%ic)



## Attaque par doublement de lettre en fin de mot
# On analyse le texte et on essayera de trouver où
# dans le texte on aura deux lettre égales
# après les avoir identifiées, on supposera la lettre
# suivante à ces deux lettre comme "e"
def attaque_doublement_lettre(text, alphalist) :
    text = clean(text)
    charE = ""
    key = 0

    for idxChar in range(len(text)) :
        if((idxChar <= len(text) - 2) and (text[idxChar] == text[idxChar + 1])) :
            # on suppose alors que la lettre à la fin du mot correspond à "e"
            charE = text[idxChar + 2]
            key = alphalist.index(charE) - alphalist.index("e") # décalage
            break
    
    # Si on a trouvé le bon décalage on affiche le résultat
    resultString = cesarToText(text, key, alphalist)
    print("\nClé " + str(key) +  " - Texte : " + resultString)
    decision = input("Pour tester la clé suivante, appuyer sur la touche N, sinon S pour stopper. ")

    if(decision == 'S' or decision == 's') :
        return "Exiting..." # TODO choose better string to print
    # Sinon on fait une attaque statistique sur "e"
    else :
        e_attack(text, alphalist)
        
## KEY_LENGTH
def getnchars(text, alphalist, index, pas):
    return text[index:index+pas];
def getoccurencesindexfor2(text, alphalist):
    pairoccurencetable = []
    tmptext = text
    pairenormalindex = []

    for i in range(len(text)) :
        temparray = []
        firstchars = getnchars(text, alphalist, i, 2)
        if(len(firstchars) < 2):
            break
        tempnormalarray = [0 for x in range(2)]
        tempnormalarray[0] = i
        tempnormalarray[1] = i + 1
        pairenormalindex.append(tempnormalarray)
        tmptext = tmptext.replace(firstchars, '  ', 1)
        indexfistoccurence = tmptext.find(firstchars)
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

def getoccurencesindexfor3(text, alphalist):
    pairoccurencetable = []
    tmptext = text
    pairenormalindex = []

    for i in range(len(text)) :
        temparray = []
        firstchars = getnchars(text, alphalist, i, 3)
        if(len(firstchars) < 3):
            break
        tempnormalarray = [0 for x in range(3)]
        tempnormalarray[0] = i
        tempnormalarray[1] = i + 1
        tempnormalarray[2] = i + 2
        pairenormalindex.append(tempnormalarray)
        tmptext = tmptext.replace(firstchars, '   ', 1)
        indexfistoccurence = tmptext.find(firstchars)
        temparray = [0 for x in range(3)]
        temparray[0] = indexfistoccurence
        temparray[1] = indexfistoccurence + 1
        temparray[2] = indexfistoccurence + 2
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
    for i in range(3, 9) :
        dividable = 0
        for item in distance :
            if item % i == 0:
                dividable += 1
        lengthgcd.append(dividable)
    
    gcd = lengthgcd.index(max(lengthgcd)) + 3
    return gcd

def getoccurencesindexfor4(text, alphalist):
    pairoccurencetable = []
    tmptext = text
    pairenormalindex = []

    for i in range(len(text)) :
        temparray = []
        firstchars = getnchars(text, alphalist, i, 4)
        if(len(firstchars) < 4):
            break
        tempnormalarray = [0 for x in range(4)]
        tempnormalarray[0] = i
        tempnormalarray[1] = i + 1
        tempnormalarray[2] = i + 2
        tempnormalarray[3] = i + 3
        pairenormalindex.append(tempnormalarray)
        tmptext = tmptext.replace(firstchars, '    ', 1)
        indexfistoccurence = tmptext.find(firstchars)
        temparray = [0 for x in range(4)]
        temparray[0] = indexfistoccurence
        temparray[1] = indexfistoccurence + 1
        temparray[2] = indexfistoccurence + 2
        temparray[3] = indexfistoccurence + 3

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
    for i in range(4, 9) :
        dividable = 0
        for item in distance :
            if item % i == 0:
                dividable += 1
        lengthgcd.append(dividable)
    
    gcd = lengthgcd.index(max(lengthgcd)) + 4
    return gcd

def getoccurencesindexfor5(text, alphalist):
    pairoccurencetable = []
    tmptext = text
    pairenormalindex = []

    for i in range(len(text)) :
        temparray = []
        firstchars = getnchars(text, alphalist, i, 5)
        if(len(firstchars) < 5):
            break
        tempnormalarray = [0 for x in range(5)]
        tempnormalarray[0] = i
        tempnormalarray[1] = i + 1
        tempnormalarray[2] = i + 2
        tempnormalarray[3] = i + 3
        tempnormalarray[4] = i + 4
        pairenormalindex.append(tempnormalarray)
        tmptext = tmptext.replace(firstchars, '     ', 1)
        indexfistoccurence = tmptext.find(firstchars)
        temparray = [0 for x in range(5)]
        temparray[0] = indexfistoccurence
        temparray[1] = indexfistoccurence + 1
        temparray[2] = indexfistoccurence + 2
        temparray[3] = indexfistoccurence + 3
        temparray[4] = indexfistoccurence + 4
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
    for i in range(5, 9) :
        dividable = 0
        for item in distance :
            if item % i == 0:
                dividable += 1
        lengthgcd.append(dividable)
    
    gcd = lengthgcd.index(max(lengthgcd)) + 5
    return gcd

def key_len(text, alphalist) :
    occurenceindexfor2=getoccurencesindexfor2(text, alphalist)
    occurenceindexfor3=getoccurencesindexfor3(text, alphalist)
    occurenceindexfor4=getoccurencesindexfor4(text, alphalist)
    occurenceindexfor5=getoccurencesindexfor5(text, alphalist)
    return max([occurenceindexfor2, occurenceindexfor3, occurenceindexfor4, occurenceindexfor4])

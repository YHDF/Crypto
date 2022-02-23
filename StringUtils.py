import unidecode
import numpy as np

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

def key_len(text, alphalist) :
    text = clean(text)
    keyLen_min = 1
    keyLen_max = len(alphalist)
    avgIC_array = dict()
    IC_array = []
    keyLen = 0 # TODO
    for currKeyLen in range(keyLen_min, keyLen_max) :
        for j in range(currKeyLen) : 
            substring = text[j:][::currKeyLen]
            IC_array.append(float(indexC(substring, alphalist)))

        
        avgIC = sum(IC_array)/len(IC_array)
        avgIC_array[currKeyLen] = avgIC

        IC_array = []
        
    return avgIC_array


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
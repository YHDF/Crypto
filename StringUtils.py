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

def occurenceOfLetter(text, alphalist) :
    occurences = []
    for letter in alphalist :
        occurences.append(text.count(letter))

    return occurences

def rateOfLetter(text, alphalist) :
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

# CryptAnalyse
## Attaque bruteforce semi-auto
def attaque_brute_force_sa(text, alphalist): 
    for key in range(len(alphalist)):
        resultText = vigToText(text, [key], alphalist)
        print("\nClé " + str(key) +  " - Texte : " + resultText)
        decision = input("Pour tester la clé suivante, appuyer sur la touche N, sinon S pour stopper. ")

        if(decision == 'S' or decision == 's') :
            return "Exiting..." # TODO choose better string to print
        
## Attaque statistique sru le "e"
def e_attack(text, alphalist) :
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
    text = toLowerCase(text)
    arrayOccurences = occurenceOfLetter(text, alphalist)
    ic = 0.0
    n = len(text)

    for nq in arrayOccurences :
        ic += float((nq * (nq - 1))) / float((n * (n - 1)))

    return float('%.4f'%ic)

def indexC_approx(text, alphalist) :
    text = toLowerCase(text)
    ic = []
    n = len(text)

    for m in range(1, 26):
        icTmp = ((n - m) / (m * (n - 1)) * ICLangue) + ((n * (m - 1)) / ((n - 1) * m) * 0.0385)
        ic.append(icTmp)
        
    print(ic)

def key_len(text, alphalist) :
    keyLen_min = 1
    keyLen_max = len(alphalist)
    avgIC_array = dict()
    IC_array = []
    keyLen = 0
    allIndicesC = []
    for currKeyLen in range(keyLen_min, keyLen_max) :
        for j in range(currKeyLen) : 
            substring = text[j:][::currKeyLen]
            IC_array.append(float(indexC(substring, alphalist)))

        
        avgIC = sum(IC_array)/len(IC_array)
        avgIC_array[currKeyLen] = avgIC

        IC_array = []
        
    # for i in range(1, 10) :
    #     allIndicesC.append(indexC(text, alphist))
    return avgIC_array

# def key_len(text, alphalist) :
#     n = len(text)
#     IC = indexC(text, alphalist)
#     numerator = (n * (ICLangue - prob_lettre_alphabet))
#     denominator = ((n * IC) - IC + ICLangue - (prob_lettre_alphabet * n))
#     result = numerator/denominator

#     return result

## Attaque par doublement de lettre en fin de mot
# On va considérer que les 3 derniers lettres contiennet "e" à la fin du mot
# si on trouve c'est bien, sinon on exécutera une attaque statistique sur "e" 
# à la fin pour déterminer le décalage
def attaque_doublement_lettre(text, alphalist) :
    text = toLowerCase(text)
    text = replaceAccents(text)
    charE = text[-1]
    key = alphalist.index(charE) - alphalist.index("e") # décalage en supposant la fin du mot est "e"

    resultString = cesarToText(text, key, alphalist)
    print("\nClé " + str(key) +  " - Texte : " + resultString)
    decision = input("Pour tester la clé suivante, appuyer sur la touche N, sinon S pour stopper. ")

    if(decision == 'S' or decision == 's') :
        return "Exiting..." # TODO choose better string to print
    else :
        e_attack(text, alphalist)
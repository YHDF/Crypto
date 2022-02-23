from Alphabet import Alphabet
import StringUtils as SU
import FileUtils as FU
import Utils as U
import numpy as np




Alphabet = Alphabet()
alphalist = Alphabet.get_letters().copy()

def fctChoisie(choix, text, key, filename) :
    result = ""
    # switcher = {
    if choix == 1 : result = SU.charToCesar(text, key, alphalist),
    if choix == 2 : result = SU.cesarToChar(text, key, alphalist),
    if choix == 3 : result = SU.textToCesar(text, key, alphalist),
    if choix == 4 : result = SU.cesarToText(text, key, alphalist),
    if choix == 5 : result = SU.textToVig(text, key, alphalist),
    if choix == 6 : result = SU.vigToText(text, key, alphalist),
    if choix == 7 : result = SU.attaque_brute_force_sa(text, alphalist),
    if choix == 8 : result = SU.e_attack(text, alphalist),
    if choix == 9 : result = SU.indexC(text, alphalist),
    if choix == 10 : result = SU.attaque_doublement_lettre(text, alphalist)
    if choix == 11 : result = U.fileToCesar(filename, key, alphalist)
    if choix == 12 : result = U.cesarTofile(filename, key, alphalist)
    if choix == 13 : result = U.fileToVig(filename, key, alphalist)
    if choix == 14 : result = U.vigTofile(filename, key, alphalist)
    
    return result
    # }
    # return switcher.get(choix, "Option invalide.")

while True :
    print(
        "\n\t----- CESAR -----\n"+
        "1. charToCesar\t"+
        "2. cesarToChar\n"+
        "3. textToCesar\t"+
        "4. cesarToText\n"+
        "\n\t----- VIGENERE -----\n"+
        "5. textToVig\t"+
        "6. vigToText\n"+
        "\n\t----- CRYPTANLYSE -----\n"+
        "7. attaque_brute_force_sa\t"+
        "8. e_attack\n"+
        "9. indexC\t\t\t"+
        "10. attaque_doublement_lettre\n"+
        "\n\t----- FICHIERS -----\n"+
        "11. fileToCesar\t"+
        "12. cesarTofile\n"+
        "13. fileToVig\t"+
        "14. vigTofile\n"
    )

    choix = int(input("Choisissez une des options (\"-1\" pour sortir): "))
    text = ""
    filename = ""
    key = 0

    if(choix == 1 or choix == 3 or choix == 5 or choix == 11 or choix == 13) :
        if choix == 11 or choix == 13 :
            filename = input("Entrez le nom du fichier: ")
        else :
            text = input("Entrez le texte à chiffrer: ")

        if choix == 5 or choix == 13 :
            key = input("Entrez la clé de chiffrage (si longueur clé supérieure à 1, mettez des virgules entre les valeurs): ")
            key = key.split(",")
            key = np.array(key, dtype=np.int32)
        else : 
            key = int(input("Entrez la clé de chiffrage: "))
    elif(choix == 2 or choix == 4 or choix == 6 or choix == 12 or choix == 14) :
        if choix == 12 or choix == 14 :
            filename = input("Entrez le nom du fichier: ")
        else :
            text = input("Entrez le texte à déchiffrer: ")
        
        if choix == 6 or choix == 14 :
            key = input("Entrez la clé de déchiffrage (si longueur clé supérieure à 1, mettez des virgules entre les valeurs): ")
            key = key.split(",")
            key = np.array(key, dtype=np.int32)
        else : 
            key = int(input("Entrez la clé de déchiffrage: "))
    elif(choix != -1):
        text = input("Entrez le texte à déchiffrer: ")
        
    if choix == -1 :
        break
    else :
        # print(choix)
        print(fctChoisie(choix, text, key, filename))
        continuer = input("Continue? [Y/N] : ")
        if continuer == "N" or continuer == "n" :
            break

    



# PARTIE TEST
# print(clean("Zé Ànus"))
# print(SU.occurenceOfLetter("objectif lune", alphalist))
# print(SU.rateOfLetter("objectif lune", alphalist))
# print(FU.openFile("testfile.txt"))
# FU.writeFile("testfile.txt", clean("Zé Ànus"))
# print(SU.charToCesar('c', 3, alphalist))
# print(SU.cesarToChar('d', 3, alphalist))
# print(SU.textToCesar('le chiffrement de cesar est pas du tout secure', 3, alphalist))
# print(SU.cesarToText('oh fkliiuhphqw gh fhvdu hvw sdv gx wrxw vhfxuh', 3, alphalist))
# print(SU.cesarToText('oh fkliiuhphqw gh fhvdu hvw sdv gx wrxw vhfxuh', 3, alphalist))
# print(U.cesarTofile('testfile.txt', 3, alphalist)) TODO ajouter les bons fichiers
# print(U.fileToCesar('testfile.txt', 3, alphalist)) TODO meme qu'en haut

# print(SU.textToVig('objectif', [1, 3, 2], alphalist))
# print(SU.vigToText('pelffvji', [1, 3, 2], alphalist))
# print(U.vigTofile('testfile.txt', [1, 3, 2], alphalist))
#print(U.fileToVig('testfile.txt', [1, 3, 2], alphalist))

# print(SU.attaque_brute_force_sa('erqmrxu d wrxwhv hw d wrxv vrbhc ohv elhqyhqxhv', alphalist))
# print(SU.e_attack("erqmrxu d wrxwhv hw d wrxv vrbhc ohv elhqyhqxhv", alphalist))

# print(SU.indexC("crpkrwsmgndrqhnduktwqqkgfwlfvwjvjppqthzvhnfwlbloplcvvujggtgtplvtgcovnbvqdlguh", alphalist))
# indicesC = SU.key_len("crpkrwsmgndrqhnduktwqqkgfwlfvwjvjppqthzvhnfwlbloplcvvujggtgtplvtgcovnbvqdlguh", alphalist)
# print(indicesC)

# # print(SU.indexC_approx("crpkrwsmgndrqhnduktwqqkgfwlfvwjvjppqthzvhnfwlbloplcvvujggtgtplvtgcovnbvqdlguh", alphalist))

# print(SU.attaque_doublement_lettre("suxqhoohkrpphihpphsuhqqhwhvw", alphalist))

# print("JAKXQSWECW"[::3])
# print("JAKXQSWECW"[1:][::3])
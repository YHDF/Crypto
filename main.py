from Alphabet import Alphabet
import StringUtils as SU
import FileUtils as FU
import Utils as U



Alphabet = Alphabet()
alphalist = Alphabet.get_letters().copy()

def clean(text) :
    return SU.replaceAccents(SU.toLowerCase(text))

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

print(SU.attaque_doublement_lettre("suxqhoohkrpphihpphsuhqqhwhvw", alphalist))

# print("JAKXQSWECW"[::3])
# print("JAKXQSWECW"[1:][::3])
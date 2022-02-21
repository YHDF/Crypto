from Alphabet import Alphabet
import StringUtils as SU

Alphabet = Alphabet()
alphalist = Alphabet.get_letters().copy()

def clean(text) :
    return SU.replaceAccents(SU.toLowerCase(text))

print(clean("Zé Ànus"))
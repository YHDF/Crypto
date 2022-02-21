import string


class Alphabet :
    
    
    def __init__(self):
        self._letters = list(string.ascii_lowercase)
        
    def get_letters(self) :
        return self._letters
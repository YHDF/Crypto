import unidecode
    
def toLowerCase(text):
    return text.lower() 

def replaceAccents(text):
    return text.replace(text, unidecode.unidecode(text))
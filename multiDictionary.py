from dictionary import Dictionary
from richWord import RichWord

class MultiDictionary:

    def __init__(self, dizionario = Dictionary()):
        self.dizionario = dizionario

    def loadDic(self, language):
        if language == "English":
            self.dizionario._dizionario = self.dizionario.loadDictionary("resources/English.txt")
        elif language == "Italian":
            self.dizionario._dizionario = self.dizionario.loadDictionary("resources/Italian.txt")
        elif language == "Spanish":
            self.dizionario._dizionario = self.dizionario.loadDictionary("resources/Spanish.txt")
        return self.dizionario._dizionario

    def printDic(self, language):
        parole = self.loadDic(language)
        return self.dizionario.printAll(parole)

    def searchWord(self, words):
        parole_txt = words.split() # crea una lista dividendo le parole presenti in un stringa costituita da
        # più parole
        parole_sbagliate = []
        for parola_txt in parole_txt:
            richword = RichWord(parola_txt)
            if richword.parola in self.dizionario.dizionario:
                richword.corretta = True
            elif richword.parola not in self.dizionario.dizionario:
                richword.corretta = False
                parole_sbagliate.append(parola_txt)
        return parole_sbagliate



m = MultiDictionary()
txt = "cry ciao abby monumento bella aamri"
m.loadDic("Italian")
print(m.searchWord(txt))
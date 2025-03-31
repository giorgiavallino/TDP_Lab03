import time

from multiDictionary import MultiDictionary

class SpellChecker:

    def __init__(self, multiDictionary = MultiDictionary()):
        self.multiDictionary = multiDictionary

    def handleSentence(self, txtIn, language):
        txt = replaceChars(txtIn)
        txt = txt.lower()
        self.multiDictionary.loadDic(language)
        tempo_iniziale = time.time()
        parole_sbagliate = self.multiDictionary.searchLinWord(txt)
        tempo_finale = time.time()
        parole_sbagliate_str = ', '.join(map(str, parole_sbagliate))
        return print(f"Le parole sbagliate sono: {parole_sbagliate_str}.\n"
                f"Il tempo di esecuzione dell'operazione è: {tempo_finale-tempo_iniziale}")

    def printMenu(self):
        print("______________________________\n" +
              "      SpellChecker 101\n"+
              "______________________________\n " +
              "Seleziona la lingua desiderata\n"
              "1. Italiano\n" +
              "2. Inglese\n" +
              "3. Spagnolo\n" +
              "4. Exit\n" +
              "______________________________\n")


def replaceChars(text):
    caratteri_speciali = "\\`*_{}[]()>#+?-.!$%^;,=_~"
    for carattere_speciale in caratteri_speciali:
        text = text.replace(carattere_speciale, "")
    return text

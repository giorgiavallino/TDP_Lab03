import time

from multiDictionary import MultiDictionary

class SpellChecker:

    def __init__(self, multiDictionary = MultiDictionary()):
        self.multiDictionary = multiDictionary

    def handleSentence(self, txtIn, language):
        txt = replaceChars(txtIn)
        txt = txt.lower()
        self.multiDictionary.loadDic(language)
        return self.multiDictionary.searchWord(txt)

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
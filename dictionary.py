class Dictionary:

    def __init__(self, dizionario=[]):
        self._dizionario = dizionario

    @property
    def dizionario(self):
        return self._dizionario

    def __repr__(self):
        return f"{self.dizionario}"

    def __str__(self):
        return f"{self.dizionario}"

    def loadDictionary(self, path):
        with open(path, "r") as file:
            parole = []
            linee = file.readlines()
            for linea in linee:
                linea = linea.replace("\n", "")
                parole.append(linea)
        return parole

    def printAll(self, dizionario_lista):
        return print(*dizionario_lista, sep=", ")
import spellchecker

sc = spellchecker.SpellChecker()

while(True):

    sc.printMenu()

    txtIn = input("Inserisci il numero dell'operazione da svolgere: ")
    # Add input control here!

    letters = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
    digits = set("0123456789")
    char = set(txtIn)

    if not char.isdisjoint(letters) and not char.isdisjoint(digits):
        print("L'input inserito non corrisponde a nessuna operazione!")

    elif txtIn.isalpha():
        print("L'input inserito non corrisponde a nessuna operazione!")

    else:
        if int(txtIn) == 1:
            txtIn = input("Inserisci la tua frase in italiano: ")
            print(txtIn)
            a = sc.handleSentence(txtIn,"Italian")
            print(a)

        elif int(txtIn) == 2:
            txtIn = input("Inserisci la tua frase in Inglese:\n")
            print(sc.handleSentence(txtIn,"English"))
            continue

        elif int(txtIn) == 3:
            txtIn = input("Inserisci la tua frase in Spagnolo:\n")
            print(sc.handleSentence(txtIn,"Spanish"))
            continue

        elif int(txtIn) == 4:
            break

        elif int(txtIn)<1 or int(txtIn)>4:
            print(f"Il numero inserito non corrisponde a nessuna operazione!")
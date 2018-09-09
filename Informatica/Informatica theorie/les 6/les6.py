# Ik kan een functie zo vaak als ik wil aanroepen
def zeg_hallo():
    print("Hello")
    print("Halloooo")

zeg_hallo()
zeg_hallo()
zeg_hallo()

##########################################
# Defineer een functie met default waardes
def naam_printer(var1="Iets",var2="Niets"):
    print(var1,var2)

# Je kan een variabele gebruiken om de waardes door te geven naar de parameter
var3 = "Esther"
naam_printer(var3, "Esther")

# Je mag ook input gebruiken om de gebruiker om input te vragen
var4 = input("Geef je naam: ")
naam_printer(var4)

#########################################
# Een functie kan een return geven van een waarde (opgeslagen in een variabele)
def vermenigvuldig(getal1,getal2):
    som = getal1*getal2
    return som

# Je kan direct de uitkomst van de functie uit printen zonder deze tussentijds op te slaan
print(vermenigvuldig(4,5))

# Maar wil je de uitkomst later nog gebruiken,
# zorg er dan voor dat je deze waarde op slaat in een variabele, anders verdwijnt hij
somsom = vermenigvuldig(4,5)
print(somsom)

# Als ik de variabele opsla kan ik deze ook als input voor de functie gebruiken
somsomsom = vermenigvuldig(somsom, 5)
print(somsomsom)

# Maar ik mag ook functies gebruiken als input voor functies
print(vermenigvuldig(vermenigvuldig(4,5),5))


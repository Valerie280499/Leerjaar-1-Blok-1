# voorbeeld code voor het gebruiken van logische operatoren

a = int(input("Geef a: "))
b = int(input("Geef b: "))

if a == b:
    print("Ze zijn gelijk")
    
elif not a == b:        #a!=b
    print("Ze zijn ongelijk")


if a == 1 and b == 2:
    print("a1b2")
    
elif a == 1 or b == 1:
    print("a of b gelijk aan 1")
    
else:
    print("Geen 1 of 2 opgegeven")


# voorbeeld uitwerking met het algoritme om een boterham met pindakaas en jam te maken
# while loop
# if-elif-else

mes = True
boterham = True
pindakaas = "Gesloten"
jam = "Gesloten"

if pindakaas == "Gesloten":
    print("Pot met pindakaas is dicht, maak open")
    pindakaas = "Open"
elif pindakaas == "Open":
    print("Pot met pindakaas is open")

if jam == "Gesloten":
    print("Pot met jam is dicht, maak open")
    jam = "Open"
elif jam == "Open":
    print("Pot met jam is open")

print("Doe pindakaas op mes")
mes_bezet = True
#getal = int(input("Hoeveel pindakaas zit er op het mes?")

while mes_bezet==True:
    print("Smeer pindakaas")
    bezet = input("Zit er nog pindakaas op het mes? (ja/nee) ")
    """if bezet == 'ja':
        mes_bezet = True
    else:
        mes_bezet = False
    """
    if bezet == "nee":
        mes_bezet = False

print("Klaar met pindakaas smeren")

print("Doe jam op mes")
mes_bezet = True

while mes_bezet==True:
    print("Smeer jam")
    bezet = input("Zit er nog jam op het mes? (ja/nee) ")
    if bezet == "nee":
        mes_bezet = False
    
print("Klaar met jam smeren")

print("Sluit potten")
pindakaas = "Gesloten"
jam = "Gesloten"

klaar = input("Is alles klaar om boterham te eten? (ja/nee) ")
if klaar == 'ja':
    print("Eten maar!")
else:
    print("Dan is er ergens iets fout gegaan")





    


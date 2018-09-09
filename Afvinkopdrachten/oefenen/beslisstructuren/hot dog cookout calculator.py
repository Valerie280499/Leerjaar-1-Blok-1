pak_hotdogs = 10
pak_broodjes = 8

boodschappenlijst = []
lijstje = []
aantal_hotdogs = 0

aantal_pers = int(input('Aantal personen:'))
print(70*'-')

print('hoeveel hot dogs wil iedereen?')
for i in range(aantal_pers):
    i += 1
    lijstje.append(i)
    hotdog_per_pers = int(input('aantal hotdogs:'))
    aantal_hotdogs += hotdog_per_pers
    lijstje.append(hotdog_per_pers)
    boodschappenlijst.append(lijstje)
    lijstje = []
print(70*'-')
    
for i in boodschappenlijst:
    if i[1] is 1:
        print('Persoon',i[0],'wil',i[1],'hotdog')
    else:
        print('Persoon',i[0],'wil',i[1],'hotdogs')
print(70*'-')
  
print('Totaal aantal hotdogs:', aantal_hotdogs)

aantal_pakkenH = aantal_hotdogs/pak_hotdogs
if aantal_pakkenH is pak_hotdogs:
    print('Aantal pakken hotdogs nodig:',aantal_pakkenH)
    print('Er zijn geen hotdogs over!')
else:
    print('Aantal pakken hotdogs nodig:',int(aantal_pakkenH+1))
    print('Aantal hotdogs over:',((int(aantal_pakkenH+1))*pak_hotdogs)-aantal_hotdogs)

aantal_broodjes = aantal_hotdogs
aantal_pakkenB = aantal_broodjes/pak_broodjes
if aantal_pakkenB is pak_broodjes:
    print('Totaal aantal broodjes:', aantal_broodjes)
    print('Er zijn geen broodjes over!')
else:
    print('Aantal pakken broodjes nodig:',int(aantal_pakkenB+1))
    print('Aantal broodjes over:',((int(aantal_pakkenB+1))*pak_broodjes)-aantal_broodjes)
print(70*'-')

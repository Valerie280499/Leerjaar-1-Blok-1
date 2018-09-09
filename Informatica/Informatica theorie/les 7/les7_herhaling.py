# Code behorend bij les7: Herhaling
# Doel: We gaan een 2D lijst maken en daarna parsen

# Hier hebben we wat gegevens, opgehaald uit een bestand of database
# Een aantal patienten, dosis medicijn a en b, en behandelend arts.
pat_id = [1,2,3,4,5]
pat_a_mg = [15,20,30,20,10]
pat_b_mg = [40,60,40,90,50]
pat_dr = ["Berends","Janssen","Janssen","Berends","Berends"]

# Hoe zet ik deze lijsten om naar een 2D lijst?
vb_2dlijst = []

# maak een index aan obv range en de lengte van de lijsten
for i in range(0,len(pat_id)):
    sublijst = [] # maak iedere loop een nieuwe sublijst, zodat de append goed gaat
    #print(pat_id[i])
    #print(pat_a_mg[i])
    #print(pat_b_mg[i])
    #print(pat_dr[i])
    #print(40*"-")

    #vul sublijst met de juiste informatie
    sublijst.append(pat_id[i])
    sublijst.append(pat_a_mg[i])
    sublijst.append(pat_b_mg[i])
    sublijst.append(pat_dr[i])

    #voeg sublijst toe aan de hoofdlijst
    vb_2dlijst.append(sublijst)
    

print(vb_2dlijst)

# Voor iedere patient wil ik nu weten:
# Wat is dosis medicijn a, medicijn b en welke arts?

# Hoe kan ik vanuit de 2D lijst filteren op behandelend arts?

# Pat_id en behandelaar voor iedere patient met dosis medicijn a >= 20

"""
for loop herhaalt voor een geven aantal waardes.

range functie:
de range functie is een handige functie om te combineren met de for loop.

for i in range(4,10):
    print(i)
    

while loop is een herhaalstructuurmet zogenaamde conditionele controle.

doorgaan = "ja"
while doorgaan == "ja":
    doorgaan = input("doorgaan ja/nee")



indez syntax.

enkel element:
string[1]

slice:
string[2:4]

positieve indices:
[2] [:2] [2:] [2:4]

negatieve indices(begin aan het einde met tellen):
[-1] [:-1] [-1:] [-4:-1]



lijsten zijn reeksen met waardes. metlijsten is het mogelijk om een aantal bij elkaar horende items o te slaan

lijst = ["apen","noten","miezen"]
lijst.append("mus")
for element in lijst:
    print(element)

lijst2 = [[1,2],[3,4],[5,6]]
print(lijst2[0])
print(lijst2[1][0])

for element in lijst2:
    print (element[0])


"""


pat_id = [1,2,3,4,5]
pat_a_mg = [15,20,30,20,10]
pat_b_mg = [40,60,40,90,50]
pet_dr = ["Berends", "Jansen","Jansen","Berends","Berends"]
#patient 1 heeft 15 mg van medicijn a, 40 mg van medicijn b en doktor Berends

#hoe zet ik deze lijsten om naar een 2D lijst?
vd_2dlijst=[]

for i in range(len(pat_id)):
    print(pat_a_mg[i])
    sublijst = []
    #sublijst = [pet_id[i], pat_a_mg[i]), pat_b_mg[i], pet_dr[i]]
    sublijst.append(pat_id[i])
    sublijst.append(pat_a_mg[i])
    sublijst.append(pat_b_mg[i])
    sublijst.append(pet_dr[i])

    vd_2dlijst.append(sublijst)
    
    #wat is de dosis van medicijn a, medicijnb en welke arts voor elke patient?
    print("Patien ID:" ,vd_2dlijst[i][0])
    print("Med A:" ,vd_2dlijst[i][1])
    print("Med B:" ,vd_2dlijst[i][2])
    print("Behadelaar:" ,vd_2dlijst[i][3])

# hoe kan ik vanuit de 2D lijst filteren op behandelend arts?
l_B = []
l_J = []
for i in range(len(vd_2dlijst)):
    arts = vd_2dlijst[i][3]
    
    if arts == "Berends":
       l_B.append(vd_2dlijst[1][0])
    
    else:
        l_J.append(vd_2dlijst[i][0])

    print("Alle patienten van dr Berends:" ,l_B)
    print("Alle patienten van dr Jansen:",l_J)
print(vd_2dlijst)




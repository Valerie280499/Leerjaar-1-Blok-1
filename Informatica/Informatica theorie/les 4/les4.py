# Voorbeeldcode uit de presentatie

i = 0
for c in ["Hello", "World","!"]:
    i += 1
    print(c)
    print(i)

for c in range(0,100):
    i += 1
    print(i)

getal = 0
totaal = 0
while getal >= 0:
    getal = int(input("Getal: "))
    totaal += getal
    print("Totaal: ", totaal)


for i in range(1,11):
    for j in range(1,11):
        print(i,"*",j,"=",i*j)

for i in range(0,10):
    print (i)

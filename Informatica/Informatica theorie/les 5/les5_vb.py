# Code voorbeelden die bij de les horen

file = open("test.txt",'r')
#print(type(file))
#print(dir(file))

#Wat is de verwachtte uitkomst van onderstaande voorbeelden?
print(file.read())
print(file.readline())
print(file.readline())

for line in file:
    print(line)

line = file.readline()
while line!="":
    print(line)   
    line=file.readline()
    
newlist = []
for line in file:
    newlist.append(line.strip().split(","))
print(newlist)

for element in newlist:
    print(element[0])


#het is altijd een optie om eerst te openen voor append, af te sluiten
#en daarna te openen voor lezen!

file = open("test.txt",'a') 
file.write("Extra regel")
file.close()

file  = open("test.txt",'r') 
print(file.read())
file.close()

# maar je kan ook gebruik maken van de a+ modus, ook om verder te lezen vanaf een bepaald punt.
# denk aan de positie van de cursor
file = open("test.txt",'a+') #append + modus (dus ook lezen)
file.write("Dit is een testregel voor aanvullen")
file.seek(0, 0) #zet cursor terug naar begin van het bestand
print(file.readline())
file.close()


# hoe kan je loopen met een print?

seq = "ATGCG" #len(seq) gelijk aan 5
letter = "G"

#hoe zat het ook alweer met string indexen?

for seq_index in range(0,len(seq)): #range 0 tot 5, ofwel 0,1,2,3,4
    print(40*"-")
    print(seq[seq_index])
    print(seq)
    print(seq_index*" "+ letter)
    if seq[seq_index] == letter:
        print("match")


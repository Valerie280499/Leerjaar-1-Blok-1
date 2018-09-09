bestand = input ('Voeg een sequentie in:\n')
seq=''
file = open(bestand).readlines()[1:]
print (seq)

for line in file:
    seq+=line.rstrip()

counter = 0
for nuc in seq:
        counter+=1

def TelStikstofbase():
    global A
    global T
    global G
    global C
    global Base
    
    A = seq.count('A')
    T = seq.count('T')
    G = seq.count('G')
    C = seq.count('C')

    print("A:" ,A)
    print("T:" ,T)
    print("G:" ,G)
    print("C:" ,C)
    
    
    Base = A+T+G+C
    print("ATGC:" ,Base)

def TelEiwitten():
    global D
    global E
    global R
    global K

    D = seq.count('D')
    E = seq.count('E')
    R = seq.count('R')
    K = seq.count('K')

    print("D:" ,D)
    print("E:" ,E)
    print("R:" ,R)
    print("K:" ,K)

    Aminozuren = (D+E+R+K)
    print ('Totaal aantal aminozuren:' ,Aminozuren)

def Per():
    global DE
    global KR
    global DERK
    
    #bereken percentages
    DE = ( (D+E)/counter ) * 100
    KR = ( (K+R)/counter ) * 100
    DERK = ( Aminozuren/counter ) * 100

    #en print ze.
    print ('Percentage DE:' ,DE)
    print ('Percentage KR:' ,KR)
    print ('Percentage DERK:' ,DERK)



TelStikstofbase()

print ('lengte van sequentie 1:' ,counter)

#als het aantal stikstofbase niet overeenkomt met de lengte van het bestand dan:
if Base != counter:
    TelEiwitten
    Per
 


if  Base == counter:
    print ('File is een DNA sequentie\n')
    bestand2 = input ('Voeg een eiwit sequentie toe:\n')
    seq=''
    file = open(bestand2).readlines()[1:]
    print (seq)

    for line in file:
        seq+=line.rstrip()

    counter = 0
    for nuc in seq:
        counter+=1

    TelEiwitten
    print ('lengte van sequentie2:' ,counter)
    Per
  
else:
    print ('File is een eiwit sequentie\n')
    bestand2 = input ('Voeg een DNA sequentie toe:\n')
    seq=''
    file = open(bestand2).readlines()[1:]
    print (seq)

    for line in file:
         seq+=line.rstrip()

    counter = 0
    for nuc in seq:
        counter+=1

    TelStikstofbase
    
    print ('lengte van sequentie2:' ,counter)

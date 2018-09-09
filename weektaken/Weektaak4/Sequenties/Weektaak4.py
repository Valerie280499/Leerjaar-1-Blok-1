bestand = input ('Voeg een sequentie in:\n')
seq=''
file = open(bestand).readlines()[1:]
print (seq)

for line in file:
    seq+=line.rstrip()

counter = 0
for nuc in seq:
        counter+=1

#tel D,E,R en K
A = seq.count('A')
R = seq.count('R')
N = seq.count('N')
D = seq.count('D')
C = seq.count('C')
F = seq.count('F')
Q = seq.count('Q')
E = seq.count('E')
G = seq.count('G')
H = seq.count('H')
I = seq.count('I')
L = seq.count('L')
K = seq.count('K')
M = seq.count('M')
P = seq.count('P')
S = seq.count('S')
T = seq.count('T')
W = seq.count('W')
Y = seq.count('Y')
V = seq.count('V')


#print ze dan.
print ('Aantal A:' ,A)
print ('Aantal R:' ,R)
print ('Aantal N:' ,N)
print ('Aantal D:' ,D)
print ('Aantal C:' ,C)
print ('Aantal F:' ,F)
print ('Aantal Q:' ,Q)
print ('Aantal E:' ,E)
print ('Aantal G:' ,G)
print ('Aantal H:' ,H)
print ('Aantal I:' ,I)
print ('Aantal L:' ,L)
print ('Aantal K:' ,K)
print ('Aantal M:' ,M)
print ('Aantal P:' ,P)
print ('Aantal S:' ,S)
print ('Aantal T:' ,T)
print ('Aantal W:' ,W)
print ('Aantal Y:' ,Y)
print ('Aantal V:' ,V)

#print de lengte van de sequentie.
print ('lengte sequentie:', counter)
#tel de aminozuren bij elkaar op.
Aminozuren = (A+R+N+D+C+F+Q+E+G+H+I+L+K+M+P+S+T+W+Y+V)
print ('Totaal aantal eiwitten:' ,Aminozuren)
print ('\n')

#bereken de eiwitgewichten en print ze dan.
GewichtA = 89.094 * A
print ('Gewicht A:', GewichtA)
GewichtR = 174.203 * R
print ('Gewicht R:', GewichtR)
GewichtN = 132.119 * N
print ('Gewicht N:', GewichtN)
GewichtD = 133.104 * D
print ('Gewicht D:', GewichtD)
GewichtC = 121.154 * C
print ('Gewicht C:', GewichtC)
GewichtF = 165.192 * F
print ('Gewicht F:', GewichtF)
GewichtQ = 146.146 * Q
print ('Gewicht Q:', GewichtQ)
GewichtE = 147.131 * E
print ('Gewicht E:', GewichtE)
GewichtG = 75.067 * G
print ('Gewicht G:', GewichtG)
GewichtH = 155.156 * H
print ('Gewicht H:', GewichtH)
GewichtI = 131.175 * I
print ('Gewicht I:', GewichtI)
GewichtL = 131.175 * L
print ('Gewicht L:', GewichtL)
GewichtK = 146.189 * K
print ('Gewicht K:', GewichtK)
GewichtM = 149.208 * M
print ('Gewicht M:', GewichtM)
GewichtP = 115.132 * P 
print ('Gewicht P:', GewichtP)
GewichtS = 105.093 * S
print ('Gewicht S:', GewichtS)
GewichtT = 119.119 * T
print ('Gewicht T:', GewichtT)
GewichtW = 204.228 * W
print ('Gewicht W:', GewichtW)
GewichtY = 181.191 * Y
print ('Gewicht Y:', GewichtY)
GewichtV = 177.148 * V
print ('Gewicht V:', GewichtV)

#gewicht Eiwit + gewicht water. Door condensatiereacties ontstaat er water.
EiwitenWater = GewichtA + GewichtR + GewichtN + GewichtD + GewichtC + GewichtF + GewichtQ + GewichtE + GewichtG + GewichtH + GewichtI + GewichtL + GewichtK + GewichtM + GewichtP + GewichtS + GewichtT + GewichtW + GewichtY + GewichtV 
print ('Gewicht eiwit en water in g/mol:' ,EiwitenWater)
print('\n')

#print de molecuul massa van water.
MolecuulMassaH20 = 18.01528
print ('Gewicht water:' ,MolecuulMassaH20)
print('\n')

#bereken het aantal h20 moleculen en print dit.
H20moleculen = Aminozuren - 1
print ('Aantal H20 moleculen:' ,H20moleculen)
print('\n')

#vermedigvuldig het aantal h20 moleculen met de moleculaire massa van water.
TotaalH20Gewicht = H20moleculen * MolecuulMassaH20
print ('Totaal gewicht water:' ,TotaalH20Gewicht)
print('\n')

#de totale massa is het gewicht van de eiwitten en water min de totale massa van het water en print deze.
EiwitMassa = EiwitenWater - TotaalH20Gewicht
print ('Totaal gewicht:' ,EiwitMassa)

bestandsnaam = input('Bestand.fasta:\n')
seq=' '

bestand = open
(bestandsnaam.readlines()[1:]
for line in bestand:
    seq+=line.rstrip()

print(seq)
aantalC= seq.count('C')
aantalG= seq.count('G')
aantalGC = aantalG+aantalC

A = (aantalGC/len(seq) * 100
print ('GC percentage:' ,A)
B = len (seq)
print ('Lengte van de sequentie:' ,B)

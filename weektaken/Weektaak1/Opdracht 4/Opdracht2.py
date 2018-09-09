b = input ('Input fasta file to check gc-percentage:\n')
file = open(b)
G = 0
C = 0
sum = 0;

for file in file:
    G+= file.count('G')
    C+= file.count('C')
    sum += len(file)
    
totalGC = str(G+C)
totalnucleotides = str(sum) 

print ('total GC:' ,totalGC)
print ('total nucleotides:',totalnucleotides)

print ('GC percentage:' ,(totalGC / totalnucleotides) * 100)

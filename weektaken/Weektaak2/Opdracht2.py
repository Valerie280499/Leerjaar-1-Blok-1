b = input ('Input fasta file to check gc-percentage:\n')
file = open(b)
g = 0
c = 0
sum = 0;

for file in file:
    g+= file.count('g')
    c+= file.count('c')
    sum += len(file)
    
print ('total GC:' + str(g+c))
print ('total nucleotides: ' + str(sum) + '\n')

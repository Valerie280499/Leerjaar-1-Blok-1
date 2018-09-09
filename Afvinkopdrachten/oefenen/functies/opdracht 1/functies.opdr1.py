def main():
    #file = input('inputbestand:')
    base = stikstofbase("dna.fasta")
    for i in base:
        print(i)

def stikstofbase(file):
    dna_file = open(file)
    
    base = []
    counterA = 0
    counterT = 0
    counterG = 0
    counterC = 0
    counter = 0
    
    for line in dna_file:
        dna_file = line.strip()
        for i in line:
            counter += 1
            #print(i)
            if i is 'A':
                counterA+=1
            if i is 'T':
                counterT+=1
            if i is 'G':
                counterG+=1
            if i is 'C':
                counterC+=1

    base.append(counterA)
    base.append(counterT)
    base.append(counterG)
    base.append(counterC)
    return base
main()

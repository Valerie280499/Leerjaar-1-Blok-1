def main():
    seq = open_bestand("genoom.fasta")
    #print(seq)
    zoek_codon(seq)

def open_bestand(file):
    sequentie = open(file).readlines()[1:]
    seq = ''
    for line in sequentie:
        seq+=line.strip()
        
    return seq

def zoek_codon(file):
    #print(file)
    start_codons=['ATG','TTG','GTG','CTG']
    #stop_codons=['TAA','TAG','TGA']
    check = []
    counter = 0
    
    print(file.index('ATG'))
    print(file.index('TTG'))
    print(file.index('GTG'))
    print(file.index('CTG'))
    
        

main()

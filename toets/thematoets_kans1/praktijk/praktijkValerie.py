def main():
    lijst = open_bestand('yeast_genes.csv')
    not_ver = not_validated(lijst)
    for el in lijst:
        if el[1] != 'Veridied':
            if 
    ion_involved(not_ver)

def open_bestand(csv):
    file = open(csv)
    lijst_2d = []
    
    for regel in file:
        sublijst = regel.strip().split(",")
        lijst_2d.append(sublijst)

    return lijst_2d

def not_validated(lijst):
    counter = 0
    not_ver = []
    for el in lijst[1:]:
        if el[1] != 'Verified':
            counter += 1
            not_ver.append(el[0])
    print(counter)
    return not_ver

def ion_involved(lijst):
    for el in lijst:
        print(el)

main()

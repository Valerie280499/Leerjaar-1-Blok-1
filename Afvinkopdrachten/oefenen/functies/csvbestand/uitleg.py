# return functies
def main():
    data = open_bestand("SC_expression.csv")
    get_patid(data[1:])
    gem = get_gemiddelde(data[1:])
    print("Gemiddelde dosis med A", gem[:20])
    


# lezen van csv bestanden

def open_bestand(bestand_naam): #string met bestandsnaam
    csv_file = open(bestand_naam)
    list_2d = []
    print(csv_file)
    for line in csv_file:
        sublijst = line.strip().split(",")
        list_2d.append(sublijst)
    return list_2d
    
def get_patid(pat_data):   #2d
    for lijstje in pat_data:
        
        print("Patient ID:", lijstje[0][:20])
    return

def get_gemiddelde(pat_data): #2d
    totaal = 0
    for lijstje in pat_data:
        totaal += int(lijstje[1])
    gemiddelde = totaal/len(pat_data)    

    return gemiddelde
main()

A = int(input('buget voor deze maand:'))
doorgaan = True
uitgave = 0
while doorgaan == True:
        uitgave += int(input('bedrag:'))
        print ('totale uitgave:' ,uitgave)
        vraag = input('nog meer uitgave?')
        if vraag == 'ja':
            doorgaan = True
        elif vraag == "nee":
            doorgaan = False
            print ('totale uitgave:' ,uitgave)
        else:
            print('error')
            
if uitgave < A:
    verschil = A - uitgave
    print ('je uitgaven zijn kleiner dan je buget:', verschil)

else:
    verschil = uitgave - A
    print ('je uitgaven zijn groter dan je buget:', verschil)

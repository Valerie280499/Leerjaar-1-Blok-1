"""
seq1= input('Eitwit sequentie 1:')
seq2= input('Ewiwit sequentie 2:')

seq4=seq1
seq3=seq2

if len(seq1)<len(seq2):
    for i in range(len(seq1)):
        if seq1[i] == seq2[i]:
            i+=1
            print(i)
        elif i == 0:
                print('Er is geen overeenkomst')

elif len(seq1) > len(seq2):
    for j in range(len(seq3)):
        if seq4[j] == seq3[j]:
            j+=1
            print(j)
        elif j == 0:
            print ('Er is geen overeenkomt')

elif len(seq1) == len(seq2):
    for k in range(len(seq1)):
        if seq1[k] == seq2[k]:
            k+=1
            print(k)
        elif k== 0:
            print ('Er is geen overeenkomst')
"""
bestand1= input('Eiwit sequentie 1:')
bestand2= input('Eiwit sequentie 2:')

seq1=''
for i in open(bestand1).readlines()[1:]:
    seq1+=i.replace('\n','')

    
seq2=''
for i in open(bestand2).readlines()[1:]:
    seq2+=i.replace('\n','')

print(seq1)
print(seq2)
aantal = 0

print (len(seq1))
print (len(seq2))

if len(seq1)>len(seq2):
    for i in range(len(seq2)):
        if seq2[i] == seq1[i]:
            aantal += 1

    print (aantal)
    perc=aantal/max(len(seq1),len(seq2))*100
    print("%.2f" % perc)

else:
    for i in range(len(seq1)):
        if seq1[i] == seq2[i]:
            aantal += 1
    print (aantal)

    perc=aantal/max(len(seq1),len(seq2))*100
    print("%.2f" % perc)

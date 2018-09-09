# red + blue  = purple
# red + yellow = orange 
# blue + yellow = green

"""
pri_colours = ['red','blue','yellow']

print('Kies 2 kleuren: red, blue or yellow')
kleur1 = input('kleur 1')
kleur2 = input('kleur 2')


if kleur1 and kleur2 in pri_colours:
    if kleur1 =='red' and kleur2 =='blue':
        print('red+blue=purple')
    if kleur1 =='red' and kleur2 =='yellow':
        print('red+yellow=orange')
    if kleur1 =='blue' and kleur2 =='yellow':
        print('blue+yellow=green')
else:
    print('je kleuren kloppen niet! probeer het nog eens.')
""" 


combi_1 = ['red','blue','purple']
combi_2 = ['red','yellow','orange']
combi_3 = ['blue','yellow','green']
#combi = [combi_1,combi_2,combi_3]
pri_colours = ['red','blue','yellow']

print('Kies 2 kleuren: red, blue or yellow')
kleur1 = input('kleur 1')
kleur2 = input('kleur 2')

if kleur1 in combi_1 and kleur2 in combi_1:
    print('dat wordt samen:' ,combi_1[2])

elif kleur1 in combi_2 and kleur2 in combi_2:
    print('dat wordt samen:' ,combi_2[2])

elif kleur1 in combi_3 and kleur2 in combi_3:
    print('dat wordt samen:' ,combi_3[2])
else:
    print('error')
    

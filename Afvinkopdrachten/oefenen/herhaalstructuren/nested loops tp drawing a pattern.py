'''
for i in range(1,11):
    for j in range(1,11):
        print(i, '*', j, '=', i*j)
'''
'''
size = 9
for i in range(size):
    #1e loop i = 0; j wordt 1 en print * 
    #2e loop i = 1; j wordt 2 en print **
    #3e loop i = 2; j wordt 3 en print ***
    #4e loop i = 3' j wordt 4 en print ****
    for j in range(i+1):
       print('*',end='')
    print()

for i in range(size):
    for j in range(i+1):
        print(' ', end = '')
    print('#')
    
''' 
'''
populatie = int(input('Starting number of organisms:'))
dag_groei = float(input('Average daily increase:'))
dagen_samen = int(input('Number of days to multiply:'))
print('Dag: 1','populaite:', populatie)
for i in range(dagen_samen-1):
    populatie += (populatie/100)*dag_groei
    #print(populatie)
    print('Dag:',i+2, 'populatie:', populatie )
        #print('dag:',i, 'populatie:',start_nummer)
'''
'''
# +1,6 millimeters per jaar.

years = 25
start_year = 2017

sea_level = 3.4
rising_mm = 0.4


print(start_year,': %.2f' % sea_level,'mm')
for i in range(years):
    start_year += 1
    sea_level += rising_mm
    print(start_year,': %.2f' % sea_level, 'mm')

'''



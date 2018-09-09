a = int(input('item1:'))
b = int(input('item2:'))
c = int(input('item3:'))
d = int(input('item4:'))
e = int(input('item5:'))

total = float(a+b+c+d+e)
tax = (total * 0.7)
totalwtax = total-tax

print ('total price:' ,total)
print ('total tax:' ,tax)
print ('total without tax:' ,totalwtax)

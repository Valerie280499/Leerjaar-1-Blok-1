Bedrag = float(input('Totaal bedrag:'))
# state sales tax = 5%
# county sales tax = 2,5%
# aankoop, state tax, county tax, total tax, total sale(state+county)

StateSale = (Bedrag * 0.05)
CountySale = (Bedrag * 0.025)
TotalSale = (StateSale+CountySale)

print ('Totaal bedrag:' ,Bedrag)
print ('State sales tax:' ,StateSale)
print ('County sales tax:' ,CountySale)
print ('Total sales tax:' , TotalSale)

# Sarvesh Gupta
# Tipper program
# 8/31/2019

def tipper15(bill):
    tip15 = .15 * bill
    return tip15

def tipper20(bill):
    tip20 = .2 * bill
    return tip20


bill=input('What was your bill? ')
bill = float(bill)

x = tipper15(bill)
y = tipper20(bill)
print ('15% tip: $', x)
print ('15% tip: $', y)

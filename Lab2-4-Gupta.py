# Sarvesh Gupta
# Car salesman program
# 8/31/2019

def fullCarPrice(carPrice):
    tax = carPrice * .075
    DL = carPrice * .05
    dealerPrep = 500
    destCharge = 1200

    fullPrice = carPrice + tax + DL + dealerPrep + destCharge

    return fullPrice


carPrice=input('What is the base price of the car? ')
carPrice = float(carPrice)

x = fullCarPrice(carPrice)
print ('Your total is $', x)


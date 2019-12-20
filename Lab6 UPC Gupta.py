# Sarvesh Gupta
# UPC program
# 9/30/2019

def checkUPC(userUPC):
    u = userUPC
    u1 = int(u[0])
    u2 = int(u[1])
    u3 = int(u[2])
    u4 = int(u[3])
    u5 = int(u[4])
    u6 = int(u[5])
    u7 = int(u[6])
    u8 = int(u[7])
    u9 = int(u[8])
    u10 = int(u[9])
    u11 = int(u[10])
    u12 = int(u[11])

    total = int(0)
    total = 3*(u1+u3+u5+u7+u9+u11) + (u2+u4+u6+u8+u10+u12)
    if (total % 10 == 0):
        return ("true")
    else:
        return ("false")


userUPC = input("upc)")
x = checkUPC(userUPC)
print(x)
    

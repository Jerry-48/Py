#25/Feb/2026
#compound interset calculation

p = int(input("Enter your money amount: "))
r = int(input("Enter interest rate: "))
n = int(input("Enter time: "))
a = p * (1 + (r/100))**n
b = a - p
print("compound interset",b)

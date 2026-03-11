#sujalkumar kalena(jerry)
#10/03/2026
#

a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

if a > b and a > c:
    print("a is elder.")
elif b > a and b > c:
    print("b is elder.")
elif c > a and c > b:
    print("c is elder.")
else:
    print("all three are equal.")
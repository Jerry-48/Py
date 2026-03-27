#27/3/26
#pattern
#kalena sujalkumar(jerry)
2
for i in range(5, 0, -1):
    for j in range(1, i + 1):
        print('*', end = '')
    print()
    
    

for i in range(1, 6):
    for j in range(1, i + 1):
        print('*', end = '')
    print()
    
    
rows = 5 # You can change this to make the triangle taller

for i in range(1, rows + 1):
    for j in range(i):
        print(j + i, end="")
    print() # This moves to the next line after each row
    
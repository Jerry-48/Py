#01/april/26
#develop program for 1 to 100 numbers odd 
#kalena sujalkumar(Jerry)

for i in range(1, 100):
     if i % 2 != 0:
         print("odd number:", i)
   
   
#develop a program for 1 to 100 numbers, which is prime or not prime
for n in range(1, 100):
    if n < 2:
        print(f"{n}: Not Prime")
        continue
    
    # Check if n has any factors
    is_p = True
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            is_p = False
            break
            
    status = "Prime" if is_p else "Not Prime"
    print(f"{n}: {status}")
    
    
#
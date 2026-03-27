#27/03/26
#find given number is prime number
#kalena sujalkumar(Jerry)

num = int(input("Enter any number: "))

if num > 1:
    # 2 se lekar num-1 tak check karo
    for i in range(2, num):
        if num % i == 0:
            print("The number", num, "is NOT a prime number.")
            break  # Ek bhi divisor mila toh loop roko
    else:
        # Ye else tab chalega jab loop poora khatam ho jaye (matlab koi divisor nahi mila)
        print("The number", num, "is a PRIME number.")
else:
    print("The number", num, "is NOT a prime number.")
    
 
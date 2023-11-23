number = int(input("Enter the number : "))

fact = 1

if number < 0 :
    print("factorial of negative does not exist")
    
if number == 0:
    print("factorial of 0 is ", 1)
    
if number > 0 :
    for i in range(2 , number + 1):
        fact = fact * i
    print("The Factorial of number is : ", fact)
     
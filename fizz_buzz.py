upper_bound = int(input("Enter an upper bound: "))

for num in range (1,upper_bound + 1):
    if num % 3 == 0 and num % 5 == 0:
        print ("FizzBuzz")
    elif num % 3 == 0:
        print ("Fizz")
    elif num % 5 == 0:
        print ("Buzz")
    else:
        print (num)
        

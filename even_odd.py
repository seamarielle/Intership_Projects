n = int(input("Enter a number: "))
even_odd = ["even" if i % 2 == 0 else "odd" for i in range (1, n+1)]

print (even_odd)
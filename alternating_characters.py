first_char = input("First character: ")
second_char = input("Second character: ")
size = int(input("Size: "))

for i in range(size):
    prefix = "-" * i
    char = first_char if i % 2 == 0 else second_char 
    print (prefix+char)
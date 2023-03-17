#Write a python program that takes an integer and prints all odd numbers up to the integer
Integer = int(input("Enter number: "))
for x in range(1, Integer+1):
    if (x % 2 != 0):
        print(x, end=",")
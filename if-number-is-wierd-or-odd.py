#Given an integer, m, perform the following conditional actions:
#If m  is even, print Weird
#If m is odd and in the inclusive range of 2 to 5, print Not Weird
#If m is odd and in the inclusive range of 6 to 20, print Weird
#If m is odd and greater than  20, print Not Weird

#answer

#!/usr/bin/python3
# checks if a number is weird or not weird

m = int(input())

if m % 2 == 0:
    print("Weird")
elif m % 2 !=0 and m >= 2 and m <= 5:
    print("Not Weird")
elif m % 2 !=0 and m >= 6 and m <= 20:
    print("Weird")
elif m % 2 !=0 and m > 20:
    print("Not Weird")


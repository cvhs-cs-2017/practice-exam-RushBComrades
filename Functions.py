"""1. Write a function that will double any integer (n) and return the result"""

def double(x):
    x = 2 * x
    return x
print(double(9))



"""2.  Write a program that will (1) ask the user for an input value, (2) take
that and double it and  (3) print the result.
Include necessary print statements and address whitespace issues."""
def MoreDouble(a):
    print("Enter a number")
    a = int(input())
    a = a * 2
    return a
print(MoreDouble(2))

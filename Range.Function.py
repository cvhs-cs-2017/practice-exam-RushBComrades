"""Use the range function to print the numbers from 1-20"""

for i in range (1,21):
    print(i)


"""Repeat the exercise above counting by 2's"""
for i in range (1,21,2):
    print(i)



"""Print all the multiples of 5 between 10 and 200 in DECENDING order"""
def by5 ():
    x = 200
    while x > 0:
        if x % 5 == 0:
            print (x)
        x = x - 1
by5()

# Define a procedure, median, that takes three
# numbers as its inputs, and returns the median
# of the three numbers.

# Make sure your procedure has a return statement.

#step1: find the bigger one between (a,b)#
def bigger(a, b):
    if a > b:
        return a
    else:
        return b


# find the median
def median(a, b, c):
    if bigger(a, b) > bigger(b, c):
        return bigger(b, c)
    if bigger(a, b) < bigger(b, c):
        return bigger(a, b)
    else:
        #bigger(a,b) == bigger(b,c)
        return bigger(a,c)



print(median(1, 2, 3))
# >>> 2

print(median(9, 3, 6))
# >>> 6

print(median(7, 8, 7))
# >>> 7

# Define a procedure, median, that takes three
# numbers as its inputs, and returns the median
# of the three numbers.

# Make sure your procedure has a return statement.



# find the median
def median(a, b, c):
    s = [a,b,c]
    return sorted(s)[1]


print(median(1, 2, 3))
# >>> 2

print(median(9, 3, 6))
# >>> 6

print(median(7, 8, 7))
# >>> 7

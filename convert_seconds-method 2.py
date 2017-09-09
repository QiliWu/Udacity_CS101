# Write a procedure, convert_seconds, which takes as input a non-negative
# number of seconds and returns a string of the form
# '<integer> hours, <integer> minutes, <number> seconds' but
# where if <integer> is 1 for the number of hours or minutes,
# then it should be hour/minute. Further, <number> may be an integer
# or decimal, and if it is 1, then it should be followed by second.
# You might need to use int() to turn a decimal into a float depending
# on how you code this. int(3.0) gives 3
#
# Note that English uses the plural when talking about 0 items, so
# it should be "0 minutes".
#


def convert_seconds(n):
    h = int(n//3600)
    m = int((n-3600*h)//60)
    s = n - 3600*h - 60*m
    #unit = {h: 'hours', m: 'minutes', s: 'seconds'}
    #give wrong result when h=m or m=s, cann't have same key
    num = [h,m,s]
    unit = ['hours', 'minutes', 'seconds']
    for i in range(3):
        if num[i]==1:
            unit[i] = unit[i][:-1]
    return str(h) + ' ' + unit[0] + ', ' + str(m) + ' ' + unit[1] + ', ' + str(s) + ' ' + unit[2]
    
    


print convert_seconds(3661)
#>>> 1 hour, 1 minute, 1 second

print convert_seconds(7325)
#>>> 2 hours, 2 minutes, 5 seconds

print convert_seconds(7261.7)
#>>> 2 hours, 1 minute, 1.7 seconds

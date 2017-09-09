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
    h=0
    while h*3600<=n:
        h=h+1
        m=0
        while m*60<=n-3600*(h-1):
            m=m+1
            s=n-3600*(h-1)-60*(m-1)
    if h-1==1:
        h_unit=' hour'
    else:
        h_unit=' hours'
    if m-1==1:
        m_unit=' minute'
    else:
        m_unit=' minutes'
    if s==1:
        s_unit=' second'
    else:
        s_unit=' seconds'
    return str(h-1)+h_unit+', '+str(m-1)+m_unit+', '+str(s)+s_unit
    
    


print convert_seconds(3661)
#>>> 1 hour, 1 minute, 1 second

print convert_seconds(7325)
#>>> 2 hours, 2 minutes, 5 seconds

print convert_seconds(7261.7)
#>>> 2 hours, 1 minute, 1.7 seconds

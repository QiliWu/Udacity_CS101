# Numbers in lists by SeanMc from forums
# define a procedure that takes in a string of numbers from 1-9 and
# outputs a list with the following parameters:
# Every number in the string should be inserted into the list.
# If a number x in the string is less than or equal
# to the preceding number y, the number x should be inserted
# into a sublist. Continue adding the following numbers to the
# sublist until reaching a number z that
# is greater than the number y.
# Then add this number z to the normal list and continue.

#Hint - "int()" turns a string's element into a number


def biggest(string):
    r=0
    i=0
    while i<len(string):
        if int(string[i])>r:
            r=int(string[i])
        else:
            r=r
        i=i+1
    return r

def numbers_in_lists2(string):
    result=[int(string[0])]
    i=1
    while i<len(string):
        sign=1
        next=[]
        if int(string[i])>biggest(string[:i]):
            result.append(int(string[i]))
            i=i+1
        else:
            next.append(int(string[i]))
            while sign:
                if i+1<len(string)and int(string[i+1])<=biggest(string[:i]):
                    next.append(int(string[i+1]))
                else:
                    sign=0
                i=i+1
            result.append(next)
    return result

print numbers_in_lists2('543987')
print numbers_in_lists2('987654321')
print numbers_in_lists2('455532123266')
print numbers_in_lists2('123456789')
string = '543987'

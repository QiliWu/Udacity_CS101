# By Websten from forums
#
# Given your birthday and the current date, calculate your age in days.
# Account for leap days.
#
# Assume that the birthday and current date are correct dates (and no
# time travel).
#


def Isleapyear(year):
    if year%400 == 0:
        return True
    elif year%100 == 0:
        return False
    elif year%4 == 0:
        return True
    return False


def daysInMonth(year, month):
    if month in [1,3,5,7,8,10,12]:
        return 31
    elif month == 2 and Isleapyear(year):
        return 29
    elif month == 2 and not Isleapyear(year):
        return 28
    return 30


def daysInYear(year):
    if Isleapyear(year):   #forgot the year in () at first
        return 366
    else:
        return 365

def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    days_a, days_b, days_c = 0, day1, day2
    if year1 < year2:
        for i in range(year1,year2):
            days_a = days_a + daysInYear(i)
            #print days_a


    if month1 > 1:
        for j in range(1,month1):
            days_b = days_b + daysInMonth(year1,j)
            #print days_b

    if month2 >1:
        for k in range(1,month2):
            days_c = days_c + daysInMonth(year2,k)
            #print days_c

    total_days = days_a + days_c - days_b
    return total_days


# Test routine

def test():
    test_cases = [((2012,1,1,2012,2,28), 58),
                  ((2012,1,1,2012,3,1), 60),
                  ((2011,6,30,2012,6,30),366),
                  ((2011,1,1,2012,8,8), 585),
                  ((1900,1,1,1999,12,31), 36523)]
    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print "Test with data:", args, 'failed'
        else:
            print 'Test case passed!'

test()








    

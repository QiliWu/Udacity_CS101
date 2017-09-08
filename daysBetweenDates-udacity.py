# By Websten from forums
#
# Given your birthday and the current date, calculate your age in days.
# Account for leap days.
#
# Assume that the birthday and current date are correct dates (and no
# time travel).
#
def is_leap_year(year):
    if year%400==0:
        return True
    if year%100==0:
        return False
    if year%4==0:
        return True
    return False


def daysInMonth(year,month):
    if month==1 or month==3 or month==5 or month==7\
       or month==8 or month==10 or month==12:
        return 31
    else:
        if month==2:
            if is_leap_year(year):
                return 29
            else:
                return 28
        return 30


def nextday(year,month,day):
    if day<daysInMonth(year,month):
        return (year,month,day+1)
    if day==daysInMonth(year,month):
        if month<12:
            return (year,month+1,1)
        else:
            return (year+1,1,1)


def dateIsBefore(year1,month1,day1,year2,month2,day2):
    if year1<year2:
        return True
    if year1==year2:
        if month1<month2:
            return True
        if month1==month2:
            if day1<day2:
                return True
    return False


def daysBetweenDates(year1,month1,day1,year2,month2,day2):
    result=0
    while dateIsBefore(year1,month1,day1,year2,month2,day2):
        result=result+1
        year1,month1,day1=nextday(year1,month1,day1)
    return result


# Test routine  ****

def test():
    test_cases = [((2012,1,1,2012,2,28), 58),
                  ((2012,1,1,2012,3,1), 60),
                  ((2011,6,30,2012,6,30), 366),
                  ((2011,1,1,2012,8,8), 585 ),
                  ((1900,1,1,1999,12,31), 36523)]
    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print "Test with data:", args, "failed"
        else:
            print "Test case passed!"

test()

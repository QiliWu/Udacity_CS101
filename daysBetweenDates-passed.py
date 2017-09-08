daysInMonth =[31,28,31,30,31,30,31,31,30,31,30,31]
   
def daystoYearStart(year,month,day):
    d,m=0,1
    while m<month:
        if year%4!=0:
            daysInMonth[1]=28
        else:
            if (year)%100!=0 or (year2)%400==0:
               daysInMonth[1]=29
        d=d+daysInMonth[m-1]
        m=m+1
    return d+day

def leapyears(year1,year2):
    i,j=0,0
    while i<=year2-year1:
        if (year1+i)%4!=0:
            j=j
        else:
            if (year1+i)%100!=0 or (year1+i)%400==0:
                j=j+1
        i=i+1
    return j

def daysBetweenDates(year1,month1,day1,year2,month2,day2):
    a=daystoYearStart(year2,month2,day2)-daystoYearStart(year1,month1,day1)
    b=(year2-year1)*365
    c=leapyears(year1,year2-1)
    n=a+b+c
    if year1==year2:
        return a
    return n



print daysBetweenDates(1989,5,4,2017,7,3)
print daysBetweenDates(1990,12,11,2017,7,3)
print daysBetweenDates(2011,6,30,2012,6,30)
print daysBetweenDates(2011,1,1,2012,8,8)
print daysBetweenDates(1900,1,1,1999,12,31)


    

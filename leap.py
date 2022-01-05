'''The year can be evenly divided by 4, is a leap year, unless:

    The year can be evenly divided by 100, it is NOT a leap year, unless:
        The year is also evenly divisible by 400. Then it is a leap year.'''

def leap(year):

    leap = False
    if year % 4 == 0 and year % 100 == 0:
        if year % 100 != 0 and year % 400 == 0 :
            return True
        
print(leap(2000))


n = 5 
count = 0
for i in n:
        count +=1
        print(count)
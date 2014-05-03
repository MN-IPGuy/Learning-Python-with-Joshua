UserYear = int(input ("Enter a year (yyyyy) to calculate if it is a Leap Year or not: "))
if (UserYear % 4) == 0:
    if (UserYear % 100 == 0):
        if (UserYear % 400 == 0):
            print (UserYear, "is a Leap Year!!!!!")
        else:
            print(UserYear, "is not a Leap Year") 
    else:
        print(UserYear, "is a Leap Year!!!!!")
else:
    print(UserYear, "is not a Leap Year")

cal = { "January":31 , "February":28 , "March":31 , "April":30 , "May":31 , "June":30 ,
        "July":31 , "August":31 , "September":30 , "October":31 , "November":30 ,
        "December":31}
#a
month = input("Enter a month name :")
for i in cal.keys():
    if i == month:
        print(i , "has",cal[i],"days.")
        break
else:
    print("Invalid month")
print()
#b
cal = dict(sorted(cal.items()))
print("months in alphabetic order",cal.keys())
print()
#c
list31 = []
for i in cal.keys():
    if cal[i] == 31:
        list31.append(i)
print("months with 31 days :" , list31)
print()
#d
cal = dict(sorted(cal.items(), key=lambda item: item[1]))
print("sorted dictionary with no.of days",cal)

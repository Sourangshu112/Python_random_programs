lst1 =eval(input("Enter a list :"))
lst2 =eval(input("Enter a list as same length of previous one :"))
if len(lst1) != len(lst2):
    print("List are not of same length.")
else:
    for i in range (len(lst1)):
        if lst1[i] == lst2[i]:
            continue
        else:
            print("The first index in which they differ is : ",i)
            break

str_list = []
str_list = eval(input("Enter a list of strings :"))
lent = len(str_list)
if lent == 0:
    print("Enter atleast one string")
else:
    long = 0
    x=0
    for i in range(1,lent):
        if len(str_list[x]) > len(str_list[i]):
            long = len(str_list[x])
        else:
            long = len(str_list[i])
            x=i
    print("The length of the longest string is ",long)


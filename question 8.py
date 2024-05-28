lst=[]
lst = eval(input("Enter a list of numbers :"))
lst.sort()
maxi = lst[-1]
ln = len(lst)
for i in range (ln):
    for j in range(i+1,ln-1):
        if lst[i] == lst[i+1]:
            temp = lst[i+1]
            del lst[i+1]
            lst.append(temp)
    if lst[i] == maxi:
        break
print("List with all duplicate vale at the end :",lst)

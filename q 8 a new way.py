lst = []
lst = eval(input("Enter a list"))
lst.sort()
maxi = lst[-1]
ln = len(lst)
i = 0
while True:
    for j in range(i+1,ln-1):
        if lst[i] == lst[i+1]:
            temp = lst[i+1]
            del lst[i+1]
            lst.append(temp)
    i = i+1
    if lst[i] == maxi:
        break
print(lst)

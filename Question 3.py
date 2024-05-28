d1 = dict(a = 1,b = 2,c = 3,d = 4,e = 5)
d2 = dict(a = 1,e = 2,i = 3,o = 4,u = 5)
lst = []
for i in (d1.keys()):
    for j in (d2.keys()):
        if i == j:
            lst.append(i)
            break
print("The first dictionary",d1)
print("The second dictionary",d2)
print("The common element of both the dictionary is :",end=" " )
print(lst)

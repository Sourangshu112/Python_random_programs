lst = []
while True:
    a = input("Enter a number(q to quit)")
    if a == "Q" or a == "q":
        break
    else:
        lst.append(int(a))
print(lst)
lst.sort()
rang = lst[-1] - lst[0]
print("Range is = ",rang)

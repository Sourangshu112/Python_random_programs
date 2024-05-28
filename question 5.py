tup=()
tup = eval(input("Enter a tuple :- "))
new_tup =()
j = 0
for i in tup:
    if j % 3 == 0:
        new_tup = new_tup+(i,)
    j=j+1
print("The original tuple:-")
print(tup)
print("The new tuple with every 3rd element from the original tuple is :-")
print(new_tup)

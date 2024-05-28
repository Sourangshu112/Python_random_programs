L=[]
L2=[]
L=eval(input("Enter a list of numbers :"))
x=int(input("Enter a number to be summed :"))
for i in L:
    a = i+x
    L2.append(a)
print("List of number summed is :",L2)

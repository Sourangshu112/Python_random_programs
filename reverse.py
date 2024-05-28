n = int(input("Enter a number greater than 1000 "))
a , y = n , 0
if n > 1000:
    while(a > 0):
        x=a%10
        y=y*10+x
        a=a//10
    print("The reverse number is" ,y) 
else:
    print("Enter a number greater than thousand")
        

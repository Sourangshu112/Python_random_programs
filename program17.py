file = open("article.txt","r")
str = file.read()

#1
l = len(str)
print("No of characters :",l)

#2
a=0
for i in str:
    if i.isalpha():
        a=a+1
print("No of alphabets: ",a)

#3
u=0
for i in str:
    if i.isupper():
        u=u+1
print("No of upper case alphabets: ",u)

#4
low=0
for i in str:
    if i.islower():
        low=low+1
print("No of lower case alphabets: ",low)

#5
d=0
for i in str:
    if i.isdigit():
        d=d+1
print("No of digits: ",d)

#^
s=0
for i in str:
    if i.isspace():
        s=s+1
print("No of spaces: ",s)

#7
sp=0
for i in str:
    if not i.isalnum() and not i.isspace():
        sp=sp+1
print("No of special: ",sp)
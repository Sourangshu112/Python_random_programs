f = open("forpg1.txt","r")
s = f.read()
f.close()
x = ""
i = 0
while i < len(s):
    if s[i]== " " and s[i+1] == " ":
        x = x+" "
        i = i + 1
    else:
        x = x + s[i]
    i = i + 1
f = open("forpg1n.txt","w")
f.write(x)
f.close()
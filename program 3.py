f = open("Report.txt","r")
def countlines_ET():
    text = f.readlines()
    countE = 0
    countL = 0
    print(text)
    for i in text:
        if i[0] == "E" or i[0] == "e":
            countE += 1
        elif i[0] == "L" or i[0] == "l":
            countL += 1
        else:
            continue
    print("Number is lines beginning with E = " , countE)
    print("Number is lines beginning with L = " , countL)

countlines_ET()

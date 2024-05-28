import csv
def DispEMP():
    file = open("emp.csv","r")
    data = csv.reader(file)
    for i in data:
        if int(i[2]) >= 4000:
            print(i[1],"has a salary of 4000 or above.")
    else:
        file.close()

DispEMP()

import pickle
def CreateFile():
    file = open("Names.dat","wb")
    while True:
        name = input("Enter a name :")
        pickle.dump(name,file)
        choice = input("For exit (enter e/E) :")
        if choice == "e" or choice == "E":
            print("Thank You \n")
            break
    file.close()
def scount():
    file = open("Names.dat","rb")
    count = 0
    try:
        while True:
            data = pickle.load(file)
            if data[0] == "S" or data[0] == "s":
                count += 1
    except EOFError:
        file.close()
    print("Number of names beginning with 'S' is :",count)

CreateFile()
scount()

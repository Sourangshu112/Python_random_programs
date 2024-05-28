def PUSH(hostel):
    N = []
    no = input("Enter the number of the hostel :")
    stu = input("Enter total number of students :")
    room = input("Enter number of rooms :")
    N = [no,stu,room]
    hostel.append(N)

def POP(hostel):
    if country_name != []:
        X = hostel.pop()
        print("Hostel number :",X[0])
        print("Number of student :",X[1])
        print("Number of Rooms :",X[2])
    else:
        print("Empty Stack of hostel.")

def SHOW(hostel):
    for i in hostel:
        print("Hostel number :",i[0])
        print("Number of student :",i[1])
        print("Number of Rooms :",i[2])
            
Stack = []
choice = ''
while choice != 'Q':
    print("P:Push , O:POP , S:SHOW , Q:QUIT")
    choice = input("Enter your choice :")
    if choice == 'P':
        PUSH(Stack)
    elif choice == 'O':
        POP(Stack)
    elif choice == 'S':
        SHOW(Stack)
    elif choice == 'Q':
        print("Thank You !!")
        break
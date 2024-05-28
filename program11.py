def PUSH(country_name):
    ename = input("Enter the name of the country :")
    country_name.append(ename)

def POP(country_name):
    if country_name != []:
        print(country_name.pop())
    else:
        print("Empty Stack of Encyclopedia.")

def SHOW(country_name):
    print(country_name)
    
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
        break


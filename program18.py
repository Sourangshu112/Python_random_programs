while True:
    isdigit=False
    len8=False
    special=False
    #check data
    file = open("security.txt","r")
    a = file.readlines()
    file.close()
    x=dict()
    for i in a:
        t=((i.rstrip("\n")).split(","))
        x[t[0]]=t[1]
    #Take new
    uid = input("Enter a userid :")
    if uid in x.keys():
        print("Username already exists enter a new one")
        continue
    password = input("Enter a password :")
    #check length
    if len(password) >= 8:
        len8 = True
    else:
        print("Password length is less than 8")
        continue
    #check digit
    for i in password:
        if i.isdigit():
            isdigit=True
            break
    else:
        print("Password does not have a digit")
        continue
    #check special
    for i in password:
        if not i.isalnum() and i in ['@','$','%']:
            special = True
            break
    else:
        print("Wrong/no special character")
        continue
    #saving
    if isdigit == True and len8 == True and special == True:
        file = open("security.txt","a")
        file.write(f"{uid},{password}\n")
        file.close()
        print("Done")
        continue
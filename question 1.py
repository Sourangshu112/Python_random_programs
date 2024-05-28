x = dict(Ayan = "ironman" ,
         Rishiraj = "batman" , 
         Ayush = "computer" , 
         Rupam = "Wakanda" , 
         Shivam = "hello125" , 
         Subhrodip = "progamer" , 
         Anushka = "violet" , 
         Sourodip = "superman" , 
         Tamaghna = "messi" , 
         Arnab = "friends"  )

username = input("Enter your username :- ")
password = input("Enter your password :- ")

for i in (x.keys()):
  if username == i:
    if password == x[username]:
      print(username)
      print("You are logged in.")
    else:
      print("Password is invalid.")
    break
else:
  print("Username is not valid.")



    
 

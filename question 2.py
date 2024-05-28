a = dict()
name=""
while True:
  if name != "Q" and name != 'q':
    name = input("Enter the name of the product(press q to quit):")
    if name != "Q" and name != 'q':
      prize = int(input("Enter the prize of the product:"))
      a[name] = prize
    continue
  else:
    print("===========================")
    ask = input("Enter the name of the product whose price you want to know(press q to quit):")
    if ask == "Q" or ask == 'q':
      break
    else:
      if ask in a.keys():
        print("product name is :",ask," || prize is :",a[ask])
      else:
        print("Product is not in dictionary")
print("Thank you!")


R = float(input('Enter the radius'))
pi = 3.14
choice = int(input("""Enter 1 for Circle area
Enter 2 for Circle perimeter"""))
if choice == 1:
    area=pi*R*R
    print("Area " ,area)
elif choice == 2:
    perimeter = 2*pi*R
    print("Perimeter ",perimeter)
else:
    print("Wrong input")

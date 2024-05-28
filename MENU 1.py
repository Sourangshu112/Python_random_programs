choice = int(input("""Enter 1 for Square
Enter 2 for rectangle
Enter 3 for Parallelogram
Enter 4 for Circle """))
if choice == 1:
    s=float(input("Enter the side of square"))
    area = s**2
    perimeter = 4*s
    print("Area " , area ," perimeter ", perimeter)
elif choice == 2:
    L=float(input("Enter the length"))
    B=float(input("Enter the breadth"))
    area = L*B
    perimeter = 2*(L+B)
    print("Area " , area ," perimeter ", perimeter)
elif choice == 3:
    B=float(input("Enter the base"))
    H=float(input("Enter the height"))
    L=float(input("Enter the length"))
    B=float(input("Enter the breadth"))
    area = B*H
    perimeter = 2 * (L+B)
    print("Area " , area ," perimeter ", perimeter)
elif choice == 4:
    R=float(input('Enter the radius'))
    pi=3.14
    area=pi*R*R
    perimeter = 2 * pi * R
    print("Area " , area ," perimeter ", perimeter)
else:
    print("Wrong inpur")

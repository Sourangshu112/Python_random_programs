import math
def tent(sh,h,r):
    area_cylinder = 2*math.pi*r*h
    area_cone = math.pi*r*sh
    area_canvas = area_cylinder+area_cone
    return area_canvas

def cost(canvas):
    price =10
    cost = canvas*price
    return cost

def netamount(amt):
    tax = 0.18*amt
    net_amt = amt+tax
    return net_amt

a = float(input("Enter the height of the tent :"))
b = float(input("Enter the radius of the tent :"))
c = float(input("Enter the slanted height of the tent :"))
area = tent(c,a,b)
amount = cost(area)
net_amount = netamount(amount)

print("Area of the canvas is = ",area)
print("Cost of the tent is = ",amount)
print("Net amount payable(inclusive of taxes) is = ",net_amount)

temp = float(input("Enter the temperature of water"))
if temp <= 0:
    print(" Water is in Solid state")
elif temp > 0 and temp <= 100:
    print("Water is in liquid state")
else:
    print("Water is in gaseous state")

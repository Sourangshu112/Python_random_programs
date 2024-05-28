p=float(input("Enter the principal"))
r=float(input("Enter the rate of interest"))
t=float(input("Enter the number of year"))
si=(p*r*t)/100
print("Simple interest = " , si)
ci=(p*(1+(r/100))**t) - p
print("compound interest = " , ci)

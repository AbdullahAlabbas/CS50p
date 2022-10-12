expression = input("Expression: ")

x, y, z = expression.split(" ")

X = float(x)
Z = float(z)

if y == "+":
    print(X+Z)
    
elif y == "-":
    print(X-Z)
    
elif y =="*":
    print(X*Z)

else:
    print(X/Z)
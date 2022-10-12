camelcase = input("camelcase: ")
for x in camelcase:
    if x.isupper():
        print("_"+x.lower().strip(), end="")
        
    else:
        print(x, end="")
        
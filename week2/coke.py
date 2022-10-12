coke = 50
while coke > 0:
    print("Amount Due: ", coke)
    cent = int(input("Insert Coin: "))
    if cent == 10 or cent == 25 or cent == 5:
        coke = coke - cent
left = abs(coke)
print("Change Owed: ", left)        

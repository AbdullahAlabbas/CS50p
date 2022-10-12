# Get the input

x = input("Answear The Great Question? ").casefold().strip()

 # if the user type 42 ((case-insensitively)) it shoult print "yes" else "no"
if x == "forty two" or x == "forty-two" or x == "42":
        print("Yes")

else:
    print("No") 
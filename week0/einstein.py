# make a constant for the speed of light square "speed"
speed = 300000000*300000000

# define a main function called "main"
def main():
    E = int(input("What is the mass??"))
    print("The Energy is equal to",pohr(E))
    
    
   
def pohr(n):
    return n*speed
    

    
main()
import random
while True:
    try:
        level = int(input("Level: "))
        if level > 0 :
            break
    except:
        pass
    
random = random.randint(1,level)
while True:
    try:
        guess = int(input("Guess: "))
        if guess > 0:
            if guess < random:
                print("Too small!")
            elif guess > random:
                print("Too large!")
            elif guess == random:
                print("Just right!")
                break
        
    except:
        pass
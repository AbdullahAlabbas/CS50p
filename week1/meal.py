def main():
    x = input("What time is it? ")
    
    time = convert(x)
    
    if time >= 7 and time <= 8:
        print("breakfast time")
    elif time >= 12 and time <= 13:
        print("lunch time")
    elif time >= 18 and time < 19:    
        print("dinner time")
    else:
        print()
def convert(time):
    hours, minutes = time.split(":")
    minute = float(minutes) / 60
    hour = float(hours)
    zime = hour + minute
    return zime


if __name__ == "__main__":
    main()
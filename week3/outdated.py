mounths = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
while True:
    date = input("Date: ")
    try:
        mounth, day, year= date.split("/")
        mounth = mounth.replace(" ","")
        year = year.replace(" ","")
        if(int(mounth)>= 1 and int(mounth)<=12 and int(day) >= 1 and int(day) <= 31):
            break

    except:
        try:
            old_mounth , old_day , year = date.split(" ")
            for i in range(len(mounths)):
                if old_mounth == mounth[i]:
                    mouth = i + 1
            day = old_day.replace(",","")
            if(int(mounth)>= 1 and int(mounth)<=12 and int(day) >= 1 and int(day) <= 31):
                break
        except:
            print()
            pass
print(f"{year}-{int(mounth):02}-{int(day):02}")        

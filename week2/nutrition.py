consumer = input("item: ").strip().casefold()
fruits = {
    "apple": 130,

    "avocado": 50,

    "sweet cherries": 100,
    
    "kiwifruit": 90,
    
    "pear": 100
}
for cal in fruits:
  if cal in consumer:
      print("Calories:",fruits[cal])
  else:
      print("")

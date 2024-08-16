farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]

# Part 1
print("Animals from NE Farm:")
for animal in farms[0]["agriculture"]:
    print(animal)

# Part 2
chosen_farm = input("Choose a farm (NE Farm, W Farm, or SE Farm): ").capitalize()
for farm in farms:
    if farm["name"] == chosen_farm:
        print(f"Plants/Animals raised on {chosen_farm}: {', '.join(farm['agriculture'])}")
        break
else:
    print("Invalid farm choice.")

# Part 3
chosen_farm = input("Choose a farm (NE Farm, W Farm, or SE Farm): ").capitalize()
for farm in farms:
    if farm["name"] == chosen_farm:
        animals = [item for item in farm['agriculture'] if item.isalpha()]
        print(f"Animals from {chosen_farm}: {', '.join(animals)}")
        break
else:
    print("Invalid farm choice.")

# SUPER BONUS
farms = [{"name": "Southwest Farm", "agriculture": ["chickens", "carrots", "celery"]},
         {"name": "Northeast Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "East Farm", "agriculture": ["bananas", "apples", "oranges"]},
         {"name": "West Farm", "agriculture": ["pigs", "chickens", "llamas"]}]


chosen_farm = input("Choose a farm: ").capitalize()
for farm in farms:
    if farm["name"] == chosen_farm:
        animals = [item for item in farm['agriculture'] if item.isalpha()]
        print(f"Animals from {chosen_farm}: {', '.join(animals)}")
        break
else:
    print("Invalid farm choice.")
from csv import excel

Players = {
    "oli": {
        "health": 100,
        "strength": 50,
        "level": 5
    },

    "alex": {
        "health": 200,
        "strength": 100,
        "level": 50
    }
}

for value in Players.values():
    print(value)
    print()

while True:
    try:
        plrtogift = input("Who would you like to send a gift to?: ").lower()
        print()
        plr = Players[plrtogift]
        print(f"You've decided to gift {plrtogift}! ")
        print()
        print(f"Their inventory is {Players[plrtogift]}")
        print()
        break
    except KeyError:
        print("Doesnt exist.")

itemtogift = input(f"What would you want to gift {plrtogift}?: ")
print()
print(f"Nice, you've chosen to give {plrtogift} a {itemtogift}! ")
print()

itemsvalue = input(f"What would you want the {itemtogift} Value to be?: ")
print()

Players[plrtogift][itemtogift] = itemsvalue

print(f"""Nice, now his account looks like this:
         {Players[plrtogift]}""")
print()

while True:
    try:
        delitem = input("What would you like to delete?: ").lower()
        del Players[plrtogift][delitem]
        print()
        break
    except KeyError:
        print("Doesnt exist.")

while True:
    try:
        plrtodamage = input("Which player do you want to damage?: ").lower()
        print()
        break
    except KeyError:
        print("Doesnt exist.")

while True:
    try:
        damageamount = int(input(f"How much do you want to damage {plrtodamage}?: "))
        print()
        break
    except ValueError:
        print("Not a number.")

Players[plrtodamage]["Health"] -= damageamount

print(f"Damaged {plrtodamage} with a damage of {damageamount},  their health is now {Players[plrtodamage]['Health']}")

print()

print(f"Their full stats are now {Players[plrtodamage]}")


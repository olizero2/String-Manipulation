from csv import excel
import time


HEADER = '\033[95m'
OKBLUE = '\033[94m'
OKCYAN = '\033[96m'
OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'

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

itemtogift = input(f"What would you want to gift {plrtogift}?: ").lower()
print()
print(f"Nice, you've chosen to give {plrtogift} a {itemtogift}! ")
print()

itemsvalue = input(f"What would you want the {itemtogift} Value to be?: ").lower()
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
        print(f"Okay well you decided to get rid of his {delitem}..")
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

try:
    STARTHEALTH = Players[plrtodamage]["health"]
except:
    print("i dont think that exists")

while True:
    try:
        damageamount = int(input(f"How much do you want to damage {plrtodamage}?: "))
        print()
        break
    except ValueError:
        print("Not a number.")

Players[plrtodamage]["health"] -= damageamount

print(f"Damaged {plrtodamage} with a damage of {damageamount},  their health is now {Players[plrtodamage]['health']}")

print()

print(f"Their full stats are now {Players[plrtodamage]}")
print("""

""")

time.sleep(1)
print(f"Lets check if they are still alive.")
time.sleep(1)
print(f"Lets check if they are still alive..")
time.sleep(1)
print(f"Lets check if they are still alive...")

print("""

""")
time.sleep(2)

print(f"So you've decided to attack {plrtodamage}.")
time.sleep(1)
print(f"So you've decided to attack {plrtodamage}..")
time.sleep(1)
print(f"So you've decided to attack {plrtodamage}...")
print("""

""")

time.sleep(2)


print(f"His starting health was {STARTHEALTH}.")
time.sleep(1)
print(f"His starting health was {STARTHEALTH}..")
time.sleep(1)
print(f"His starting health was {STARTHEALTH}...")
print("""

""")


time.sleep(2)


print(f"The damage you dealt was {damageamount}.")
time.sleep(1)
print(f"The damage you dealt was {damageamount}..")
time.sleep(1)
print(f"The damage you dealt was {damageamount}...")
print("""

""")

time.sleep(2)

print(f"If we do the math.. {STARTHEALTH} - {damageamount} equals.")
time.sleep(1)
print(f"If we do the math.. {STARTHEALTH} - {damageamount} equals..")
time.sleep(1)
print(f"If we do the math.. {STARTHEALTH} - {damageamount} equals...")
print("""

""")

time.sleep(2)



endhealth = STARTHEALTH - damageamount

print(f"{endhealth}.")
print("""

""")

time.sleep(2)

if endhealth < 0:
    print(f"{WARNING}Hes dead.")
else:
    print(f"{OKGREEN}Hes alive.")
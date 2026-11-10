
from datetime import date
today = date.today().isoformat()
import time

action_delay_seconds= 1

class Baby:
    def __init__(self, name, birthdate, height=20, weight=130):

        if birthdate is None:
            self.birthdate = date.today().isoformat()
        else:
            self.birthdate = birthdate

        self.name = name
        self.height = height
        self.starting_weight = weight
        self.weight = weight
        self.mood = "content"
        self.eat_count = 0
        self.drink_count = 0
        self.feeding_count = 0
                 
    def laugh(self):
        self.mood = "happy"

    def cry(self):
        self.mood = "sad"

    def sleep(self):
        self.mood = "content"


# baby1 = Baby("Bob", birthdate= "2026-11-01")
# baby2 = Baby("RoboBob", birthdate= None, height=25, weight=140)

# baby1.laugh()
# baby2.cry()

# baby1.display_status()
# print()
# baby2.display_status()

    def laugh(self):
            self.mood = "happy"

    def cry(self):
            self.mood = "sad"

    def sleep(self):
            self.mood = "content"
            time.sleep(action_delay_seconds)

    def scream(self):
            self.mood = "mad"
            time.sleep(action_delay_seconds)


    def eat(self, food="vegetables"):
            self.eat_count += 1
            self.weight += 11
            self.feeding_count += 1

            if food == "goodies" or food == "fruit":
                self.laugh()

            elif food == "vegetables":
                self.cry()

            elif food == "cereal":
                self.sleep()

            else:
                self.sleep()


            if self.eat_count == 3 or self.eat_count % 3 == 0:
                self.poop()

            if self.feeding_count % 3 == 0:
                self.burp()

    def drink(self):
            self.weight += 8
            self.drink_count += 1
            self.feeding_count += 1
            self.sleep()

            if self.drink_count % 3 == 0:
                self.pee()

            if self.feeding_count % 3 == 0:
                self.burp()

    def burp(self):
            self.mood = "happy"

    def poop(self):
            self.weight -= 5
            self.mood = "content"

    def pee(self):
            self.weight -=4
            self.mood = "content"

    def display_status(self):
        print("Name:", self.name)
        print("Birthdate:", self.birthdate)
        print("Height:", self.height)
        print("Starting Weight:", self.starting_weight)
        print("Current Weight:", self.weight)
        print("Mood:", self.mood)
        print("Eat Count:", self.eat_count)
        print("Drink Count:", self.drink_count)
        print("Feeding Count:", self.feeding_count)

# Test A: Three Eats
# baby1 = Baby("Bob", "2026-11-01")
# baby1.eat()
# baby1.eat()
# baby1.eat()
# baby1.display_status()

# print()

# Test B: Three Drinks
# baby2 = Baby("RoboBob", "2026-10-15")
# baby2.drink()
# baby2.drink()
# baby2.drink()
# baby2.display_status()

# print()

# Test C: Mixed Feedings
# baby3 = Baby("BabyBot", "2026-09-20")
# baby3.eat("fruit")
# baby3.drink()
# baby3.eat("cereal")
# baby3.display_status()

# print()

baby_name = input("Enter the baby's name: ")

birthdate = input("Enter the baby's birthdate (or leave blank for today's data): ")
if birthdate is None or birthdate.strip() == "":
    birthdate = date.today().isoformat()

height = input("Enter the baby's height in inches (or leave blank for 20): ")
if height.strip() == "":
    height = 20
else:
    height = float(height)

weight = input("Enter the baby's starting weight in ounces (or leave blank for 130): ")
if weight.strip() == "":
    weight = 130
else:
    weight = float(weight)

baby = Baby(baby_name, birthdate, height, weight)

while True:
    print("Pick an action from the following:")
    print("1. eat")
    print("2. drink")
    print("3. laugh")
    print("4. cry")
    print("5. sleep")
    print("6. scream")
    print("7. status")
    print("8. home")

    action = input("Enter your choice (1-8): ").strip().lower()

    if action == "1":
       food = input("What food should the baby eat?")
       if food.strip() == "":
           food = "vegetables"
       baby.eat(food)

    elif action == "2":
        baby.drink()

    elif action == "3":
        baby.laugh()

    elif action == "4":
        baby.cry()

    elif action == "5":
            baby.sleep()

    elif action == "6":
            baby.scream()

    elif action == "7":
            baby.display_status()

    elif action == "8":
            print("Returning home...")
            break

    else:
            print("Invalid choice. Please enter a number between 1 and 8.")


    if baby.weight >= baby.starting_weight * 2:
            print("The baby has doubled its starting weight!")
            break

print("\nFinal Baby Status:")
baby.display_status()


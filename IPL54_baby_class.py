
from datetime import date
today = date.today().isoformat()

class Baby:
    def __init__(self, name, birthdate, height=20, weight=130):

        if birthdate is None:
            self.birthdate = date.today().isoformat()
        else:
            self.birthdate = birthdate

        self.name =name
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

    def display_status(self):
        print("Name:", self.name)
        print("Birthdate:", self.birthdate)
        print("Height:", self.height)
        print("Starting Weight:", self.starting_weight)
        print("Weight:", self.weight)
        print("Mood:", self.mood)
        print("Eat Count:", self.eat_count)
        print("Drink Count:", self.drink_count)
        print("Feeding Count:", self.feeding_count)

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

    def scream(self):
            self.mood = "mad"

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
baby1 = Baby("Bob", "2026-11-01")
baby1.eat()
baby1.eat()
baby1.eat()
baby1.display_status()

print()

# Test B: Three Drinks
baby2 = Baby("RoboBob", "2026-10-15")
baby2.drink()
baby2.drink()
baby2.drink()
baby2.display_status()

print()

# Test C: Mixed Feedings
baby3 = Baby("BabyBot", "2026-09-20")
baby3.eat("fruit")
baby3.drink()
baby3.eat("cereal")
baby3.display_status()

print()
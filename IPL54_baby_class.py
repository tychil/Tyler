
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

baby1 = Baby("Bob", birthdate= "2026-11-01")
baby2 = Baby("RoboBob", birthdate= None, height=25, weight=140)

baby1.laugh()
baby2.cry()

baby1.display_status()
print()
baby2.display_status()

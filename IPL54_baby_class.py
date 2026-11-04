
from datetime import date
today = date.today().isoformat()

class Baby:
    def __init__(self, name, birthdate, height=20, weight=130):
        self.name =name
        self.birthdate = birthdate if birthdate else date.today().isoformat()
        self.height = height
        self.starting_weight = weight
        self.weight = weight
        self.mood = "content"
        self.eat_count = 0
        self.drink_count = 0
        self.feeding_count = 0
                 
def laugh(self):
    print("The baby is laughing.")

def cry(self):
def sleep(self):
def display_status(self):
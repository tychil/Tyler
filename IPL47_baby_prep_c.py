


def dance():
    print("Baby is dancing!")


def introduce_baby(baby_name, age, current_weight):
    print("Meet", baby_name + "!")
    print("Age:", age)
    print("Weight:", current_weight)

    activity = random.choice(["dance", "stay still"])
    if activity == "dance":
        dance()
    else:
        print(baby_name, "is staying still.")


def eat(current_weight, eat_count, poop_count):
    eat_count += 1
    current_weight += 11

    if eat_count % 3 == 0:
        current_weight = poop(current_weight)
        poop_count += 1
        print(baby_name, "pooped")

    return current_weight, eat_count, poop_count


def drink(current_weight, drink_count):
    current_weight += 1
    drink_count += 1

    if drink_count % 3 == 0:
        current_weight = pee(current_weight)
        print(baby_name, "peed")

    return current_weight, drink_count


def poop(current_weight):
    current_weight -= 5
    return current_weight


def pee(current_weight):
    current_weight - 4
    return current_weight


def cry():
    print("Baby is crying...")


def sleep():
    print("Baby is sleeping...")


def display_status(baby_name, current_weight, mood, eat_count, drink_count):
    print("Name:", baby_name)
    print("Weight:", current_weight)
    print("Mood:", mood)
    print("Feedings:", eat_count)
    print("Drinks:", drink_count)


baby_name = input("Enter baby's name: ")
age = input("Enter baby's age: ")
starting_weight = float(input("Enter baby's starting weight: "))

current_weight = starting_weight
mood = "Happy"
eat_count = 0
drink_count = 0
poop_count = 0

introduce_baby(baby_name, age, current_weight)

while True:
    print("1 - Eat")
    print("2 - Drink")
    print("3 - Cry")
    print("4 - Sleep")
    print("5 - Status")
    print("6 - Home")

    choice = input("Choose an action: ")

    if choice == "1":
        current_weight, eat_count, poop_count = eat(
            current_weight,
            eat_count,
            poop_count
        )
        mood = "Happy"
        print(baby_name, "ate 11 oz.")

        if poop_count == 3:
            print("Excessive pooping. Game over!")
            break

    elif choice == "2":
        current_weight, drink_count = drink(current_weight, drink_count)
        mood = "Happy"
        print(baby_name, "drank 8 oz.")

    elif choice == "3":
        cry()
        mood = "Sad"

    elif choice == "4":
        sleep()
        mood = "Content"

    elif choice == "5":
        display_status(
            baby_name,
            current_weight,
            mood,
            eat_count,
            drink_count
        )

    elif choice == "6":
        break

    else:
        print("Invalid choice. Please try again.")
>>>>>>> 85a2fa6 (Added RoboBaby introduction)

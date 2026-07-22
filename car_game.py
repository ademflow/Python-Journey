class Car:
    def __init__(self, color, brand, fuel_level):
        self.color = color
        self.brand = brand
        self.fuel_level = fuel_level
        self.is_running = False
        self.mileage = 0

    def start(self):
        if self.is_running:
            print(f"The {self.color} {self.brand} is already running!")
            return

        if self.fuel_level < 5:
            print("Out of gas!")
            self.is_running = False
        elif not self.is_running and self.fuel_level >= 5:
            self.is_running = True
            print(f"The {self.color} {self.brand} has started!")
            self.fuel_level -= 5

    def stop(self):
        if self.is_running:
            self.is_running = False
            print(f"The {self.color} {self.brand} has stopped!")
        else:
            print(f"The {self.color} {self.brand} is already stopped!")

    def refuel(self):
        self.fuel_level = 100
        print(f"The {self.color} {self.brand} is refueled!")

    def drive(self, distance):
        cost = distance / 10
        if not self.is_running:
            print(
                "Your car is not turned on, you can't drive!")
            return

        if self.fuel_level < cost:
            print("Not enough gas for this trip!")
            return
        self.fuel_level -= cost
        self.mileage += distance
        print(f"You went {distance} miles!")

    def show_stats(self):
        print(f"\n--- {self.brand} Dashboard ---")
        print(f"Status: {'Running' if self.is_running else 'Off'}")
        print(f"Fuel: {self.fuel_level}%")
        print(f"Mileage: {self.mileage} miles")
        print("-------------------\n")


my_car = Car("green", "bmw", 100)
while True:

    print("\n--- Car Game ---")
    print("1. Start the car")
    print("2. Stop the car")
    print("3. Drive")
    print("4. Refuel")
    print("5. Show status")
    print("6. Exit the game")

    choice = input("Choose an option: ")

    if choice == "1":
        my_car.start()
    elif choice == "2":
        my_car.stop()
    elif choice == "3":
        try:
            distance = int(input("How many miles do u wanna drive?: "))
            my_car.drive(distance)
        except ValueError:
            print("Please enter a valid number for miles!")
    elif choice == "4":
        my_car.refuel()
    elif choice == "5":
        my_car.show_stats()
    elif choice == "6":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Choose between 1-6")

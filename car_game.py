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


my_car = Car("blue", "Ford", 150)
my_car.fuel_level = 20

my_car.drive(50)

my_car.start()

my_car.drive(50)

print(f"Total mileage: {my_car.mileage}")
print(f"Fuel left: {my_car.fuel_level}")

my_car.drive(200)

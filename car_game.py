class Car:
    def __init__(self, color, brand, fuel_level):
        self.color = color
        self.brand = brand
        self.fuel_level = fuel_level
        self.is_running = False

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


my_red_car = Car("red", "bmw", 5)
my_red_car.start()
my_red_car.stop()
my_red_car.start()
my_red_car.refuel()
my_red_car.start()

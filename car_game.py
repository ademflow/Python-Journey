class Car:
    def __init__(self, color, brand, horsepower):
        self.color = color
        self.brand = brand
        self.horsepower = horsepower
        self.is_running = False

    def start(self):
        self.is_running = True
        print(f"The {self.color} {self.brand} has started!")

    def stop(self):
        if self.is_running:
            self.is_running = False
            print(f"The {self.color} {self.brand} has stopped!")
        else:
            print(f"The {self.color} {self.brand} is already stopped!")


my_red_car = Car("red", "bmw")
my_red_car.start()
my_red_car.stop()

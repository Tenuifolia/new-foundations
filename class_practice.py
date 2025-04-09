


class Vehicle:
    def __init__(self, v_color, v_make, v_model):
        self.color = v_color
        self.make = v_make
        self.model = v_model
        self.speed = 0

    def drive(self, v_speed):
        self.speed = v_speed
        return f"Driving at {self.speed}mph"

    def stop(self):
        self.speed = 0
        return "Stopping"


car_1 = Vehicle('red', 'Honda', 'Civic')
car_2 = Vehicle('Metallic Silver', 'Toyota', 'Avalon')

print(car_1.speed)

print(car_1.drive(25))

print(car_2.speed)

# print(car_1.stop())

# print(car_1.speed)
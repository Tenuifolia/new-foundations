

class Animal:
    def __init__(self, name, color, number_of_legs):
        self.name = name
        self.color = color
        self.number_of_legs = number_of_legs

    def make_sound(self):
        print("Generic Animals make no sound")

    def print_me(self):
        print(f'name: {self.name}')
        print(f'color: {self.color}')
        print(f'legs: {self.number_of_legs}')
        print(type(self))


class Cat(Animal):
    def __init__(self, color):
        Animal.__init__(self, 'Cat', color, 4)

    def make_sound(self):
        print("Meow!!")

class Dog(Animal):
    def __init__(self, color):
        Animal.__init__(self, 'Dog', color, 4)

    def make_sound(self):
        print("Woof!! Woof!!")

class Bird(Animal):
    def __init__(self, color, beak_color):
        Animal.__init__(self, 'Bird', color, 2)
        self.beak_color = beak_color

    def make_sound(self):
        print("Tweet, tweet!")

    def flap_wings(self):
        print("Wings flap sounds")


animal_1 = Animal('Fish', 'gray', 0)
cat_1 = Cat('Orange')
dog_1 = Dog('Black')
bird_1 = Bird('Blue', 'Black')

print(Bird.__mro__)

# print(bird_1.beak_color)
# bird_1.print_me()

# animal_1.make_sound()
# cat_1.make_sound()
# dog_1.make_sound()
# bird_1.make_sound()

# dog_1.print_me()


# cat_1.print_me()


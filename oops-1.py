class Pet:
    def __init__(self, name, age, animal):
        self.name = name
        self.age = age
        self.animal = animal
    
    def show(self):
        print(f"I am {self.name} and I am {self.age} years old")
    
    def animal_type(self):
        animal = self.animal.lower()
        match animal:
            case "cat":
                print("I am a Cat")
            case "dog":
                print("I am a Dog")
            case _:
                print("I am not a Cat or a Dog")
    def speak(self):
        print("I don't know what to say")

class Cat(Pet):
    def __init__(self, name, age, animal, color):
        super().__init__(name, age, animal)
        self.color = color

    def bark(self):
        print(f"I am a cat, my name is {self.name} and I am {self.age} years old and I am {self.color} in color")

    def speak(self):
        print("Meow")
    
    def show(self):
        print(f"I am {self.color} in color")

class Dog(Pet):
    def bark(self):
        print(f"I am a dog, my name is {self.name} and I am {self.age} years old")

    def speak(self):
        print("Bark")

class Fish(Pet):
    pass

# p = Pet('Katty', 10)
# p.show()
p = Pet("cherry", 10, 'human')
p.speak()

c = Cat("Bill", 20, 'cat', 'white')
c.animal_type()
c.show()
c.speak()
c.bark()

d = Dog('Dough', 12, 'dog')
d.animal_type()
d.show()
d.speak()

f = Fish("Larry", 10, 'fish')
f.speak()
# cat = Cat('Kate', 3)
# cat.bark()

# dog = Dog('John', 10)
# dog.bark()
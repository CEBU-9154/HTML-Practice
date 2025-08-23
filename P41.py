class Cat:
    def __init__(self, name, age):
        self.name=name
        self.age=age
    def info(self):
        print(f"I'm a cat. My name is {self.name}. I am {self.age} years old.")
    def sound(self):
        print("Meow")

class Dog:
    def __init__(self, name, age):
        self.name=name
        self.age=age
    def info(self):
        print(f"I'm a dog. My name is {self.name}. I'm {self.age} years old.")
    def sound(self):
        print("Woof")

cat1=Cat("Dodo", 2.5)
dog1=Dog("Tyson", 8)

for animal in (cat1, dog1):
    animal.sound()
    animal.info()

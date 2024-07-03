class Animal:
    def speak(self):
        raise NotImplementedError("Subclass must implement abstract method")

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

def animal_sound(animal: Animal):
    print(animal.speak())

dog = Dog()
cat = Cat()
animal_sound(dog)
animal_sound(cat)

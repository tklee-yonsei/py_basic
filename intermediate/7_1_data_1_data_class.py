from dataclasses import dataclass

@dataclass
class Person:
    name: str
    age: int

person = Person(name="Alice", age=30)
print(person)
print(person.name)
print(person.age)

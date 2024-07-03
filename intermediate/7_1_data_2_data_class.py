from dataclasses import dataclass


@dataclass(frozen=True)
class Person:
    name: str
    age: int


person1 = Person(name="Alice", age=30)
person2 = Person(name="Bob", age=25)
person3 = Person(name="Alice", age=30)

print(person1)  # 출력: Person(name='Alice', age=30)
print(person1.name)
print(person1.age)
print(person1 == person3)  # 출력: True
print(person1 == person2)  # 출력: False
print(hash(person1))  # 해시값 출력 (에러)


# 수동으로 작성한 클래스
class PersonManual:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"PersonManual(name={self.name!r}, age={self.age!r})"

    def __eq__(self, other):
        if not isinstance(other, PersonManual):
            return NotImplemented
        return self.name == other.name and self.age == other.age

    def __hash__(self):
        return hash((self.name, self.age))


person_manual1 = PersonManual(name="Alice", age=30)
person_manual2 = PersonManual(name="Bob", age=25)
person_manual3 = PersonManual(name="Alice", age=30)

print(person_manual1)  # 출력: PersonManual(name='Alice', age=30)
print(person_manual1 == person_manual3)  # 출력: True
print(person_manual1 == person_manual2)  # 출력: False
print(hash(person_manual1))  # 해시값 출력

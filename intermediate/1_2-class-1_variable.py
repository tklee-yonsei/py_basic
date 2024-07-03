class Person:
    species = "Homo sapiens"  # 클래스 변수

    def __init__(self, name, age):
        self.name = name  # 인스턴스 변수
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

# 클래스 변수 접근
print(Person.species)  # 출력: Homo sapiens

# 인스턴스 생성
person1 = Person("Alice", 30)
person2 = Person("Bob", 25)

# 인스턴스를 통해 클래스 변수와 인스턴스 변수에 접근
print(person1.species)  # 출력: Homo sapiens
print(person2.species)  # 출력: Homo sapiens
print(person1.name)  # 출력: Alice
print(person2.name)  # 출력: Bob

# 클래스 변수 변경
Person.species = "Homo erectus"
print(person1.species)  # 출력: Homo erectus
print(person2.species)  # 출력: Homo erectus

# 인스턴스 변수 변경
person1.name = "Charlie"
print(person1.name)  # 출력: Charlie
print(person2.name)  # 출력: Bob
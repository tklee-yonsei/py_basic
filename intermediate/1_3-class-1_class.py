class Person:
    species = "Homo sapiens"  # 클래스 변수

    def __init__(self, name, age):
        self.name = name  # 인스턴스 변수
        self.age = age
        print(f"{self.name}이(가) 생성되었습니다.")

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

    def __del__(self):
        print(f"{self.name}이(가) 소멸되었습니다.")

# 인스턴스 생성
person1 = Person("Alice", 30)
person1.greet()

# 인스턴스 소멸
del person1

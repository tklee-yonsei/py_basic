class Person:
    def __init__(self, name, age):
        self.name = name  # 퍼블릭 속성
        self._age = age  # 프로텍티드 속성
        self.__social_security_number = "123-45-6789"  # 프라이빗 속성

    def display_info(self):
        print(f"Name: {self.name}, Age: {self._age}")

person = Person("Alice", 30)
print(person.name)  # 접근 가능
print(person._age)  # 경고: 접근 가능하지만 권장되지 않음
print(person._Person__social_security_number)  # 접근 가능하지만 매우 권장되지 않음
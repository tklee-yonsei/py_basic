# 기본 인자가 있는 함수
def greet(name="Guest"):
    print("Hello,", name)

greet()  # 기본값 사용
greet("Alice")  # 인자 전달

# 키워드 인자를 사용하는 함수
def introduce(name, age=35):
    print(f"My name is {name} and I am {age} years old.")

introduce(name="Alice", age=30)
introduce(age=25, name="Bob")
introduce(name="Choi")
introduce("Choi")

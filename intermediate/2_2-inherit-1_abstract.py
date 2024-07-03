from abc import ABC, abstractmethod
from math import pi

# 추상 클래스 Shape 정의
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

# Rectangle 클래스 정의
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# Circle 클래스 정의
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return pi * self.radius ** 2

# Shape 타입을 사용하는 예제
def print_area(shape: Shape):
    print(f"The area is {shape.area()}")

# Rectangle 객체 생성 및 사용
rectangle_1: Shape = Rectangle(3, 4)
print_area(rectangle_1)

# Circle 객체 생성 및 사용
circle_1: Shape = Circle(5)
print_area(circle_1)

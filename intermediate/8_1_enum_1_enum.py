from enum import Enum

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

print(Color.RED)
print(Color.GREEN)
print(Color.BLUE)

# 열거형 사용 예제
favorite_color = Color.RED

if favorite_color == Color.RED:
    print("Your favorite color is red!")
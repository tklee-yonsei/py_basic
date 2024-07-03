# 람다 함수
multiply = lambda a, b: a * b
print(multiply(3, 4))  # 출력: 12

# map()과 함께 사용
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x * x, numbers))
print(squared_numbers)  # 출력: [1, 4, 9, 16, 25]

# 절차형 프로그래밍 예제
numbers = [1, 2, 3, 4, 5]
squared_numbers = []
for number in numbers:
    squared_numbers.append(number * number)
print(squared_numbers)  # 출력: [1, 4, 9, 16, 25]

# 함수형 프로그래밍 예제
squared_numbers = list(map(lambda x: x * x, numbers))
print(squared_numbers)  # 출력: [1, 4, 9, 16, 25]

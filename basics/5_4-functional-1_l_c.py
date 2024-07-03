# 리스트 컴프리헨션
squared_numbers = [x * x for x in range(1, 6)]
print(squared_numbers)  # 출력: [1, 4, 9, 16, 25]

# 조건부 리스트 컴프리헨션
even_numbers = [x for x in range(1, 6) if x % 2 == 0]
print(even_numbers)  # 출력: [2, 4]

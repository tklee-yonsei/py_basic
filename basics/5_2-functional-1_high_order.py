from functools import reduce

# map() 예제
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x * x, numbers))
print(squared_numbers)  # 출력: [1, 4, 9, 16, 25]

# filter() 예제
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)  # 출력: [2, 4]

# reduce() 예제
sum_of_numbers = reduce(lambda x, y: x + y, numbers)
print(sum_of_numbers)  # 출력: 15

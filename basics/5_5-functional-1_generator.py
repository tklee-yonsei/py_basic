# 제너레이터 함수
def generate_numbers():
    for i in range(1, 6):
        yield i

gen = generate_numbers()
print(next(gen))  # 출력: 1
print(next(gen))  # 출력: 2
print(list(gen))  # 출력: [3, 4, 5]

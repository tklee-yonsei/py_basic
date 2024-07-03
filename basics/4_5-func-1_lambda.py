# 람다 함수
multiply = lambda a, b: a * b
print("곱하기 결과:", multiply(3, 4))

# 람다 함수를 활용한 정렬
points = [(1, 2), (3, 1), (5, 4), (2, 3)]
points.sort(key=lambda point: point[1])
print("y좌표를 기준으로 정렬된 points:", points)

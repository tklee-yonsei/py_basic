def square(x):
    return x * x

def apply_function(func, value):
    return func(value)

result = apply_function(square, 5)
print(result)  # 출력: 25

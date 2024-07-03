# 가변 인자 (*args)
def sum_all(*args):
    return sum(args)

print("합계:", sum_all(1, 2, 3, 4, 5))

# 키워드 인자 (**kwargs)
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=30, city="New York")

# 키워드 인자2 (**kwargs)
def print_info2(name, **kwargs):
    print(f"name: {name}")
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info2(name="Elf", city="New York", age=40)

def count_calls(func):
    nonlocal i = 0
    def wrapper():
        nonlocal i = i + 1
        result = func()
        print(f"Функция {func.__name__}, вызвана {i} раз")
        return result
    return wrapper


@count_calls
def hello():
    print("Hello!")


hello()
hello()
hello()
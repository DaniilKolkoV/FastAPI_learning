def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Ошибка: Делить на ноль нельзя!"
    return round(a/b, 2)


if __name__ == "__main__":
    print(add(5, 3))
    print(subtract(10, 4))
    print(multiply(6, 7))
    print(divide(20, 2))
print("=== Пример 3: предчувствие декораторов ===")

def log_calls(func):
    def wrapper(*args, **kwargs):
        print(f"Вызов {func.__name__} с args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"Результат: {result}")
        return result
    return wrapper


def add(a, b):
    return a + b


def greet(name, greeting="Привет"):
    return f"{greeting}, {name}!"


# Оборачиваем функции в логгер
add_with_log = log_calls(add)
greet_with_log = log_calls(greet)

print(add_with_log(5, 3))
print(greet_with_log("Daniil"))
print(greet_with_log("Anna", greeting="Здравствуй"))
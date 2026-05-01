import random

def retry(count):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(1,count + 1):
                try:
                    print(f"Попытка {i}:")
                    result = func(*args, **kwargs)
                    return result
                except Exception as e:
                    print(f"Попытка {i} не удалась, потому что {e}, попытка не удалась")
                    if i == count:
                        raise
        return wrapper
    return decorator


@retry(5)
def unstable_5():
    n = random.randint(1, 4)
    if n != 1:
        raise ValueError(f"Не повезло, выпало {n}")
    return "Успех (5 попыток)!"


@retry(2)
def unstable_2():
    n = random.randint(1, 4)
    if n != 1:
        raise ValueError(f"Не повезло, выпало {n}")
    return "Успех (2 попытки)!"


print(unstable_5())
print("===")
print(unstable_2())
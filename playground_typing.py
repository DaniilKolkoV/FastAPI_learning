# 1. Функция, которая принимает список чисел и возвращает их сумму
def sum_all(nums: list[int]) -> int:
    sum_num = sum(nums)
    return sum_num

# 2. Функция, которая принимает имя и возраст, возвращает строку-приветствие
#    Пример: greet("Daniil", 22) -> "Привет, Daniil, тебе 22"
def greet(name: str, age: int) -> str:
    return f"Привет, {name}, тебе {age}"

# 3. Функция, которая принимает список строк и возвращает самую длинную из них.
#    Если список пустой — вернуть None.
def longest(list_str: list[str]) -> str | None:
    if not list_str:
        return None
    else:
        a = max(list_str, key = len)
        return a

# 4. Функция, которая принимает словарь {имя: возраст}
#    и возвращает список имён тех, кому 18 или больше.
def adults(people: dict[str, int]) -> list[str]:
    soverchennoletnie = []
    for name, age in people.items():
        if age >= 18:
            soverchennoletnie.append(name)
    return soverchennoletnie

print(adults({"Daniil": 22, "Anna": 15, "Petya": 30}))
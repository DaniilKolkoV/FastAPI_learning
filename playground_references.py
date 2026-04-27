a = 100
b = 100
print(a is b)


print("=== Эксперимент 1: бирки на одном объекте ===")
a = [1, 2, 3]
b = a
print("id(a):", id(a))
print("id(b):", id(b))
print("a is b:", a is b)

print("=== Эксперимент 2: копия — это другой объект ===")
c = a.copy()
print("id(a):", id(a))
print("id(c):", id(c))
print("a is c:", a is c)
print("a == c:", a == c)

print("=== Эксперимент 3: изменение видно через все бирки ===")
b.append(99)
print("a:", a)
print("b:", b)
print("c:", c)
print("a is b:", a is b)
print("id(a):", id(a))
print("id(b):", id(b))

print("=== Эксперимент 4: кэш чисел заканчивается ===")
x1 = 100
x2 = 100
print("100 is 100:", x1 is x2)

y1 = 1000
y2 = 1000
print("1000 is 1000:", y1 is y2)

z1 = 256
z2 = 256
print("256 is 256:", z1 is z2)

z3 = 257
z4 = 257
print("257 is 257:", z3 is z4)

print("=== Эксперимент 4b: динамические числа ===")
import random
n1 = random.randint(1000, 2000)
n2 = random.randint(1000, 2000)
# Принудительно сделаем их равными:
n1 = 1500
n2 = int("1500")   # тут число строится в рантайме, не как литерал
print("n1:", n1, "n2:", n2)
print("n1 is n2:", n1 is n2)

# А вот ещё показательнее: складываем два числа
m1 = 500 + 500  # компилятор сразу свернёт в литерал 1000
m2 = 999 + 1    # это тоже свернёт
print("m1 is m2:", m1 is m2)

# А вот тут уже не свернёт — переменная участвует
k = 500
m3 = k + 500
m4 = k + 500
print("m3 is m4:", m3 is m4)
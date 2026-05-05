from dataclasses import dataclass

@dataclass
class Book:
    title: str
    author: str
    pages: int

book1 = Book("Война и мир", "Лев Толстой", 1225)
print(book1)
print(book1.title)

book2 = Book("Война и мир", "Лев Толстой", 1225)
print(book1 == book2)
print(book1 is book2)


@dataclass
class User:
    name: str
    age: int


u1 = User("Daniil", 22)
print(u1)

# Эксперимент: передаём строку вместо числа
u2 = User("Anna", "двадцать пять")
print(u2)
print(type(u2.age))


@dataclass
class Product:
    name: str
    price: float
    quantity: int = 1

p1 = Product("Сметана", 56.59, 1)
p2 = Product("Сметана", 56.59)

print(p1)
print(p2)
print(p1 == p2)
print(p1.quantity == p2.quantity)

@dataclass(frozen=True)
class Coordinates:
    x: float
    y: float


point = Coordinates(10.0, 20.0)
print(point)

# Попробуем поменять
point.x = 99.0
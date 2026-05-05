class Book:
    def __init__(self, title: str, author: str, pages: int):
        self.title = title
        self.author = author
        self.pages = pages

    def describe(self):
        return f"Книга '{self.title}' автора {self.author}, {self.pages} страниц"

book1 = Book("Война и мир", "Льва Толстого", 1225)
print(book1.describe())

book2 = Book("Сказка о рыбаке и рыбки","Народная сказка",5)
print(book2.describe())

class EBook(Book):
    def __init__(self, title: str, author: str, pages: int, file_size_mb: float):
        super().__init__(title, author, pages)
        self.file_size_mb = file_size_mb

    def describe(self):
        inf = super().describe()
        return f"{inf}, весит {self.file_size_mb} мегабайт"


ebook1 = EBook("Чистый код", "Роберт Мартин", 464, 12.5)
print(ebook1.describe())
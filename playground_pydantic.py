from pydantic import BaseModel, Field, ValidationError, EmailStr


class User(BaseModel):
    name: str = Field(min_length=1, max_length=50)
    age: int = Field(ge=0, le=150)
    email: EmailStr

try:
    user1 = User(name = "Victor", age = 27, email = "victor@gmail.com")
    print(user1)
except ValueError as e:
    print(f"Не удалось создать пользователя, поймал ошибку - {e}")

try:
    user2 = User(name = "", age = 13, email = "pusto@q.ru")
    print(user2)
except ValueError as e:
    print(f"Не удалось создать пользователя, поймал ошибку - {e}")

try:
    user3 = User(name = "Anna", age = -5, email = "pochta_dima")
    print(user3)
except ValueError as e:
    print(f"Не удалось создать пользователя, поймал ошибку - {e}")

try:
    user4 = User(name = "Dima", age = 200, email = "anya_email")
    print(user4)
except ValidationError as e:
    print(f"Не удалось создать пользователя, поймал ошибку - {e}")
    print("=============")
    print("Структурированные ошибки:", e.errors())
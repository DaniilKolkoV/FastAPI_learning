from pydantic import BaseModel, field_validator, Field

class Account(BaseModel):
    username: str
    age: int = Field(ge=0)
    password: str = Field(min_length=8)

    @field_validator("username")
    @classmethod
    def username_check(cls, value: str) -> str:
        if not value.isascii():
            raise ValueError("Используйте только латиницу")
        return value

    @field_validator("password")
    @classmethod
    def password_must_have_digit(cls, value: str) -> str:
        if not any(char.isdigit() for char in value):
            raise ValueError("Пароль должен содержать хотя бы одну цифру")
        return value

accoumt1 = Account(username = "Daniil", age = 20, password = "12345678")
print(accoumt1)

try:
    accoumt2 = Account(username = "Витя", age = 20, password = "12345678")
    print(accoumt2)
except ValueError as e:
    print(f"Не удалось создать пользователя, из-за ошибки :{e}")

try:
    accoumt3 = Account(username = "Artur", age = -1, password = "12345678")
    print(accoumt3)
except ValueError as e:
    print(f"Не удалось создать пользователя, из-за ошибки :{e}")

try:
    accoumt4 = Account(username = "Daniil", age = 20, password = "1234567")
    print(accoumt4)
except ValueError as e:
    print(f"Не удалось создать пользователя, из-за ошибки :{e}")
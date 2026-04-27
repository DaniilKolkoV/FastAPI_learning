def make_account(initial_balance):
    balance = initial_balance

    def deposit(amount):
        nonlocal balance
        balance = balance + amount
        return balance

    def withdraw(amount):
        nonlocal balance
        if amount > balance:
            return "Недостаточно средств"
        balance = balance - amount
        return balance

    def get_balance():
        return balance

    return deposit, withdraw, get_balance


dep, wd, bal = make_account(100)
print(bal())  # ?
print(dep(50))  # ?
print(wd(30))  # ?
print(wd(200))  # ?
print(bal())  # ?
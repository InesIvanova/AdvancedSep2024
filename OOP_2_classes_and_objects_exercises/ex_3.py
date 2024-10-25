from typing import Union

class Account:
    def __init__(self, id: int, name: str, balance: int = 0) -> None:
        self.id = id
        self.name = name
        self.balance = balance

    def credit(self, amount: int) -> int:
        self.balance += amount
        return self.balance

    def debit(self, amount: int) -> Union[str, int]:
        if self.balance >= amount:
            self.balance -= amount
            return self.balance
        return "Amount exceeded balance"

    def info(self) -> str:
        return (f"User {self.name} with account {self.id} "
                f"has {self.balance} balance")


account = Account(5411256, "Peter")
print(account.debit(500))
print(account.credit(1000))
print(account.debit(500))
print(account.info())



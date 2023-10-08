class BankAccount:
    def __init__(self, account_name: str, initial_balance: int = 0) -> None:
        # mypy will infer the correct types for these instance variables
        # based on the types of the parameters
        self.account_name = account_name
        self.balance = initial_balance


    def deposit(self, amount: int) -> None:
       self.balance += amount

    def withdraw(self, amount: int) -> None:
        self.balance -= amount


# User-defined classes are valid as types in annotations
account: BankAccount = BankAccount("Alice", 4000)
def transfer(src: BankAccount, dst: BankAccount, amount: int) ->None:
    src.withdraw(amount)
    dst.deposit(amount)

# Functions that accept BankAccount also accept any subclass of BankAccout!
class AuditedBankAccount(BankAccount):
    # You can optionally declare instance variables in the class body
    audit_log: list[str]


    def __init__(self, account_name: str, initial_balance: int = 0) -> None:
        super().__init__(account_name, initial_balance)
        self.audit_log: list[str] = []


    def deposit(self, amount: int) -> None:
        self.audit_log.append(f"Deposited {amount}")
        self.balance += amount


    def withdraw(self, amount: int) -> None:
        self.audit_log.append(f"Withdrew {amount}")
        self.balance -= amount

audited = AudtedBankAccount("Bob", 300)
transfer(audited, account, 100)


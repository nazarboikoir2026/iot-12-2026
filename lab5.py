class BankAccount :

    def __init__(self, account_id, owner_name, balance=0):
        """Конструктор: створює акаунт з id, ім'ям власника та балансом."""
        self._id = account_id
        self._owner_name = owner_name
        self._balance = balance

    def __del__(self):
        """Деструктор: викликається, коли об'єкт знищується."""
        print(f"Акаунт {self._id} видалено з пам'яті")

    # Функції доступу (геттери)
    @property
    def id(self):
        return self._id

    @property
    def owner_name(self):
        return self._owner_name

    @property
    def balance(self):
        return self._balance

    def show_account(self):
        """Виведення інформації про акаунт."""
        print(f"ID: {self._id} | Власник: {self._owner_name} | Баланс: {self._balance:.2f}")

    def deposit(self, amount):
        """Поповнення балансу (приймає і ціле, і дробове число)."""
        if not isinstance(amount, (int, float)) or amount <= 0:
            print("Некоректна сума для поповнення")
            return
        self._balance += amount
        return

    def withdraw(self, amount):
        """Зняття готівки."""
        if not isinstance(amount, (int, float)) or amount <= 0:
            print("Некоректна сума для зняття")
            return
        if amount > self._balance:
            print("Недостатньо коштів на рахунку")
            return
        self._balance -= amount
        return


class Bank:
    def __init__(self):
        """Конструктор: створює порожній список рахунків."""
        self._accounts = []

    def find_account(self, account_id):
        """Повертає акаунт за id або None, якщо його немає."""
        for account in self._accounts:
            if account.id == account_id:
                return account
        return None

    def add_account(self, account):
        """Додає акаунт у банк (id має бути унікальним)."""
        if self.find_account(account.id) is not None:
            print(f"Рахунок з id {account.id} вже існує")
            return
        self._accounts.append(account)
        return

    def remove_account(self, account_id):
        """Видаляє акаунт з банку за id."""
        account = self.find_account(account_id)
        if account is None:
            print(f"Рахунок з id {account_id} не знайдено")
            return
        self._accounts.remove(account)
        return

    def sort_by_balance(self, reverse=False):
        """Сортує акаунти за балансом (reverse=True - за спаданням)."""
        self._accounts.sort(key=lambda account: account.balance, reverse=reverse)

    def show_all(self):
        """Виводить усі акаунти банку."""
        if not self._accounts:
            print("У банку немає рахунків")
            return
        for account in self._accounts:
            account.show_account()


def main():
    bank = Bank()

    print("=== Створення та додавання рахунків ===")
    acc1 = BankAccount(1, "Іван Петренко", 500)
    acc2 = BankAccount(2, "Марія Коваль", 1200.50)
    acc3 = BankAccount(3, "Олег Шевченко")
    bank.add_account(acc1)
    bank.add_account(acc2)
    bank.add_account(acc3)
    bank.show_all()

    print("\n=== Спроба додати рахунок з існуючим id ===")
    bank.add_account(BankAccount(2, "Дублікат", 10))

    print("\n=== Поповнення (ціле і дробове число) ===")
    acc3.deposit(300)
    acc3.deposit(99.99)
    acc3.show_account()

    print("\n=== Зняття готівки ===")
    acc1.withdraw(200)
    acc1.show_account()
    acc1.withdraw(10000)  # більше, ніж є на рахунку
    acc1.deposit(-50)  # некоректна сума

    print("\n=== Сортування за балансом (за зростанням) ===")
    bank.sort_by_balance()
    bank.show_all()

    print("\n=== Сортування за балансом (за спаданням) ===")
    bank.sort_by_balance(reverse=True)
    bank.show_all()

    print("\n=== Видалення рахунку за id ===")
    bank.remove_account(2)
    bank.remove_account(99)  # неіснуючий id
    del acc2  # прибираємо змінну, щоб спрацював деструктор
    bank.show_all()

    print("\n=== Кінець програми ===")


if __name__ == "__main__":
    main()










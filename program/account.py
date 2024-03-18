# account.py
# This module will contain the Account, SavingsAccount, and CheckingAccount classes.
class Account:
    def __init__(self, balance, annual_interest_rate):
        self.balance = balance
        self.num_deposits = 0
        self.num_withdrawals = 0
        self.annual_interest_rate = annual_interest_rate
        self.monthly_service_charges = 0

    def deposit(self, amount):
        self.balance += amount
        self.num_deposits += 1

    def withdraw(self, amount):
        self.balance -= amount
        self.num_withdrawals += 1

    def calc_int(self):
        monthly_interest_rate = self.annual_interest_rate / 12
        monthly_interest = self.balance * monthly_interest_rate
        self.balance += monthly_interest

    def monthly_proc(self):
        self.balance -= self.monthly_service_charges
        self.calc_int()
        self.num_withdrawals = 0
        self.num_deposits = 0
        self.monthly_service_charges = 0


class SavingsAccount(Account):
    def __init__(self, balance, annual_interest_rate):
        super().__init__(balance, annual_interest_rate)
        self.status = "active"

    def withdraw(self, amount):
        if self.status == "active":
            super().withdraw(amount)
            if self.balance < 25:
                self.status = "inactive"
                print("Account is now inactive due to balance below $25.")
        else:
            print("Withdrawal not allowed. Account is inactive.")

    def deposit(self, amount):
        if self.status == "inactive":
            if self.balance + amount >= 25:
                self.status = "active"
                print("Account is now active.")
        super().deposit(amount)

    def monthly_proc(self):
        if self.num_withdrawals > 4:
            self.monthly_service_charges += (self.num_withdrawals - 4)
            if self.balance - self.monthly_service_charges < 25:
                self.status = "inactive"
                print("Account is now inactive due to balance below $25.")
        super().monthly_proc()


class CheckingAccount(Account):
    def __init__(self, balance, annual_interest_rate):
        super().__init__(balance, annual_interest_rate)

    def withdraw(self, amount):
        if self.balance - amount < 0:
            print("Insufficient funds. Withdrawal cancelled.")
            return
        elif self.balance - amount < -15:
            self.balance -= 15
            print("Service charge of $15 applied.")
        super().withdraw(amount)

    def monthly_proc(self):
        self.monthly_service_charges += 5 + 0.1 * self.num_withdrawals
        super().monthly_proc()

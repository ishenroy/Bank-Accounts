# main.py
# This module will contain the main code for interacting with the bank accounts.
from bank.account import SavingsAccount, CheckingAccount

def main():
    savings_balance = float(input("Enter initial balance for savings account: "))
    checking_balance = float(input("Enter initial balance for checking account: "))
    savings_annual_interest_rate = float(input("Enter annual interest rate for savings account: "))
    checking_annual_interest_rate = float(input("Enter annual interest rate for checking account: "))

    savings = SavingsAccount(savings_balance, savings_annual_interest_rate)
    checking = CheckingAccount(checking_balance, checking_annual_interest_rate)

    deposits = float(input("Enter total deposits for the month for savings account: "))
    withdrawals = float(input("Enter total withdrawals for the month for savings account: "))
    savings.deposit(deposits)
    savings.withdraw(withdrawals)
    savings.monthly_proc()

    deposits = float(input("Enter total deposits for the month for checking account: "))
    withdrawals = float(input("Enter total withdrawals for the month for checking account: "))
    checking.deposit(deposits)
    checking.withdraw(withdrawals)
    checking.monthly_proc()

    print("Statistics for the month:")
    print("Savings Account - Balance:", savings.balance)
    print("Checking Account - Balance:", checking.balance)

if __name__ == "__main__":
    main()

# Mini Banking System using Python (Console-based)

class Account:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Rs.{amount} deposited successfully.")
        else:
            print("Enter a valid amount.")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Rs.{amount} withdrawn successfully.")
        else:
            print("Insufficient balance.")

    def check_balance(self):
        print(f"Available Balance: Rs.{self.balance}")

# Main program
def main():
    print("Welcome to Mini Banking System")
    name = input("Enter your name: ")
    user = Account(name)

    while True:
        print("""
        1. Deposit
        2. Withdraw
        3. Check Balance
        4. Exit
        """)
        choice = input("Enter your choice: ")

        if choice == '1':
            amount = float(input("Enter amount to deposit: "))
            user.deposit(amount)
        elif choice == '2':
            amount = float(input("Enter amount to withdraw: "))
            user.withdraw(amount)
        elif choice == '3':
            user.check_balance()
        elif choice == '4':
            print("Thank you for using Mini Banking System!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()

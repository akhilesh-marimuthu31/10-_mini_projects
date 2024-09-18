class Transaction:
    def __init__(self, amount, category, transaction_type):
        self.amount = amount
        self.category = category
        self.transaction_type = transaction_type

class Tracker:
    def __init__(self):
        self.balance = 0
        self.transactions = []
    
    def add_income(self, amount, category):
        income = Transaction(amount, category, "Income")
        self.transactions.append(income)
        self.balance += amount
        print("\n" + "="*40)
        print(f"✅ Income of {amount} added to category '{category}'")
        print(f"💰 Current Balance: {self.balance}")
        print("="*40 + "\n")
    
    def add_expense(self, amount, category):
        if amount > self.balance:
            print("\n❌ Not enough balance to make this expense.\n")
            return
        expense = Transaction(amount, category, "Expense")
        self.transactions.append(expense)
        self.balance -= amount
        print("\n" + "="*40)
        print(f"💸 Expense of {amount} in category '{category}' added")
        print(f"💰 Current Balance: {self.balance}")
        print("="*40 + "\n")
    
    def view_transactions(self):
        print("\n" + "="*40)
        print("📜 ALL TRANSACTIONS 📜")
        print("="*40)
        
        if not self.transactions:
            print("No transactions to show.")
        else:
            for i, transaction in enumerate(self.transactions, 1):
                print(f"{i}. [{transaction.transaction_type}] - {transaction.category}: {transaction.amount}")
        
        print("="*40 + "\n")
    
    def view_balance(self):
        print("\n" + "="*40)
        print(f"💼 CURRENT BALANCE: {self.balance}")
        print("="*40 + "\n")


def main():
    tracker = Tracker()
    
    while True:
        print("\n" + "="*40)
        print("📊 WELCOME TO EXPENSE TRACKER 📊")
        print("="*40)
        print("1. ➕ Add Income")
        print("2. ➖ Add Expense")
        print("3. 📄 View All Transactions")
        print("4. 💼 View Current Balance")
        print("5. 🚪 Exit")
        print("="*40)
        
        choice = input("Choose an option (1-5): ")

        if choice == '1':
            amount = float(input("Enter income amount: "))
            category = input("Enter category for income (e.g., Salary, Freelancing): ")
            tracker.add_income(amount, category)

        elif choice == '2':
            amount = float(input("Enter expense amount: "))
            category = input("Enter category for expense (e.g., Food, Rent): ")
            tracker.add_expense(amount, category)

        elif choice == '3':
            tracker.view_transactions()

        elif choice == '4':
            tracker.view_balance()

        elif choice == '5':
            print("\n🔒 Exiting the Expense Tracker. Goodbye!\n")
            break

        else:
            print("\n❌ Invalid choice! Please try again.\n")


if __name__ == "__main__":
    main()

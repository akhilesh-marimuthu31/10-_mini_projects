"""
Expense Tracker Program

This program allows users to track their income and expenses. The user can add income or expenses, 
view all transactions, and check the current balance. Each transaction is stored with its type 
(Income or Expense), amount, and category. The program ensures that expenses do not exceed the 
available balance and provides a simple text-based user interface for interaction.
"""
# Class representing a transaction, whether it's income or expense
class Transaction:
    def __init__(self, amount, category, transaction_type):
        # Initialize the transaction with amount, category (e.g., food, salary), and type (income/expense)
        self.amount = amount
        self.category = category
        self.transaction_type = transaction_type

# Class representing the expense tracker that handles balance and transaction history
class Tracker:
    def __init__(self):
        # Initialize with a balance of 0 and an empty list of transactions
        self.balance = 0
        self.transactions = []
    
    # Method to add income to the tracker
    def add_income(self, amount, category):
        # Create a new income transaction and append it to the transactions list
        income = Transaction(amount, category, "Income")
        self.transactions.append(income)
        # Increase the balance by the income amount
        self.balance += amount
        # Print confirmation and updated balance
        print("\n" + "="*40)
        print(f"✅ Income of {amount} added to category '{category}'")
        print(f"💰 Current Balance: {self.balance}")
        print("="*40 + "\n")
    
    # Method to add an expense to the tracker
    def add_expense(self, amount, category):
        # Check if the balance is sufficient to make the expense
        if amount > self.balance:
            print("\n❌ Not enough balance to make this expense.\n")
            return
        # Create a new expense transaction and append it to the transactions list
        expense = Transaction(amount, category, "Expense")
        self.transactions.append(expense)
        # Decrease the balance by the expense amount
        self.balance -= amount
        # Print confirmation and updated balance
        print("\n" + "="*40)
        print(f"💸 Expense of {amount} in category '{category}' added")
        print(f"💰 Current Balance: {self.balance}")
        print("="*40 + "\n")
    
    # Method to view all transactions (income and expense)
    def view_transactions(self):
        print("\n" + "="*40)
        print("📜 ALL TRANSACTIONS 📜")
        print("="*40)
        
        # Check if there are no transactions to display
        if not self.transactions:
            print("No transactions to show.")
        else:
            # Loop through each transaction and print its details
            for i, transaction in enumerate(self.transactions, 1):
                print(f"{i}. [{transaction.transaction_type}] - {transaction.category}: {transaction.amount}")
        
        print("="*40 + "\n")
    
    # Method to view the current balance
    def view_balance(self):
        print("\n" + "="*40)
        print(f"💼 CURRENT BALANCE: {self.balance}")
        print("="*40 + "\n")

# Main function to handle user input and run the program
def main():
    tracker = Tracker()  # Create a new tracker instance
    
    # Main loop for user interaction
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
        
        # Get user choice
        choice = input("Choose an option (1-5): ")

        if choice == '1':
            # User chose to add income
            amount = float(input("Enter income amount: "))
            category = input("Enter category for income (e.g., Salary, Freelancing): ")
            tracker.add_income(amount, category)

        elif choice == '2':
            # User chose to add an expense
            amount = float(input("Enter expense amount: "))
            category = input("Enter category for expense (e.g., Food, Rent): ")
            tracker.add_expense(amount, category)

        elif choice == '3':
            # User chose to view all transactions
            tracker.view_transactions()

        elif choice == '4':
            # User chose to view current balance
            tracker.view_balance()

        elif choice == '5':
            # User chose to exit the program
            print("\n🔒 Exiting the Expense Tracker. Goodbye!\n")
            break

        else:
            # User entered an invalid option
            print("\n❌ Invalid choice! Please try again.\n")

# Ensure the main function runs only when the script is executed directly
if __name__ == "__main__":
    main()

       

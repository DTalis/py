# Part I: BankAccount Class

class BankAccount:
    def __init__(self, balance=0, username='', password=''):
        self.balance = balance
        self.username = username
        self.password = password
        self.authenticated = False

    def deposit(self, amount):
        if amount <= 0:
            raise Exception("Deposit amount must be positive")
        if not self.authenticated:
            raise Exception("You must authenticate first.")
        self.balance += amount
        print(f"Deposited: {amount}, New balance: {self.balance}")

    def withdraw(self, amount):
        if amount <= 0:
            raise Exception("Withdrawal amount must be positive")
        if not self.authenticated:
            raise Exception("You must authenticate first.")
        if self.balance < amount:
            raise Exception("Insufficient balance.")
        self.balance -= amount
        print(f"Withdrew: {amount}, New balance: {self.balance}")

    def authenticate(self, username, password):
        if self.username == username and self.password == password:
            self.authenticated = True
            print("Authentication successful!")
        else:
            print("Invalid username or password.")


# Part II: MinimumBalanceAccount Class

class MinimumBalanceAccount(BankAccount):
    def __init__(self, balance=0, username='', password='', minimum_balance=0):
        super().__init__(balance, username, password)
        self.minimum_balance = minimum_balance

    def withdraw(self, amount):
        if not self.authenticated:
            raise Exception("You must authenticate first.")
        if self.balance - amount < self.minimum_balance:
            raise Exception(f"Cannot withdraw: balance must remain above {self.minimum_balance}")
        super().withdraw(amount)


# Part III: Expanded BankAccount Class with Authentication


# Part IV: ATM Class

class ATM:
    def __init__(self, account_list, try_limit=2):
        if not isinstance(account_list, list):
            raise Exception("Account list must be a list.")
        if not all(isinstance(acc, (BankAccount, MinimumBalanceAccount)) for acc in account_list):
            raise Exception("All accounts must be instances of BankAccount or MinimumBalanceAccount.")
        if try_limit <= 0:
            raise Exception("Try limit must be a positive number.")
        
        self.account_list = account_list
        self.try_limit = try_limit
        self.current_tries = 0

        self.show_main_menu()

    def show_main_menu(self):
        while True:
            print("\nATM Main Menu:")
            print("1. Log in")
            print("2. Exit")
            choice = input("Choose an option: ")
            if choice == '1':
                username = input("Enter username: ")
                password = input("Enter password: ")
                self.log_in(username, password)
            elif choice == '2':
                print("Exiting ATM.")
                break
            else:
                print("Invalid choice, try again.")

    def log_in(self, username, password):
        if self.current_tries >= self.try_limit:
            print("Maximum login attempts reached. Shutting down the ATM.")
            return

        for account in self.account_list:
            account.authenticate(username, password)
            if account.authenticated:
                self.show_account_menu(account)
                return
        
        print("Authentication failed. Try again.")
        self.current_tries += 1
        if self.current_tries < self.try_limit:
            print(f"You have {self.try_limit - self.current_tries} attempts left.")
            self.show_main_menu()
        else:
            print("Maximum login attempts reached. Shutting down the ATM.")

    def show_account_menu(self, account):
        while True:
            print("\nAccount Menu:")
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Exit")
            choice = input("Choose an option: ")
            if choice == '1':
                amount = float(input("Enter deposit amount: "))
                try:
                    account.deposit(amount)
                except Exception as e:
                    print(f"Error: {e}")
            elif choice == '2':
                amount = float(input("Enter withdrawal amount: "))
                try:
                    account.withdraw(amount)
                except Exception as e:
                    print(f"Error: {e}")
            elif choice == '3':
                print("Exiting account menu.")
                break
            else:
                print("Invalid choice, try again.")


# Example usage of the classes

acc1 = BankAccount(balance=100, username="user1", password="pass1")
acc2 = MinimumBalanceAccount(balance=200, username="user2", password="pass2", minimum_balance=50)

atm = ATM([acc1, acc2])


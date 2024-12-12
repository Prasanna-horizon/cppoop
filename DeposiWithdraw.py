def deposit(balance, amount):
    return balance + amount

# Function for withdrawal
def withdraw(balance, amount):
    if balance >= amount:
        return balance - amount
    else:
        print("Insufficient funds for withdrawal.")
        return balance

def main():
    balance = 0
    while True:
        print("\n--- Menu ---")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Show Balance")
        print("4. Exit")
        
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            amount = int(input("Enter amount to deposit: "))
            balance = deposit(balance, amount)
            print(f"{amount} deposited. New balance is: {balance}")
        
        elif choice == 2:
            amount = int(input("Enter amount to withdraw: "))
            balance = withdraw(balance, amount)
            if balance != None:
                print(f"{amount} withdrawn. New balance is: {balance}")
        
        elif choice == 3:
            print(f"Current balance is: {balance}")
        
        elif choice == 4:
            print("Exiting program.")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

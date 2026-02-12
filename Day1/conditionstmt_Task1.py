balance = 5000

while True:
    print("\nChoose what you want to do")
    print("1. Withdraw")
    print("2. Deposit")
    print("3. Display balance")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    match choice:
        case 1:
            amount = float(input("Enter amount to withdraw: "))
            if amount <= balance:
                balance -= amount
                print("Withdrawal successful.")
            else:
                print("Insufficient balance.")

        case 2:
            amount = float(input("Enter amount to deposit: "))
            balance += amount
            print("Deposit successful.")

        case 3:
            print(f"Current balance: {balance}")

        case 4:
            print("Exiting...")
            break

        case _:
            print("Invalid choice. Try again.")
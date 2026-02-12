balance=5000
print("Initial Balance:",balance);
print("1. Deposit");
print("2. Withdraw");
print("3. Balance Enquiry");
choice=int(input("Enter your choice:"))
if choice==1:
    amount=int(input("Enter the amount to deposit:"));
    balance+=amount;
    print("Amount Deposited:",amount)
    print("Updated Balance:",balance);

elif choice==2:
    amount=int(input("Enter the amount to withdraw:"));
    if amount>balance:
        print("Insufficient Balance");
    else:
        balance-=amount;
        print("Amount Withdrawn:",amount);
        print("Updated Balance:",balance);
elif choice==3:
    print("Current Balance:",balance)
else:
    print("Invalid Choice");
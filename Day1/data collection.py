#fruits=["apple","banana","grapes","apples"]
#print(fruits)      #Indexing

cart = []

while True:
    print("\n--- Shopping Cart Menu ---")
    print("1. Add item")
    print("2. View all items")
    print("3. Search item")
    print("4. Remove item")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        item = input("Enter item to add: ")
        cart.append(item)
        print(item, "added to cart")

    elif choice == 2:
        if len(cart) == 0:
            print("Cart is empty")
        else:
            print("Items in cart:")
            for i in cart:
                print("-", i)

    elif choice == 3:
        item = input("Enter item to search: ")
        if item in cart:
            print(item, "is in the cart")
        else:
            print(item, "not found")

    elif choice == 4:
        item = input("Enter item to remove: ")
        if item in cart:
            cart.remove(item)
            print(item, "removed from cart")
        else:
            print(item, "not found")

    elif choice == 5:
        print("Thank you! Exiting...")
        break

    else:
        print("Invalid choice")
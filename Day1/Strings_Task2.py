cart = []

while True:
    print("\n1. Add item")
    print("2. View all items")
    print("3. Search item")
    print("4. Exit")

    ch = int(input("Enter choice: "))

    if ch == 1:
        item = input("Enter item name: ")
        cart.append(item)

    elif ch == 2:
        print("Cart items:", cart)

    elif ch == 3:
        item = input("Enter item to search: ")
        if item in cart:
            print("Item found")
        else:
            print("Item not found")

    elif ch == 4:
        break

    else:
        print("Invalid choice")
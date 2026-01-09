from Controller import InventoryController


def main():
    inventory = InventoryController()

    while True:
        print("\n1. Add Product")
        print("2. Purchase Product")
        print("3. Sell Product")
        print("4. View Inventory")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            inventory.add_product(
                int(input("Product ID: ")),
                input("Name: "),
                float(input("Price: ")),
                int(input("Quantity: ")),
                int(input("Reorder Level: "))
            )

        elif choice == "2":
            inventory.purchase_product(
                int(input("Product ID: ")),
                int(input("Quantity: "))
            )

        elif choice == "3":
            inventory.sell_product(
                int(input("Product ID: ")),
                int(input("Quantity: "))
            )

        elif choice == "4":
            inventory.view_inventory()

        elif choice == "5":
            print("Goodbye 👋")
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()

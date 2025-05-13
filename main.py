from inventory import Inventory
from product import Electronics, Grocery, Clothing

def run():
    inventory = Inventory()
    inventory.load_from_file("inventory.json")
    print("🛍️ Welcome to Inventory System!")

    while True:
        print("\n📌 Menu:")
        print("1. Add Product")
        print("2. Remove Product")
        print("3. Search by Name")
        print("4. Search by Type")
        print("5. List All Products")
        print("6. Sell Product")
        print("7. Restock Product")
        print("8. Total Inventory Value")
        print("9. Remove Expired Products")
        print("10. Exit")
        choice = input("👉 Your choice: ")

        try:
            if choice == "1":
                p_id = int(input("ID: "))
                name = input("Name: ")
                price = float(input("Price: "))
                qty = int(input("Stock: "))
                ptype = input("Type (Electronics, Grocery, Clothing): ").lower()
                if ptype == "electronics":
                    warranty = int(input("Warranty (yrs): "))
                    brand = input("Brand: ")
                    p = Electronics(p_id, name, price, qty, warranty, brand)
                elif ptype == "grocery":
                    expiry = input("Expiry Date (YYYY-MM-DD): ")
                    p = Grocery(p_id, name, price, qty, expiry)
                elif ptype == "clothing":
                    size = input("Size: ")
                    material = input("Material: ")
                    p = Clothing(p_id, name, price, qty, size, material)
                else:
                    print("❌ Invalid type.")
                    continue
                inventory.add(p)

            elif choice == "2":
                pid = int(input("Product ID to remove: "))
                inventory.remove(pid)

            elif choice == "3":
                name = input("Product Name: ")
                results = inventory.search_by_name(name)
                print(*results if results else ["❌ Not found."], sep="\n")

            elif choice == "4":
                ptype = input("Enter type: ")
                results = inventory.search_by_type(ptype)
                print(*results if results else ["❌ No items of this type."], sep="\n")

            elif choice == "5":
                inventory.list_all()

            elif choice == "6":
                pid = int(input("Product ID: "))
                qty = int(input("Quantity to sell: "))
                inventory.sell(pid, qty)

            elif choice == "7":
                pid = int(input("Product ID: "))
                qty = int(input("Quantity to restock: "))
                inventory.restock(pid, qty)

            elif choice == "8":
                inventory.total_value()

            elif choice == "9":
                inventory.remove_expired()

            elif choice == "10":
                inventory.save_to_file("inventory.json")
                print("💾 Saved & Exiting. Goodbye!")
                break

            else:
                print("❌ Invalid choice.")
        except Exception as e:
            print("⚠️ Error:", e)

if __name__ == "__main__":
    run()

# Shopping List Manager
shopping_list = []

def display_menu():
    print("Shopping List Manager")  # Ensure this exists
    print("1. Add Item")  # Ensure this exists as written
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")
    
def add_item():
    item = input("Enter the item to add: ").strip()
    if item:
        shopping_list.append(item)
        print(f"{item} has been added to the shopping list.")
    else:
        print("Invalid input. Please enter a valid item name.")

def remove_item():
    item = input("Enter the item to remove: ").strip()
    # Convert both input and stored items to lowercase for case-insensitive matching
    item_lower = item.lower()
    
    found = False
    for stored_item in shopping_list:
        if stored_item.lower() == item_lower:
            shopping_list.remove(stored_item)
            print(f"{stored_item} has been removed from the shopping list.")
            found = True
            break
    
    if not found:
        print(f"{item} is not in the shopping list.")

def view_list():
    if shopping_list:
        print("\nShopping List:")
        for item in shopping_list:
            print(f"- {item}")
    else:
        print("Your shopping list is empty. Start by adding an item!")

def main():
    while True:
        display_menu()
        choice = input("Choose an option (1-4): ").strip()
        
        if choice == '1':
            add_item()
        elif choice == '2':
            remove_item()
        elif choice == '3':
            view_list()
        elif choice == '4':
            print("Exiting the Shopping List Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
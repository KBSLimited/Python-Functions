#Task 1: Write a function that lets the user add items to a list.

def add_to_list(my_list):
    """Function to add items to a list."""
    while True:
        item = input("Enter an item to add to the list (or 'done' to finish): ")
        if item.lower() == 'done':
            break
        else:
            my_list.append(item)
    return my_list

# Example usage:
my_list = []
print("Add items to the list:")
updated_list = add_to_list(my_list)
print("Updated list:", updated_list)

#Task 2: Include a feature to remove items from the list.

def modify_list(my_list):
    """Function to add or remove items from a list."""
    while True:
        action = input("Do you want to add or remove items? (add/remove/done): ").lower()
        
        if action == 'add':
            item = input("Enter an item to add to the list (or 'done' to finish): ")
            if item.lower() == 'done':
                break
            else:
                my_list.append(item)
        elif action == 'remove':
            if len(my_list) == 0:
                print("List is empty. Nothing to remove.")
            else:
                print("Current list:", my_list)
                item_to_remove = input("Enter the item you want to remove: ")
                if item_to_remove in my_list:
                    my_list.remove(item_to_remove)
                    print(f"'{item_to_remove}' has been removed from the list.")
                else:
                    print(f"'{item_to_remove}' not found in the list.")
        elif action == 'done':
            break
        else:
            print("Invalid action. Please enter 'add', 'remove', or 'done'.")

    return my_list

# Example usage:
my_list = []
print("Modify the list:")
updated_list = modify_list(my_list)
print("Updated list:", updated_list)

#Task 3: Add a function that prints out the entire list in a formatted way.

def modify_list(my_list):
    """Function to add, remove, or print items in a list."""
    while True:
        action = input("Do you want to add, remove, or print items? (add/remove/print/done): ").lower()
        
        if action == 'add':
            item = input("Enter an item to add to the list (or 'done' to finish): ")
            if item.lower() == 'done':
                break
            else:
                my_list.append(item)
        elif action == 'remove':
            if len(my_list) == 0:
                print("List is empty. Nothing to remove.")
            else:
                print("Current list:", my_list)
                item_to_remove = input("Enter the item you want to remove: ")
                if item_to_remove in my_list:
                    my_list.remove(item_to_remove)
                    print(f"'{item_to_remove}' has been removed from the list.")
                else:
                    print(f"'{item_to_remove}' not found in the list.")
        elif action == 'print':
            if len(my_list) == 0:
                print("List is empty.")
            else:
                print("Current list:")
                for i, item in enumerate(my_list, start=1):
                    print(f"{i}. {item}")
        elif action == 'done':
            break
        else:
            print("Invalid action. Please enter 'add', 'remove', 'print', or 'done'.")

    return my_list

# Example usage:
my_list = []
print("Modify the list:")
updated_list = modify_list(my_list)
print("Final list:", updated_list)
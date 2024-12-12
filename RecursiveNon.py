def insert_in_sorted_order(phonebook, name, mobile):
    phonebook.append((name, mobile))
    phonebook.sort(key=lambda x: x[0])

def binary_search_recursive(phonebook, name, low, high):
    if high >= low:
        mid = (high + low) // 2
        if phonebook[mid][0] == name:
            return mid
        elif phonebook[mid][0] > name:
            return binary_search_recursive(phonebook, name, low, mid - 1)
        else:
            return binary_search_recursive(phonebook, name, mid + 1, high)
    else:
        return -1

def binary_search_non_recursive(phonebook, name):
    low = 0
    high = len(phonebook) - 1

    while low <= high:
        mid = (high + low) // 2
        if phonebook[mid][0] == name:
            return mid
        elif phonebook[mid][0] < name:
            low = mid + 1
        else:
            high = mid - 1

    return -1

def main():
    phonebook = []

    while True:
        print("\n--- Menu ---")
        print("1. Add Friend")
        print("2. Search Friend (Recursive Binary Search)")
        print("3. Search Friend (Non-Recursive Binary Search)")
        print("4. Display Phonebook")
        print("5. Exit")
        
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            name = input("Enter friend's name: ")
            mobile = input("Enter friend's mobile number: ")
            insert_in_sorted_order(phonebook, name, mobile)
            print(f"{name} added to phonebook.")
        
        elif choice == 2:
            name = input("Enter friend's name to search: ")
            index = binary_search_recursive(phonebook, name, 0, len(phonebook) - 1)
            if index != -1:
                print(f"Friend found: Name: {phonebook[index][0]}, Mobile: {phonebook[index][1]}")
            else:
                print(f"Friend not found. Adding {name} to phonebook.")
                mobile = input("Enter friend's mobile number: ")
                insert_in_sorted_order(phonebook, name, mobile)
                print(f"{name} added to phonebook.")
        
        elif choice == 3:
            name = input("Enter friend's name to search: ")
            index = binary_search_non_recursive(phonebook, name)
            if index != -1:
                print(f"Friend found: Name: {phonebook[index][0]}, Mobile: {phonebook[index][1]}")
            else:
                print(f"Friend not found. Adding {name} to phonebook.")
                mobile = input("Enter friend's mobile number: ")
                insert_in_sorted_order(phonebook, name, mobile)
                print(f"{name} added to phonebook.")
        
        elif choice == 4:
            print("\nPhonebook:")
            for entry in phonebook:
                print(f"Name: {entry[0]}, Mobile: {entry[1]}")
        
        elif choice == 5:
            print("Exiting program.")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

def insert_in_sorted_order(phonebook, name, mobile):
    phonebook.append((name, mobile))
    phonebook.sort(key=lambda x: x[0])

def fibonacci_search(phonebook, name):
    size = len(phonebook)
    fib_2 = 0  # (m-2)'th Fibonacci number
    fib_1 = 1  # (m-1)'th Fibonacci number
    fib_m = fib_2 + fib_1  # m'th Fibonacci number

    while fib_m < size:
        fib_2 = fib_1
        fib_1 = fib_m
        fib_m = fib_2 + fib_1

    offset = -1

    while fib_m > 1:
        i = min(offset + fib_2, size - 1)

        if phonebook[i][0] < name:
            fib_m = fib_1
            fib_1 = fib_2
            fib_2 = fib_m - fib_1
            offset = i
        elif phonebook[i][0] > name:
            fib_m = fib_2
            fib_1 = fib_1 - fib_2
            fib_2 = fib_m - fib_1
        else:
            return i

    if fib_1 and offset < size - 1 and phonebook[offset + 1][0] == name:
        return offset + 1

    return -1

def main():
    phonebook = []

    while True:
        print("\n--- Menu ---")
        print("1. Add Friend")
        print("2. Search Friend")
        print("3. Display Phonebook")
        print("4. Exit")
        
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            name = input("Enter friend's name: ")
            mobile = input("Enter friend's mobile number: ")
            insert_in_sorted_order(phonebook, name, mobile)
            print(f"{name} added to phonebook.")
        
        elif choice == 2:
            name = input("Enter friend's name to search: ")
            index = fibonacci_search(phonebook, name)
            if index != -1:
                print(f"Friend found: Name: {phonebook[index][0]}, Mobile: {phonebook[index][1]}")
            else:
                print(f"Friend not found. Adding {name} to phonebook.")
                mobile = input("Enter friend's mobile number: ")
                insert_in_sorted_order(phonebook, name, mobile)
                print(f"{name} added to phonebook.")
        
        elif choice == 3:
            print("\nPhonebook:")
            for entry in phonebook:
                print(f"Name: {entry[0]}, Mobile: {entry[1]}")
        
        elif choice == 4:
            print("Exiting program.")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

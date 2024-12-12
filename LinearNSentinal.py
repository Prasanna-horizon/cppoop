def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

def sentinel_search(arr, x):
    n = len(arr)
    last = arr[n - 1]
    arr[n - 1] = x
    i = 0
    while arr[i] != x:
        i += 1
    arr[n - 1] = last
    if i < n - 1 or arr[n - 1] == x:
        return i
    else:
        return -1

def main():
    roll_numbers = []
    num_students = int(input("Enter the number of students: "))
    for _ in range(num_students):
        roll_number = int(input("Enter roll number: "))
        roll_numbers.append(roll_number)

    while True:
        print("\n--- Menu ---")
        print("1. Check attendance using Linear Search")
        print("2. Check attendance using Sentinel Search")
        print("3. Exit")
        
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            search_roll_number = int(input("Enter roll number to search: "))
            result = linear_search(roll_numbers, search_roll_number)
            if result != -1:
                print(f"Student with roll number {search_roll_number} attended the training program.")
            else:
                print(f"Student with roll number {search_roll_number} did not attend the training program.")
        
        elif choice == 2:
            search_roll_number = int(input("Enter roll number to search: "))
            result = sentinel_search(roll_numbers, search_roll_number)
            if result != -1:
                print(f"Student with roll number {search_roll_number} attended the training program.")
            else:
                print(f"Student with roll number {search_roll_number} did not attend the training program.")
        
        elif choice == 3:
            print("Exiting program.")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

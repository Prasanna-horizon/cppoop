def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0

    while low <= high:
        mid = (high + low) // 2

        # If x is greater, ignore left half
        if arr[mid] < x:
            low = mid + 1

        # If x is smaller, ignore right half
        elif arr[mid] > x:
            high = mid - 1

        # x is present at mid
        else:
            return mid

    # x is not present in array
    return -1

def fibonacci_search(arr, x):
    size = len(arr)
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

        if arr[i] < x:
            fib_m = fib_1
            fib_1 = fib_2
            fib_2 = fib_m - fib_1
            offset = i
        elif arr[i] > x:
            fib_m = fib_2
            fib_1 = fib_1 - fib_2
            fib_2 = fib_m - fib_1
        else:
            return i

    if fib_1 and offset < size - 1 and arr[offset + 1] == x:
        return offset + 1

    return -1

def main():
    roll_numbers = []
    num_students = int(input("Enter the number of students: "))
    for _ in range(num_students):
        roll_number = int(input("Enter roll number: "))
        roll_numbers.append(roll_number)

    roll_numbers.sort()
    print(f"Sorted roll numbers: {roll_numbers}")

    while True:
        print("\n--- Menu ---")
        print("1. Search using Binary Search")
        print("2. Search using Fibonacci Search")
        print("3. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            search_roll_number = int(input("Enter roll number to search: "))
            result = binary_search(roll_numbers, search_roll_number)
            if result != -1:
                print(f"Student with roll number {search_roll_number} attended the training program.")
            else:
                print(f"Student with roll number {search_roll_number} did not attend the training program.")

        elif choice == 2:
            search_roll_number = int(input("Enter roll number to search: "))
            result = fibonacci_search(roll_numbers, search_roll_number)
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

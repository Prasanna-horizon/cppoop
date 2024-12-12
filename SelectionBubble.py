def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def top_five_scores(arr):
    return arr[-5:]

def main():
    percentages = []
    num_students = int(input("Enter the number of students: "))
    for _ in range(num_students):
        percentage = float(input("Enter percentage: "))
        percentages.append(percentage)
    
    while True:
        print("\n--- Menu ---")
        print("1. Sort using Selection Sort")
        print("2. Sort using Bubble Sort")
        print("3. Display Top Five Scores")
        print("4. Exit")
        
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            sorted_percentages = selection_sort(percentages.copy())
            print("Sorted array using Selection Sort:", sorted_percentages)
        
        elif choice == 2:
            sorted_percentages = bubble_sort(percentages.copy())
            print("Sorted array using Bubble Sort:", sorted_percentages)
        
        elif choice == 3:
            sorted_percentages = sorted(percentages.copy())
            top_scores = top_five_scores(sorted_percentages)
            print("Top five scores:", top_scores)
        
        elif choice == 4:
            print("Exiting program.")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

def get_average_score(marks):
    total_marks = sum(mark for mark in marks if mark is not None)
    count = sum(1 for mark in marks if mark is not None)
    return total_marks / count if count != 0 else 0

def get_highest_and_lowest_score(marks):
    valid_marks = [mark for mark in marks if mark is not None]
    highest = max(valid_marks) if valid_marks else None
    lowest = min(valid_marks) if valid_marks else None
    return highest, lowest

def count_absent_students(marks):
    return marks.count(None)

def get_highest_frequency_mark(marks):
    valid_marks = [mark for mark in marks if mark is not None]
    if not valid_marks:
        return None
    frequency = {mark: valid_marks.count(mark) for mark in valid_marks}
    most_frequent_mark = max(frequency, key=frequency.get)
    return most_frequent_mark

# Sample data: Marks of N students (None represents an absent student)
marks = [85, 92, 88, None, 75, 92, 79, None, 92, 85]

# a) The average score of the class
average_score = get_average_score(marks)
print(f"Average Score of the class: {average_score}")

# b) Highest score and lowest score of the class
highest_score, lowest_score = get_highest_and_lowest_score(marks)
print(f"Highest Score in the class: {highest_score}")
print(f"Lowest Score in the class: {lowest_score}")

# c) Count of students who were absent for the test
absent_count = count_absent_students(marks)
print(f"Number of students who were absent: {absent_count}")

# Display mark with highest frequency
highest_frequency_mark = get_highest_frequency_mark(marks)
print(f"Mark with highest frequency: {highest_frequency_mark}")

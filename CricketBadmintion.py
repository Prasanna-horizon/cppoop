def cricket_and_badminton(cricket, badminton):
    return cricket & badminton

def either_cricket_or_badminton_but_not_both(cricket, badminton):
    return (cricket | badminton) - (cricket & badminton)

def neither_cricket_nor_badminton(total_students, cricket, badminton):
    return len(total_students - (cricket | badminton))

def cricket_and_football_but_not_badminton(cricket, football, badminton):
    return len((cricket & football) - badminton)

# Example sets of students
total_students = {"A", "B", "C", "D", "E", "F", "G", "H", "I", "J"}
cricket = {"A", "B", "C", "E"}
badminton = {"B", "C", "D", "F"}
football = {"A", "C", "E", "G", "H"}

# a) List of students who play both cricket and badminton
print("Students who play both cricket and badminton:", cricket_and_badminton(cricket, badminton))

# b) List of students who play either cricket or badminton but not both
print("Students who play either cricket or badminton but not both:", either_cricket_or_badminton_but_not_both(cricket, badminton))

# c) Number of students who play neither cricket nor badminton
print("Number of students who play neither cricket nor badminton:", neither_cricket_nor_badminton(total_students, cricket, badminton))

# d) Number of students who play cricket and football but not badminton
print("Number of students who play cricket and football but not badminton:", cricket_and_football_but_not_badminton(cricket, football, badminton))

#Task 1: Code a function to calculate the average grade.

def calculate_average_grade(grades):
    """Function to calculate the average grade."""
    if not grades:
        return "No grades provided"
    else:
        total_grades = sum(grades)
        average_grade = total_grades / len(grades)
        return average_grade

# Example usage:
grades = [85, 90, 75, 92, 88]
average = calculate_average_grade(grades)
print("Average grade:", average)

#Task 2: Implement a function to find the highest and lowest grade.

def find_highest_and_lowest_grade(grades):
    """Function to find the highest and lowest grade."""
    if not grades:
        return "No grades provided"
    else:
        highest_grade = max(grades)
        lowest_grade = min(grades)
        return highest_grade, lowest_grade

# Example usage:
grades = [85, 90, 75, 92, 88]
highest, lowest = find_highest_and_lowest_grade(grades)
print("Highest grade:", highest)
print("Lowest grade:", lowest)

#Task 3: Create a feature that categorizes grades into letter grades (A, B, C, etc.).

def categorize_grades(grades):
    """Function to categorize grades into letter grades."""
    if not grades:
        return "No grades provided"
    else:
        letter_grades = []
        for grade in grades:
            if grade >= 90:
                letter_grades.append('A')
            elif grade >= 80:
                letter_grades.append('B')
            elif grade >= 70:
                letter_grades.append('C')
            elif grade >= 60:
                letter_grades.append('D')
            else:
                letter_grades.append('F')
        return letter_grades

# Example usage:
grades = [85, 90, 75, 92, 88]
letter_grades = categorize_grades(grades)
print("Letter grades:", letter_grades)
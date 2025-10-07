"""
Create a grade processing system with the following requirements:

A global variable passing_grade = 50

(1) A function input_students(num_students) that:

- Creates and returns a list of dictionaries
- Each dictionary contains: {'name': str, 'scores': [list of 3 scores]}

(2) A function calculate_averages(students) that:

- Uses nested loops to calculate each student's average
- Adds an 'average' key to each student dictionary
- Modifies the original list (demonstrate list mutability)

(3) A function display_results(students) that:
- Loops through students
- Uses the global passing_grade to determine pass/fail
- Prints each student's name, average, and status (PASS/FAIL)
"""
"""
Grade Processing System
-----------------------
This program processes student grades using functions and demonstrates:
- Use of global variable (passing_grade)
- List mutability
- Nested loops
"""
passing_grade = 50


def input_students():
    num_students = int(input("Enter number of students: "))
    students = []
    
    print("\n--- Enter Student Information ---\n")
    
    for i in range(num_students):
        print(f"=== Student {i + 1} ===")
        name = input(f"Name: ")
        scores = []
        for j in range(3):
            score = float(input(f"  Score {j + 1}: "))
            scores.append(score)
        students.append({'name': name, 'scores': scores})
        print("-----------------------------\n") 
    
    """
        students = [
        {'name': 'Ratthaphon', 'scores': [55, 60, 70]},
        {'name': 'Nichakamol', 'scores': [40, 45, 50]},
    ]
    """

    return students


def calculate_averages(students):
    """
    Calculates each student's average score and adds it to their dictionary.
    Demonstrates list mutability by modifying the original list.
    """
    for student in students:
        total = sum(student['scores'])
        student['average'] = total / len(student['scores'])


def display_results(students):
    """
    Displays each student's name, average score, and pass/fail status.
    Uses the global variable 'passing_grade' to determine pass/fail.
    """
    print("\n--- Grade Report ---")
    for student in students:
        status = "PASS" if student['average'] >= passing_grade else "FAIL"
        print(f"Name: {student['name']:<12}  Average: {student['average']:.2f}  Status: {status}")


def main():
    """
    Main program flow.
    """
    students = input_students()
    calculate_averages(students)
    display_results(students)



main()

# This dictionary will store all student data.
# Structure:
# {
#   "Student Name": {
#     "Subject1": [grade1, grade2, ...],
#     "Subject2": [grade1, grade2, ...],
#     ...
#   },
#   ...
# }
students_data = {}

def add_student(name):
    """Adds a new student to the tracker."""
    if name in students_data:
        print(f"Student '{name}' already exists.")
    else:
        students_data[name] = {}
        print(f"Student '{name}' added successfully.")

def add_grade(student_name, subject, grade):
    """Adds a grade for a specific subject for a student."""
    if student_name not in students_data:
        print(f"Error: Student '{student_name}' not found.")
        return

    try:
        grade = float(grade) # Ensure grade is a number
        if not (0 <= grade <= 100): # Basic grade validation
            print("Error: Grade must be between 0 and 100.")
            return
    except ValueError:
        print("Error: Invalid grade. Please enter a numeric value.")
        return

    if subject not in students_data[student_name]:
        students_data[student_name][subject] = []

    students_data[student_name][subject].append(grade)
    print(f"Grade {grade} added for {student_name} in {subject}.")

def calculate_subject_average(student_name, subject):
    """Calculates the average grade for a specific subject for a student."""
    if student_name not in students_data:
        # This case should ideally be caught before calling, but good for robustness
        return None
    if subject not in students_data[student_name]:
        return None # No grades for this subject

    grades = students_data[student_name][subject]
    if not grades:
        return 0.0 # Or None, depending on how you want to handle no grades
    return sum(grades) / len(grades)

def calculate_overall_average(student_name):
    """Calculates the overall average grade for a student across all subjects."""
    if student_name not in students_data:
        return None

    all_grades = []
    student_subjects = students_data[student_name]
    if not student_subjects: # No subjects added for the student
        return 0.0

    for subject in student_subjects:
        all_grades.extend(student_subjects[subject])

    if not all_grades:
        return 0.0 # No grades recorded at all
    return sum(all_grades) / len(all_grades)

def display_student_report(student_name):
    """Displays all grades and averages for a specific student."""
    if student_name not in students_data:
        print(f"Error: Student '{student_name}' not found.")
        return

    print(f"\n--- Report for {student_name} ---")
    student_subjects = students_data[student_name]

    if not student_subjects:
        print("No subjects or grades recorded for this student yet.")
        print("Overall Average: N/A")
        print("------------------------")
        return

    for subject, grades in student_subjects.items():
        avg_subject_grade = calculate_subject_average(student_name, subject)
        grades_str = ", ".join(map(str, grades))
        print(f"  Subject: {subject}")
        print(f"    Grades: {grades_str if grades else 'No grades yet'}")
        print(f"    Average: {avg_subject_grade:.2f}" if avg_subject_grade is not None else "    Average: N/A")

    overall_avg = calculate_overall_average(student_name)
    print(f"Overall Average: {overall_avg:.2f}" if overall_avg is not None else "Overall Average: N/A")
    print("------------------------")

def display_all_students_summary():
    """Displays a summary (name and overall average) for all students."""
    if not students_data:
        print("No students in the tracker yet.")
        return

    print("\n--- All Students Summary ---")
    for student_name in students_data:
        overall_avg = calculate_overall_average(student_name)
        print(f"{student_name}: Overall Average = {overall_avg:.2f}" if overall_avg is not None else f"{student_name}: Overall Average = N/A")
    print("--------------------------")

def main_menu():
    """Displays the main menu and handles user interaction."""
    while True:
        print("\n--- Student Grade Tracker ---")
        print("1. Add Student")
        print("2. Add Grade")
        print("3. View Student Report")
        print("4. View All Students Summary")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            name = input("Enter student's name: ").strip()
            if name:
                add_student(name)
            else:
                print("Student name cannot be empty.")
        elif choice == '2':
            student_name = input("Enter student's name: ").strip()
            if student_name not in students_data:
                print(f"Error: Student '{student_name}' not found. Please add the student first.")
                continue
            subject = input("Enter subject name: ").strip()
            grade_input = input("Enter grade: ")
            if student_name and subject and grade_input:
                add_grade(student_name, subject, grade_input)
            else:
                print("Student name, subject, and grade cannot be empty.")
        elif choice == '3':
            student_name = input("Enter student's name to view report: ").strip()
            if student_name:
                display_student_report(student_name)
            else:
                print("Student name cannot be empty.")
        elif choice == '4':
            display_all_students_summary()
        elif choice == '5':
            print("Exiting Grade Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    # You can pre-populate with some data for testing if you like:
    # add_student("Alice")
    # add_grade("Alice", "Math", 90)
    # add_grade("Alice", "Math", 85)
    # add_grade("Alice", "Science", 92)
    # add_student("Bob")
    # add_grade("Bob", "Math", 78)

    main_menu()
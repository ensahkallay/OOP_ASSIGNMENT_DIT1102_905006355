class Student:
    """Represents one student and the student's examination result."""

    students_created = 0

    def __init__(self, student_id, name, age, programme, score=0):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.programme = programme
        self.score = score
        Student.students_created += 1

    def update_score(self, new_score):
        """Update the student's examination score after validation."""
        if not 0 <= new_score <= 100:
            raise ValueError("Score must be between 0 and 100.")
        self.score = new_score

    def display_info(self):
        """Return the student's details and calculated grade."""
        grade = Student.calculate_grade(self.score)
        return (
            f"Student ID: {self.student_id}\n"
            f"Name: {self.name}\n"
            f"Age: {self.age}\n"
            f"Programme: {self.programme}\n"
            f"Score: {self.score}/100\n"
            f"Grade: {grade}"
        )

    @classmethod
    def get_total_created(cls):
        """Return the number of Student objects created."""
        return cls.students_created

    @staticmethod
    def calculate_grade(score):
        """Calculate a grade without needing a Student object."""
        if not 0 <= score <= 100:
            raise ValueError("Score must be between 0 and 100.")
        if score >= 80:
            return "A"
        elif score >= 70:
            return "B"
        elif score >= 60:
            return "C"
        elif score >= 50:
            return "D"
        return "F"


class ResultsManagementSystem:
    """Manages student objects using a single list."""

    def __init__(self, system_name):
        self.system_name = system_name
        self.students = []

    def add_student(self, student):
        """Add a Student object if its ID is not already in the list."""
        for existing_student in self.students:
            if existing_student.student_id == student.student_id:
                print("Error: A student with that ID already exists.")
                return False

        self.students.append(student)
        print(f"{student.name} was registered successfully.")
        return True

    def find_student(self, student_id):
        """Find and return a student by ID; return None if not found."""
        for student in self.students:
            if student.student_id == student_id:
                return student
        return None

    def display_records(self):
        """Display every student record stored in the list."""
        if not self.students:
            print("\nNo student records are available.")
            return

        print(f"\n===== {self.system_name} =====")
        for student in self.students:
            print("\n" + "-" * 35)
            print(student.display_info())
        print("\n" + "-" * 35)
        print(f"Total registered students: {len(self.students)}")


def get_integer(prompt, minimum=None, maximum=None):
    """Read and validate an integer from the user."""
    while True:
        try:
            value = int(input(prompt))
            if minimum is not None and value < minimum:
                print(f"Enter a number of at least {minimum}.")
                continue
            if maximum is not None and value > maximum:
                print(f"Enter a number no greater than {maximum}.")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a whole number.")


def run_program():
    """Main menu for the results management system."""
    system = ResultsManagementSystem("Digital Exam & Results Management System")

    while True:
        print("\n========== MAIN MENU ==========")
        print("1. Register student")
        print("2. Display all student records")
        print("3. Search for a student")
        print("4. Update a student's score")
        print("5. Show number of Student objects created")
        print("0. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            student_id = input("Enter student ID: ").strip()
            name = input("Enter student name: ").strip()
            programme = input("Enter programme: ").strip()

            if not student_id or not name or not programme:
                print("ID, name and programme cannot be empty.")
                continue

            age = get_integer("Enter age: ", 1, 120)
            score = get_integer("Enter examination score (0-100): ", 0, 100)

            student = Student(student_id, name, age, programme, score)
            system.add_student(student)

        elif choice == "2":
            system.display_records()

        elif choice == "3":
            student_id = input("Enter the student ID to search: ").strip()
            student = system.find_student(student_id)
            if student:
                print("\n" + student.display_info())
            else:
                print("Student record not found.")

        elif choice == "4":
            student_id = input("Enter the student ID: ").strip()
            student = system.find_student(student_id)
            if student:
                new_score = get_integer("Enter the new score (0-100): ", 0, 100)
                student.update_score(new_score)
                print("Student score updated successfully.")
            else:
                print("Student record not found.")

        elif choice == "5":
            print(
                "Total Student objects created:",
                Student.get_total_created()
            )

        elif choice == "0":
            print("Thank you for using the system.")
            break

        else:
            print("Invalid option. Please choose from the menu.")


if __name__ == "__main__":
    run_program()

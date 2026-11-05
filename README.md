# OOP1 Assignment: Digital Exam & Results Management System

## Project domain
Education — Digital Exam & Results Management System.

## Description
This Python command-line application registers students, stores their examination
scores, calculates grades, searches for records, displays results, and updates scores.

## Requirements
- Python 3.8 or later
- No external packages are required

## How to run
1. Download or clone this project.
2. Open a terminal in the project folder.
3. Run:

   ```bash
   python oop1_assignment.py
   ```

## OOP concepts demonstrated

### 1. Classes and objects
- `Student` represents an individual student.
- `ResultsManagementSystem` manages Student objects.
- The program creates Student objects when a user registers students.

### 2. Attributes
Each Student object stores:
- `student_id`
- `name`
- `age`
- `programme`
- `score`

### 3. Instance methods
- `update_score()` changes a student's score.
- `display_info()` displays a student's information.

### 4. Class method
`Student.get_total_created()` uses `@classmethod` to return the number
of Student objects created.

### 5. Static method
`Student.calculate_grade()` uses `@staticmethod` to calculate a grade
from a score without requiring a Student object.

### 6. Data structure
The management system uses one main data structure: a Python list named
`students`. Student objects are appended to the list, searched, and displayed.

## Digital Public Goods (DPG) alignment
- **Open source:** The source code can be published in a public GitHub repository.
- **Inclusive and accessible:** The application uses a straightforward text menu
  and clear prompts; it does not depend on a graphical interface.
- **Privacy-respecting:** The program does not connect to a server or upload records.
  Use fictional/sample data for demonstrations and do not enter sensitive personal data.
- **Modular and reusable:** Student and management-system responsibilities are
  separated into classes, and the main menu is placed in `run_program()`.

## Suggested tests
1. Register a student with a score of 85. The grade should be A.
2. Register a second student with a score of 72. The grade should be B.
3. Search using an existing student ID.
4. Search using an ID that does not exist.
5. Try to register a duplicate student ID.
6. Update a student's score and display the records again.
7. Try scores below 0 and above 100; the menu should reject them.

## Limitations
This is an educational prototype. Records are held in memory and are lost when
the program closes. It does not implement user accounts, a database, or online
services. Those features are outside the simplified assignment scope.

## GitHub submission
Create a public repository, for example `oop1-digital-results-management`.
Upload `oop1_assignment.py` and this `README.md`, then copy the repository URL
into your assignment submission.

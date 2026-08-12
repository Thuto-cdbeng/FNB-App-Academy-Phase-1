# The program processes a list of student dictionaries (each with name and marks for three subjects), generate a grade and status for each student, and produce a full class summary report.

# Function definitions
def letter_grade(mark):
    if (mark >= 80):
        return 'A' 

    elif ((mark >= 70) and (mark < 80)):
        return 'B'
    
    elif ((mark >= 60) and (mark < 770)):
        return 'C'
    
    elif ((mark >= 50) and (mark < 60)):
        return 'D'
    
    elif ((mark > 40) and (mark < 50)):
        return 'F'

    else: 
        return "F - Needs intervention"
    
def mark_status(mark):
    if (mark >= 50):
        return "Pass"
    else: 
        return "Fail"
    
def search_student(name):
    #Search contact by name and return the contact if found
    for student in class_report:
        if student["name"].lower() == name.lower():
            return student
    return "Student does not exist in current records"

# Store at least 5 students and their three subject marks in a list of dictionaries
class_records = [
    {"name": "Thabo M", "maths": 60, "english": 59, "science": 35},
    {"name": "Kyle B", "maths": 65, "english": 52, "science": 22},
    {"name": "Lepa J", "maths": 78, "english": 63, "science": 36},
    {"name": "Mireille A", "maths": 54, "english": 55, "science": 55},
    {"name": "Nathi K", "maths": 98, "english": 100, "science": 67},
    {"name": "Thabo S", "maths": 66, "english": 84, "science": 77}
]

# Calculate each student's average using loop
# Apply the grade/status logic in grade_classifier.py
# Build a results list of dictionaries with: name, average, grade, status
class_report = []
for student in class_records:
    average = round((student["maths"] + student["english"] + student["science"]) / 3, 2)

    # Insert new student recorc with the grade being the letter grade and status being pass or fail
    student_report = {"name": student["name"], "average": average, "grade": letter_grade(average), "status": mark_status(average)}
    class_report.append(student_report)

# After the main loop, calculate: class average, highest mark, lowest mark
mark_sheet = []
for student in class_report:
    mark_sheet.append(student["average"])

# Sort the class marksheet
mark_sheet_sorted = sorted(mark_sheet)

# Display a formatted class report showing individual resukts and class statistics

#Welcome message
print("Welcome to the class grade record. Please follow the prompts to be able to view class stats and also access indiividual student records")

print('\n'+'-' * 70)
print("\t CLASS REPORT ")
print('-' * 70)
print("Student   \t|Average Mark \t|Letter Grade \t|Status")
print('-' * 70)

# Display individual marks
for student in class_report:
    print(f"{student["name"]}   \t|{student["average"]} \t\t|{student["grade"]} \t\t|{student["status"]}")

# Display class statistics
print('\n'+'-' * 70)
print("\t CLASS STATISTIICS ")
print('-' * 70)
print(f"Highest mark: \t {mark_sheet_sorted[-1]}")
print(f"Lowest mark: \t {mark_sheet_sorted[0]}")
print('-' * 70 + '\n') 

# Use a while loop to let the user search for a student by name after the report is shown
user_input = input("Would you like to search for a student within the records? Y or N: ")
while (user_input.strip().lower() != "n"):
    name = input("Please enter  the name of the student: ")
    print(search_student(name))
    user_input = input("Repeat search? Y or N: ")

# End of program 
print("\nProgram has ended. Goodbye")

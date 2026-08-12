# The program  that takes a learner’s name and marks for three subjects, calculates an average, assigns a grade and a status (Pass/Fail), and displays a full report card

# Welcome message
print("\nWelcome to the student grade classifier. Please follow the prompts to view the report card of the learner for three subjects")
# Collect learner name and marks three subjects

learner_name = input("Please enter the learner's name: ")
subject1_mark = float(input("Please enter the mark for Subject 1: "))
subject2_mark = float(input("Please enter the mark for Subject 2: "))
subject3_mark = float(input("Please enter the mark for Subject 3: "))

# List of marks
learner_marks = [subject1_mark, subject2_mark, subject3_mark]

# Calculate the average mark of the three subjects 
average_mark = round(((subject1_mark + subject2_mark + subject3_mark) / 3), 2)

print('\n'+'-' * 50)
print(f"\tREPORT CARD FOR: {learner_name.title()}")
print('-' * 50)
print("Subject   \t|Mark \t|Letter Grade \t|Comment")
print('-' * 50)
#  Assign a letter grade to individual marks
i = 1 # For subject numbering
for mark in learner_marks:
    if (mark >= 80):
        print(f"Subject {i} \t|{mark} \t|A \t\t|")
    
    elif ((mark >= 70) and (mark < 80)):
        print(f"Subject {i} \t|{mark} \t|B \t\t|")
    
    elif ((mark >= 60) and (mark < 770)):
        print(f"Subject {i} \t|{mark} \t|C \t\t|")
    
    elif ((mark >= 50) and (mark < 60)):
        print(f"Subject {i} \t|{mark} \t|D \t\t|")
    
    elif ((mark > 40) and (mark < 50)):
        print(f"Subject {i} \t|{mark} \t|F \t\t|")

    else: 
        print(f"Subject {i} \t|{mark} \t|F \t\t|Needs intervention")
    i += 1

# Display average mark and if it is a pass or fail
print('-' * 50)
print('-' * 50)
print(f"Average Mark: \t {average_mark: .2f}")
if (average_mark >=50):
    print("Outcome: \t Pass")
else: 
    print("Outcome: \t Fail")
print('-' * 50)
print('-' * 50)

# End of program
print("\n Program has ended. Goodbye")
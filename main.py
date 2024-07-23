# Code Your Solution Here
# Define the class roster
roster = [
    "Joel Luna,64,82,97,59,68,50,96,56,62,76",
    "Carla Maldonado,68,59,83,76,68,80,91,68,78,62",
    "Jacob Henderson,91,82,68,69,69,76,60,50,81,71",
    "Amber Oneal,100,53,59,92,51,51,81,89,62,79",
    "Katherine Osborne,97,53,84,76,87,58,58,50,89,82",
    "Hannah Bailey,64,68,94,83,84,92,64,66,95,69",
    "Christine Kirby,53,50,55,67,56,55,98,99,81,67",
    "Debra Wilkerson,98,84,97,83,64,83,100,63,63,90",
    "Dylan Fuller,76,84,59,57,72,65,77,66,98,51",
    "Cody Decker,62,76,96,98,70,85,93,89,52,93",
    "Tiffany Jackson MD,100,64,66,53,87,53,75,59,52,70",
    "Timothy Campbell,77,88,90,55,94,98,77,92,80,89",
    "Brandy Huffman,85,92,87,53,52,59,92,59,97,77",
    "Erin Jackson,96,69,76,50,88,58,56,67,94,97",
    "Sandra Atkins,50,90,88,75,71,93,58,51,90,87",
    "Brittany Soto,55,65,80,68,94,57,71,99,97,95",
    "Tyler Hawkins,70,75,56,54,55,94,91,55,78,92",
    "Kevin Bailey,75,73,100,65,71,82,62,50,58,88",
    "Brittany Turner,96,98,56,79,82,83,63,98,81,58",
    "Morgan Osborne,88,74,91,75,66,55,68,69,71,53",
    "Robert Mitchell,71,90,64,100,60,99,84,59,75,82",
    "Darren Medina,90,71,74,80,52,55,77,94,60,92",
    "Jason Brown,88,85,57,88,80,50,92,79,73,64"
]

# Function to calculate the average grade
def calculate_average(grades):
    return sum(grades) / len(grades)

# Function to determine the letter grade
def determine_letter_grade(average):
    if 90 <= average <= 100:
        return 'A'
    elif 80 <= average < 90:
        return 'B'
    elif 70 <= average < 80:
        return 'C'
    elif 60 <= average < 70:
        return 'D'
    else:
        return 'F'

# Process each student in the roster
for student in roster:
    # Split the student data into name and grades
    data = student.split(',')
    name = data[0]
    grades = list(map(int, data[1:]))
    
    # Calculate the average grade
    average_grade = calculate_average(grades)
    
    # Determine the letter grade
    letter_grade = determine_letter_grade(average_grade)
    
    # Print the result
    print(f"{name}: {average_grade:.2f} ({letter_grade})")

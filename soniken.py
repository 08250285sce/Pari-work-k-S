# Step 1: we have to take the input as the last two digits of the student ID of both students.
id1 = int(input("Enter Student 1 ID: "))  # take input of first student ID
id2 = int(input("Enter Student 2 ID: "))  # take input of second student ID

# Extract last two digits using modulus (%) operator
last1 = id1 % 100   # Gets last two digits of first ID
last2 = id2 % 100   # Gets last two digits of second ID

# Generate unique value
unique_value = (last1 + last2) % 10   # Add and take mod 10

# Display the unique value
print("Unique value:", unique_value)


# Step 2: and after getting the unique value we have to store the student names in the dictionary
students = {}   # after storing create empty dictionary

while True:
    name = input("Enter student name (or type 'exit' to stop): ")
    
    # the loop will continue until we stop so Stop the loop if incase user types 'exit'
    if name.lower() == "exit":
        break
    
    # Skip if blank name is entered
    if name == "":
        print("Blank name skipped.")
        continue
    
    # Add student to dictionary with initial score 0
    students[name] = 0


# Step 3: Conduct quiz for each student
for name in students:
    print(f"Quiz for {name}")
    
    score = 0   # Initialize score for the each student for the correct answers

    # Question 1
    ans = int(input(f"{unique_value} + 2 = "))
    if ans == unique_value + 2:   # Check correct answer
        score += 1               # Add 1 mark if correct

    # Question 2
    ans = int(input(f"{unique_value} * 3 = "))
    if ans == unique_value * 3:
        score += 1

    # Question 3
    ans = int(input(f"{unique_value} + 5 = "))
    if ans == unique_value + 5:
        score += 1

    # Store final score in dictionary
    students[name] = score


# Step 4: show the  results, performance, certificate, and stars of each students accordingly
for name, score in students.items():
    print(f"{name}'s Score:", score)

    # Determine performance level
    if score == 3:
        performance = "Excellent"
    elif score == 2:
        performance = "Good"
    elif score == 1:
        performance = "Average"
    else:
        performance = "Poor"

    print("Performance:", performance)

    # Check certificate eligibility
    if score >= 2:
        print("Certificate: Eligible")
    else:
        print("Certificate: Not Eligible")

# Step 5: Print star pattern based on score

    print("Stars:")
    if score == 0:
        print("(No stars)")   # If score is 0, print nothing or message
    else:
        for i in range(score):
            print("*" * (i + 1))   # Print increasing stars
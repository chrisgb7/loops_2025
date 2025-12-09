# Example Practice:
# Given this list of fruits:
fruits = ["apple", "banana", "cherry", "date"]
print(len(fruits))
# Challenge:
# Use a for loop to print each fruit on a new line.
print(fruits[0])
print(fruits[1])
print(fruits[2])
for fruit in fruits:
    print(fruit)
# i just worked with loops

# Given a list of school subjects:
subjects = ["Math", "Science", "History", "Art"]
for subject in subjects:
    print(subject)
    print(len(subject))
for subject in subjects:
    print(subject)
    if subject == "History":
        continue
    else:
        print(subject)
# Challenge:
# Use a for loop and range to print each subject along with its index:
# Example output: "Subject 0: Math"
for subject in subjects:
    print(subject)
    if subject == "Science":
        break
    else:
        print(subject)

# Given:
numbers = [5, 10, 15, 20]

# Challenge:
# Use a for loop to add all the numbers and print the total.
for index in range(len(subjects)):
    print("Subject"+ str(index) + ": " + subjects[index])

total = 0 
for number in numbers:
    total += number
print("total:", total)

new_numbers = list(range(1, 600001))
tote = 0
for new_number in new_numbers:
    tote += new_number
print(tote)

# -------------------------------------------
# Exercise 2: Control Flow and Loops
# -------------------------------------------
# In this exercise, you’ll review how to:
# - Use if, elif, and else statements
# - Control program flow with conditions
# - Use for and while loops effectively
#
# You may discuss and work with your classmates,
# but each learner must submit their own file individually.
# -------------------------------------------
# Task 1: Even or Odd
# -------------------------------------------
print("-------------------------------------------\n"
    + "Task 1: Even or Odd\n"
    + "-------------------------------------------")
# TODO:
# 1. Ask the user for a number (integer).
# 2. Use an if/else statement to check if the number is even or odd.
# 3. Print "<number> is even" or "<number> is odd".
#
# Example:
# Enter a number: 7
# Output: 7 is odd
#
# Write your code below:

number = int(input("Choose a number between 1 and 50: "))
if number %2 == 0:
    print(f"{number} is even.")
else:
    print(f"{number} is odd")

# -------------------------------------------
# Submitting Your Work
# -------------------------------------------
# Once you’ve completed this exercise:
# 1. Save your file
# 2. Open the terminal
# 3. Run:
#    git add Ex2_review.py
#    git commit -m "Completed task 1"
#    git push origin main
# -------------------------------------------
# Task 2: Grade Feedback
# -------------------------------------------
print("-------------------------------------------\n"
    + "Task 2: Grade Feedback\n"
    + "-------------------------------------------")
# TODO:
# 1. Ask the user to enter their test score (0–100).
# 2. Use if/elif/else to print:
#    - "Excellent!" for 70 and above
#    - "Good effort!" for 50–69
#    - "Needs improvement." for below 50
#
# Example:
# Enter your score: 85
# Output: Excellent!
#
# Write your code below:

test = int(input("Enter the test score: "))
if test >= 70:
    print(f"{test} is Excellent!")
elif test <= 49:
    print(f"{test} this Needs Improvement.")
else:
    print(f"{test} this is a Good Effort")

# -------------------------------------------
# Submitting Your Work
# -------------------------------------------
# Once you’ve completed this exercise:
# 1. Save your file
# 2. Open the terminal
# 3. Run:
#    git add Ex2_review.py
#    git commit -m "Completed task 2"
#    git push origin main
# -------------------------------------------
# Task 3: Countdown with While Loop
# -------------------------------------------
print("-------------------------------------------\n"
     + "Task 3: Countdown with While Loop\n"
     + "-------------------------------------------")
# TODO:
# 1. Ask the user for a starting number.
# 2. Use a while loop to count down to 1.
# 3. Print each number as you go.
# 4. When the loop ends, print "Blast off!"
#
# Example:
# Enter a starting number: 5
# Output:
# 5
# 4
# 3
# 2
# 1
# Blast off!
#
# Write your code below:

num = int(input("Choose a starting number: "))
while num > 0:
    print(num)
    num = num - 1
print("Lift off!")

# -------------------------------------------
# Submitting Your Work
# -------------------------------------------
# Once you’ve completed this exercise:
# 1. Save your file
# 2. Open the terminal
# 3. Run:
#    git add Ex2_review.py
#    git commit -m "Completed task 3"
#    git push origin main
# -------------------------------------------
# Task 4: Multiplication Table
# -------------------------------------------
print("-------------------------------------------\n"
    + "Task 4: Multiplication Table\n"
    + "-------------------------------------------")
# TODO:
# 1. Ask the user for a number.
# 2. Use a for loop to print that number’s multiplication table (1 to 10).
# 3. Format each line like: "3 x 4 = 12"
#
# Example:
# Enter a number: 3
# Output:
# 3 x 1 = 3
# 3 x 2 = 6
# ...
# 3 x 10 = 30
#
# Write your code below:

num = int(input("Choose a whole number: "))
for i in range(1, 11):
    print(f"{num} x {i} =", num * i)

# -------------------------------------------
# Submitting Your Work
# -------------------------------------------
# Once you’ve completed this exercise:
# 1. Save your file
# 2. Open the terminal
# 3. Run:
#    git add Ex2_review.py
#    git commit -m "Completed task 4"
#    git push origin main
# -------------------------------------------
# Task 5: Number Guessing Game
# -------------------------------------------
print("-------------------------------------------\n"
    + "Task 5: Number Guessing Game\n"
    + "-------------------------------------------")
# TODO:
# 1. Set a secret number between 1 and 10.
# 2. Ask the user to guess the number.
# 3. Use a while loop to keep asking until they get it right.
# 4. Give hints: "Too high!" or "Too low!" when wrong.
# 5. Print "Correct! Well done." when guessed.
#
# Example:
# Enter your guess: 5
# Output:
# Too low!
# Enter your guess: 9
# Output:
# Correct! Well done.
#
# Write your code below:

secret_num = 9
guess = int(input("Guess the number: "))
while guess != secret_num:
    if guess > secret_num:
        print("Too high!") 
        guess = int(input("Try again: "))
    elif guess < secret_num:
        print("Too low!")
        guess = int(input("Try again: "))
print("Correct!")
        
# -------------------------------------------
# Submitting Your Work
# -------------------------------------------
# Once you’ve completed this exercise:
# 1. Save your file
# 2. Open the terminal
# 3. Run:
#    git add Ex2_review.py
#    git commit -m "Completed task 5"
#    git push origin main
# -------------------------------------------
# -------------------------------------------
# EXTENSION ACTIVITIES
# -------------------------------------------
# Extension 1:
# -------------------------------------------
print("-------------------------------------------\n"
    + "Extension 1:\n"
    + "-------------------------------------------")
# Create a loop that asks the user for a number 5 times.
# Add up all the numbers and print the total.
#
# Example:
# Enter number 1: 3
# Enter number 2: 5
# Enter number 3: 2
# Enter number 4: 8
# Enter number 5: 1
# Output: The total is 19
#
# Write your code below:
# I'm sure there must be an easier way to do this but I couldn't make it work any other way! I understood
# it was something to do with a FOR loop because we had a set amount of numbers but I couldn't figure out
# how to get a loop for inputs and where to store them. I thought that they could probably go into a list
# but I couldn't make that work! So I ended up with this really ugly & repetitive method!

for i in range(1,6): 
    num_1 = int(input("Enter number 1: "))
    num_2 = int(input("Enter number 2: "))
    num_3 = int(input("Enter number 3: "))
    num_4 = int(input("Enter number 4: "))
    num_5 = int(input("Enter number 5: "))
    print("The total is:", num_1+num_2+num_3+num_4+num_5)
    break

# Extension 2:
# -------------------------------------------
print("-------------------------------------------\n"
    + "Extension 2:\n"
    + "-------------------------------------------")
# Create a simple login simulation.
# - The correct password is "python123".
# - Use a while loop that keeps asking until the user types the correct password.
# - Print "Access granted!" when correct.
#
# Example:
# Enter password: hello
# Output: Incorrect, try again.
# Enter password: python123
# Output: Access granted!
#
# Write your code below:

password = "python123"
attempt = input("Enter password: ")
while attempt != password:
    print("Incorrect, try again.")
    attempt = input("Enter password: ")
print("Access granted!")

# -------------------------------------------
# ADVANCED ACTIVITY
# -------------------------------------------
print("-------------------------------------------\n"
     + "ADVANCED ACTIVITY\n"
     + "-------------------------------------------")
# This is an optional challenge for extra practice.
#
# Build a simple menu-driven program:
# 1. Display options:
#    1. Count to 10
#    2. Show even numbers between 1–20
#    3. Exit
# 2. Use a while loop to keep showing the menu until "3" is chosen.
# 3. Run the correct action for each menu choice.
#
# Example:
# Menu:
# 1. Count to 10
# 2. Show even numbers
# 3. Exit
# Enter your choice: 1
# 1 2 3 4 5 6 7 8 9 10
#
# Write your code below:

# I really struggled with this one. It seems once I specified and used a range in line 298 I couldnt
# then use the print(*range(2,21,2)) in line 303 to give the even numbers up to 20? Is this because the
# range had already been set in line 298? If it is how do I get it to reset so I can use range again?

menu = ["Menu:", "1. Count to 10", "2. Show even numbers", "3. Exit"]
print(*menu,sep='\n')
num = int(input("Select an option: "))
while num != 3:
    if num == 1:
        print(*range(1,11)) 
        print(*menu,sep='\n')
        num = int(input("Select an option: "))
    elif num == 2:
        print("2 4 6 8 10 12 14 16 18 20")
        print(*menu,sep='\n')
        num = int(input("Select an option: "))

# -------------------------------------------
# Submitting Your Work
# -------------------------------------------
# Once you have completed all required tasks:
# 1. Save your file.
# 2. Open the terminal and use Git commands to stage, commit, and push your changes.
#    (Hint: recall the commands for adding, committing, and pushing.)
# 3. Check GitHub to confirm your final version appears in your repository.
# -------------------------------------------

# logic_quiz.py
score = 0
print("Welcome to the Logic gate Quiz!")
print("------------------------------")

#Queston 1 
ans1 = input("1. Which logic gets need BOTH inpts to be True? "). lower()

if ans1 == "and":
    print("Correct!")
    score = score + 1
elif ans1 == "amd gate":
    print("Close! The answer is just 'AND'.")
    score = score = 0.5
else:
    print("Wrong! The correct answer is AND.")

# Queston 2 
ans2 = input("2. Which logic gate need AT LEAST ONE inpute tot be True? ").lower()

if ans2 == "or":
    print("Correct!")
    score = score + 1
elif ans2 == "or gate":
    print("Close! The answer is just 'OR'.")
    score = score + 0.5
else:
    print("Wrong! The correct answer is OR.")

# Question 3: Mini Logic Simulator
print("\n--- AND Gate Simulator ---")
num1 = int(input("Enter first number (0 or 1): "))
num2 = int(input("Enter second number (0 or 1): "))

# Check what the AND gate should produce
if num1 == 1 and num2 == 1:
    correct_ans = 1
else:
    correct_ans = 0
ans3 = int(input("What will the AND gate outpu? (0 or 1): "))

if ans3 == correct_ans:
    print("Correct!")
    score = score + 1
else:
    print("Wrong answer.")

# Final Results
print("\n------------------------------")
print(f"Your final score is: {score} out of 3")

if score == 3:
    print("Grade: A - Great job!")
elif score >= 1.5:
    print ("Grade B - Pass!")
else:
    print("Grade: keep practicing!")

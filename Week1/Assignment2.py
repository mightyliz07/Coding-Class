# logic_quiz.py
# Computer Science Quiz Project

# Star sscore at 0
score = 0

print("welcome to my logic gates quiz!")
print("-------------------------------")

# Question 1
q1 = input("Q1: What gate gives True ONLY if both inputs are True? ")
if q1 == "AND" or q1 == "and":
    print("Correct! You get 1 point")
    score = score + 0.5
else:
    print("Wrong, the answer was AND")
print("")

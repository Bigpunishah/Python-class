#!/usr/bin/env python3

# display a welcome message
print("The Test Scores program")
print()
print("Enter 3 test scores")
print("======================")

# get scores from the user
total_score = 0       # initialize the variable for accumulating scores
score1 = int(input("Enter test score 1: "))
score2 = int(input("Enter test score 2: "))
score3 = int(input("Enter test score 3: "))
total_score = score1 + score2 + score3
# calculate average score
average_score = round(total_score / 3)

#Display each score
print("Test 1 score is:\t", score1)
print()
print("Test 2 score is:\t ", score2)
print()
print("Test 3 score is:\t", score3)

# format and display the result
print("======================")
print("Total Score:  ", total_score,
      "\nAverage Score:", average_score)
print()
print("Bye")



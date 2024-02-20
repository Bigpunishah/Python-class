#!/usr/bin/env python3
#Vikel Cunningham 3-1

# display a welcome message
print("The Test Scores application")
print()
print("Enter test scores")
print("Enter end to end input")
print("======================")

# initialize variables
counter = 0
score_total = 0
test_score = 0

# while loop
while test_score != "end":

    test_score = str(input("Enter test score: "))
    if test_score != "end":

        tscore = int(test_score)
        if tscore >= 0 and tscore <= 100:
            score_total += tscore
            counter += 1
        else:
            print("Test score must be from 0 through 100. Score discarded. Try again.")
    elif test_score == "end":
        break

# calculate average score
average_score = round(score_total / counter)
                
# format and display the result
print("======================")
print("Total Score:", score_total,
      "\nAverage Score:", average_score)
print()
print("Bye")



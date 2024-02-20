
#!/ Vikel Cunningham

def display_welcome():
    print("The Test Scores program")
    print("Enter 'x' to exit")
    print("")


def get_scores():
    counter = 0
    list1 = []
    while True:
        scoreInput = input("Enter test score: ")
        if scoreInput == "x":
            print(list1)
            return list1
        else:
            scoreInput = int(scoreInput)
            if scoreInput >= 0 and scoreInput <= 100:
                list1.append(scoreInput)
                list1.sort()
                counter += 1
            else:
                print("Test score must be from 0 through 100. " +
                      "Score discarded. Try again.")


def process_scores(list1):
    # calculate average score
    count = 0
    score_total = 0
    n = len(list1)

    for i in range(len(list1)):
        count += i
        score_total += list1[i]

    average = score_total / count

    lowest_value = min(list1)
    highest_value = max(list1)

    if n % 2 == 0:
        median1 = list1[n // 2]
        median2 = list1[n // 2 - 1]
        median = (median1 + median2) / 2
    else:
        median = list1[n // 2]

    # format and display the result
    print()
    print("Score total:       ", score_total)
    print("Number of Scores:  ", count)
    print("Average Score:     ", average)
    print("Lowest Score:      ", lowest_value)
    print("Highest Score:     ", highest_value)
    print("Median Score:      ", median)


def main():
    display_welcome()
    list1 = get_scores()
    process_scores(list1)
    print("")
    print("Bye!")


# if started as the main module, call the main function
if __name__ == "__main__":
    main()

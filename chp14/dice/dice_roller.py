from dice import Dice, Die


def main():

    print("The Dice Roller program")
    six = " _____ \n" + \
        "|o   o|\n" + \
        "|o   o|\n" + \
        "|o___o|"

    five = " _____ \n" + \
           "|o   o|\n" + \
           "|  o  |\n" + \
           "|o___o|"

    four = " _____ \n" + \
           "|o   o|\n" + \
           "|     |\n" + \
           "|o___o|"

    three = " _____ \n" + \
        "|o    |\n" + \
        "|  o  |\n" + \
        "|____o|"

    two = " _____ \n" + \
        "|o    |\n" + \
        "|     |\n" + \
        "|____o|"

    one = " _____ \n" + \
        "|     |\n" + \
        "|  o  |\n" + \
        "|_____|"

    print()

    # get number of dice from user
    count = int(input("Enter the number of dice to roll: "))
    dice_values = [0] * count
    counter = 0
    # create Die objects and add to Dice object
    dice = Dice()
    for i in range(count):
        die = Die()
        dice.addDie(die)

    while True:
        # roll the dice
        dice.rollAll()
        print("YOUR ROLL: ")
        for die in dice.list:
            # print(die.value, end=" ")
            if (die.value == 1):
                print(one)
            elif (die.value == 2):
                print(two)
            elif (die.value == 3):
                print(three)
            elif (die.value == 4):
                print(four)
            elif (die.value == 5):
                print(five)
            elif (die.value == 6):
                print(six)

            dice_values[counter] = die.value
            counter += 1
            print()

        def getTotal():
            sum = 0
            for i in dice_values:
                  sum += i
            print("TOTAL:\t", sum)
            print("\n")
        getTotal()
        counter = 0
        choice = input("Roll again? (y/n): ")
        if choice != "y":
            print("Bye!")
            break


if __name__ == "__main__":
    main()

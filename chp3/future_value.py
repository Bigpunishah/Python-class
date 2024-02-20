#!/usr/bin/env python3

#Vikel Cunningham exercise 3-1

# display a welcome message
print("Welcome to the Future Value Calculator")
print()

choice = "y"
while choice.lower() == "y":

    # get input from the user

    monthly_investment = float(input("Enter monthly investment:\t"))
    while monthly_investment <= 0:
        print("Please enter a valid investment amount")
        monthly_investment = float(input("Enter monthly investment:\t"))
    else:


        yearly_interest_rate = float(input("Enter yearly interest rate:\t"))
    while yearly_interest_rate <= 0 or yearly_interest_rate >= 15:
        print("Please enter a valid interest rate.")
        yearly_interest_rate = float(input("Enter yearly interest rate:\t"))
    else:


        years = int(input("Enter number of years:\t\t"))
    while years >= 50 or years <= 0:
        print("Please enter a valid number of years.") 
        years = int(input("Enter number of years:\t\t"))
    else:


    # convert yearly values to monthly values
        monthly_interest_rate = yearly_interest_rate / 12 / 100
    months = years * 12

    # calculate the future value
    future_value = 0
    for i in range(months):
        future_value += monthly_investment
        monthly_interest_amount = future_value * monthly_interest_rate
        future_value += monthly_interest_amount
        year = 1
    for i in range(years):
        print("Future value year",  year,":" + "\t\t\t " + str(round(future_value / years, 2)))
        year = year + 1

    # display the result
    print("Future value total:\t\t\t" + str(round(future_value, 2)))
    print()

    # see if the user wants to continue
    choice = input("Continue (y/n)? ")
    print()

print("Bye!")

#!/usr/bin/env python3
#Vikel Cunningham Chapter 
        
def calculate_future_value(monthly_investment, yearly_interest, years):
    # convert yearly values to monthly values
    monthly_interest_rate = yearly_interest / 12 / 100
    months = years * 12

    # calculate future value
    future_value = 0.0
    for i in range(0, months):
        future_value += monthly_investment
        monthly_interest = future_value * monthly_interest_rate
        future_value += monthly_interest

    return future_value
def get_int():
    num = 0
    #What is this function for? The directions do not specify
def get_float():
        monthly_investment = 0
        low_Validity = float(input("Enter low validity value:"))
        high_validity = float(input("Enter high validity value:"))
        while monthly_investment == 0 or monthly_investment < low_Validity or monthly_investment >= high_validity:
            monthly_investment = float(input("Enter monthly investment:\t"))
        if monthly_investment <= 0:
            print("Plese try again!")
        return monthly_investment
            

def main():
    choice = "y"
    while choice.lower() == "y":
        # get input from the user
        # get_float()
        monthly_investment = get_float()
        
        yearly_interest_rate = float(input("Enter yearly interest rate:\t"))
        years = int(input("Enter number of years:\t\t"))

        # get and display future value
        future_value = calculate_future_value(
            monthly_investment, yearly_interest_rate, years)

        print("Future value:\t\t\t" + str(round(future_value, 2)))
        print()

        # see if the user wants to continue
        choice = input("Continue? (y/n): ")
        print()

    print("Bye!")
    
if __name__ == "__main__":
    main()

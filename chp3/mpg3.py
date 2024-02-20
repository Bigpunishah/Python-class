#!/usr/bin/env python3
#Vikel Cunningham exercise 3-1

# display a welcome message
print("The Miles Per Gallon program")
print()

# get input from the user
trips = int(input("Enter the number of trips you would like to calculate:\t"))
x = int(0)
while(x < trips):

    gallons_used = float(input("Enter gallons of gas used:\t"))
    price_gas = float(input("Enter the price of gas per gallon:\t"))
    miles_driven= float(input("Enter miles driven:\t\t"))
# if values are invalid please try again
    if  gallons_used <= 0:
        print("Gallons used must be greater than 0. Please try again")
    elif miles_driven <= 0:
        print("Miles driven must be greater than 0. Please try again")
    elif price_gas <= 0:
        print("The price of gas must be greater than 0. Please try again")


    else:
# calculate miles per gallon
        mpg = round(miles_driven / gallons_used, 2)

# calculate cost of gas
    total_gas_cost = round(gallons_used * price_gas, 2)

#calculate cost of gas
    cost_per_mile = round(gallons_used / price_gas, 2)
            
# format and display the result
    print()
    print("Miles Per Gallon:\t\t" + str(mpg))
    print()
    print("Total cost of gas driven:\t\t" + str(total_gas_cost))
    print()
    print("Cost per mile:\t\t" + str(cost_per_mile))
    print()
    print("I hope you had a great trip!")
    print("\n\n")
x = x+1


print("Bye")



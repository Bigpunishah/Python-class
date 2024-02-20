#!/usr/bin/env python3

# display a welcome message
print("The Miles Per Gallon program")
print()

# get input from the user
miles_driven= float(input("Enter miles driven:\t\t"))
gallons_used = float(input("Enter gallons of gas used:\t"))
price_gas = float(input("Enter the price of gas per gallon:\t"))

# calculate miles per gallon
mpg = miles_driven / gallons_used
mpg = round(mpg, 1)

# calculate cost of gas
total_gas_cost = gallons_used * price_gas
total_gas_cost = round(total_gas_cost, 1)

cost_per_mile = gallons_used / price_gas
cost_per_mile = round(cost_per_mile, 1)
            
# format and display the result
print()
print("Miles Per Gallon:\t\t" + str(mpg))
print()
print("Total cost of gas driven:\t\t" + str(total_gas_cost))
print()
print("Cost per mile:\t\t" + str(cost_per_mile))



print("Bye")



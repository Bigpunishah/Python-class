#! Vikel Cunningham
import csv


def get_miles_driven():
    while True:
        miles_driven = float(input("Enter miles driven :     "))
        if miles_driven > 0:
            return miles_driven
        else:
            print("Entry must be greater than zero. Please try again.\n")
            continue


def get_gallons_used():
    while True:
        gallons_used = float(input("Enter gallons of gas:     "))
        if gallons_used > 0:
            return gallons_used
        else:
            print("Entry must be greater than zero. Please try again.\n")
            continue


def addToList():
    miles = get_miles_driven()
    gallons = get_gallons_used()
    mpg = round((miles / gallons), 2)
    data = []
    data.append(int(miles))
    data.append(int(gallons))
    data.append(mpg)
    return data


def main():
    # display a welcome message
    print("The Miles Per Gallon application")
    print()

    data_list = []
    more = "y"
    while more.lower() == "y":

        data = []
        data = addToList()
        data_list.append(data)

        more = input("More entries? (y or n): ")

    filename = "Trips.csv"
    feilds = ["Distance", "Gallons", "MPG"]
    with open(filename, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(feilds)
        for i in range(len(data_list)):
            csvwriter.writerow(data_list[i])
        

    print(data_list)

    print("Bye")


if __name__ == "__main__":
    main()

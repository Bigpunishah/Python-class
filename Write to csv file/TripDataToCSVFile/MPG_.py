#!Vikel Cunningham
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


def getTrips():
    trips = []
    miles = get_miles_driven()
    gals = get_gallons_used()
    mpg = round((miles / gals), 2)
    trips.append(int(miles))
    trips.append(int(gals))
    trips.append(mpg)
    return trips


def listTrips(read=[]):
    print()
    for i in read:
        print(i)


def main():
    # display a welcome message
    print("The Miles Per Gallon application")
    print()
    trips_data = []

    more = "y"
    while more.lower() == "y":
        trips = []
        trips = getTrips()
        trips_data.append(trips)

        filename = "trips.csv"
        title = ["The Miles Per Gallon program"]
        feilds = ["Distance", "Gallons", "MPG"]

        with open(filename, 'w', newline='') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(title)
            csvwriter.writerow(feilds)
            for i in range(len(trips_data)):
                csvwriter.writerow(trips_data[i])
                # print(trips_data[i])

            # listTrips(trips_data)

        with open(filename) as readcsvFile:
            read = csv.reader(readcsvFile)
            listTrips(read)

        print()

        more = input("More entries? (y or n): ")

    print("Bye")


if __name__ == "__main__":
    main()

#! Vikel Cunningham
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
    data.append(int(mpg))
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

    for i in range(len(data_list)):
        data_to_byte = bytearray(data_list[i])
        filename = "trips.bin"
        binary_file = open(filename, 'wb')
        binary_file.write(data_to_byte)

    print(data_list)

    print("Bye")


if __name__ == "__main__":
    main()

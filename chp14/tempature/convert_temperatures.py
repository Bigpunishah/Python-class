#Vikel Cunningham

from temperature import Temp as temp

def display_menu():
    print("The Convert Temperatures program")
    print()
    print("MENU")
    print("1. Fahrenheit to Celsius")
    print("2. Celsius to Fahrenhit")
    print()

def convert_temp():
    option = int(input("Enter a menu option: "))
    if option == 1:
        f = float(input("Enter degrees Fahrenheit: "))
        c = temp.to_celsius(f)
        print("Degrees Celsius:", c)  
        print("Degrees Fahrenheit:", f)  

    elif option == 2:
        c = float(input("Enter degrees Celsius: "))
        f = temp.to_fahrenheit(c)
        print("Degrees Fahrenheit:", f)
        print("Degrees Celsius:", c)
    else:
        print("You must enter a valid menu number.")

def main():
    display_menu()
    again = "y"
    while again.lower() == "y":
        convert_temp()
        print()
        again = input("Convert another temperature? (y/n): ")
        print()
    print("Bye!")

if __name__ == "__main__":
    main()

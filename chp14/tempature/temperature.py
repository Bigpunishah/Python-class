#Vikel Cunningham

class Temp:
    def to_celsius(fahrenheit):
        celsius = (fahrenheit - 32) * 5/9
        return celsius

    def to_fahrenheit(celsius):
        fahrenheit = celsius * 9/5 + 32
        return fahrenheit

    # for temp in range(0, 212, 40):
    #     print(temp, "Fahrenheit equals", round(to_celsius(temp), 2), "Celsius")

    # for temp in range(0, 100, 20):
    #     print(temp, "Celsius equals", round(to_fahrenheit(temp), 2), "Fahrenheit")


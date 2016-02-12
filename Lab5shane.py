"""Prints a temperature conversion table."""

def main():
    print()
    print("  Celsius       Kelvin        Fahrenheit         Rankine")
    print()

    for celsius in range(-30, 60, 10):

        # Calculate temperature conversions
        kelvin = celsius + 273.15
        fahr = celsius * 1.8 + 32
        rankine = kelvin * 1.8 + 32

        # Convert to strings
        celsius_str = str(celsius)
        kelvin_str = str("%.2f" % kelvin)
        fahr_str = str("%.2f" % fahr)
        rankine_str = str("%.2f" % rankine)

        # Print (aligned right)
        print("   ", celsius_str.rjust(3), "      ", kelvin_str.rjust(7), "       ", fahr_str.rjust(7), "         ", rankine_str.rjust(7))


main()
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5
CELSIUS_OFFSET = 32
def convert_to_celsius(fahrenheit):
    """Converts Fahrenheit to Celsius"""
    return (fahrenheit - CELSIUS_OFFSET) * FAHRENHEIT_TO_CELSIUS_FACTOR
def convert_to_fahrenheit(celsius):
    """Converts Celsius to Fahrenheit"""
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + CELSIUS_OFFSET
def main():
    try:
        temperature = float(input("Enter the temperature to convert: "))
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
        if unit == 'C':
            converted_temperature = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is {converted_temperature}°F")
        elif unit == 'F':
            converted_temperature = convert_to_celsius(temperature)
            print(f"{temperature}°F is {converted_temperature}°C")
        else:
            print("Invalid unit. Please enter C for Celsius or F for Fahrenheit.")
    except valueError:
        print("Invalid temperature. Please enter a numeric value.")
if __name__ == "__main__":
    main()

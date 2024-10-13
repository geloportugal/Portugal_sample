print("What is your name? ")
name = input()

print(f"Hello, {name}! Welcome to the Celsius-Fahrenheit, Fahrenheit-Celcius Converter. \nWhat would you like to convert from? Pick a number: \n1. Celcius to Fahrenheit \n2. Fahrenheit to Celcius")
conv_type = float(input())

if conv_type == 1:
    print("You are now converting from Celcius to Fahrenheit. Input the temperature value: ")
    ctemp = float(input()) 
    cel_to_fah = (ctemp*9/5)+32
    convtemp = round(cel_to_fah, 2)
    print(f"Hello {name}! {ctemp}°C in Fahrenheit is {convtemp}°F.")

elif conv_type == 2:
    print("You are now converting from Fahrenheit to Celcius. Input the temperature value: ")
    ctemp = float(input())
    fah_to_cel = (ctemp-32)*5/9
    convtemp = round(fah_to_cel, 2)
    print(f"Hello, {name}! {ctemp}°F in Celcius is {convtemp}°C.")

else:
    print("Please input a number only between 1 and 2. Run the program again.")
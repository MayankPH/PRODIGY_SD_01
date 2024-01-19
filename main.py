def input_cel(temp):
    f = (9 * temp / 5) + 32
    k = temp + 273
    print(f"{temp}°C is {f}°F and {k}K")


def input_far(temp):
    c = (temp - 32) * 5 / 9
    k = c + 273
    print(f"{temp}°F is {c}°C and {k}K")


def input_kel(temp):
    c = temp - 273
    f = (9 * c / 5) + 32
    print(f"{temp}K is {c}°C and {f}°F")


temp = int(input("Enter the Magnitude of Temperature: "))
unit = input('''Enter Unit: 
                Celsius     ->  C
                Fahrenheit  ->  F
                Kelvin      ->  K
''').lower()

if unit == 'c':
    input_cel(temp)
elif unit == 'f':
    input_far(temp)
elif unit == 'k':
    input_kel(temp)
else:
    print("Invalid Input! Please try Again!!!")
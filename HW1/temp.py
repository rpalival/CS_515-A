f_temp_string = input('Enter temperature in Fahrenheit: ')
f_temp = float(f_temp_string)

def celsius_to_fahrenheit(f_temp):
    c_temp = (f_temp - 32) * (5 / 9)
    return c_temp

print(f'Temperature in Celsius: {celsius_to_fahrenheit(f_temp)}')
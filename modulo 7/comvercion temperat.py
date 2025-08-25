def celsius_a_fahrenheit(celsius):  
    return (celsius * 9/5) + 32

def fahrenheit_a_celsius(fahrenheit):  
    return (fahrenheit - 32) * 5/9

def celsius_a_kelvin(celsius):  
    return celsius + 273.15

def kelvin_a_celsius(kelvin):  
    return kelvin - 273.15

# Ejemplo de uso
temp_c = 25
print(f"{temp_c}°C = {celsius_a_fahrenheit(temp_c)}°F")
print(f"{temp_c}°C = {celsius_a_kelvin(temp_c)}K")

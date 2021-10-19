# converts fahrenheit to degree celcius
"""
lower = int(0)
upper = int(400)
step = int(20)
fahr = lower

while fahr <= upper:
    celcius = (5 * (fahr - 32))/9
    Celcius = float(celcius)
    print(fahr, round(Celcius, 2))
    fahr = fahr + step
"""

# convert the user input to degree celcius

lower = int(0)
upper = input('Enter the temperature(in fahrenheit): ')
Upper = float(upper)
fahr = lower

while lower <= Upper:
    celcius = (5 * (Upper - 32))/9
    Celcius = float(celcius)

    print('The temperature in Celcius is', round(Celcius, 2))

    break
    

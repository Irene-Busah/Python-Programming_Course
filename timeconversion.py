#converts seconds to hours and minutes
"""
def second_conversion(seconds):
    hours = int(seconds / 3600)
    minutes = int((seconds - hours * 3600) / 60)
    remaining_seconds = seconds - hours * 3600 - minutes * 60
    return hours, minutes, remaining_seconds

hours, minutes, seconds = second_conversion(5000)
print(hours, minutes, seconds)
"""


#take the number of seconds from the user and break it down into hours, minutes & remaining seconds.
"""
def second_conversion():
    hr = int(hrs / 3600)
    minutes = int((hrs - hr * 3600) / 60)
    remaining_second = int(hrs - hr * 3600 - minutes * 60)
    return hr, minutes, remaining_second
hours = input("Please enter the time(in seconds): ")
hrs = int(hours)
hr, minutes, remaining_second = second_conversion()
print(hr, minutes, remaining_second)
"""

# code verifies the length of login names of workers in company


def name_checker():

    if len( name ) <= 3:
        return("Invalid name. Try again")

    elif len(name) > 15:
        return("Long login name. Try again")
    else:
        return("You have logged in successfully")


name = input("Enter your login name: ")
name = name_checker()
print(name.upper())


"""
def computepay(hr, r):
    if hr > 40:
        pay = hr * r
        grossPay = (hr - 40) * (r * 0.5)
        netPay = pay + grossPay

    else:
        netPay = hr * r
    return netPay

hours = input("Enter the number of hours: ")
hr = float(hours)
rate = input("Enter the rate: ")
r = float(rate)


print("Your salary for the month is: ", computepay(hr, r))
"""

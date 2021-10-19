# prints the pay of employees
"""
def computePay(hr, r):


    if hr > 40:
        pay = hr * r
        netPay = (hr - 40) * (1.5 * r)
        grossPay = pay + netPay

    else:
        grossPay = hr * r

    return grossPay
hour = input('Enter the hours you worked: ')
hr = float(hour)
rate = input('Enter the rate: ')
r = float(rate)

grossPay = computePay(hr, r)

print('Your salary is', grossPay)

"""
def computePay(hr, r):

        if hr > 40:
            pay = hr * r
            grossPay = (hr - 40) * (1.5 * r)
            netPay = pay + grossPay
        else:
            netPay = hr * r

        return netPay

hour = input('Enter the hours you worked: ')
hr = float(hour)
rate = input('Enter the rate: ')
r = float(rate)

netPay = computePay(hr, r)
print('Your salary is', netPay)
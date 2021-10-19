# this code executes the salary of workers

def computepay(hr, r):
    if hr > 40:
        Grosspay = (hr - 40) * (r * 0.5)
        pay = hr * r
        Netpay = Grosspay + pay
    else:
        Netpay = hr * r

    return Netpay


hours = input('Enter the number of hours: ')
hr = float(hours)
rate = input('Enter your rate(in percentage): ')
r = float(rate)

Netpay = computepay(hr, r)

print('Your salary for the month is', Netpay)

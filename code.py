# this code calculate the amount a worker receives taking overtime into consideration

hour = input('Enter the number of hours: ')
hr = float(hour)
rate = input('Enter your rate: ')
r = float(rate)

if hr > 40:
    Grosspay = (hr - 40) * (r * 0.5)
    pay = hr * r
    Netpay = Grosspay + pay
else:
    Netpay = hr * r

print('Your pay for the month is', Netpay)


# this code prints out the largest & smallest numbers the user puts in

largest = None
smallest = None

while True:

    try:
        number = input('Enter the number: ')
        if number == 'done':
            break
        n = int(number)
        if largest is None or n > largest:
            largest = n
        elif smallest is None or n < smallest:
            smallest = n

    except:
        print('Invalid input')
        continue

print('The maximum number is', largest)
print('The minimum number is', smallest)



#remodifying the above code, including list

# Largest = None
# Smallest = None
# new_list = []
#
# while True:
#     try:
#         number = input("Please enter the number: ")
#         if number == 'done':
#             break
#         num = int(number)
#         new_list.append(num)
#
#     except:
#         print("Invalid Input")
#         continue
# print(new_list)
# print("The maximum number is ", max(new_list))
# print("The minimum number is ", min(new_list))






"""
count = 0
total = 0
average = 0
while True:
    try:
        num = input("Please enter a number: ")

        if (num == "done"):
            break
        number = float(num)
        count = count + 1
        total = total + number
        average = total / count


    except:
        print("Invalid input")
        continue

print("Number of items is: ", count)
print("The total of the numbers is ", total)
print("The average of the numbers is ", average)

"""


"""
total = list()
while True:
    try:
        num = input("Enter the number: ")
        if num == 'done':
            break
        number = float(num)
        total.append(number)

    except:
        print("Invalid input")
        continue

print("Average: ", sum(total)/len(total))
"""

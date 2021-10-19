# code works like the ATM system

print("Welcome to Ghana Commercial Bank!")
restart = ("Y")
Balance = 67.9
chances = 3

while chances >= 0:
    password = input("Please enter your secret number: ")
    pin = int(password)
    if pin // 10 >= 4:
        print("You are logged in successfully")
        while restart not in ("No", "N", "no", "n"):
            print("Press 1 to check your Balance")
            print("Press 2 to make withdrawal")
            print("Press 3 to pay in")
            print("Press 4 to Return card")
            option = int(input("Choose an option: "))
            if option == 1:
                print("Your balance is Ghc ", Balance)
                restart = input("Would your like to do anything else? ")
                if restart in ("No", "N", "no", "n"):
                    print("Thank you")
                    break
            elif option == 2:
                option2 = ("y")
                withdraw = float(input("Amount to withdraw: \n Ghc 10\ Ghc 20\ Ghc 40\ Ghc 60\ Ghc 80\ Ghc 100"))
                if withdraw in [10, 20, 40, 60, 80, 100]:
                    Balance = Balance - withdraw
                    print("Your balance is ", Balance)
                    restart = input("Would you like to do anything else? ")
                    if restart in ("No", "N", "no", "n"):
                        print("Thank you")
                        break
                elif withdraw != [10, 20, 40, 60, 80, 100]:
                    print("Invalid Amount, Please re-try!")
                    restart = ("y")
                elif withdraw == 1:
                    withdraw = float(input("Please enter your desired amount: "))

            elif option == 3:
                pay_in = float(input("How much do you want to deposit? "))
                Balance = Balance + pay_in
                print("Your balance is Ghc ", Balance)
                restart = input("Would you want to do anything else? ")
                if restart in ("No", "N", "no", "n"):
                    print("Thank you for your service")
                    break

            elif option == 4:
                print("Please wait whilst your card is being returned.....")
                print("Thank you for your service!")
                break
            else:
                print("Please enter a correct number: ")
                restart = ("y")

    elif pin // 10 != 4:
        print("Incorrect password")
        chances -= 1
        if chances == 0:
            print("You have no tries")
            break

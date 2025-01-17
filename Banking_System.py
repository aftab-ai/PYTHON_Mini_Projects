# Banking System

def showBalance(balance):
    print("**************")
    print("Your balance is $",balance)

def deposit():
    amount = float(input("Enter an amount to be deposit: "))

    if amount < 0:
        print("**************")
        print("That's not a valid amount")
        return 0
    else:
        return amount

def withdraw(balance):
    amount = float(input("Enter amount to be withdrawn: "))

    if amount > balance:
        print("**************")
        print("Insufficient funds!")
    elif amount < 0:
        print("**************")
        print("Amount must be greater than 0")
        return 0
    else:
        return amount

def main():
    balance = float(0)
    is_running = True

    while is_running:
        print("**************")
        print("Banking System")
        print("1.Show Balance")
        print("2.Deposit")
        print("3.Withdraw")
        print("4.Exit")
        print("**************")

        userChoice = int(input("Enter your choice (1 - 4): "))

        if (userChoice == 1):
            showBalance(balance)
        elif (userChoice == 2):
            balance += deposit()
        elif (userChoice == 3):
            balance -= withdraw(balance)
        elif (userChoice == 4):
            is_running = False
        else:
            print("**************")
            print("Please select a valid choice !")

    print("**************")
    print("Thank You! Have a nice day.")

if __name__ == "__main__":
    main()
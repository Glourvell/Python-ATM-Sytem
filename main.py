pin = 3030
Balance = 500

#menu
def menu():
        print("ATM MENU")
        print("1. Check balance")
        print("2. Withdraw money")
        print("3. Deposit money")
        print("4. Change PIN")
        print("Please choose a number to select an option below")

        user_choice = int(input())
        if user_choice == 1:
             print('Your balance is Ksh:', Balance)
        elif user_choice == 2:
             print("How much do you want to withdraw:")
             withdrawal_amount = int(input())
             new_balance = Balance - withdrawal_amount
             print(f"You have successfuly withdrawn Ksh: {withdrawal_amount}, your new amount is Ksh: {new_balance}")
        elif user_choice == 3:
             print("How much money do you want to deposit: ")
             deposit = int(input())
             new_balance = Balance + deposit
             print(f"You have succesfully deposited Ksh: {deposit}, your new balance is Ksh: {new_balance}")
             
            


def pin_verifier(pin):
    print("Enter your PIN:")
    user_pin = int(input())
    if user_pin == pin:
        print("Your PIN is correct")
        menu()
    else:
        def attempt():
            i = 1
            while i < 4:
                print(f"You have entered a wrong PIN, you have {4 - i} attempts left")
                if user_pin == pin:
                    print("Your PIN is correct")
                    return
                i += 1
                print("You are out of attempts")

        attempt()



pin_verifier(pin)
 






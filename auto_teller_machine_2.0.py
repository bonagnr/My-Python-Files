balance = 1000.00
while True:
    print('\t*** ATM - Auto Teller Machine ***')
    print("[1].Check Balance")
    print("[2].Deposit")
    print('[3].Withdraw')
    print('[4].Exit')
    number = int(input("choose one number: "))
    match number:
        case 1:
            print(f'\nYour Balance is {balance}\n')
            
        case 2:
            deposit = float(input('\nInput Deposit amount: '))
            # print()
            if deposit <= 0:
                print("\nInvalid amount\n")
            else:
                balance += deposit
                print("\nDeposit successful\n")

        case 3:
            withdraw = float(input('\nInput Withdraw amount: '))
            if withdraw <= 0:
                print("\nInvalid amount\n")
            elif withdraw > balance:
                print("\nInsufficient Balance\n")
            else:
                balance -= withdraw
            print("\nWithdraw successful\n")
            # print()

        case 4:
            print('\nExit program...\n')
            exit(0)
            
        case _:
            print('\nError: Wrong number input again\n')
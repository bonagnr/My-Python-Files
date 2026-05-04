import os  # ADD THIS at the top

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    # 'cls'   → Windows
    # 'clear' → Linux / Mac

def sum(a,b):
    c = a + b
    return c

def sub(a,b):
    c = a - b
    return c

def mul(a,b):
    c = a * b
    return c

def div(a,b):
    c = a / b
    return c

while True:
    print('\t*** Calculator 1.0 ***')
    print("[1].Sum")
    print("[2].Sub")
    print('[3].Mul')
    print('[4].Div')
    print('[5].Clear Screen')   # ✅ Uncommented
    print('[0].Exit')
    number = int(input("choose number: "))
    match number:
        case 0:
            print('\nExit program...\n')
            exit(0)
        case 1:
            a = float(input('input a : '))
            b = float(input('input b : '))
            print(f'{a:,} + {b:,} = {sum(a,b):,}')
        case 2:
            a = float(input('input a : '))
            b = float(input('input b : '))
            print(f'{a:,} - {b:,} = {sub(a,b):,}')
        case 3:
            a = float(input('input a : '))
            b = float(input('input b : '))
            print(f'{a:,} * {b:,} = {mul(a,b):,}')
        case 4:
            a = float(input('input a : '))
            b = float(input('input b : '))
            print(f'{a:,} / {b:,} = {div(a,b):,}')
        case 5:
            clear_screen()      # ✅ Uncommented and working
        case _:
            print('\nError: Wrong number input again\n')
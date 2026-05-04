import os

class Calculator: #oop calculator
    def sum(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def mul(self, a, b):
        return a * b

    def div(self, a, b):
        if b == 0:
            return "Error: Division by zero"
        return a / b

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def run(self):
        calc = Calculator()

        while True:
            print('\t*** Calculator 1.0 ***')
            print("[1].Sum")
            print("[2].Sub")
            print('[3].Mul')
            print('[4].Div')
            print('[5].Clear Screen')
            print('[0].Exit')
            number = int(input("choose number: "))

            match number:
                case 0:
                    print('\nExit program...\n')
                    exit(0)

                case 1:
                    a = float(input('input a : '))
                    b = float(input('input b : '))
                    print(f'{a:,} + {b:,} = {self.sum(a, b):,}')

                case 2:
                    a = float(input('input a : '))
                    b = float(input('input b : '))
                    print(f'{a:,} - {b:,} = {self.sub(a, b)}')

                case 3:
                    a = float(input('input a : '))
                    b = float(input('input b : '))
                    print(f'{a:,} * {b:,} = {self.mul(a, b)}')

                case 4:
                    a = float(input('input a : '))
                    b = float(input('input b : '))
                    print(f'{a:,} / {b:,} = {self.div(a, b)}')

                case 5:
                    self.clear_screen()

                case _:
                    print('\nError: Wrong number input again\n')


# Entry point
app = Calculator()
app.run()
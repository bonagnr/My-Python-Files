class Car:
    def __init__(self,brand,year,color):
        self.brand = brand
        self.year = year
        self.color = color

    def car_age(self,current_year=2026):
        return current_year - self.year
    
    def showCar(self):
        print(f'- Car\t\t: {self.brand}')    
        print(f'- Made in\t: {self.year}')
        print(f'- Color\t\t: {self.color}')
        
    def change_color(self, new_color):
        self.color = new_color


class ElectricCar(Car):
    def __init__(self, brand, year, color,battery_size):
        super().__init__(brand, year, color) # super function()
        self.battery_size = battery_size

    def showEv(self):
        super().showCar()
        print(f'- Battery\t: {self.battery_size}%')
        
        
# object
obj_car = Car('porsche',2021,'red')
obj_ev = ElectricCar('BMW',2024,'black',90)


# output
obj_car.showCar()
print()
obj_ev.showEv()

'''
    age = obj_car.car_age()
    print(f"The car age is {age} years old")
    # print(f'- Car brand: {self.brand}')     
    # print(f'- Made in: {self.year}')
    # print(f'- Color: {self.color}')
    # print(f'This car is {current_year - self.year} years old.')    
'''
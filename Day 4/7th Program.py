#7. Write a program to demonstrate classes and their attributes

class Car:
    company = 'Toyato'
    def __init__(self,car_id,model,price):
        self.car_id = car_id
        self.car_model = model
        self.car_price = price
        
    def display(self):
        print(f'\nCar Id : {self.car_id}')
        print(f'Car Model : {self.car_model}')
        print(f'Car Price : {self.car_price}')
        print(f'Company : {self.company}')
        
Car1 = Car(101,'Innova',250000)
print('\nCar Details:')
Car1.display()

Car2 = Car(102,'Fortuner',350000)
Car2.display()

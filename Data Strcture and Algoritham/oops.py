class Car:
    brand = None
    model = None

    def  __init__(self,brand,model):
        self.brand = brand
        self.model = model
    def full_name(self):
        return f"{self.brand} {self.model}"


class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):
        self.battery_size = battery_size
        super().__init__(brand,model)


        
Tesla = ElectricCar("Tesla","class S","10KWH")
print(Tesla.battery_size)
print(Tesla.model)
print(Tesla.brand)
# my_car = Car("Toyota","Corola")
# my_car_1 = Car("Tata","Punch")
# print(my_car.full_name())
# print(my_car_1.full_name())
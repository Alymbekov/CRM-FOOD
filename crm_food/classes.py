class Car:
    def __init__(self,automobile_owner,automobile_make,automobile_model,production_year):
        self.owner = automobile_owner
        self.make = automobile_make
        self.model = automobile_model
        self.year = production_year
        self.odometer = 0

    def go(self,km):
        self.odometer = self.odometer + km
        print("Whuuuuuum")

new_car = Car('Dastan','BMW','34',2002) #this is instance / экземпляр класса
# наша машина масловая , проверим показатель одометра
print(new_car.odometer)
#проедем на тачке
new_car.go(121)    # use class's method(function)
#Теперь после проезда тоже проверим


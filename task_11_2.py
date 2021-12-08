'''
class Car:
    car_speed = 0
    def max(self, name, make, age):
        print("Погнали!!")
        self.name = name
        self.make = make
        self.age = age
        Car.car_speed += 5
    def min(self, name, make, age):
        print("Впереди менты")
        self.name = name
        self.make = make
        self.age = age
        Car.car_speed -= 5 
    def stop(self):
        print('Лада заглохла')

car_a= Car()  
car_a.max("Lada", "Sidan", 2002)  
print(car_a.name)  
print(car_a.car_speed)'''

class Car:
    def __init__(self, name, age, speed):
        self.__name = name
        self.__age = age
        self.__speed = speed

    def name_a(self):
        return self.__name

    def age_a(self):
        return self.__age

    def speed_a(self):
        return self.__speed

    def max_speed(self):
        self.__speed += 5
        print(self.__speed)

    def min_speed(self):
        self.__speed = self.__speed - 5
        print(self.__speed)

    def STOP(self):
        print ('заглохли')

    def turn_around(self):
        self.__speed = -self.__speed

    def print(self):
        print(self.__name)
        print(self.__age)
        print(self.__speed)

car_a = Car('Lada Sidan', '2002', 0)
car_a.max_speed()
car_a.print()
car_a.STOP()
car_a.print()
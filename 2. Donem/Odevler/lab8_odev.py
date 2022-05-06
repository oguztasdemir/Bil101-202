class plane:
    speed = 1200
    
class car:
    passNumber = 2
    
class FlyingCar(car,plane):
    print(plane.speed)
    print(car.passNumber)

start = FlyingCar()
start
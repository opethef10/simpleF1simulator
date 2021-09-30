from Session import Session

session = Session()
session.simulate()

for car in session.carList: 
    print(car.driver, round(car.fastestLap, 3))
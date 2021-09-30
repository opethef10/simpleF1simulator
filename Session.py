import csv
from Track import Track
from Turn import Turn
from Tyre import Tyre
from Car import Car
from Engine import Engine
from Chassis import Chassis

class Session:
    def __init__(self):
        with open("io/drivers.csv") as carsCsv,\
             open("io/turn.csv") as turnCsv,\
             open("io/inp.txt") as trckCsv:
            
            name, laps = next(csv.reader(trckCsv))
            
            self.totalLaps = int(laps)
            self.track = Track(
                trackName = name,
                turnList = [Turn.create(line["type"],int(line["no"]),line["type"],float(line["length"]),float(line["avgSpeed"]))
                            for line 
                            in csv.DictReader(turnCsv)]
            )
           
            self.carList =  [
                Car(carNo = int(line["carNo"]),
                    driver = line["driver"],
                    tyre = Tyre.create(line["tyre"]),
                    chassis = Chassis.create(line["chassis"]),
                    engine = Engine.create(line["engine"])
                ) 
                for line 
                in csv.DictReader(carsCsv)
            ]

    def __str__(self):
        return "totalLaps: {}\ntrack: {}\ncarList: {}".format(self.totalLaps,self.track,self.carList)
    
    def simulate(self):
        with open("io/out.txt", "w") as outputText:
            print("***SIMULATION STARTED***")
            print(f"trackName: {self.track.trackName}, length: {self.track.trackLength():.3f} km, totalLaps: {self.totalLaps}, totalLength: {self.track.trackLength()*self.totalLaps:.1f} km", file=outputText)
            print(self.track.turnList,file=outputText)
            #print(self.track.turnList)
            
            for lap in range(self.totalLaps):
                for viraj in self.track.turnList:
                    for car in self.carList:
                        car.tick(viraj,lap)
                #print("LAP:",lap+1,"\n",self.carList)
                print("LAP:", lap+1, file=outputText)
                for car in self.carList:
                    print(car, file = outputText)
            print("FINAL CLASSIFICATION:",file=outputText)
            for car in sorted(self.carList):
                print(car, file=outputText)
            print("***SIMULATION FINISHED, CHECK OUT.TXT***")
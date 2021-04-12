import csv
import json
from Session import *
from Track import *
from Turn import *
from Tyre import *
from Car import *
from Engine import *
from Chassis import *
from Helper import *

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

    def __repr__(self):
        return "totalLaps: {}\ntrack: {}\ncarList: {}".format(self.totalLaps,self.track,self.carList)
    
    def simulate(self):
        with open("io/out.txt", "w") as outputText:
            if self.track==None:
                print("No track")
                return None
            
            print("***SIMULATION STARTED***")
            print("trackName: {}, length: {:.3f} km, totalLaps: {}, totalLength: {:.1f} km".format(self.track.trackName,self.track.trackLength(),self.totalLaps,self.track.trackLength()*self.totalLaps),file=outputText)
            print(self.track.turnList,file=outputText)
            #print(self.track.turnList)
            
            for lap in range(self.totalLaps):
                for viraj in self.track.turnList:
                    for car in self.carList:
                        car.tick(viraj,lap)
                #print("LAP:",lap+1,"\n",self.carList)
                print("LAP:",lap+1,"\n",self.carList,file=outputText)
            print("FINAL CLASSIFICATION:\n",sorted(self.carList),file=outputText)
            print("***SIMULATION FINISHED, CHECK OUT.TXT***")
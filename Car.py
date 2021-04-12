import random, datetime
from math import inf
from Tyre import *
from Helper import pitStopConstructor

class Car:
    def __init__(self,carNo=0,driver="",tyre=None,chassis=None,engine=None):
        self.carNo=carNo
        self.driver=driver
        self.speed=0.0
        self.lastLap= 10e10
        self.totalTime=0.0
        self.fastestLap = 10e10
        self.tyre=tyre
        self.engine=engine
        self.chassis=chassis
   
    def __repr__(self):
        return "\n\t\t#{:<2} {:<11} speed: {:.1f} kph  lastLap: {}  totalTime: {} chassis: {} engine: {} tyre: {}".format(self.carNo,self.driver,self.speed*3.6,str(datetime.timedelta(milliseconds=self.lastLap*1000))[3:-3],str(datetime.timedelta(milliseconds=self.totalTime*1000))[:-3],self.chassis,self.engine,self.tyre)
    
    def __lt__(self, other):
         return self.totalTime < other.totalTime
    
    def pitStop(self,lap):
        currentCompound=self.tyre.compound
        print("LAP:",lap,currentCompound,end=" ")
        self.tyre=pitStopConstructor(currentCompound)
        pitStopTime= round(random.normalvariate(2.5,0.2),2)
        print(pitStopTime,end=" ")
        self.lastLap += 25.0 + pitStopTime
        self.totalTime += 25.0 + pitStopTime
        print(self.driver,self.tyre.compound)
        
    
    def tick(self,viraj,lap):
        if viraj.turnNo==0:
            if self.lastLap < self.fastestLap:
                self.fastestLap = self.lastLap
            self.lastLap=0.0 
        
        tyreMult = self.tyre.speedMult
        engineMult = self.engine.multiplier if viraj.turnType=="Straight" else 1.0
        chassisMult = (self.chassis.downforceMult)**3 if viraj.turnType=="HighSpeedTurn" else (self.chassis.downforceMult)**2 if viraj.turnType=="MediumSpeedTurn" else (self.chassis.downforceMult) if viraj.turnType=="LowSpeedTurn" else 1.0
        tyreWearMult = (-0.000273 * self.tyre.degradation) + 0.999899
        
        self.speed = viraj.avgSpeed * tyreMult * tyreWearMult * engineMult * chassisMult

        self.tyre.tick(viraj)
        
        if self.tyre.degradation>90: self.pitStop(lap)
        self.lastLap += (viraj.length/self.speed)
        self.totalTime += (viraj.length/self.speed)
        
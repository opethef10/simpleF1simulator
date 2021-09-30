class Track:
    def __init__(self,trackName="",turnList=[]):
        self.trackName=trackName
        self.turnList=turnList
        
    def __str__(self):
        return "\ttrackName: {}\n\tturnList: {}".format(self.trackName,self.turnList)
    
    def trackLength(self) :
        param=0.0;
        for turn in self.turnList:
            param+=turn.length
        return param/1000
